'''
===================================================================================================================================================
Hello!
We are Julia Shen and Yolanda Shen, and this is our CS10 Final Project. 
We decided to make Battleship, but with a smart CPU.
===================================================================================================================================================
'''

from random import randint
from time import sleep


### Board Creation and Labelling ###

# 1: Player's ship + CPU guesses
board = []
for x in range(0, 8):
  board.append(["-"] * 8)

# 2: Player's guesses
player_guesses = []
for x in range(0, 8):
  player_guesses.append(["."] * 8)

def print_board(game_board):
  global board
  print( )
  print(' '.join(['   ', '0', '1', '2', '3', '4', '5', '6', '7']))
  print('   ________________')
  row_numb = 0
  for row in game_board:
    print(str(row_numb) + ' | ' + ' '.join(row))
    row_numb += 1
  if board == game_board:
    print('Your Ships (+ = ship, X = empty computer guess, ! = computer hit)')
  else:
    print('Your Guesses (0 = empty guess, ! = hit)')
  print( )

'==================================================================================================================================================='

### Welcome ###

for i in range(15):
  print('Welcome to Battleship!')
sleep(1)
for i in range(15):
  print('Please enlarge your terminal for this game.')
sleep(2)
print_board(player_guesses)
print("Board 1: Above is the board where you will guess the positions of the CPU's ships.")
print('=========================================================================================')
sleep(3)
print_board(board)
print("Board 2: Above is the board where the CPU's guesses and your ships will be.")
print('=========================================================================================')

sleep(3)

'==================================================================================================================================================='

### Player ship placement ###

# Player places first ship (1x1)
playershiplocations = []

def proper_input(text):           # Takes an input and makes sure it is a) an integer, and b) in range
  global board
  if type(text) == int and text in range(0, len(board)):
    return True
  else:
    return False

print("Place your 1x1 battleship (indicated by +)")
ship1_row = int(input("Ship Row: "))
ship1_col = int(input("Ship Col: "))
while not(proper_input(ship1_row)) and not(proper_input(ship1_row)):
    print("Oops, that's not a proper ship location.")
    ship1_row = int(input("Ship Row: "))
    ship1_col = int(input("Ship Col: "))
board[ship1_row][ship1_col] = "+"
playershiplocations.append([ship1_row, ship1_col])
print_board(board)

# Player places second ship (2x1)
ship2_row = 0
ship2_col = 0
ship2_part2_row = 0
ship2_part2_col = 0
def ship2_step1():
  global ship2_row
  global ship2_col
  print("Place the first half of your 2x1 battleship (indicated by +)")
  ship2_row = int(input("Ship Row: "))
  ship2_col = int(input("Ship Col: "))
  if not(proper_input(ship2_row)) and not(proper_input(ship2_col)):
    print("You need to enter an integer as a row/col.")
    return ship2_step1()
  elif ship2_row not in range(0, len(board)) or ship2_col not in range(0, len(board)):                         #test this
    print("Oops, that's not even in the ocean.")
    return ship2_step1()
  elif not(board[ship2_row][ship2_col] == '-'):
    print('There is already a ship there! Put this ship elsewhere.')
    return ship2_step1()
  else:
    board[ship2_row][ship2_col] = "+"
    print_board(board)
def ship2_step2():
  global ship2_row
  global ship2_col
  global ship2_part2_row
  global ship2_part2_col
  print("Place the second half of your 2x1 battleship (indicated by +) by inputting 'top', 'right', 'bottom', or 'left'. 'Top' places the second half directly above the first half, 'right' places it directly to the right, and so on." )
  direction = input("Direction: ")
  if direction == "top" and not(ship2_row == 0):
    ship2_part2_row = ship2_row - 1
    ship2_part2_col = ship2_col
  elif direction == "right" and not(ship2_col == 7):
    ship2_part2_row = ship2_row
    ship2_part2_col = ship2_col + 1
  elif direction == "bottom" and not(ship2_row == 7):
    ship2_part2_row = ship2_row + 1
    ship2_part2_col = ship2_col
  elif direction == "left" and not(ship2_col == 0):
    ship2_part2_row = ship2_row
    ship2_part2_col = ship2_col - 1
  else:
    print("That isn't a valid position for your battleship.")
    return ship2_step2()
  if not(board[ship2_part2_row][ship2_part2_col] == "-"):
    print('There is already a ship there! Put this ship elsewhere.')
    return ship2_step2()
  else:
    board[ship2_part2_row][ship2_part2_col] = "+"
    print_board(board)

