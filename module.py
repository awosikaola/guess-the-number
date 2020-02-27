import random
secretno = random.randint(1, 20)
print('There is a number in my mind now between 1-20')

for guesstaken in range(1, 7):
    guess = int(input('Take a quick guess: '))
    if guess<secretno:
        print('your guess is a bit low, keep trying')
    elif guess>secretno:
        print('your guess is high, keep trying')
    else:
        break
if guess==secretno:
    print('You have done well champ, you guessed right in ' + str(guesstaken))
else:
    print('Nope, you missed all chances, the number i thought of was ' + str(secretno))