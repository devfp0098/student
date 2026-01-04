import random as r
import time as t

royalflush = 1
straightflush = 2
fourkind = 3
fullhouse = 4
flush  = 5
straight = 6
threekind = 7
twopair = 8
pair = 9
highcard = 10
chips = 50
randcard = []
pack = []#array [deck] in 1D
flop = ['?', '?', '?']
turn = '?'
river = '?'
allhands = []
foldedplayers = []
botstatus = {'p2': '', 'p3' : '', 'p4' : '', 'p5' : '', 'p6' : ''}
activeplayers = ['p1', 'p2', 'p3', 'p4', 'p5', 'p6']

deck = [['ca', 'cb', 'cc', 'cd', 'ce', 'cf', 'cg', 'ch', 'ci', 'cj', 'ck', 'cl', 'cm'], 
        ['da', 'db', 'dc', 'dd', 'de', 'df', 'dg', 'dh', 'di', 'dj', 'dk', 'dl', 'dm'], 
        ['ha', 'hb', 'hc', 'hd', 'he', 'hf', 'hg', 'hh', 'hi', 'hj', 'hk', 'hl', 'hm'], 
        ['sa', 'sb', 'sc', 'sd', 'se', 'sf', 'sg', 'sh', 'si', 'sj', 'sk', 'sl', 'sm']]# m = ace

for suit in deck:
    for card in suit:
        randcard.append(card)
        pack.append(card)

def deal():
    return randcard.pop(r.randint(0, len(randcard)-1))

handp1, handp2, handp3, handp4, handp5, handp6 = [deal(), deal()], [deal(), deal()], [deal(), deal()], [deal(), deal()], [deal(), deal()], [deal(), deal()]
allhands.append(handp1), allhands.append(handp2), allhands.append(handp3), allhands.append(handp4), allhands.append(handp5), allhands.append(handp6)   

def search(array, sought):
    left, right = 0, len(array) -1
    while left <= right:
        midpoint = (left + right) // 2
        if sought == array[midpoint]:
            return midpoint
        elif sought < array[midpoint]:
            right = midpoint - 1
        else:
            left = midpoint + 1
    return midpoint

def sort(array):
    for i in range(0,len(array)-1):
        for n in range(0,len(array)-i-1):
            if array[n] > array[n+1]:
                temp, array[n] = array[n], array[n+1]
                array[n+1] = temp
    return array

def getpos(hand, board):
    global cards
    cards = []#hand & board
    for card in hand:
        cards.append(card)
    for card in board:
        cards.append(card)
    sort(cards)
    pack_pos = []#pos of all cards in [cards] in the [pack]
    for card in cards:
        pack_pos.append(search(pack, card))
    global deck_pos
    deck_pos = []#pos of all cards in [cards] in the [deck]
    varcount = 0
    for index in pack_pos:
        if varcount < 13:
            deck_pos.append([0, index])
        elif varcount < 26:
            deck_pos.append([1, index-13])
        elif varcount < 39:
            deck_pos.append([2, index-26])
        else:
            deck_pos.append([3, index-39])
        varcount += 1
    sort(deck_pos)

