from random import randint
luckey_number = randint(1,100)
attempts = 1
while attempts <=5:
    num = int(input("Enter a number between 1 and 100: "))
    if num == luckey_number and attempts == 1:
        print('GENIOUS- Take a BOW')
        break
    elif num == luckey_number:
        print('YOU WIN with',attempts, 'attempts')
        break
    elif num > luckey_number:
        print('Go Small')
        attempts += 1
    else:
        print('Go Big')
        attempts += 1
if(attempts > 5):
    print('YOU ARE A LOOSER','The number is',luckey_number)
    