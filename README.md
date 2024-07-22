# Card-Game
This is a simple variant of the card game twenty-one implemented using Python.

<h2>Rules</h2>

<p>
<h3>Cards:</h3> 7, 8, 9, 10, jack, queen, king and ace in all four suits (clubs ♣, spades ♠, hearts ♥ and diamonds ♦.
  
<h3>Card Values:</h3> 
<ul>
  <li>Ace: 11 points</li>
  <li>King: 4 points</li>
  <li>Queen: 3 points (I didn't make the rules of this game!)</li>
  <li>Jack: 2 points</li>
  <li>Numbers: as stated</li>
</ul>

<h3>Description:</h3>

First, confirm that you want to play and enter the number and names of players.

The goal is to get one's points up to or as close to 21 points as possible. 
Who has more than 21 points however, looses.

The program will act as the bank, 'draw' one card for itself and give all players two cards.

If a player has 21 points already, they win immediately.
(In case a player has two aces, this combination will not be counted as 2x11 = 22, but as 21 and thus the player wins too.)

If nobody has reached 21 points, the program asks the players - one by one - if they want another card.
In case a player reaches 21 points or two aces, the winner is declared.
Otherwise, the program continues asking until no player wants more cards.

Then, the program draws further cards for the bank. If the program itself reaches 21 or two aces, the bank wins and all other players lose.

If the bank ends up with more than 21 points, the bank loses and the other players' cards will be evaluated.
In this case, the player with the most points wins the game and the game ends.
</p>