def checkfinalhand(hand, board):
    getpos(hand, board)
    returnval = []
    for i in range(0, 7):
        for j in range(i+1, 7):
            curr_cards = [card for card in cards if (cards.index(card)) != i and (cards.index(card)) != j]
            curr_deck_pos = [card for card in deck_pos if (deck_pos.index(card)) != i and (deck_pos.index(card)) != j]
            if curr_cards[0][0] == curr_cards[1][0] == curr_cards[2][0] == curr_cards[3][0] == curr_cards[4][0]:#checks for flush
                if (curr_deck_pos[0][1] == curr_deck_pos[1][1]-1 == curr_deck_pos[2][1]-2 == curr_deck_pos[3][1]-3 == curr_deck_pos[4][1]-4) or (curr_deck_pos[4][0]-11 == curr_deck_pos[0][0]-1 == curr_deck_pos[1][0]-2 == curr_deck_pos[2][0]-3 == curr_deck_pos[3][0]-4):#check for straight
                    if curr_deck_pos[0][1] == 8:#checks for royalflush
                        returnval.append(royalflush)
                    else:
                        returnval.append(straightflush)
                else:
                    returnval.append(flush)
            elif (curr_deck_pos[0][1] == curr_deck_pos[1][1]-1 == curr_deck_pos[2][1]-2 == curr_deck_pos[3][1]-3 == curr_deck_pos[4][1]-4) or (curr_deck_pos[4][0]-11 == curr_deck_pos[0][0]-1 == curr_deck_pos[1][0]-2 == curr_deck_pos[2][0]-3 == curr_deck_pos[3][0]-4):#check for straight
                returnval.append(straight)

            for k in range(j+1, 5):#four of a kind
                curr_deck_pos4 = [card for card in curr_deck_pos if (curr_deck_pos.index(card)) != k]
                if curr_deck_pos4[0][1] == curr_deck_pos4[1][1] == curr_deck_pos4[2][1] == curr_deck_pos4[3][1]:
                    returnval.append(fourkind) 

                for l in range(k+1, 4):#three of a kind
                    curr_deck_pos3 = [card for card in curr_deck_pos4 if (curr_deck_pos4.index(card)) != l]
                    curr_deck_pos2 = [curr_deck_pos[k], curr_deck_pos[l]]
                    if curr_deck_pos3[0][1] == curr_deck_pos3[1][1] == curr_deck_pos3[2][1]:
                        if curr_deck_pos2[0][1] == curr_deck_pos2[1][1]:
                            returnval.append(fullhouse)
                        else:
                            returnval.append(threekind)
            
                for m in range(0, 4):
                    for n in range(m+1, 4):
                        curr_deck_pos2 = [card for card in curr_deck_pos4 if (curr_deck_pos4.index(card)) != m and (curr_deck_pos4.index(card)) != n]
                        curr_deck_pos2_2ndset = [curr_deck_pos4[m], curr_deck_pos4[n]]
                        if curr_deck_pos2[0][1] == curr_deck_pos2[1][1]:#first pair
                            if curr_deck_pos2_2ndset[0][1] == curr_deck_pos2_2ndset[1][1]:#second pair
                                returnval.append(twopair)
                            else:
                                returnval.append(pair)
    returnval.append(highcard)
    sort(returnval)
    return returnval[0]

def translate(card):
    suit = ''
    num = ''
    if card == '?':
        return '?                '
    if card[0] == 'c':
        suit = 'clubs'
    elif card[0] == 's':
        suit = 'spades'
    elif card[0] == 'h':
        suit = 'hearts'
    else:
        suit = 'diamonds'
    
    num = ord(card[1]) - 95
    if num >= 11:
        if num == 11:
            num = 'Jack'
        elif num == 12:
            num = 'Queen'
        elif num == 13:
            num = 'King'
        elif num == 14:
            num = 'Ace'
    returnline = f'{num} of {suit}'
    for n in range(len(returnline), 17):
        returnline += ' '#formatting
    return returnline

def showtable(reveal, round, folded):#bool, ['flop', 'turn', 'river'], [numbers that have folded]
    folded.append(1)
    folded = list(dict.fromkeys(folded))
    print('_____________________________________________________________________________\n')
    print('\n\n[Flop]:%21s    |%21s    |%21s\n\n%13s[Turn]:%21s    |  [River]:%21s'%(translate(flop[0]) if 'flop' in round else '?%8s'%(''), translate(flop[1]) if 'flop' in round else '?%8s'%(''), translate(flop[2]) if 'flop' in round else '?%8s'%(''),'', translate(turn) if 'turn' in round else '?%8s'%(''), translate(river) if 'river' in round else '?%8s'%('')))
    print('\n\n\nPlayer1:%-11sPlayer2:%-11sPlayer3:%-11sPlayer4:%-11sPlayer5:%-11sPlayer6:'%('', '', '', '', ''))
    if not reveal:
        for i in range(1, 7):
            if i in folded:
                print(f'{translate(allhands[i-1][0])}', end='%2s'%(''))
            else:
                print('%-16s'%('?'), end='%3s'%(''))
        print('')
        for i in range(1, 7):
            if i in folded:
                print(f'{translate(allhands[i-1][1])}', end='%2s'%(''))
            else:
                print('%-16s'%('?'), end='%3s'%(''))
    else:
        for i in range(1, 7):
            print(f'{translate(allhands[i-1][0])}', end='%2s'%(''))
        print('')
        for i in range(1, 7):
            print(f'{translate(allhands[i-1][1])}', end='%2s'%(''))
    print('\n_______________________________________________________________________________________')

