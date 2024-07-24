# Card-Game
This is a simple variant of the card game twenty-one implemented using Python, i.e. no bets, split, double down, insurance, surrender.

<h2>Rules</h2>

<p>
<h3>Cards:</h3> 2, 3, 4, 5, 6, 7, 8, 9, 10, jack, queen, king and ace in all four suits (clubs ♣, spades ♠, hearts ♥ and diamonds ♦).
  
<h3>Card Values:</h3> 
<ul>
  <li>Ace: 1 or 11 points (in general, 11 points, unless that would result in a score over 21 points. In this case, it takes the value of 1.) </li>
  <li>King: 10 points</li>
  <li>Queen: 10 points</li>
  <li>Jack: 10 points</li>
  <li>Numbers: as stated</li>
  <br>
  <li>'Black Jack' i.e. the combinations of Ace and 10 or Ace and King/ Queen/ Jack: 21 points</li>
</ul>

<h3>Description:</h3>

First, confirm that you want to play and enter the number and names of players.

The goal is to get one's points up to or as close to 21 points as possible. 
If a player has more than 21 points however, the player looses.

The program will act as the dealer.
It will deal one card for each player, one card for itself and then a second card for each player.

In case a player has 21 points already, they win immediately.

As long as nobody has reached 21 points, the program asks the players - one by one - if they want further cards.
If a player reaches 21 points, the winner is declared. Does a player's score exceed 21 points, they loose.

When no player wants further cards, it's the dealer's turn to draw. 
If the dealer's points reach 21, the dealer wins and all other players lose.

If the dealer ends up with more than 21 points, the dealer loses and the other players' cards will be evaluated.
In this case, the player with the most points wins the game and the game ends.
</p>
