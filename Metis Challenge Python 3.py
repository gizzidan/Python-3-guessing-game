import random

print ("Hello, I have chosen a secret number between 0 and 100 (inclusive). Let's see if you can guess it in 10 tries." + '\n')

secret_number = random.randint(0,100)
guesses_left = 10

while 1 <= guesses_left <= 10:
  while True:
    try:
      guess = int(input("Please take a guess:"))
      break
    except ValueError:
      print ("Numbers only please!")
    
    
  if 0 <= int(guess) <= 100:
    guesses_left = guesses_left - 1
    
    if guess < secret_number:
      print ("You guessed too low")
    elif guess > secret_number:
      print ("You guessed too high")
    else:
      break
  else:
    print ("Your guess must be a number between 0 and 100")
    
if guess == secret_number:
  print ("You win! %d was the correct answer." % guess)
if guess != secret_number:
  print ("You lose! The secret number is %d." % secret_number)


  