def checkchanceswcurrhand(hand, board):
    totalhand = hand + board
    rf = []# all possible royalflushes
    for suit in ['c', 'd', 'h', 's']:
        rf.append([i for n in deck for i in n if i[0] == suit and i[1] >= 'i'])
    
    validcards = 0
    for suit in rf:
        temp = 0
        for card in totalhand:
            if card in suit:
                temp += 1
        if temp > validcards:
            validcards = temp
    
    if (validcards >= 3 and len(totalhand) == 5) or (validcards >= 4 and len(totalhand) == 6) or (validcards >= 5 and len(totalhand) == 7):
        return royalflush
    
    validcards = 0
    for suit in deck:
        for card in range(0, 9):
            temp = 0
            for card2 in totalhand:
                if card2 in deck[search(deck, suit)][card:card+5]:
                    temp += 1
            if temp > validcards:
                validcards = temp

    if (validcards >= 3 and len(totalhand) == 5) or (validcards >= 4 and len(totalhand) == 6) or (validcards >= 5 and len(totalhand) == 7):
        return straightflush
    
    validcards = 0
    for card1 in totalhand:
        temp = 0
        for rest in totalhand:
            if card1[1] == rest[1]:
                temp += 1
        if temp > validcards:
            validcards = temp
    
    if (validcards >= 2 and len(totalhand) == 5) or ((validcards >= 3 and len(totalhand) == 6) or (validcards >= 4 and len(totalhand) == 7)):
        return fourkind
    
    validcards = []
    totalhand2 = []
    for n in range(0, len(totalhand)):
        for i in range(0, len(totalhand)):
            if totalhand[n][1] == totalhand[i][1]:
                totalhand2.append(totalhand[n])
                totalhand2.append(totalhand[i])
    
    totalhand2 = list(dict.fromkeys(totalhand2))
    for i in range(0, len(totalhand2)):
        rest = [n for n in totalhand2[i+1:] if totalhand2[i][1] == n[1]]
        if len(rest) == 2:
            validcards.append(1)
            totalhand2.remove(rest[0]), totalhand2.remove(rest[1]), totalhand2.remove(totalhand2[i])
        elif len(rest) == 1:
            validcards.append(0)
            totalhand2.remove(rest[0]), totalhand2.remove(totalhand2[i])



    if (len(validcards) >= 1 and len(totalhand) == 5) or ((validcards.count(1) >= 1 or validcards.count(0) >= 2) and len(totalhand) == 6) or (validcards.count(1) >= 1 and validcards.count(0) >= 1):
        return fullhouse
    
    validcards = 0
    for card in totalhand:
        temp = 0
        for rest in totalhand[search(totalhand, card)+1:]:
            if card[0] == rest[0]:
                temp += 1
        if temp > validcards:
            validcards = temp
    
    if (validcards >= 3 and len(totalhand) == 5) or (validcards >= 4 and len(totalhand) == 6) or (validcards >= 5 and len(totalhand) == 7):
        return flush
    
    validcards = 0
    totalhand3 = [n[1] for n in totalhand]
    totalhand4 = list(dict.fromkeys(totalhand3))
    sort(totalhand4)
    for card in range(0, len(totalhand4)):
        temp = 0
        for rest in range(card+1, len(totalhand4)):
            if ord(totalhand4[card])+rest-card == ord(totalhand4[rest]):
                temp += 1
        if temp > validcards:
            validcards = temp

    if (validcards >= 2 and len(totalhand) == 5) or (validcards >= 3 and len(totalhand) == 6) or validcards >= 4:
        return straight
    
    validcards = 0
    for card in range(0, len(totalhand)):
        temp = 0
        for rest in range(card, len(totalhand)):
            if totalhand[card][1] == totalhand[rest][1]:
                temp += 1
        if temp > validcards:
            validcards = temp
    
    if (validcards >= 1 and len(totalhand) == 5) or (validcards >= 2 and len(totalhand) == 6) or validcards >= 3:
        return threekind
    
    return 0
    
