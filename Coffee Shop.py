#Here's my coffee and muffin shop code! I added the choices of donuts and scones!

#First, we must define the variables. Technically, you do not have to do this part since the prices and percent for tax are unchanging, but I wanted to get more comfortable with variables.
variableCoffee = 5
variableMuffin = 4
variableDonut = 2
variableScone = 3
tax = (.06)

#Now, we have to get the customer inputs! I did the same thing for all choices. I asked for an input and assigned that input to both an integer and a variable for later use.

print('Hi, customer! We have muffins, coffee, donuts and scones!\n',
      'Muffins cost $4.00 each, coffee costs $5.00, donuts cost $2.00 and scones are $3.00!\n',
      'First, how many coffees would you like?')
    
coffee = input()
coffee = int(coffee)

print('Very good. How many muffins would you like?')

muffin = input()
muffin = int(muffin)

print('Great, how many donuts?')

donut = input()
donut = int(donut)

print('Lastly, how many scones?')

scone = input()
scone = int(scone)

#Now that that's done, I went ahead and completed the arithmetic step. Pretty easy once you have all of your variables named.

totalCoffee = (variableCoffee * coffee)

totalMuffin = (variableMuffin * muffin)

totalDonut = (variableDonut * donut)

totalScone = (variableScone * scone)

totalTax = (totalMuffin + totalCoffee + totalDonut + totalScone) * tax

totalWithtax = totalTax + (totalMuffin + totalCoffee + totalDonut + totalScone)

#Now, it is time for the receipt! I assigned the user's answer to 'Answer' to make it easy on myself. I also assigned the "Answer' to a string since the user is answering a "Yes" or "No" question; not a numerical question.

print('Would you like a receipt?')

Answer = input()
Answer = str(Answer)

#Here, I formatted these specific variables to show two decimal points at the end of the number. This was not necessary, but I added it because it makes my code look a lot nicer in my own opinion. I'm also sure there's a more efficient way to do this, but I don't know how yet!

totalCoffee = format(totalCoffee, ".2f")
totalMuffin = format(totalMuffin, ".2f")
totalDonut = format(totalDonut, ".2f")
totalScone = format(totalScone, ".2f")
totalTax = format(totalTax, ".2f")
totalWithTax = format(totalWithtax, ".2f")
totalWithtax = format(totalWithtax, ".2f")

#This is my first 'if' statement! I figured this assignment would be a fun way to try it out even though it is not asked for in the assignment.

if Answer in ['Yes','yes','yeah','yes please','Yes please']:
    print(

#The last part of the receipt (and the most messy in my opinion). Here I displayed all of the information my program already gathered to the user (if they ask for a receipt only, of course). The \n all indicate a new line to avoid messiness when actually running the program. I used the '{}'.format() to convert all of my variables to a string just for that statement; this is so that it could actually display to the user in the right format. You could also use variable = str(variable) to convert them. 
#I am still having some trouble with indentation and how it looks after the program has ran and I'm not sure why? I could definitely use some help in that area. I tried using \t but then only some statements took and not others.
        
'\n  *********************\n',
'My Coffee and Muffin Shop\n\n',
'Number of coffees bought?\n{}\n'.format(coffee),
'Number of muffins bought?\n{}\n'.format(muffin),
'Number of donuts bought?\n{}\n'.format(donut),
'Number of scones bought?\n{}\n'.format(scone),
'*********************\n\n\n',
'*********************\n',
'My Coffee and Muffin Shop Receipt\n',
'{}'.format(coffee) + ' Coffee(s) at $5.00 each: ${}\n'.format(totalCoffee),
'{}'.format(muffin) + ' Muffin(s) at $4.00 each: ${}\n'.format(totalMuffin),
'{}'.format(donut) + ' Donut(s) at $2.00 each: ${}\n'.format(totalDonut),
'{}'.format(scone) + ' Scone(s) at $3.00 each: ${}\n'.format(totalScone),
'6% tax: ${}\n'.format(totalTax),
'-----------\n  Total: ${}'.format(totalWithtax),
'\n *********************'
'\nHave a wonderful day! And thank you!')

#My last part! This is an 'if' statement as well. Just thought it would be fun to add it, considering I let my friends aand partner use my program to test it out and they just love pushing my me and my program's "buttons". Because everyone wants 2,000,000 donuts right?

if Answer in ['No','no']:
    print('No worries! Have a great day and enjoy your food!')
