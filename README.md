# TKinter-Card-Game
TKinter-based solitaire game where a player has to find all the targeted cards by flipping them in order to win


## To Play
On the bottom of the window, there is a conveyor belt of all the symbol images for the game. The target symbol is indicated with the yellow star mark. 
A player flips a card by clicking it. If the flipped card has the targeted symbol, the indicator (star sign) on the coveyor belt goes to the right. If not, to the left. If the indicator goes to the left end after continued failures to find the symbols, the game ends.


## main.py
This python file runs the app on the main loop with TKinter root class.


## app.py
The app python file contains and creates the image lists: the card game table and the symbol conveyor belt.


## maintable.py
This python file creates the main (card game) table. The images and alphabets are randomized. The click event is tagged into the images


## conveyor.py
This coneyor python file not only creates the conveyor belt but also checks if the targeted symbol and the flipped card match. Furthermore, the match functions move the belt either to the right or to the left according to the match result.


## imagebtn.py
The hidden symbol images on the back sides are bound with the cards.