def decipherchances(returnstatement): # returnstatement from def(checkchanceswcurrhand)
    raisebet = 1
    callbet = 2
    foldhand = 3
    if returnstatement in range(1, 5):
        return raisebet
    
    if returnstatement in range(5, 8):
        return callbet

    bluffchance = r.randint(1, 4)# chance that bot will bluff
    if bluffchance == 1:
        return 4
    else:
        return foldhand

def botaction(action, botnum, round): # action from def(decipherchances)
    bot = 'p' + str(botnum)
    if round == 'flop' or (round != 'flop' and action != 4):
        botstatus[bot] = action
    
    #set action
    if botstatus[bot] == 1:
        return 'raises'
    elif botstatus[bot] == 2:
        return 'calls'
    elif botstatus[bot] == 3:
        return 'folds!'
    else:
        if round != 'river':
            return 'calls'
        else:
            return 'raises'
        
def makebet(round):
    global chips
    global activeplayers
    if round == 'pre-flop':
        play = input('Do you want to play? (y/n): ')
        if play == 'n':
            return False
        chips -= 2
        print(f'\nPre-flop bet is 2 chips.\nYou have {chips} chips remaining.\n\n')
        t.sleep(3)
        return True

    occurredrounds = []
    if round == 'river':
        occurredrounds.extend(['flop', 'turn', 'river'])
    elif round == 'turn':
        occurredrounds.extend(['flop', 'turn'])
    else:
        occurredrounds.append('flop')

    showtable(False, occurredrounds, foldedplayers)
    t.sleep(3)
    if round in ('flop', 'turn'):
        bettingover = False
        amount = 0
        count = 0
        while not bettingover:
            for player in activeplayers:
                if player == 'p1':
                    if count == 0:
                        playermove = input('\n\n' + round.capitalize() + ':\nYou have ' + str(chips) +' chips.\nWhat do you want to do?\n\n1) Raise\n2) Call\n3) Fold\n\nPick an option(1-3): ')
                        while playermove not in ('1', '2', '3'):
                            playermove = input('Invalid. Re-enter(1-3): ')

                        t.sleep(1)
                        playermove = int(playermove)
                        if playermove != 3:
                            if playermove == 1:
                                raiseval = input('How much do you want to raise by? ')
                                while not raiseval.isdigit() or int(raiseval) not in range(1, 6):
                                    raiseval = input('Invalid.\nFor the flop you can only raise by up to 5 chips.\nRe-enter: ')
                                chips -= int(raiseval)
                            chips -= amount
                            amount = 0
                        else:
                            return False
                    else:
                        playermove = input('\n\nBet is ' + str(amount) + ' chips.\nYou have ' + str(chips) + ' chips.\nWhat do you want to do?\n\n1) Call\n2) Fold\n\nPick an option(1-2): ')
                        while playermove not in ('1', '2'):
                            playermove = input('Invalid. Re-enter(1-2): ')
                        
                        playermove = int(playermove)
                        if playermove == 2:
                            return False
                        else:
                            chips -= amount
                else:
                    if count == 0:
                        botmove = botaction(decipherchances(checkchanceswcurrhand(allhands[int(player[1])-1], table)), int(player[1]), round)
                        print('\nPlayer', player[1], botmove)
                        if botmove == 'folds!':
                            print(f'Player {player[1]}\'s cards are {translate(allhands[int(player[1])-1][0])} and {translate(allhands[int(player[1])-1][1])}' )
                            foldedplayers.append(player[1])
                            t.sleep(1)
                        
                        if botmove == 'raises':
                            botraiseval = r.randint(1, 5)
                            print('\033[FPlayer', player[1], botmove, 'by', botraiseval, 'chips.')
                            amount += botraiseval
                        
                        t.sleep(1)
                    else:
                        botmove = botaction(decipherchances(checkchanceswcurrhand(allhands[int(player[1])-1], table)), int(player[1]), round)
                        print('\nPlayer', player[1], '%s' %(botmove if botmove == 'folds!' else 'calls'))
                        t.sleep(1)
                        if botmove == 'folds!':
                            print(f'Player {player[1]}\'s cards are {translate(allhands[int(player[1])-1][0])} and {translate(allhands[int(player[1])-1][1])}' )
                            foldedplayers.append(player[1])
                            t.sleep(1)
            if count == 1 or amount == 0:
                bettingover = True
            count += 1
            activeplayers = [n for n in activeplayers if n[1] not in foldedplayers]

    if round == 'river':
        bettingover = False
        amount = 0
        count = 0
        while not bettingover:
            for player in activeplayers:
                if player == 'p1':
                    if count == 0:
                        playermove = input('\n\n' + str(round.capitalize()) + ':\nYou have ' + str(chips) + ' chips.\nWhat do you want to do?\n\n1) Raise\n2) Call\n3) Fold\n\nPick an option(1-3): ')
                        while playermove not in ('1', '2', '3'):
                            playermove = input('Invalid. Re-enter(1-3): ')

                        t.sleep(1)
                        playermove = int(playermove)
                        if playermove != 3:
                            if playermove == 1:
                                raiseval = input('How much do you want to raise by? ')
                                while not raiseval.isdigit() or int(raiseval) > 20:
                                    if raiseval.isdigit():
                                        raiseval = input('Invalid. You can only raise by up to 20 chips.\nRe-enter: ')
                                    else:
                                        raiseval = input('Invalid. Re-enter: ')
                                chips -= int(raiseval)
                            chips -= amount
                            amount = 0
                        else:
                            return False
                    else:
                        t.sleep(0.8)
                        playermove = input('\n\nBet is ' + str(amount) + 'chips.\n You have ' + str(chips) + 'chips.\nWhat do you want to do?\n\n1) Call\n2) Fold\n\nPick an option(1-2): ')
                        while playermove not in ('1', '2'):
                            playermove = input('Invalid. Re-enter(1-2): ')
                        
                        playermove = int(playermove)
                        if playermove == 3:
                            return False
                        else:
                            chips -= amount
                else:
                    if count == 0:
                        botmove = botaction(decipherchances(checkchanceswcurrhand(allhands[int(player[1])-1], table)), int(player[1]), round)
                        print('\nPlayer', player[1], botmove)
                        if botmove == 'folds!':
                            print(f'Player {player[1]}\'s cards are {translate(allhands[int(player[1])-1][0])} and {translate(allhands[int(player[1])-1][1])}.' )
                            foldedplayers.append(player[1])
                        
                        if botmove == 'raises':
                            botraiseval = r.randint(5, 21)
                            print('\033[FPlayer', player[1], botmove, 'by', botraiseval, 'chips.')
                            amount += botraiseval
                        
                        t.sleep(1)
                    else:
                        botmove = botaction(decipherchances(checkchanceswcurrhand(allhands[int(player[1])-1], table)), int(player[1]), round)
                        print('\nPlayer', player[1], '%s' %(botmove if botmove == 'folds!' else 'calls'))
                        t.sleep(1)
                        if botmove == 'folds!':
                            print(f'Player {player[1]}\'s cards are {translate(allhands[int(player[1])-1][0])} and {translate(allhands[int(player[1])-1][1])}.' )
                            foldedplayers.append(player[1])
                            t.sleep(1)
            if count == 1 or amount == 0:
                bettingover = True
            count += 1
            activeplayers = [n for n in activeplayers if n[1] not in foldedplayers]

    return True

