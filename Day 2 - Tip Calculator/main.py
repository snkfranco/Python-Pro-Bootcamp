import os 

os.system('cls')

print('\n Welcome to the Tip Calculator!\n')

totalBill = float(input(' [+] Total bill: '))
percentageTip = int(input(' [+] Bill percentage ( 10% / 12% / 15% ) : '))
people = int(input(' [+] Number of people: '))

percentageValue = totalBill * (percentageTip / 100)

totalValue = totalBill + percentageValue

billForEachOne = totalValue / people

print(f'\n [+] Every person should pay: {billForEachOne:.2f}')