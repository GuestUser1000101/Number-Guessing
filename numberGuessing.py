import random
import time
import math

#HEY YOU!
#I see what you're doing there
#You're trying to cheat!
#Play the game normally >:(

difficulty = 100000

print('Trivial - 100')
print('Easy - 500')
print('Medium - 1000')
print('Hard - 5000')
print('Impossible - 10000')
print('Asian - 100000')
print('')
print('Enter the maximum range of the target')
while True:
  try:
    response = int(input('>'))
    if response >= 1:
      difficulty = response
      break
    else:
      print('Sorry, your input must be greater than 1')
  except:
    print('Sorry, your response was invalid, please try again')
print('')


def inputInt(prompt, inputRange=(1, difficulty)):
  while True:
    try:
      response = int(input(prompt))
      if response >= inputRange[0] and response <= inputRange[1]:
        return response
      else:
        print('Sorry, your input must be between ' + str(inputRange[0]) +
              ' and ' + str(inputRange[1]))
    except:
      print('Sorry, your response was invalid, please try again')


traps = [''] * (difficulty + 1
                )  #'p' Percise trap, 'r' Range trap, 's' Shuffle Trap
target = random.randint(1, difficulty)
guess = -1
guessCount = 1

while True:
  print('What location would you like to go to')
  guess = inputInt('>')

  if guess == target:
    if difficulty < 50000:
      print('')
      print('You win! The target is at ' + str(target))
      time.sleep(1)
      print('')
      print('You took ' + str(guessCount) + ' guesses')
      break
    elif difficulty < 100000:
      print('')
      print('''You've accomplished the impossible...''')
      time.sleep(3)
      print('')
      print('''But it's not over yet''')
      time.sleep(3)
      print('')
      print('You took ' + str(guessCount) + ' guesses')
      break
    else:
      print('')
      print('''No...''')
      time.sleep(3)
      print('')
      print('''You had dreams,''')
      time.sleep(1)
      print('')
      print('''aspirations,''')
      time.sleep(2)
      print('')
      print('''but you chose to do THIS...''')
      time.sleep(3)
      print('')
      print('''...why?''')
      time.sleep(3)
      print('')
      print('You took ' + str(guessCount) + ' guesses')
      break
  elif traps[guess] == 's':
    print('')
    print('Oh no, you landed on a shuffle trap!')
    time.sleep(1)
    print('')
    print('The target has moved to a new location and your turn was skipped')
    print('')
    target = random.randint(0, difficulty)
    time.sleep(1)

  else:
    print('')
    print('What tool would you like to use?')
    print('')
    time.sleep(1)
    print('1 Innacurate Distance Gauge')
    print('2 Random Range Radar')
    print('3 Precise Trap')
    print('4 Range Trap')

    tool = inputInt('>', (1, 4))

    if tool == 1:
      distance = str(abs(target - guess))
      distance = list(distance)
      random.shuffle(distance)
      if distance[0] == '0':
        del distance[0]
      distance = ''.join(distance)

      print('')
      print(
        'Your location is ' + distance +
        ' away from the target, but the digits in the distance were shuffled!')
    elif tool == 2:
      distance = abs(target - guess)
      radar = random.randint(math.ceil(difficulty / 6),
                             math.ceil(difficulty / 4))
      print('')
      print('You activate your radar')
      if distance <= radar:
        print('')
        print('The target is within your radar range of ' + str(radar) +
              ' units!')
      else:
        print('')
        print('The target is not within your radar range of ' + str(radar) +
              ' units.')
    elif tool == 3:
      print('')
      print('You placed a percise mine at ' + str(guess))
      time.sleep(1)
      print('')
      print('The mine will trigger when the target is on the mine')
      traps[guess - 1] = 'p'
    elif tool == 4:
      print('')
      print('You placed a range mine at ' + str(guess))
      time.sleep(1)
      print('')
      print(
        'The mine will trigger when the target is on or directly next to the mine'
      )
      traps[guess - 1] = 'r'

    time.sleep(2)
    move = random.randint(math.ceil(difficulty / 50),
                          math.ceil(difficulty / 25))
    print('')
    print('The target got scared and moved ' + str(move) + ' units')
    print('')
    time.sleep(1)
    if random.randint(0, 1) == 0:
      sign = -1
    else:
      sign = 1

    target += move * sign
    if target < 0:
      target += 2 * move
    elif target > difficulty:
      target -= 2 * move

  if random.randint(0, 1) == 0:
    sign = -1
  else:
    sign = 1

  if traps[target] == 'p':
    traps[target] = ''
    print('The target landed on a Percise Trap at ' + str(target) + '!')
    time.sleep(1)
    print('')
    print('The target got super scared and moved 1 unit')
    print('')
    target += sign
    if target < 0:
      target += 2
    elif target > difficulty:
      target -= 2
  elif traps[target - 2] == 'r' or traps[target -
                                         1] == 'r' or traps[target] == 'r':
    traps[target] = ''
    print('The target landed on a Range Trap at ' + str(target) + '!')
    time.sleep(1)
    print('')
    print('The target got super scared and moved 2 units')
    print('')
    target += sign * 2
    if target < 0:
      target += 4
    elif target > difficulty:
      target -= 4

  if guessCount % 3 == 0:
    time.sleep(2)
    print(
      '''The target placed a Shuffle Trap, but you don't know where it is''')
    print('')
    traps[target] = 's'
    time.sleep(2)

  #debugging ¯\_(ツ)_/¯
  print('target location:', target)
  print('')
  time.sleep(2)

  guessCount += 1
