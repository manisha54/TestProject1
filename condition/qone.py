'''
1.Price of a house is $1M.
If buyer has good credit,
they need to put down 10%
otherwise
they need to put down 20%.
Print the down payment.
'''
price_of_house = 1000000
credit = input("Do you have good credit yes or no?: ")
if credit == "yes":
    down_payment = int(price_of_house / 10)
else:
    down_payment = int(price_of_house /20)
print(f"the down payment for the buyer is: ${down_payment}")