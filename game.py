import pygame



pygame.init()

taille_ecran = (1500,1000)
ecran = pygame.display.set_mode(taille_ecran)

pygame.display.set_caption("Pokemon DragonFly")
icon = pygame.image.load("images/Pikachu.jpg").convert()
pygame.display.set_icon(icon)
fond = pygame.image.load("images/fond.jpg")
fond = pygame.transform.scale(fond, (1500, 1000))

ecran.blit(fond,(0,0))

perso = pygame.image.load("images/perso_dracaufeu-1.png")
ecran.blit(perso,(750,500))

position_x=0
position_y=0
position_perso = perso.get_rect()








pygame.display.flip()



jeu_en_cours = True


while jeu_en_cours :

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jeu_en_cours = False
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                position_perso[1]-=5
                
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                position_perso[1]+=5
                
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                position_perso[0]+=5
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                position_perso[0]-=5
            
            
        ecran.blit(fond,(0,0))
        ecran.blit(perso,position_perso)
        
        
        
        pygame.display.flip()
            
            
            
            
            


pygame.quit()

