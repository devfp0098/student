import random as r
import time as t

def checkbet(bets):
    for bet in bets:
        if bet.isdigit():
            if bet in ('00', '0'):
                return True
            elif 1 <= int(bet) <= 36:
                return True
            else:
                return False
        else:
            if bet in ('odd', 'even', 'red', 'black', 'low', 'high'):
                return True
            else:
                return False

def turnover(bets, result):
    global payout
    payout = []
    for bet in bets:
        if bet.isdigit() and int(bet) == result:
            payout.append(35)
        elif bet == 'low' and 1 <= result <= 18:
            payout.append(2)
        elif bet == 'high' and 19 <= result <= 36:
            payout.append(2)
        elif bet == 'odd' and (result % 2 == 1):
            payout.append(2)
        elif bet == 'even' and (result % 2 == 0):
            payout.append(2)
        elif not bet.isdigit():#red/black/lose
            if 1 <= result <= 10 and result % 2 == 0 and bet == 'black':
                payout.append(2) 
            elif 1 <= result <= 10 and result % 2 == 1 and bet == 'red':
                payout.append(2)
            elif 11 <= result <= 18 and result % 2 == 0 and bet == 'red':
                payout.append(2)
            elif 11 <= result <= 18 and result % 2 == 1 and bet == 'black':
                payout.append(2)
            elif 19 <= result <= 28 and result % 2 == 0 and bet == 'black':
                payout.append(2)
            elif 19 <= result <= 28 and result % 2 == 1 and bet == 'red':
                payout.append(2)
            elif result >= 29 and result % 2 == 0 and bet == 'red':
                payout.append(2)
            elif result >= 29 and result % 2 == 1 and bet == 'black':
                payout.append(2)
            bet = str(bet)
        else:
            payout.append(0)

#array payout to be used with array debts  
money = 50
playagain = True
debts = []
earnings = []
wheel = [str(num) for num in range(1, 37)]
wheel.append('0'), wheel.append('00')
while playagain and money > 0:
    print("\n____________________________________________________________\n")
    bet = input("What do you want to bet on? ")
    bet = bet.split()
    validbet = checkbet(bet)
    while not validbet:
        bet = input("\nInvalid. Re-enter:\nWhat do you want to bet on (0, 00, 1-36, red, black, odd, even, low, high)? ")
        validbet = checkbet(bet)

    debts = []
    for num in range(0, len(bet)):
        print (f"\nYou have £{money}")
        debt = int(input(f"How much do you want to bet on {bet[num]}? £"))
        money -= debt
        validdebt = False
        while not validdebt:
            if debt >= money and num != len(bet)-1:
                debt = int(input("\nInvalid. Re-enter:\nHow much do you want to bet? "))
            else:
                validdebt = not validdebt
        debts.append(debt)
    
    ball = int(r.choice(wheel))
    turnover(bet, ball)
    for n in range(0, len(debts)):
        earnings.append((debts[n]*payout[n]))

    for n in earnings:
        money += n
    print("The ball lands on:")
    t.sleep(3)
    print(ball)
    print(f'\nYou have £{money} remaining.')
    if money == 0:
        print("\nYou ran out of money. Game over.")
    else:
        again = input('Do you want to play again? (y/n): ')
        while again not in ('y', 'n'):
            again = input('\nInvalid. Re-enter:\nDo you want to play again? (y/n): ')
        if again == 'n':
            playagain = False