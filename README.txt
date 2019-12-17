Projet 5 - Utilisez les données publiques de l'OpenFoodFacts

L'application est développée pourl a startup Pur Beurre.
La société recheche en effet une solution lui permettant de remplacer les
ingrédients qu'elle utilise toiut en respectant les goûts et préférences 
de sa clientèle.

Description du parcours utilisateur
L'utilisateur est sur le terminal. Ce dernier lui affiche les choix suivants :

1 - Quel aliment souhaitez-vous remplacer ?
2 - Retrouver mes aliments substitués.

L'utilisateur sélectionne 1. Le programme pose les questions suivantes à l'utilisateur et ce dernier sélectionne les réponses :

Sélectionnez la catégorie. [Plusieurs propositions associées à un chiffre. L'utilisateur entre le chiffre correspondant et appuie sur entrée]
Sélectionnez l'aliment. [Plusieurs propositions associées à un chiffre. L'utilisateur entre le chiffre correspondant à l'aliment choisi et appuie sur entrée]
Le programme propose un substitut, sa description, un magasin ou l'acheter (le cas échéant) et un lien vers la page d'Open Food Facts concernant cet aliment.
L'utilisateur a alors la possibilité d'enregistrer le résultat dans la base de données.
 

Fonctionnalités
Recherche d'aliments dans la base Open Food Facts.
L'utilisateur interagit avec le programme dans le terminal, mais si vous souhaitez développer une interface graphique vous pouvez,
Si l'utilisateur entre un caractère qui n'est pas un chiffre, le programme doit lui répéter la question,
La recherche doit s'effectuer sur une base MySql.

Livrables
- Modèle physique de données (ou modèle relationnel) et utilisant l’outil informatique de votre choix
 (pas de dessin à main levée !).
- Script de création de votre base de données
- Code source publié sur Github
- Tableau Trello, Taiga ou Pivotal Tracker.
- Document texte expliquant la démarche choisie, les difficultés rencontrées et les solutions trouvées
 et incluant le lien vers votre code source sur Github. Développez notamment le choix de l'algorithme et
 la méthodologie de projet choisie. Expliquez également les difficultés rencontrées et les solutions trouvées. 
Le document doit être en format pdf et ne pas excéder 2 pages A4. Il peut être rédigé en anglais ou en français, 
au choix, mais prenez bien en considération que les fautes d’orthographe et de grammaire seront évaluées ! 

Contraintes
- Votre code sera écrit en anglais : variables, noms de fonctions, commentaires, documentation, ...
- Votre projet sera versionné et publié sur Github pour que votre mentor puisse laisser des commentaires.

Etapes
1 Création du README
2 Création du Trello
3 Réalisation du schéma de base de données
4 Création de la base de donnée locale
5 Peuplement à partir de l'API d' OpenFoodFacts
6 Construction de l'architecture

7 Développement des fonctionnalités
8 Rédaction du document texte expliquant la démarche choisie


1 Récupérer dans POSTMAN les données d'OpenFoodFacts
2 Les comparer à l'énoncé
3 coder la requete en POO
4 Créer la base de données mysql
5 Utiliser notre programme pour récupérer les données et les insérer dans la bdd
6 Coder le programme du terminal
7 S'assurer de respecter PEP8, 257, etc
8 Pipenv


Pourl e schéma de base de données: champs json openfacts foods retenus
products/"product_name"
stores
countries_tag
"nutrition_grades"
categories