def checkwin(winnerhands):
    if len(winnerhands) == 0:
        return True
    else:
        result = [n for n in winnerhands if n < checkfinalhand(handp1, table)]
        if len(result) > 0:
            return False
        else:
            full = {}
            for i in range(1, 7):
                full[('p'+str(i))] = [checkfinalhand(x, table) for x in allhands][i-1]
            for x, y in full.items():
                if y not in winnerhands:
                    del full[x]
            highest = dict.fromkeys(full.keys())

            if full['p1'] == 2:#straightflush
                for x in highest.keys():
                    endcards = allhands[int(x[1])-1] + table
                    for i in range(0, 6):
                        for j in range(i+1, 7):
                            endcards1 = [n for n in endcards if n not in (endcards[i], endcards[j])]
                            sort(endcards1)
                            if len([n for n in endcards1 if endcards1[0] == n[0]]) == 5:
                                endcards2 = [n[1] for n in endcards1]
                                if len([n for n in endcards2 if ord(n) in range(ord(endcards2[0]), ord(endcards2[0])+5)]) == 5:
                                    highest[x] = endcards2[-1]
                if len([n for n in highest.values() if n > highest['p1']]) == 0:
                    return True
                else:
                    return False
            
            if full['p1'] == 3:#fourkind
                for x in highest.keys():
                    endcards = allhands[int(x[1])-1] + table
                    for i in range(0, 5):
                        for j in range(i+1, 6):
                            for k in range(j+1, 7):
                                endcards1 = [n for n in endcards if n not in (endcards[i], endcards[j], endcards[k])]
                                endcards2 = [n[1] for n in endcards1]
                                if len([n for n in endcards2 if n == endcards2[0]]) == 4:
                                    highest[x] = endcards2[1]
                if len([n for n in highest.values() if n > highest['p1']]) == 0:
                    return True
                else:
                    return False

            if full['p1'] == 4:#fullhouse
                for x in highest.keys():
                    endcards = allhands[int(x[1])-1] + table
                    for i in range(0, 6):
                        for j in range(i+1, 7):
                            endcards1 = [n for n in endcards if n not in (endcards[i], endcards[j])]#5 cards
                            for k in range(0, 4):
                                for l in range(k+1, 5):
                                    endcards2 = [n for n in endcards1 if n not in (endcards1[k], endcards1[l])]#3 cards
                                    endcards3 = [n[1] for n in endcards2]# 3 ranks
                                    if len([n for n in endcards3 if n == endcards3[0]]) == 3 and endcards[i][1] == endcards[j][1]:
                                        highest[x] = endcards3[0]
                if len([n for n in highest.values() if n > highest['p1']]) == 0:
                    return True
                else:
                    return False
            
            if full['p1'] == 5:#flush
                for x in highest.keys():
                    endcards = allhands[int(x[1])-1] + table
                    for i in range(0, 6):
                        for j in range(i+1, 7):
                            endcards1 = [n for n in endcards if n not in (endcards[i], endcards[j])]
                            endcards2 = [n[0] for n in endcards1]
                            if len([n for n in endcards2 if n == endcards2[0]]) == 5:
                                sort(endcards2)
                                highest[x] = endcards2[-1]
                if len([n for n in highest.values() if n > highest['p1']]) == 0:
                    return True
                else:
                    return False

            if full['p1'] == 6:#straight
                for x in highest.keys():
                    endcards = allhands[int(x[1])-1] + table
                    for i in range(0, 6):
                        for j in range(i+1, 7):
                            endcards1 = [n for n in endcards if n not in (endcards[i], endcards[j])]
                            endcards2 = [n[1] for n in endcards1]
                            sort(endcards2)
                            if len([n for n in endcards2 if ord(n) in range(ord(endcards2[0]), ord(endcards2[0])+5)]) == 5:
                                highest[x] = endcards2[-1]
                if len([n for n in highest.values() if n > highest['p1']]) == 0:
                    return True
                else:
                    return False
                
            if full['p1'] == 7:#threekind
                for x in highest.keys():
                    endcards = allhands[int(x[1])-1] + table
                    for i in range(0, 4):
                        for j in range(i+1, 5):
                            for k in range(j+1, 6):
                                for l in range(k+1, 7):
                                    endcards1 = [n for n in endcards if n not in (endcards[i], endcards[j], endcards[k], endcards[l])]
                                    endcards2 = [n[1] for n in endcards1]
                                    if len([n for n in endcards2 if n == endcards2[0]]) == 3:
                                        highest[x] = endcards2[0]
                if len([n for n in highest.values() if n > highest['p1']]) == 0:
                    return True
                else:
                    return False
            
            if full['p1'] == 8:#twopair
                for x in highest.keys():
                    endcards = allhands[int(x[1])-1] + table
                    for i in range(0, 5):
                        for j in range(i+1, 6):
                            for k in range(j+1, 7):
                                endcards1 = [n for n in endcards if n not in (endcards[i], endcards[j], endcards[k])]#4 cards
                                for l in range(0, 3):
                                    for m in range(l+1, 4):
                                        endcards2 = [n for n in endcards1 if n not in (endcards1[l], endcards1[m])]#2 cards
                                        endcards3 = [endcards1[l] + endcards[m]]
                                        if endcards2[0][1] == endcards2[1][1] and endcards3[0][1] == endcards3[1][1]:
                                            highest[x] = (endcards2[0][1] if endcards2[0][1] > endcards3[0][1] else endcards3[0][1])
                if len([n for n in highest.values() if n > highest['p1']]) == 0:
                    return True
                else:
                    return False    
            
            if full['p1'] == 9:#pair
                for x in highest.keys():
                    endcards = allhands[int(x[1])-1] + table
                    for i in range(0, 3):
                        for j in range(i+1, 4):
                            for k in range(j+1, 5):
                                for l in range(k+1, 6):
                                    for m in range(l+1, 7):
                                        endcards1 = [n for n in endcards if n not in (endcards[i], endcards[j], endcards[k], endcards[l], endcards[m])]
                                        endcards2 = [n[0] for n in endcards1]
                                        if endcards2[0] == endcards2[1]:
                                            highest[x] = endcards2[0]
                if len([n for n in highest.values() if n > highest['p1']]) == 0:
                    return True
                else:
                    return False
            
            whole = [n for n in allhands if (search(allhands, n)+1) in [int(i[1]) for i in full.keys()]]
            whole = [i[1] for i in [n for n in whole]]
            p1ranks = [whole[0], whole[1]]
            sort(whole)
            if whole[0] not in p1ranks:
                return False
            else:
                return True

