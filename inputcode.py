file = open("C:/Users/Admin/Desktop/text.txt","w") 

large1 = 6 + 1 
large2 = 6 + 1.75
large3 = 6 + 2.50
large4 = 6 + 3.35
large1tax = (6 + 1) * 0.13
large2tax = (6 + 1.75) * 0.13
large3tax = (6 + 2.50) * 0.13
large4tax = (6 + 3.35) * 0.13
large1totalcost = (6 + 1) * 1.13
large2totalcost = (6 + 1.75) * 1.13
large3totalcost = (6 + 2.50) * 1.13
large4totalcost = (6 + 3.35) * 1.13
extralarge1cost = 10 + 1
extralarge2cost = 10 + 1.75
extralarge3cost = 10 + 2.50
extralarge4cost = 10 + 3.35
extralarge1tax = (10 + 1) * 0.13
extralarge2tax = (10 + 1.75) * 0.13
extralarge3tax = (10 + 2.50) * 0.13
extralarge4tax = (10 + 3.35) * 0.13
extralarge1totalcost = (10 + 1) * 1.13
extralarge2totalcost = (10 + 1.75) * 1.13
extralarge3totalcost = (10 + 2.50) * 1.13
extralarge4totalcost = (10 + 3.35) * 1.13

pizza_cost = input('What size did you choose? Enter the size (large or extralarge) and then the number of toppings (between 1 and 4) example "large1" or "extralarge2"')

if pizza_cost == 'large1':
	file.write ( 'Subtotal: ${}'.format(round(large1, 2)))
	file.write ( 'Tax: ${}'.format(round(large1tax, 2)))
	file.write ( 'Total: ${}'.format(round(large1totalcost, 2)))

elif pizza_cost == 'large2':
	file.write ( 'Subtotal: ${}'.format(round(large2, 2)))
	file.write ( 'Tax: ${}'.format(round(large2tax, 2)))
	file.write ( 'Total: ${}'.format(round(large2totalcost, 2)))

elif pizza_cost == 'large3':
	file.write ( 'Subtotal: ${}'.format(round(large3, 2)))
	file.write ( 'Tax: ${}'.format(round(large3tax, 2)))
	file.write ( 'Total: ${}'.format(round(large3totalcost, 2)))

elif pizza_cost == 'large4':
	file.write ( 'Subtotal: ${}'.format(round(large4, 2))) 
	file.write ( 'Tax: ${}'.format(round(large4tax, 2)))
	file.write ( 'Total: ${}'.format(round(large4totalcost, 2)))

if pizza_cost == 'extralarge1':
	file.write ( 'Subtotal: ${}'.format(round(extralarge1cost, 2)))
	file.write ( 'Tax: ${}'.format(round(extralarge1tax, 2)))
	file.write ( 'Total: ${}'.format(round(extralarge1totalcost, 2)))

elif pizza_cost == 'extralarge2':
	file.write ( 'Subtotal: ${}'.format(round(extralarge2cost, 2)))
	file.write ( 'Tax: ${}'.format(round(extralarge2tax, 2)))
	file.write ( 'Total: ${}'.format(round(extralarge2totalcost, 2)))

elif pizza_cost == 'extralarge3':
	file.write ( 'Subtotal: ${}'.format(round(extralarge3cost, 2)))
	file.write ( 'Tax: ${}'.format(round(extralarge3tax, 2)))
	file.write ( 'Total: ${}'.format(round(extralarge3totalcost, 2)))

elif pizza_cost == 'extralarge4':
	file.write ( 'Subtotal: ${}'.format(round(extralarge4cost, 2))) 
	file.write ( 'Tax: ${}'.format(round(extralarge4tax, 2)))
	file.write ( 'Total: ${}'.format(round(extralarge4totalcost, 2)))
