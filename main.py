import pygame # importation du module pygame



pygame.init() #­ on initialise pygame



# création de la surface d'affichage(écran) par rapport à la taille de l'écran
largeur_ecran = 500
longueur_ecran = 800
taille_ecran = (longueur_ecran, largeur_ecran)
ecran = pygame.display.set_mode(taille_ecran)


# on fait apparaître le nom et l'icône du jeu
pygame.display.set_caption("Pokemon DragonFly")
icon = pygame.image.load("images/Pikachu.jpg").convert()
pygame.display.set_icon(icon)

# on change les mesures du fond, puis on affiche le fond en haut à gauche de l'écran
fond = pygame.image.load("images/fond.jpg").convert()
fond = pygame.transform.scale(fond, (taille_ecran))
ecran.blit(fond,(0,0))


# création du personnage, changement de ses mesures
perso = pygame.image.load("images/perso_dracaufeu.png").convert()
largeur_perso = 40
longueur_perso = 40
perso = pygame.transform.scale(perso, (longueur_perso, largeur_perso))

perso.set_colorkey([0,0,0]) # on change la couleur du rect du perso en transparent

ecran.blit(perso,(0,0)) # on affiche le perso aux coordonnées marquées


# définition des positions en x et en y de base, et de la vitesse du perso
vitesse_perso = 3

position_perso = perso.get_rect() # on définition la position du perso dans un rect


pygame.display.flip() # on met à jour l'écran entier



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


    # on réaffiche le fond et le perso à la même position
    ecran.blit(fond,(0,0))
    ecran.blit(perso,position_perso)

    pygame.display.flip() # on met à jour l'écran entier pour faire apparaître les nouveaux évènements


    FPS.tick(60) # on définit le nombre de FPS à 60 dans la boucle de jeu



pygame.quit() # la fenêtre du jeu se ferme