# shop.py
#
#




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
        BuyDict[line[1]]=line[2].replace('\n','')
    elif line[0] == 'Sell':
        SellDict[line[1]]=line[2].replace('\n','')
        
#menu                
while True:
    print('-------------------- Menu --------------------')
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
        print(f'Item                    Price')
        for key in BuyDict:
            print(f'{'')





    elif menuopt == '7':
        break
    else:
        print('\nPlease enter a valid option\n')
c.close