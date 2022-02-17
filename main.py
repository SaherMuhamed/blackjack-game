############### Blackjack Project #####################

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

import random
import replit
import art

#Declared functions..
def deal_card():
  """Returns a random cards from a deck."""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card


def calculate_score(list_cards):
  """Returns the sum of input lists."""
  if sum(list_cards) == 21 and len(list_cards) == 2:
    return 0
  if 11 in list_cards and sum(list_cards) > 21:
    list_cards.remove(11)
    list_cards.append(1)
  return sum(list_cards)  


#Hint: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.
def compare(user_score, computer_score):
  if user_score == computer_score:
    return "Draw"
  elif computer_score == 0:
    return "Lose, opponent has a Blackjack."
  elif user_score == 0:
    return "You win with a Blackjack."
  elif user_score > 21:
    return "You went over. You lose."
  elif computer_score > 21:
    return "Opponent went over. You win."
  elif user_score > computer_score:
    return "You win"
  else:
    return "You lose."


def play_game():
  user_cards = []
  computer_cards = []
  is_game_over = False
  
  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
  
  while not is_game_over:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"    Your cards: {user_cards}, current score: {sum(user_cards)}")
    print(f"    Computer's first card: {computer_cards[0]}")
    
    if user_score == 0 or computer_score == 0 or user_score > 21:
      is_game_over = True
    else:
      user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ").lower()
      if user_should_deal == 'y':
        user_cards.append(deal_card())
      else:
        is_game_over = True
  
  #Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.
  while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)
  
  print(f"    You final hand: {user_cards}, your final score: {user_score}")
  print(f"    Computer's final hand: {computer_cards}, computer's final score: {computer_score}")
  print(compare(user_score, computer_score))

#Hint: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.


print(art.logo)
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y'.lower():
  play_game()



