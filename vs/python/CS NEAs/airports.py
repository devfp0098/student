file = open("/home/dev/vs/python/CS NEAs/Airports.txt")# ,'rt' is the default setting so doesnt need to be included
airports = {}
homecode = None
awaycode = None
firstclass = None
standardclass = None
flight = None
for line in file:
    line = line.strip()
    line = line.split(',')
    airports[line[0]] = {'code' : line[0], 'name' : line[1], 'distanceLPL' : int(line[2]), 'distanceBOH' : int(line[3])}

def flightdetails():
    global flight, firstclass, standardclass, flighttypes
    flighttypes = [['Medium narrow body', 8, 2650, 180, 8], ['Large narrow body', 7, 5600, 220, 10], ['Medium wide body', 5, 4050, 406, 14]]
    flight = input(f'''Which type of flight is it?
                   
1) {flighttypes[0][0]}
2) {flighttypes[1][0]}
3) {flighttypes[2][0]}

Enter type (1-3): ''')
    
    while flight not in ('1', '2', '3'):
        flight = input('Invalid. Re-enter: ')

    flight = int(flight) - 1
    
    print('\n' + f'''Type: {flighttypes[flight][0]}
Running cost per seat per 100km : £{flighttypes[flight][1]}
Maximum flight range(km): {flighttypes[flight][2]}
Capacity if all seats are standard-class: {flighttypes[flight][3]}
Minimum number of first-class seats(if any): {flighttypes[flight][4]}''')
    
    firstclass = input('\nEnter the number of first-class seats: ')
    valid = False
    while not valid:
        if firstclass.isdigit():
            if int(firstclass) != 0 and flighttypes[flight][3] < int(firstclass) < (flighttypes[flight][4]/2):
                firstclass = input('Invalid number of first-class seats. Re-enter: ')
            else:
                valid = True
        else: firstclass = input('Invalid. Re-enter: ') 
    
    firstclass = int(firstclass)
    standardclass = flighttypes[flight][3] - (firstclass*2)
    print(f'Standard-class seats: {standardclass}')
    pass

def airportdetails():
    global homecode, awaycode
    homecode = input('Enter the UK airport code: ')
    homecode = homecode.upper()
    while homecode not in ('LPL', 'BOH'):
        homecode = input('Invalid code. Re-enter: ')
        homecode = homecode.upper()

    awaycode = input('Enter the overseas airport code: ')
    awaycode = awaycode.upper()
    if len([code for code in airports.keys() if code == awaycode]):
        print(airports[awaycode]['name'])
    else:
        print('Invalid code.\n\n')
    pass

def profitcalc():
    if homecode == None or flight == None or awaycode == None or firstclass == None:
        return print('Airport details have not been entered.')
    
    if not flighttypes[flight][2] >= airports[awaycode][('distance'+homecode)]:
        return print('Flight range is insufficient for journey.')

    standardprice = input('Enter price of a standard-class seat: £')
    while (not standardprice.isdigit()) and (not (standardprice[-3] == '.' and int(standardprice[:-3]).isdigit() and int(standardprice[-2:]).isdigit())):
        standardprice = input('Invalid. Re-enter price: £')

    firstprice = input('Enter price of a first-class seat: £')
    while (not firstprice.isdigit()) and (not (firstprice[-3] == '.' and int(firstprice[:-3]).isdigit() and int(firstprice[-2:]).isdigit())):
        firstprice = input('Invalid. Re-enter price: £')
    
    standardprice, firstprice = int(standardprice), int(firstprice)
    costpseat = flighttypes[flight][1] * airports[awaycode]['distance'+homecode] / 100
    totalcost = costpseat * (firstclass + standardclass)
    income = (firstclass * firstprice) + (standardclass * standardprice)
    profit = income - totalcost
    print(f'''
Flight cost per seat: £{round(costpseat, 2)}
Flight cost: £{totalcost}
Flight income: £{income}
Flight profit: £{round(profit, 2)}''')
    pass

active = True
while active:
    menu = input('_____________________________________________________\nMenu:\n\n1) Enter airport details\n2) Enter flight details:\n3) Enter price plan and calculate profit\n4) Clear data\n5) Exit\n\nPick an option (1-5): ')
    while int(menu) not in range(1, 6):
                menu = input('Invalid. Re-enter: ')

    if menu == '1':
        airportdetails()
    elif menu == '2':
        flightdetails()
    elif menu == '3':
        profitcalc()
    elif menu == '4':
        homecode = None
        awaycode = None
        firstclass = None
        standardclass = None
        flight = None
    elif menu == '5':
        active = False
        print('\n\nquit')
        

file.close()