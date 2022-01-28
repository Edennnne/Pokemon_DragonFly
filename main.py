import pygame # importation du module pygame



pygame.init() #­ on initialise pygame



# création de la surface d'affichage(écran) par rapport à la taille de l'écran
largeur_ecran = 900
longueur_ecran = 1200
taille_ecran = (longueur_ecran, largeur_ecran)
ecran = pygame.display.set_mode(taille_ecran)


# on fait apparaître le nom et l'icône du jeu
pygame.display.set_caption("Pokemon DragonFly")
icon = pygame.image.load("images/icone_jeu.png").convert()
pygame.display.set_icon(icon)

# on change les mesures du fond, puis on affiche le fond en haut à gauche de l'écran
fond = pygame.image.load("images/fond.jpg").convert()
fond = pygame.transform.scale(fond, (taille_ecran))


# on charge l'inventaire
fond_inventaire = pygame.image.load("images/fond_inventaire.jpg").convert()
fond_inventaire = pygame.transform.scale(fond_inventaire, (taille_ecran))


# on charge l'icône de l'inventaire en bas à gauche de l'écran
icone_inventaire = pygame.image.load("images/boutonX.png").convert_alpha()
icone_inventaire = pygame.transform.scale(icone_inventaire, (75,75))


icone_sac = pygame.image.load("images/sac.png").convert_alpha()
icone_sac = pygame.transform.scale(icone_sac, (50,50))

icone_esc = pygame.image.load("images/bouton_esc.png").convert_alpha()
icone_esc = pygame.transform.scale(icone_esc, (30,30))

# création du personnage, changement de ses mesures
perso = pygame.image.load("images/Dragon Rouge.png").convert()
largeur_perso = 40
longueur_perso = 40
perso = pygame.transform.scale(perso, (longueur_perso, largeur_perso))

perso.set_colorkey([0,0,0]) # on change la couleur du rect du perso en noir

# définition des positions en x et en y de base, et de la vitesse du perso
vitesse_perso = 3

position_perso = perso.get_rect() # on définition la position du perso
position_perso[0] = 200
position_perso[1] = 200


FPS = pygame.time.Clock() # création de la variable FPS

jeu_en_cours = True # booléen représentant l'état de l'écran à la valeur True

# création de la boucle du jeu
while jeu_en_cours :

    # Pour chaque évènement dans les évènements du jeu, si le type d'event est de type QUIT, le jeu s'arrête
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jeu_en_cours = False

    pressed = pygame.key.get_pressed() # création de la variable pressed signifiant qu'une touche du clavier est enclenchée

    # déplacement du perso si une flèche directionnelle est enclenchée + possibilité de se déplacer en restant appuyé dessus. Et impossibilité de dépasser la surface de l'écran ( création des bordures de l'écran )
    if pressed[pygame.K_DOWN] and position_perso[1] < largeur_ecran - largeur_perso:
        position_perso[1]+=vitesse_perso

    elif pressed[pygame.K_UP] and position_perso[1] > 0 :
        position_perso[1]-=vitesse_perso

    elif pressed[pygame.K_RIGHT] and position_perso[0] < longueur_ecran - longueur_perso:
        position_perso[0]+=vitesse_perso

    elif pressed[pygame.K_LEFT] and position_perso[0] > 0:
        position_perso[0]-=vitesse_perso

    

        
    # on réaffiche tout
    ecran.blit(fond,(0,0))
    ecran.blit(perso,position_perso)
    ecran.blit(fond_inventaire,(0,-30))
    ecran.blit(icone_esc,(longueur_ecran-32 ,largeur_ecran-32))
    #ecran.blit(icone_inventaire,(longueur_ecran-100 ,largeur_ecran-130))
    #ecran.blit(icone_sac,(longueur_ecran-85 ,largeur_ecran-55))
    
    # on met à jour l'écran entier pour faire apparaître les nouveaux évènements
    pygame.display.flip() 
    

    FPS.tick(60) # on définit le nombre de FPS à 60 dans la boucle de jeu



pygame.quit() # la fenêtre du jeu se ferme