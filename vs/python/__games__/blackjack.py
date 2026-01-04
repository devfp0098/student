import random as r
import time as t
def cardchange(card, player):
    if card <= 9:
        return card+1
    elif card in (10, 11, 12):
        return 10
    else:
        if player:
            ace = True
        else:
            dealerace = True
        return 11
def namecard(card):
    if 1 <= card <= 9:
        return card
    elif card == 10:
        return 'Jack'
    elif card == 11:
        return 'Queen'
    elif card == 12:
        return 'King'
    else:
        return 'Ace'
global ace
ace = False
global dealerace
dealerace = False
total = 0
dealertotal = 0
hit = True
while hit:
    card = cardchange(r.randint(1, 13), 1)
    print(f'\nYour card is: {namecard(card)}')
    if ace:
        if (total + card) <= 21:
            total += card
        else:
            total += (card - 10)
    else:
        total += card
    t.sleep(0.8)
    print(f'Your score is: {total}')

    if total == 21:
        print("\nYou win!")
        hit = not hit
    elif total > 21:
        t.sleep(1.2)
        print("\nYou lose!")
        hit = not hit
    else:
        t.sleep(0.8)
        again = input("Do you want to hit? (y/n): ")
        if again == 'n':
            hit = not hit
            while dealertotal < total and dealertotal < 21:
                dealercard1 = r.randint(1, 13)
                dealercard = cardchange(dealercard1, 0)
                if dealerace:
                    if (dealertotal + dealercard) <= 21:
                        dealertotal += dealercard
                    else:
                        dealertotal += (dealercard - 10)
                else:
                    dealertotal += dealercard
                print(f'\nDealer\'s card is: {namecard(dealercard1)}\nDealer\'s score is: {dealertotal}')
                t.sleep(1.2)
            if dealertotal > total and dealertotal <= 21:
                print("Dealer wins! You lose!")
            else:
                print("You win!")


t.sleep(10)     