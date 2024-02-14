variableCoffee = 5
variableMuffin = 4
tax = (.06)

print('Hi, customer! We have muffins and coffee!\nMuffins cost $4.00 each and coffee costs $5.00. First, how many coffees would you like?')
    
coffee = input()
coffee = int(coffee)

totalCoffee = (variableCoffee * coffee)


print('Very good. How many muffins would you like?')

muffin = input()
muffin = int(muffin)

totalMuffin = (variableMuffin * muffin)

totalTax = (totalMuffin + totalCoffee) * tax

totalAll = totalMuffin + totalCoffee

totalWithtax = totalTax + (totalMuffin + totalCoffee)

print('Would you like a receipt?')

Answer = input()
Answer = str(Answer)

totalCoffee = format(totalCoffee, ".2f")
totalMuffin = format(totalMuffin, ".2f")
totalTax = format(totalTax, ".2f")
totalWithTax = format(totalWithtax, ".2f")

if Answer in ['Yes','yes','yeah','yes please','Yes please']:
    print(

'\n  *********************\n',
'My Coffee and Muffin Shop\n\n',
'Number of coffees bought?\n{}\n'.format(coffee),
'Number of muffins bought?\n{}\n'.format(muffin),
'*********************\n\n\n',
'*********************\n',
'My Coffee and Muffin Shop Receipt\n',
'{}'.format(coffee) + ' Coffee(s) at $5.00 each: ${}\n'.format(totalCoffee),
'{}'.format(muffin) + ' Muffin(s) at $4.00 each: ${}\n'.format(totalMuffin),
'6% tax: ${}\n'.format(totalTax),
'-----------\n  Total: ${}'.format(totalWithtax),
'\n *********************')

if Answer in ['No','no']:
    print('No worries! Have a great day and enjoy your food!')
