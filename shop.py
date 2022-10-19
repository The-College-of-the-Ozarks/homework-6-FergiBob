# shop.py
#
# 
while True:
    f = input('Please enter the file name of the product list: ')
    try:
        c = open(f,'r')
        break
        
    except:
        print('Invalid file name. Please try again.')
        
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
    
    if menuopt == 1:
    
    