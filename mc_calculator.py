# Name:         Trace Sweeney
# Email:        sweenetr@oregonstate.edu
# Description:  Microservice which returns the amount of capitol a user would
#               need to add monthly to an account to reach their financial goals
# INPUT:        R = annual rate of return, G = Savings goal, P = Starting principal, Y = years to save
# OUTPUT:       Monthly Contribution amount
import time
import os

print('Microservice Active')
while True:
    time.sleep(0.5)
    if os.stat("user_input.txt").st_size != 0:
        user_input_file = open("user_input.txt", "r")
        input = user_input_file.read()
        user_input_file.close()
        monthly_savings_amount_file = open("monthly_savings_amount.txt", "w")
        currentline = input.split(",")
        R = float(currentline[0])
        G = int(currentline[1])
        P = int(currentline[2])
        Y = int(currentline[3])
        frequency = R/12
        interest = (1+frequency)**(Y*12)
        p_value = P*interest
        g_value = G - p_value
        numerator = frequency * g_value
        denominator = interest - 1
        monthly_contribution = numerator/denominator
        monthly_savings_amount_file.write(str(round(monthly_contribution, 2)))
        monthly_savings_amount_file.close()
