secret_number = 5
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
  guess = int(input("Guess a number and get lucky: "))
  guess_count += 1 
  if guess_count == 1:
    if guess == secret_number:
        print("You won!")
        break
    print("You got it wrong, you have 2 more tries left.")
  if guess_count == 2:
    if guess == secret_number:
        print("You won!")
        break
    print("You got it wrong again, this is your last try, so make it count!")
  if guess == secret_number:
        print("You won!")
        break
else:
  print("Sorry, you didn't get lucky :(")
