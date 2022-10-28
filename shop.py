# shop.py
#
#


profit = 0

#file import prompt 
while True:
    f = input('Please enter the file name of the product list: ')
    try:
        c = open(f,'r')
        break
        
    except:
        print('Invalid file name. Please try again.')


#define and sort dictionaries
BuyDict = {}
SellDict = {}

for line in c:
    
    line = line.split('\t')
    if line[0] == 'Buy':
        BuyDict[line[1]]=line[2].replace('\n','').replace('$','')
    elif line[0] == 'Sell':
        SellDict[line[1]]=line[2].replace('\n','').replace('$','')
        
#menu                
while True:
    print('\n\n-------------------- Menu --------------------')
    print('Profit:',profit)
    print(' [1] Print Buy List')
    print(' [2] Print Sell List')
    print(' [3] Buy Item')
    print(' [4] Sell Item')
    print(' [5] Add item to Buy/Sell list')
    print(' [6] Change price of item in Buy/Sell list')
    print(' [7] Quit\n\n')
    print('*Enter the number of the desired option*\n')
    menuopt = input()
    
    if menuopt == '1':
        print(f'\n\nItem                                     Price\n')
        for key in list(BuyDict):
            print(f'{str(key).strip:40}${str(BuyDict[key]).strip}')
        input('\nPress enter to continue')

    elif menuopt == '2':
        print(f'\n\nItem                                     Price\n')
        for key in list(SellDict):
            print(f'{str(key):40}${str(BuyDict[key])}')
        input('\nPress enter to continue')

    elif menuopt == '3':
        buy = input('\n\nWhat would you like to buy?  ')
        for key in list(BuyDict):
            if key == buy:
                cost = int(str(BuyDict[key]))
                profit += cost
                BuyDict.pop(key)
            else:
                print('\nInvalid item\n\n')
    
    elif menuopt == '4':
        sell = input('\n\nWhat would you like to sell?  ')
        for key in list(SellDict):
            if key == sell:
                cost = int(str(BuyDict[key]))
                profit -= cost
                SellDict.pop(key)
            else:
                print('\nInvalid item\n\n')

    elif menuopt == '5':
        newItem = input('\n\nPlease enter the item name and its price seperated by a comma: ')
        newItem = newItem.split(',')
        while True:
            whichList = input('\nWould you like to add it to the list of items to (buy) or (sell)?').lower()
            if whichList == 'buy':
                BuyDict[newItem[0]] = newItem[1]
                break
            elif whichList == 'sell':
                SellDict[newItem[0]] = newItem[1]
                break
            else:
                print('\nInvalid list name\n')

    elif menuopt == '6':
        while True:
            whichList = input('\n\nWhich list is the item you wish to edit on: (buy) or (sell)?').lower()
            if whichList == 'buy':
                item = input('\nWhat is the name of the item you want to edit?  ')
                for key in list(BuyDict):
                    if key == item:
                        newPrice = input('\nWhat should the new price be?').replace('$','')
                        BuyDict[key] = newPrice
                break
            elif whichList == 'sell':
                item = input('\nWhat is the name of the item you want to edit?  ')
                for key in list(SellDict):
                    if key == item:
                        newPrice = input('\nWhat should the new price be?').replace('$','')
                        SellDict[key] = newPrice
                break
            else:
                print('\nInvalid list name\n')

    elif menuopt == '7':
        break
    else:
        print('\nPlease enter a valid option\n')
c.close