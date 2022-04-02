#first I welcome the user
print()
print()
Welcome_heading = ('Welcome to Jonathans Terrific Tip Calculator!'.upper())# Using the .upper function to make sure my heading is in ALL CAPS.
print(Welcome_heading)
print()
# print('Welcome to Jonathans Terrific Tip Calculator!')
print()
print()
#then I will need some input from the user. I am doing this with input functions. I'm assigning there input all a variable. The program will ask the user each question in sequence after each one is answered until finished and move into the math section of code. Also using the /n line seperator.
bill = float(input('Please enter the bill total?\n'))
print()#leaving a space in between the lines for readability
patrons = int(input('How many patrons in the party?\n'))
print()
sales_tax = .07
sales_tax_owed = (bill * sales_tax)
tip = int(input('Percentage of tip given for service?\n'))
print()
tip_percentage = tip / 100.00 # "user input" for the variable {Tip} divided by 100 is the percentage equation and is assigned to a variable
print()
total_tip_given =  bill * tip_percentage # "user input" for {bill} times {tip_percentage} is equation for total tip given and assigned to a variable
print()
grand_total_amount = bill + total_tip_given + sales_tax # "user input" {bill} plus {total_tip_given} is equation for grand total amount and assigned to variable
print()
amount_per_patron = grand_total_amount / patrons # grand total amount of bill and tax times the amount of patrons using two variables
print()
grand_total = '{:.2f}'.format(amount_per_patron) # giving the grand total using the .format function and the {amount_per_patron} variable and the .2f meaning to format the display message 2 digits after the decimal point. (found this on Google. I could'nt figure out how to make it put the decimal point in to show the correct float format. figuring out this math was harder than the coding lol)
print()
print(f'Total tip amount: ${total_tip_given}')
print()
print(f'Tax:{sales_tax_owed}')
print()
print(f'Each patron should pay: ${grand_total}') #use a print statement with a f string and the {grand_total} variable to print out the total each patron should pay
print()
print(f'Grand total due: ${grand_total_amount}')
#using a print statement and a f string with the {bill} variable to give the grand total of the bill
print()
print()
print('Thank you for dining with us and using my Terrific Tip Calculator, please come again!')
print()
print()


