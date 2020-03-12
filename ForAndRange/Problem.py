# 1. have the user enter their investment amount and expected interest
#2. each year their investment will increase by thier investment + thier investment * the interest rate
#3. print out their earnings after a 10 year period

#COMPOUND INTEREST

investment_amount = input('enter ur investment amt:')
investment_amount = float(investment_amount)
expected_interest = input("enter the percent of interest:")
expected_interest = float(expected_interest) * .01

for i in range(10):
    investment_amount =investment_amount+(investment_amount * expected_interest)
print('invest after 10 years {:.2f}'.format(investment_amount))