ship2_step1()
ship2_step2()
playershiplocations.append([ship2_row, ship2_col])
playershiplocations.append([ship2_part2_row, ship2_col])

#Player places third ship (2x1)
ship3_row = 0
ship3_col = 0
ship3_part2_row = 0
ship3_part2_col = 0
def ship3_step1():
  global ship3_row
  global ship3_col
  print("Place the first half of your second 2x1 battleship (indicated by +)")
  ship3_row = int(input("Ship Row: "))
  ship3_col = int(input("Ship Col: "))
  if not(proper_input(ship3_row)) and not(proper_input(ship3_col)):
    print("You need to enter an integer as a row/col.")
    return ship2_step1()
  elif ship3_row not in range(0, len(board)) or ship3_col not in range(0, len(board)):
    print("Oops, that's not even in the ocean.")
    return ship3_step1()
  elif not(board[ship3_row][ship3_col] == '-'):
    print('There is already a ship there! Put this ship elsewhere.')
    return ship3_step1()
  else:
    board[ship3_row][ship3_col] = "+"
    print_board(board)
def ship3_step2():
  global ship3_row
  global ship3_col
  global ship3_part2_row
  global ship3_part2_col
  print("Place the second half of your 2x1 battleship (indicated by +) by inputting 'top', 'right', 'bottom', or 'left'. 'Top' places the second half directly above the first half, 'right' places it directly to the right, and so on." )
  direction = input("Direction: ")
  if direction == "top" and not(ship3_row == 0):
    ship3_part2_row = ship3_row - 1
    ship3_part2_col = ship3_col
  elif direction == "right" and not(ship3_col == 7):
    ship3_part2_row = ship3_row
    ship3_part2_col = ship3_col + 1
  elif direction == "bottom" and not(ship3_row == 7):
    ship3_part2_row = ship3_row + 1
    ship3_part2_col = ship3_col
  elif direction == "left" and not(ship3_col == 0):
    ship3_part2_row = ship3_row
    ship3_part2_col = ship3_col - 1
  else:
    print("That isn't a valid position for your battleship.")
    return ship3_step2()
  if not(board[ship3_part2_row][ship3_part2_col] == "-"):
    print('There is already a ship there! Put this ship elsewhere.')
    return ship3_step2()
  else:
    board[ship3_part2_row][ship3_part2_col] = "+"
    print_board(board)

ship3_step1()
ship3_step2()
playershiplocations.append([ship3_row, ship3_col])
playershiplocations.append([ship3_part2_row, ship3_part2_col])

print_board(player_guesses)
print_board(board)

'==================================================================================================================================================='

### Places computer battleships in random locations ###

domain = [2, 3, 4, 5]
cpu_ships = []
for x in range(0, 8):
  cpu_ships.append(["0"] * 8)

def random_row(board):                                                # Chooses a random value for the row
  return randint(1, len(board)-1)
def random_col(board):                                                # Chooses a random value for the col
  return randint(1, len(board)-1)
def random(domain):                                                   # Chooses a random item out a list
  return domain[randint(0, len(domain)-1)]

def onaship(row, col):                               # Checks if a new ship is on a previous ship
  if cpu_ships[row][col] == '+':
    return True
  else:
    return False

def nexttoship(row, col, max):                       # Checks that the new ship is not adjacent to any other CPU ships
  ship_count = 0
  if not(cpu_ships[row + 1][col] != '+'):
    ship_count += 1
  if not(cpu_ships[row - 1][col] != '+'):
    ship_count += 1
  if not(cpu_ships[row][col + 1] != '+'):
    ship_count += 1
  if not(cpu_ships[row][col - 1] != '+'):
    ship_count += 1
  if ship_count > max:
    return True
  else:
    return False