print('\n\n\n\033[1m♤♡POKER♧♢\033[0m\n\n')
gameactive = True
roundnumber = 0
rounds = ['pre-flop', 'flop', 'turn', 'river']
while gameactive:
    gameround = rounds[roundnumber]
    if roundnumber == 1:
        flop.clear()
        flop.extend([deal(), deal(), deal()])
        table = [n for n in flop]
    elif roundnumber == 2:
        turn = deal()
        table.append(turn)
    elif roundnumber == 3:
        river = deal()
        table.append(river)
    gameactive = makebet(gameround)
    if gameactive and roundnumber == 3:
        results = [checkfinalhand(n, table) for n in [i for i in allhands[1:] if search(allhands, i)+1 in [x[1] for x in activeplayers]]]
        winners = [n for n in results if n <= checkfinalhand(handp1, table)]
        if checkwin(winners) or (len(activeplayers) == 1 and activeplayers[0] == 'p1'):
            break
        else:
            gameactive = False

    if not gameactive and roundnumber >= 1:# folds or loses
        showtable(True, ['flop', 'turn', 'river'], [])
        print('\n\nYou lost. Work on that poker face.')
    roundnumber += 1

showtable(True, ['flop', 'turn', 'river'], [])
if gameactive:
    print('\n\nYou win!')
print('\n\n\033[1m♤♡POKER♧♢\033[0m')