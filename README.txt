Project 5 - Use the Openfoodfacts API to access its open data.
In this project we had to work on two different subjects.
Firstable web scraping. I fetched about 5000 products classified in 5 categories. I used the python's 'requests' built-in module to collect data and the peewee ORM to populate my mysql database.
Then I used the peewee ORM and the input method to manipulate my data with a command line interface. 

So what we built is a kind of game where we select products, where we save our preferences in a database table. 
The list of products is given by the OpenFoodFacts API.

How it works:
The program offers us two choices for starting.
1- Which product do you want to replace
2 - Display your favorites

Choice 1
- The program asks us to select a category.
- The program shows us the list of every products in the chosen category
- We are asked to select one article
- Once entered the program displays the list of products which possess a better nutrigrade (if nutrigrade is not already 'A')
- We have to select one of the displayed articles
- Its data and data of the replaced product are stored into the database

Choice 2
The program displays the data that are stored in the favorites table.  

Trello: https://trello.com/b/lbqJxrk7/p5