recur_count = 0
def acceptable_placement(row, domain1):              # Returns column value so ship is not adjacent or on top of other ships
  global recur_count
  col = random(domain1)
  if nexttoship(row, col, 0) or onaship(row, col):      # Checks if on top of or next to a ship
    recur_count += 1
    if recur_count > 4:                                 # Runs the function again, while providing solution for potential recursion
      row = random(domain1)
      return acceptable_placement(row, domain1)
    else:
      return acceptable_placement(row, domain1)
  else:
    return col

def cpuship_part2(row1, col1):                       # Creates back half of the 2x1 ships, with limitations
  posit = ['top', 'bottom', 'left', 'right']
  back = random(posit)
  if back == "top":                                    # Each if/elif statement adds the back half
    if nexttoship(row1 - 1, col1, 1):                                 # Each checks that the new back half is not adjacent to another ship
      return cpuship_part2(row1, col1)
    else:
      return [row1 - 1, col1]
  elif back == "right":
    if nexttoship(row1, col1 + 1, 1):
      return cpuship_part2(row1, col1)
    else:
      return [row1, col1 + 1]
  elif back == "bottom":
    if nexttoship(row1 + 1, col1, 1):
      return cpuship_part2(row1, col1)
    else:
      return [row1 + 1, col1]
  elif back == "left":
    if nexttoship(row1, col1 - 1, 1):
      return cpuship_part2(row1, col1)
    else:
      return [row1, col1 - 1]
  else:
    return cpuship_part2(row1, col1)

print('')
print('The computer is placing its battleships...')
sleep(2)
cpushiplocations = []

##CPU Ship 1
cpuship1_row = random_row(cpu_ships)
cpuship1_col = random_col(cpu_ships)
cpu_ships[cpuship1_row][cpuship1_col] = '+'
cpushiplocations.append([cpuship1_row, cpuship1_col])

## CPU Ship 2 
# Part 1 of CPU Ship 2
cpuship2_row = random(domain)
cpuship2_col = acceptable_placement(cpuship2_row, domain)
cpu_ships[cpuship2_row][cpuship2_col] = '+'
cpushiplocations.append([cpuship2_row, cpuship2_col])
# Part 2 of CPU Ship 2
cpuship2 = cpuship_part2(cpuship2_row, cpuship2_col)
cpuship2_part2_row = cpuship2[0]
cpuship2_part2_col = cpuship2[1]
cpu_ships[cpuship2_part2_row][cpuship2_part2_col] = '+'
cpushiplocations.append([cpuship2_part2_row, cpuship2_part2_col])

## CPU Ship 3
# Part 1 of CPU Ship 3
cpuship3_row = random(domain)
cpuship3_col = acceptable_placement(cpuship3_row, domain)
cpu_ships[cpuship3_row][cpuship3_col] = '+'
cpushiplocations.append([cpuship3_row, cpuship3_col])
# Part 2 of CPU Ship 3
cpuship3 = cpuship_part2(cpuship3_row, cpuship3_col)
cpuship3_part2_row = cpuship3[0]
cpuship3_part2_col = cpuship3[1]
cpu_ships[cpuship3_part2_row][cpuship3_part2_col] = '+'
cpushiplocations.append([cpuship3_part2_row, cpuship3_part2_col])

'==================================================================================================================================================='

### Starts the game ###

count = 1
player_count = 1
computer_count = 1
cpuships_hit = 0
playerships_hit = 0
print('=========================================================================================')
print('')
print('The game is now starting. You have 14 turns to find the CPU battleship.')
sleep(1)
print("It is now the player's turn to guess where the CPU's battleship is.")
sleep(1)

