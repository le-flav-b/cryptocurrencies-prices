******************************************************************************
*************************  Cryptocurrencies  Prices  *************************
******************************************************************************

Flavien BOULEAU
Bastien OLLIVER



		Consignes :

• L'objectif est de réaliser une interface graphique avec Tkinter qui permet
de visualiser des données au format JSON (ou csv, ou xml) issues d'un OpenData
(ou autre serveur ou API, mais dans tous les cas, l'application doit venir
récupérer les données en ligne). Vous devrez aussi mettre en oeuvre au minimum
une classe (POO).

• Le sujet est libre, à vous de choisir.

• Une présentation de 5 min sera réalisée (à l'aide d'un diaporama).

• Vous travaillerez en binôme, il faut donc bien se répartir les tâches.



		Idée de base :

   Le sujet étant libre, nous avons décidé de réaliser notre projet sur un
thème à la fois d'actualité mais aussi utilisable au quotidien. Il nous est
donc venu l'idée de reproduire un logiciel de trading des cryptomonnaies.
(PS: objectif accomplit car m'intéressant au sujet, je lance l'application
presque tous les jours)

   L'idée trouvée, nous nous sommes accordés sur une forme finale potentielle
(Cf presentation.pptx), sachant que nous allions y aller étapes par étapes et
que rien ne nous empêchait d'aller plus loin.



		Résultat :

   Emportés par le sujet, nous avons surpassé nos attentes avec un résultat
que nous n'aurions pas même soupçonné : une page de chargement, un graphique
dynamique, des menus déroulants, des sous-parties pour des informations
supplémentaires, etc.

   Nous avons essayé de faire une interface à la fois fonctionnelle,
ergonomique, et esthétique avec un design simple. Nous sommes donc tous les
deux très fiers du rendu, et contents de nous être amusé sur le sujet.

   Une erreur est relevée à la fermeture de la page de chargement ; cette
erreur est due au rappel récursif de la méthode update dans la classe
LoadingWindow. Elle ne gène en rien le fonctionnement du programme car la
fenêtre de chargement est ensuite abandonnée.



		Arborescence du projet :

assets
  |-> icon.ico
  |-> update.png
  |-> wait.ico
  |-> wait_animation.gif
scripts
  |-> cryptocurrencies_prices.py
  |-> date_verification.py
  |-> find_peaks.py
  |-> graph.py
  |-> loading_window.py
  |-> lower_right_area.py
  |-> main.py
  |-> scrolling_menus.py
Cryptocurrencies Prices.exe
evolution_value_cryptocurrencies.py
presentation.pptx
README.txt

Pour lancer le programme, ouvrir Cryptocurrencies Prices.exe
ou evolution_value_cryptocurrencies.py en veillant à ce qu'ils soient dans le
même dossier que les sous-dossiers assets et scripts.



		Lien de l'API cryptocompare :

https://min-api.cryptocompare.com/



		Packages à installer :

- requests
- matplotlib
- tkinter
