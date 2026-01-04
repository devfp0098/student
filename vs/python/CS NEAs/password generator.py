import random as r

def displaymenu():
    option = input('\nMenu:\n\n1 - Check Password\n2 - Generate Password\n3 - Quit\n\nEnter a number (1-3):')
    while option not in ('1', '2', '3'):
        option = input('\nInvalid.\nRe-enter (1-3): ')
    return int(option)

def getpass():
    valid = False
    count = 1
    while not valid:
        if count:
            password = input('Enter password: ')
        else:
            password = input('Invalid.\nRe-enter password: ')
        for char in password:
            if char != ' ': 
                if ( 8 <= len(password) <= 24) and (ord(char) in range(65, 91) or ord(char) in range(97, 123) or char in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+')):
                    valid = True
        count = 0
    return password

def check(passw):
    global score
    global strength
    strength = ''
    score = len(passw)
    cap = 0
    low = 0
    letters = 0
    num = 0
    sym = 0
    row1 = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p']
    row2 = ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l']
    row3 = ['z', 'x', 'c', 'v', 'b', 'n', 'm']
    for char in passw:
        if char.isalpha():
            letters += 1
            if char.isupper():
                cap += 1
            else:
                low += 1
        elif char.isdigit():
            num += 1
        else:
            sym += 1
    
    if cap:
        score += 5
    if low:
        score += 5
    if num:
        score += 5
    if sym:
        score += 5
    if cap and low and num and sym:
        score += 10

    if letters == 0 and num == 0:
        score -= 5
    if letters == 0 and sym == 0:
        score -= 5
    if num == 0 and sym == 0:
        score -= 5

    for i in range(0, len(passw)-2):
        for key in range(0, len(row1)-2):
            if passw[i].lower() == row1[key] and passw[i+1].lower() == row1[key+1] and passw[i+2].lower() == row1[key+2]:
                score -= 5
        for key in range(0, len(row2)-2):
            if passw[i].lower() == row2[key] and passw[i+1].lower() == row2[key+1] and passw[i+2].lower() == row2[key+2]:
                score -= 5
        for key in range(0, len(row3)-2):
            if passw[i].lower() == row3[key] and passw[i+1].lower() == row3[key+1] and passw[i+2].lower() == row3[key+2]:
                score -= 5

    if score <= 0:
        strength = 'weak'
    elif score > 20:
        strength = 'strong'
    else:
        strength = 'medium'

def generate():
    valid = False
    end = ''

    allowed = []
    for n in range (65, 91):
        allowed.append(chr(n))
    for n in range(97, 123):
        allowed.append(chr(n))
    for n in range(0, 10):
        allowed.append(str(n))
    allowed.extend(['!', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+'])

    while not valid:
        length = r.randint(8, 12)
        for n in range(0, length+1):
            end += r.choice(allowed)
        check(end)
        if strength == 'strong':
            valid = True

    print(f'\n\n\nGenerated password: {end}\nScore: {score}')

valid = False
while not valid:
    quit = displaymenu()
    if quit == 1:
        check(getpass())
        print(f'Score: {score}\t\t\tStrength: {strength}')
    elif quit == 2:
        generate()
    elif quit == 3:
        valid = True
        print('\nquit')