# Player turn function
def player(player_count):
  global cpuships_hit
  print('Player Turn ' + str(player_count) + '. ' + str(14 - player_count) + ' turns left.')
  print('')
  sleep(2)
  guess_row = int(input("Guess Row: "))
  guess_col = int(input("Guess Col: "))
  print('=========================================================================================')
  if guess_row not in range(0, len(board)) or \
    guess_col not in range(0, len(board)):               # Checks if it is in the ocean
    print("Oops, that's not even in the ocean.")
  elif player_guesses[guess_row][guess_col] == "0":      # Checks if guess has already been guessed before
    print("You guessed that one already." )
  elif [guess_row, guess_col] in cpushiplocations:       # Hit
    print("Congratulations! You hit one of the computer's battleships at: Row: " + str(guess_row) + ' Col: ' + str(guess_col))
    player_guesses[guess_row][guess_col] = '!'
    cpuships_hit += 1
    if cpuships_hit == 5:                                # Win
      for i in range(15):
        print("Win" * 15)
      print("Congratulations! You beat the computer!")
      sleep(1)
      print('The CPU ships were located at:')
      for location in cpushiplocations:
        print(location)
      print('You sank ' + str(cpuships_hit) + ' CPU ships.')
      print('Thanks for playing Battleship!')
      exit()
  else:                                                  # Miss
    print("You missed the computer's battleship!")
    player_guesses[guess_row][guess_col] = "0"
  print_board(player_guesses)


# Smart computer guessing
cpu_correct_guesses = {}
def cpu_smartguess(turn):                                     # Returns a guess based on previous guesses
  global board
  if (turn - 1) in cpu_correct_guesses.keys():
    posit = ['top', 'bottom', 'left', 'right']
    row = cpu_correct_guesses[turn - 1][0]
    col = cpu_correct_guesses[turn - 1][1]
    if row == 0:
      posit.remove('top')
    if row == 7:
      posit.remove('bottom')
    if col == 0:
      posit.remove('left')
    if col == 7:
      posit.remove('right')
    direc = random(posit)
    if direc == 'top':
      return [row - 1, col]
    elif direc == "right":
      return [row, col + 1]
    elif direc == "bottom":
      return [row + 1, col]
    elif direc == "left":
      return [row, col - 1]
  else:
    return [random_row(board), random_col(board)]

# Computer turn function
def cpu(computer_count):
  global playerships_hit
  print("Computer Turn " + str(computer_count))
  print('The computer is now guessing...')
  print('')
  sleep(2)
  cpusmartguess = cpu_smartguess(computer_count)
  cpuguess_row = cpusmartguess[0]            # Computer guesses smartly
  cpuguess_col = cpusmartguess[1]
  print('=========================================================================================')
  if board[cpuguess_row][cpuguess_col] != "-":                # Checks if guess has already been guessed before
    return cpu(computer_count)
  if [cpuguess_row, cpuguess_col] in playershiplocations:     # CPU guesses correctly
    print("The computer guessed " + str(cpuguess_row) + "," + str(cpuguess_col))
    print("Oh no! The computer hit your battleship!")
    sleep(1)
    board[cpuguess_row][cpuguess_col] = '!'
    cpu_correct_guesses[computer_count] = [cpuguess_row, cpuguess_col]
    playerships_hit += 1
    if playerships_hit == 5:                                  # Loss
      for i in range(15):
        print("Lose" * 15)
      print("Sorry, the computer beat you!")
      sleep(1)
      print('The CPU ships were located at:')
      for location in cpushiplocations:
        print(location)
      sleep(1)
      print('You sank ' + str(cpuships_hit) + ' CPU ships.')
      print("Thanks for playing Battleship!")
      exit()
  else:                                                       # Miss
    print("The computer guessed Row: " + str(cpuguess_row) + " Col: " + str(cpuguess_col))
    print("The computer missed your battleship!") 
    sleep(1)
    board[cpuguess_row][cpuguess_col] = "X" 
  print_board(board)
  sleep(4)

'========================================================================================='

### The actual game! ###S

## Alternating turns
while count < 28:
# Player turn
    if count % 2 == 1:
        print_board(player_guesses)
        player(player_count)
        player_count += 1  
        count += 1  
# Computer turn
    else:
        cpu(computer_count)
        computer_count += 1  
        count += 1  
  
## Ends game ##
if count == 28:
    print('The CPU ships were located at:')
    for location in cpushiplocations:
      print(location)
    print(" ")
    print('You hit a CPU ship ' + str(cpuships_hit) + ' times.')
    print('The CPU hit your ship ' + str(playerships_hit) + ' times.')
    print("Game Over. Thanks for playing Battleship!")
    exit()
