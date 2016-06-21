~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Programme web de création de fractale avec percolaton
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
-------------------------------------------------------------------
    @Authors                                                      |
             Serigne Fallou NDIAYE  & Chuhan WANG                 |
             Jordan N'Guessan KONAN & Mingshan  ZHG               |
    @From: Ecole Centrale de Lyon                                 |
    @Prog: Projet d'Application web en Python                     |
    @Date: 08 - 06 - 2016                                         | 
-------------------------------------------------------------------

#################################################################

~~~~~~~~ Structure du projet ~~~~~~~~~~~~~~~~

La partie client est essentiellement basée sur un thême inspiré de ce site:https://usman.it/themes/charisma/
Dans l'arborescence on ne détaille que les dossiers et fihcier dans lesquels on a modifié ou ajouté des choses

-> fractale
	|-> serveur.py
	|-> fractale.py
	|-> fractale2.py
	|-> init_BDD.py
	|-> generic.py
	|-> percolation.sqlite
	|-> README.txt
	|-> client
		|-> equipe.html
		|-> index.html
		|-> percolation2.html
		|-> percolation.html
		|-> bower_components
		|-> fonts
		|-> misc
		|-> images
		|-> img
		|-> js
			|-> monscript.js
			|-> monscript2.js
		|-> css
			|-> moncss.css

###############################################################

~~~~~~~~~~~~ Mise en marche et fonctionnement ~~~~~~~~~~~~~~~~~
1) se placer dans le dossier fractale
2) vider la base de données et le dossier images (lors d'une première utilisation bien sûr) 
	en executant le fichier init_BDD.py
4) executer le fichier serveur.py
3) se connecter sur un navigateur avec l'url: localhost:8080
4) naviguer dans le site dans le menu qui se trouve à gauche (avec 2 variantes de percolations)


