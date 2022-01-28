# **Pokemon_DragonFly**

*Projet Pokemon en groupe avec Aryan, Ronan et Eden.*

➤ **LE PROJET** :

✦ Notre groupe est composé de Ronan Aryan et Eden.

✦ Notre Projet principal est le projet sur le thème Pokémon, on fera un jeu plutôt ouvert, c'est à dire le joueur pourra se promener dans un grand environnement avec   des zones (ville, plaine...). Il pourra y attraper des Pokémon, combattre des dresseurs , faire soigner ses Pokémon etc... Nos priorité pour l'instant c'est d'avoir   un système de rencontre aléatoire de Pokémon dans les hautes herbes, une mechanique de combats (combat entre deux pokémon amusant), la jouabilité hors combats         c'est à dire se promener sur la map.

➤ **EXEMPLE DE JEU SIMILAIRE** :


- Projet de l'an dernier : https://github.com/williamFlouret/ProjectNSI_Flouret_Bernacki
- Projet réalisé dans le cadre d'un devoir universitaire : https://github.com/DuarteVi/pokemon
- Projet mini jeu Pokemon : https://github.com/cloudStrif/pokemon

➤ **EXEMPLE VISUEL DE CE QU'ON SOUHAITE FAIRE** :

![image](https://user-images.githubusercontent.com/95481171/145786051-32a6f91d-5258-4a9d-912d-7aad599d7e72.png)  

![image](https://user-images.githubusercontent.com/95481171/145786189-3ab1e07e-30dd-4a49-9818-7fa5891420f2.png)

![gif](https://64.media.tumblr.com/61606b0eb6a0e85f5808ead926536e2f/tumblr_nipbgzqf8o1t0pgjqo1_640.gifv)


➤ **CARACTERISTIQUE** :


<pre>
✦ 2D :
    ┗ Un jeu en 2D pixelisé

✦ MAP 
    ┗ (Une seule) Map limité avec une ville et ses alentours, assez grande pour s'y aventurer
    
✦ CONTRÔLE : 
    ┗ Contrôle exclusivement au clavier (flèches directionnelles + entré / espace / souris)
    
✦ MAP STRUCTURÉ :
    ┣ chemin qui mène vers d'autres zones, par exemple combat, découverte ou bien la ville avec tous ses batiments
    ┣ hautes herbes (pokémon qui apparaissent de manière aléatoire)
    ┣ ville comportant des bâtiments utiles (centre pokémon servant a soigner ses pokémon), accessible + exécutable et aussi un magasin pour acheter ses potions
    ┗ PNJ utiles et interactif (donne des récompenses (potions, pokéballs) + possibilité de les combattre )
    
✦ INTERFACE UTILISATEUR :
    ┗ hotbar des pokémons (pokémon visible sur l'écran avec leur barres de vies)

✦ AUDIO :
    ┗ musique de combat + de ville 

✦ BRUITAGE :
    ┣ lorsque le pokémon attaque
    ┣ Lorsque l'on achète un objet
    ┣ lorsqu'on lance un combat
    ┗ lorsque le joueur perds ou gagne un combat

✦ ANIMATION :
    ┣ Pokémon animé en fichier gif
    ┣ déplacement du personnage (ne pas passer sur les maisons, arbres etc..)
    ┣ Lorsque le Pokémon envoie une attaque
    ┣ barre de la vie qui descend ou monte
    ┣ lancement d'un combat
    ┣ si le joueur perd le combat, le joueur réapparait au centre pokemon
    ┗ camera qui suit le personnage (la map bouge et le personnage reste au centre)
</pre>


➤ **ORGANISATION, PLANNING, COMMENT VA-T-ON PRECEDER POUR LA CREATION DU PROJET** :
<br/>

*Tout d'abord nous comptons terminer notre Projet en 9 semaines voir 10, on aimerais avoir une marge de 2 semaines pour pouvoir travailler et corriger les bugs présents pour que le jeu soit parfait pour le rendre. Nous allons continuer et avancer chez nous pour gagner du temps si jamais et avoir de l'avance pour pouvoir aouter un peu plus de détails au jeu
<pre>
✦ 4ème semaine :
   ┣ création des PNJ par Eden 
   ┣ Début du programme → création de la fenêtre : titre, taille, miniature par Ronan
   ┣ Progammer les mouvements du personnages par Aryan
   ┗ création de la map par Aryan
   
✦ 5ème semaine : 
   ┣ Terminer la map par Aryan 
   ┣ Ronan va s'occuper des commandes pour bouger le personnage
   ┗ Eden s'occupera de la création de la hotbar des Pokémon (points de vies) qui baisserai à chaque attaques reçus par l'ennemi (voir exemple ci-dessous)
   </pre>

   ![gif](https://i.imgur.com/WGfwL.gif)
   
<pre>

✦ 6ème semaine : 
   ┣ Importation de la barre de vie du Pokémon dans le code par Ronan 
   ┣ Ajout de la map dans le code et création du décors de combat (endroit où les Pokémons s'affronteront) par Aryan
   ┗ animer le personnage (créer les différentes positions de mouvements par Eden)

✦ 7ème semaine :
   ┣ Terminer le décors de combat et ensuite commencer l'intérieur des bâtiments par Aryan
   ┣ Gestion de la barre de vie → programmer quand un pokémon se prend une attaque donc perds des PV par Ronan
   ┗ Animation du personnage si ce n'est pas fini, si oui alors animation des attaques des Pokemons par Eden

✦ 8ème semaine :
   ┣ Programmer les collisions et une physique aux bâtiments (ne pas marcher par dessus une maison) par Ronan
   ┣ Animation des combats Pokémon par Eden
   ┗ Programmer les attaques Pokémon par Aryan

✦ 9ème semaine :
   ┣ Programmation des attaques Pokémon par Aryan
   ┣ Programmation des collisions et physique des bâtiments par Ronan
   ┗ ajouter les animations aux programmes par Eden

✦ 10ème semaine :
   ┣ Ajout de l'audio (musique) dans le programme par Aryan
   ┣ Ajout des bruitages (Pokémon qui attaque) dans le programmes par Eden
   ┗ Programmer les PNJ pour qu'ils invitent le joueur a faire un duel si le joueur passe devant ce PNJ par Ronan 



</pre>






































⌜Si ce premier Projet principal ne prend pas forme, nous nous orienterons vers un jeu qui a pour thème le combat, on s'inspire du fameux jeu de combat Super Smash Bros pour le faire, c'est un jeu 1 contre 1, joueur contre joueur ou joueur contre robot (intelligence artificielle) . Le joueur peut incarner plusieurs personnages emblématique du monde du Jeu vidéo par exemple Mario, Pikachu, Link, Donkey Kong... contre d'autre personnages issues de différents Jeux Videos aussi, le combat se passe sur une plateforme aérienne avec plusieurs type de combos possible.⌟





