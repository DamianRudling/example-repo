menu_list = ['cake' , 'scones' , 'butter' , 'cheese'] # creating a list

stock_dict = { 'cake' : 22, #creating a dictionary called stock_dict
        'scones' : 40,
        'butter' : 30,
        'cheese' : 10
        }

price_dict = { 'cake' : 25, #creating a dictionary called price_dict
        'scones' : 22,
        'butter' : 16,
        'cheese' : 20
        }

total = 0  #setting the total to zero to count the total price of all the stock at the end of the program

for item in menu_list:          # Using a for loop to loop through the menu_list. This will look for each item in the list and the corresponding item in each dictionary
        x = int(stock_dict[item])   # This is to make sure each keys value is an integer so that a mathematical calculation can take place
        y = int(price_dict[item])   # This foor loop uses the item in the menu list to loop through the corresponding items in the dictionaries
        total = total + (x*y)              # This totals the prices. Each individual price is calculated by multiplying the x and y values from the stock and price dictionaries. After it is multiplied, the values are summed to provide the total.

print (total)



