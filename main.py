import random
import time

# Function to simulate a single spin of the slots
def spin_slots():
  # Generate 3 random numbers between 0 and 9
  slots = []
  for i in range(3):
    slots.append(random.randint(0, 9))

  return slots


# Function to check if the player has won
def check_win(slots):
  # Check if any five or more of the numbers are the same
  for slot in slots:
    if slots.count(slot) >= 2:
      # Apply the appropriate multiplier to the player's winnings
      if slot == 0:
        multiplier = 0.50
      elif slot == 1:
        multiplier = 0.70
      elif slot == 2:
        multiplier = 0.90
      elif slot == 3:
        multiplier = 1.00
      elif slot == 4:
        multiplier = 1.00
      elif slot == 5:
        multiplier = 1.00
      elif slot == 6:
        multiplier = 1.20
      elif slot == 7:
        multiplier = 1.30
      elif slot == 8:
        multiplier = 1.40
      elif slot == 9:
        multiplier = 1.50

      return multiplier
  return False



# Function to play the slots game
def play_slots(balance, bet):
  # Deduct the bet from the player's balance
  balance -= bet
  
  # Print the player's new balance
  print("Balance: ${:.2f}".format(balance))
  time.sleep(1)

  # Spin the slots
  slots = spin_slots()
  
  # Check if the player has won
  multiplier = check_win(slots)
  if multiplier:
    # Calculate the player's initial winnings
    initial_winnings = bet
    print("Spinning...")
    for slot in slots:
      print(slot)
      time.sleep(1) # Add a delay of 1 second
    print()
    
    # Print a message indicating that the user won
    print("You won!")
    
    # Apply the multiplier to the player's winnings
    initial_winnings *= multiplier
    
    # Print the player's final winnings
    print("You won ${:.2f}!".format(initial_winnings))

    # Calculate the player's new balance
    balance += initial_winnings
    
  else:
    print("Spinning...")
    for slot in slots:
      print(slot)
      time.sleep(1) # Add a delay of 1 second
    print()
    
    # Print a message indicating that the user lost
    print("You lost.")

  # Return the player's new balance
  return balance




# Function to create a user interface for the game
def game_ui():
  # Print a welcome message
  print("Welcome to the slots game!")

  
  # Set the player's starting balance
  balance = int(input("Enter your balance: "))
  
  # Check if the player has no balance
  if balance <= 0:
    print("Cannot play without a balance.")
    return
  
  # Format the starting balance as currency
  print("Your starting balance is: ${:,.2f}".format(balance))
  
  # Prompt the user to play the game
  play = input("Would you like to play? (y/n) ")
  
  # If the user does not want to play, print a goodbye message and exit the function
  if play == "n":
    print("Goodbye!")
    return
  
  # Keep playing the game until the user chooses to quit
  while play == "y":
    # Prompt the user to enter a bet
    bet = input("Enter an amount to bet from your balance: ")
    
    # Convert the bet to an integer
    bet = int(bet)
    
    # Check if the bet is less than or equal to 0
    if bet <= 0:
      print("Your bet must be greater than 0!")
      continue
    
    # Check if the bet is less than or equal to $5
    if bet > 5:
      print("You cannot bet more than $5!")
      continue
    
    # Play the game
    balance = play_slots(balance, bet)
    
    # Check if the player has run out of money
    if balance <= 0:
      print("You have run out of money. Game over.")
      break
    
    # Format the new balance as currency
    print("Your current balance is: ${:,.2f}".format(balance))
    
    # Prompt the user to play again
    play = input("Would you like to play again? (y/n) ")
    
    # If the user does not want to play again, print a goodbye message and exit the loop
    if play == "n":
      print("Thanks for playing, Goodbye!")
      break


# Start the game
game_ui()
