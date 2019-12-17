Projet 5 - Utilisez les donn�es publiques de l'OpenFoodFacts

L'application est d�velopp�e pourl a startup Pur Beurre.
La soci�t� recheche en effet une solution lui permettant de remplacer les
ingr�dients qu'elle utilise toiut en respectant les go�ts et pr�f�rences 
de sa client�le.

Description du parcours utilisateur
L'utilisateur est sur le terminal. Ce dernier lui affiche les choix suivants :

1 - Quel aliment souhaitez-vous remplacer ?
2 - Retrouver mes aliments substitu�s.

L'utilisateur s�lectionne 1. Le programme pose les questions suivantes � l'utilisateur et ce dernier s�lectionne les r�ponses :

S�lectionnez la cat�gorie. [Plusieurs propositions associ�es � un chiffre. L'utilisateur entre le chiffre correspondant et appuie sur entr�e]
S�lectionnez l'aliment. [Plusieurs propositions associ�es � un chiffre. L'utilisateur entre le chiffre correspondant � l'aliment choisi et appuie sur entr�e]
Le programme propose un substitut, sa description, un magasin ou l'acheter (le cas �ch�ant) et un lien vers la page d'Open Food Facts concernant cet aliment.
L'utilisateur a alors la possibilit� d'enregistrer le r�sultat dans la base de donn�es.
 

Fonctionnalit�s
Recherche d'aliments dans la base Open Food Facts.
L'utilisateur interagit avec le programme dans le terminal, mais si vous souhaitez d�velopper une interface graphique vous pouvez,
Si l'utilisateur entre un caract�re qui n'est pas un chiffre, le programme doit lui r�p�ter la question,
La recherche doit s'effectuer sur une base MySql.

Livrables
- Mod�le physique de donn�es (ou mod�le relationnel) et utilisant l�outil informatique de votre choix
 (pas de dessin � main lev�e !).
- Script de cr�ation de votre base de donn�es
- Code source publi� sur Github
- Tableau Trello, Taiga ou Pivotal Tracker.
- Document texte expliquant la d�marche choisie, les difficult�s rencontr�es et les solutions trouv�es
 et incluant le lien vers votre code source sur Github. D�veloppez notamment le choix de l'algorithme et
 la m�thodologie de projet choisie. Expliquez �galement les difficult�s rencontr�es et les solutions trouv�es. 
Le document doit �tre en format pdf et ne pas exc�der 2 pages A4. Il peut �tre r�dig� en anglais ou en fran�ais, 
au choix, mais prenez bien en consid�ration que les fautes d�orthographe et de grammaire seront �valu�es ! 

Contraintes
- Votre code sera �crit en anglais : variables, noms de fonctions, commentaires, documentation, ...
- Votre projet sera versionn� et publi� sur Github pour que votre mentor puisse laisser des commentaires.

Etapes
1 Cr�ation du README
2 Cr�ation du Trello
3 R�alisation du sch�ma de base de donn�es
4 Cr�ation de la base de donn�e locale
5 Peuplement � partir de l'API d' OpenFoodFacts
6 Construction de l'architecture

7 D�veloppement des fonctionnalit�s
8 R�daction du document texte expliquant la d�marche choisie


1 R�cup�rer dans POSTMAN les donn�es d'OpenFoodFacts
2 Les comparer � l'�nonc�
3 coder la requete en POO
4 Cr�er la base de donn�es mysql
5 Utiliser notre programme pour r�cup�rer les donn�es et les ins�rer dans la bdd
6 Coder le programme du terminal
7 S'assurer de respecter PEP8, 257, etc
8 Pipenv


Pourl e sch�ma de base de donn�es: champs json openfacts foods retenus
products/"product_name"
stores
countries_tag
"nutrition_grades"
categories




