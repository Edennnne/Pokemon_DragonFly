import pygame
import pytmx
import pyscroll



BLANC = [255, 255, 255]
NOIR = [0, 0, 0]
BLEU_NUIT = [25, 25, 112]


class Player(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()

        # charger la sprite sheet
        self.sprite_sheet = pygame.image.load("perso/spritesheet player.png").convert()
        self.image = self.get_image(0, 0) # image du perso par défaut (en haut à gauche)
        self.rect = self.image.get_rect()
        self.position = [x,y]
        # dictionnaire qui associe les images de la sprite sheet à une direction
        self.images = { 'UP': self.get_images(self.image.get_width()),
                        'DOWN': self.get_images(0),
                        'RIGHT': self.get_images(self.image.get_width()*3),
                        'LEFT': self.get_images(self.image.get_width()*2) }
        self.frame = 0
        self.next_frame = 0
        self.vitesse = 3
        self.old_position = self.position.copy()
        # rect servant pour les collisions du perso
        self.feet = pygame.Rect(0, 0, self.image.get_width()*0.5, self.image.get_height()*0.5)


    def get_image(self, x, y):
        """ permet de récupérer une image dans la sprite sheet selon sa position x et y, puis de la renvoyer """
        self.image = pygame.Surface([32, 32])
        self.image.set_colorkey(NOIR)
        self.image.blit(self.sprite_sheet, (0, 0), (x, y, self.image.get_width(), self.image.get_height()))
        return self.image


    def get_images(self, y):
        """ permet de récupérer les images d'une ligne de la sprite sheet selon l'ordonnée donnée en argument, puis de renvoyer la liste des images """
        images = []
        for i in range(0,4):
            x = i*self.image.get_width()
            image = self.get_image(x, y)
            images.append(image)

        return images


    def animation_deplacement(self, direction):
        """ selon sa direction, l'animation du déplacement va s'effectuer et sera ralentie """

        self.image = self.images[direction][self.frame]
        self.image.set_colorkey(NOIR)
        self.next_frame += 1

        if self.next_frame >= 12:
            self.frame = (self.frame + 1) %  4
            self.next_frame = 0


    def update(self):
        """ permet d'actualiser la position du rect du perso (plus au topleft de l'écran), et du rect feet (en bas du rect du perso) """
        self.rect.topleft = self.position
        self.feet.midbottom = self.rect.midbottom


    def stop(self):
        """ c'est comme la fonction update sauf que cette fois la position du perso = son ancienne position, il va donc s'arrêter """
        self.position = self.old_position
        self.update()



class Dragon(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        # charge la sprite sheet du dragon
        self.dragon_sprite_sheet = pygame.image.load("images/dragon_sprite_sheet.png").convert_alpha()
        width = 140
        height = 120
        # récupère dans l'ordre toutes les images de la sprite sheet
        self.dragonSprite = [self.dragon_sprite_sheet.subsurface(width*(x%5), height*(x//5), width, height)for x in range(0,30)]
        self.frame = 0
        self.next_frame = 0


    def animation_dragon(self):
        """ permet une animation continue du dragon au ralenti (pas 60 FPS, mais 12 FPS) """
        self.dragon = self.dragonSprite[self.frame]
        self.dragon.set_colorkey(NOIR)
        self.next_frame += 20

        if self.next_frame >= 100:
            self.frame = (self.frame + 1) %  30
            self.next_frame = 0



class Portail:

    def __init__(self, monde_avant, monde_cible, switch_rect, player_spawn):

        self.monde_avant = monde_avant
        self.monde_cible = monde_cible
        self.switch_rect = switch_rect
        self.player_spawn = player_spawn



class Map:

    def __init__(self, nom, obstacles=list(), group=pyscroll.PyscrollGroup, tmx_data=pytmx.TiledMap, portails=list()):

        self.nom = nom
        self.obstacles = obstacles
        self.group = group
        self.tmx_data = tmx_data
        self.portails = portails



class MapSwitcher:

    def __init__(self, ecran, player):

        self.ecran = ecran
        self.player = player
        self.maps = dict()
        self.monde = "map"

        # permet de passer de la map aux maisons, aux autres bâtiments et à la tour
        self.charger_map("map", zoom = 1, portails=[
        Portail(monde_avant="map", monde_cible="house", switch_rect="maison_entrée1", player_spawn="joueur_house"),
        Portail(monde_avant="map", monde_cible="house2", switch_rect="maison_entrée2", player_spawn="joueur_house2")
        ])

        # permet de sortir de house ou bien d'accéder à l'étage
        self.charger_map("house", zoom = 1.5, portails=[
        Portail(monde_avant="house", monde_cible="map", switch_rect="maison_sortie", player_spawn="joueur_sortie_maison1"),
        Portail(monde_avant="house", monde_cible="house_etage", switch_rect="maison_etage", player_spawn="joueur_etage")
        ])

        # permet de descendre de l'étage de house
        self.charger_map("house_etage", zoom = 1.5, portails=[
        Portail(monde_avant="house_etage", monde_cible="house", switch_rect="maison_floor", player_spawn="joueur_floor")
        ])

        # permet de sortir de house2
        self.charger_map("house2", zoom = 1.5, portails=[
        Portail(monde_avant="house2", monde_cible="map", switch_rect="maison_sortie2", player_spawn="joueur_sortie_maison2")
        ])

        # place le joueur au point "spawn_joueur", le point de spawn du joueur, placé sur Tiled
        self.spawn_player("spawn_joueur")


    def get_map(self):
        """ fonction qui renvoie le dictionnaire maps avec le nom du monde dans lequel on se trouve """
        return self.maps[self.monde]

    def get_group(self):
        """ fonction qui renvoie le groupe de calques qui constitue la map """
        return self.get_map().group

    def get_obstacles(self):
        """ fonction qui renvoie les obstacles selon la map actuelle """
        return self.get_map().obstacles

    def get_object(self, nom):
        """ fonction qui renvoie le nom d'un objet qui constitue la map actuelle """
        return self.get_map().tmx_data.get_object_by_name(nom)


    def spawn_player(self, nom):
        """ permet de définir le point de spawn du joueur sur Tiled en donnant le nom de l'objet """
        spawn = self.get_object(nom)
        self.player.position[0] = spawn.x
        self.player.position[1] = spawn.y
        # debug
        self.player.old_position = self.player.position


    def verifier_collisions(self):
        """ récupère les infos du switch_rect pour que, si le joueur rentre en collison avec, il puisse changer de monde. Et vérification des collisions avec les obstacles """

        # si le monde_avant de la classe Portail est le même que le monde, on définit le rect du point de passage à un autre monde
        for portail in self.get_map().portails:
            if portail.monde_avant == self.monde:
                rect = self.get_object(portail.switch_rect)
                rect_changement_monde = pygame.Rect(rect.x, rect.y, rect.width, rect.height)

                # si les pieds du joueur rentrent en collision avec le switch_rect, la map devient le monde_cible, et le joueur apparaît à l'objet player_spawn placé sur Tiled
                if self.player.feet.colliderect(rect_changement_monde):
                    self.monde = portail.monde_cible
                    self.spawn_player(portail.player_spawn)

        # si les pieds du joueur rentre en collision avec la liste d'obstacles, il garde sa position d'avant être rentré en collision avec un obstacle
        if self.player.feet.collidelist(self.get_obstacles()) > -1:
            self.player.stop()


    def charger_map(self, nom, zoom=int, portails=[]):
        """ permet de charger la map selon son nom, ainsi que tous ses attributs(obstacles, group, tmx_data et portails) """
        # charger une map
        tmx_data = pytmx.load_pygame(f"map/{nom}.tmx")
        map_data = pyscroll.TiledMapData(tmx_data)
        map_layer = pyscroll.BufferedRenderer(map_data, self.ecran.get_size(), zoom = zoom)

        # liste de Rectangles de collisions: obstacles
        obstacles = []

        for objet in tmx_data.objects:
            if objet.type == "collision":
                obstacles.append(pygame.Rect(objet.x, objet.y, objet.width, objet.height))

        # définir un groupe de calques
        group = pyscroll.PyscrollGroup(map_layer = map_layer, default_layer = 4)
        group.add(self.player)

        # instancier la classe Map selon le nom d'une map, chaque map possède son nom, ses obstacles, son groupe, ses données tmx et ses portails
        self.maps[nom] = Map(nom, obstacles, group, tmx_data, portails)


class Audio:

    def __init__(self):

        self.sons = {
            'son_accueil': pygame.mixer.Sound("audio/Title.mp3"),
            'main_theme': pygame.mixer.Sound("audio/City.mp3")
        }

    def play(self, nom):
        self.sons[nom].play()

    def stop(self, nom):
        self.sons[nom].stop()

    def set_volume(self, nom, volume=int):
        self.sons[nom].set_volume(volume)



class Jeu:

    def __init__(self):

        # création de la surface d'affichage + du nom du jeu + de son icône
        self.ecran = pygame.display.set_mode((1000, 700))
        self.ecran_rect = self.ecran.get_rect()
        pygame.display.set_caption("Pokemon DragonFly")
        pygame.display.set_icon(pygame.image.load("images/icone_jeu.png").convert())


        # on charge toutes les images
        fond_invent = pygame.image.load("images/fond_inventaire.jpg").convert() # Fond de l'inventaire
        self.fond_invent = pygame.transform.scale(fond_invent, (self.ecran.get_size()))

        icone_tab = pygame.image.load("images/tab.png").convert_alpha() # Touche TAB
        self.icone_tab = pygame.transform.scale(icone_tab, (80,50))

        icone_entrer = pygame.image.load("images/boutonEntrer.png").convert_alpha() # Touche ENTER
        self.icone_entrer = pygame.transform.scale(icone_entrer, (190,55))

        img_acc = pygame.image.load("images/start screen.png").convert() # Image de l'accueil
        self.img_acc = pygame.transform.scale(img_acc, (self.ecran.get_size()))

        icone_sac = pygame.image.load("images/sac.png").convert_alpha() # Sac
        self.icone_sac = pygame.transform.scale(icone_sac, (50,50))

        icone_esc = pygame.image.load("images/bouton_esc.png").convert_alpha() # Touche ECHAP
        self.icone_esc = pygame.transform.scale(icone_esc, (50,50))

        # on charge le texte d'accueil + son rect situé au centre de l'écran
        police = pygame.font.Font(None, 40)
        self.texte = police.render('Appuyez sur ENTER',True, BLEU_NUIT)
        self.texte_rect = self.texte.get_rect()
        self.texte_rect.center = self.ecran_rect.center

        # instances de classes
        self.player = Player(0, 0)
        self.dragon = Dragon()
        self.map_switcher = MapSwitcher(self.ecran, self.player)
        self.audio = Audio()


    def deplacement_perso(self):
        """ possibilité de se déplacer en restant appuyé sur une flèche directionnelle + animation du perso selon sa direction """

        pressed = pygame.key.get_pressed() # lorsqu'une touche du clavier est enclenchée

        if pressed[pygame.K_RIGHT]:
            self.player.position[0] += self.player.vitesse
            self.player.animation_deplacement('RIGHT')

        elif pressed[pygame.K_LEFT]:
            self.player.position[0] -= self.player.vitesse
            self.player.animation_deplacement('LEFT')

        elif pressed[pygame.K_UP]:
            self.player.position[1] -= self.player.vitesse
            self.player.animation_deplacement('UP')

        elif pressed[pygame.K_DOWN]:
            self.player.position[1] += self.player.vitesse
            self.player.animation_deplacement('DOWN')


    def running(self):
        """ c'est la boucle du jeu avec toutes les fonctions, les entrées clavier, les images à afficher... """
        clock = pygame.time.Clock()

        running = True
        ecran_accueil = True
        inventaire = False

        while running:

            # on peut fermer la fenêtre du jeu
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # Ecran d'accueil
            if ecran_accueil == True:

                self.audio.play('son_accueil') # joue la musique de l'écran d'accueil
                self.audio.set_volume('son_accueil', 0.3) # baisse le volume à 30%

                # passer sur la map --> ENTER
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        ecran_accueil = False

            # Map
            else :

                # fonctions de la map
                if inventaire == False:

                    self.audio.stop('son_accueil') # stop le son de l'écran d'accueil
                    self.audio.play('main_theme') # joue le main theme
                    self.audio.set_volume('main_theme', 0.3) # baisse le volume à 30%

                    self.player.old_position = self.player.position.copy()# récupère l'ancienne position du perso
                    self.deplacement_perso() # déplace et anime le perso

                    self.player.update() # actualise la position du joueur ainsi que celle du rect feet
                    self.map_switcher.verifier_collisions() # vérifie les collisions de switch_rect et d'obstacles
                    self.map_switcher.get_group().center(self.map_switcher.player.rect.center) # centre le perso et la map


                    # ouvrir l'inventaire --> TAB
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_TAB:
                            inventaire = True

                # Inventaire
                if inventaire == True:

                    self.audio.set_volume('main_theme', 0.1) # baisse le volume à 10%
                    self.dragon.animation_dragon() # anime en continu le dragon dans l'inventaire

                    # fermer l'inventaire --> ECHAP
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            inventaire = False


            # si écran d'accueil, on affiche les images de l'accueil
            if ecran_accueil == True:

                self.ecran.blit(self.img_acc,(0,0))
                self.ecran.blit(self.icone_entrer,(self.ecran.get_width() - 195 ,self.ecran.get_height() - 60))
                pygame.draw.rect(self.ecran, BLEU_NUIT, pygame.Rect(self.texte_rect[0]-3, self.texte_rect[1]-3, 290, 33), 2)
                self.ecran.blit(self.texte, self.texte_rect)

            # autrement, on affiche les images...
            else:

                # ... de l'inventaire
                if inventaire == True:

                    self.ecran.blit(self.fond_invent,(0,0))
                    self.ecran.blit(self.icone_esc,(self.ecran.get_width() - 55 ,self.ecran.get_height() - 55))
                    self.ecran.blit(self.dragon.dragon, (300, 200))

                # ... de la map
                else:

                    self.map_switcher.get_group().draw(self.ecran) # dessine le groupe de calques
                    self.ecran.blit(self.icone_sac,(self.ecran.get_width() - 130 ,self.ecran.get_height() - 50))
                    self.ecran.blit(self.icone_tab,(self.ecran.get_width() - 90 ,self.ecran.get_height() - 50))


            pygame.display.flip() # actualise l'écran

            clock.tick(60) # La boucle tourne à 60 FPS

        pygame.quit()


# initialiser le jeu
pygame.init()
jeu = Jeu()
jeu.running()
