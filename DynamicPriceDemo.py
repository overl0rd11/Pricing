# -*- coding: utf-8 -*-
"""
Created on Thu Jan 19 07:48:50 2017

@author: Arjun Kaul
"""
from random import randrange
import warnings
import numpy as np
from collections import Counter

df = {'70':[], '80':[], '90':[],'100':[]}


increment = 70
increment2=200
flag=0
flag2=0


while (flag<160):
    for i in df:
        if (i=='70'):
             df[i].append([randrange(60,80,1) + 100])
        elif (i=='80'):
             df[i].append([randrange(30,50,1) + 90])
        elif (i=='90'):
             df[i].append([randrange(10,30,1) + 75])
        else:
             df[i].append([randrange(0,10,1) + 70])
           
    flag+=1 
    
"""for i in df:
    print(df[i])"""

""" put in a sales number, lets say today's sales 
were 85 units at 100 Rs. You want to boost this 
sales number by 30 units. The price you would need
for this? and the maximum no. of sales units you
should increase for max profit will be determined
by this algorithm """

cost_price = 50
def k_nearest_neighbors(data, predict, k=5):
    if len(data) >= k:
        warnings.warn("K is set to a value less than total voting groups")
    distances = []
    for group in data:
        for features in data[group]:
            euc_dist = np.linalg.norm(np.array(features)-np.array(predict))
            distances.append([euc_dist, group])
    votes = [i[1] for i in sorted(distances)[:k]]
    vote_result = Counter(votes).most_common(1)[0][0]
    return vote_result
def maxprofit(data):
    profit=[]
    for i in data:
        for j in data[i][0]:
            profit.append(j*(int(i)-cost_price))
    return max(profit)
    

            
sold_today = input("Enter how many units you sold today:")
sell_price = input("what price did you sell them at?:")

today_profit = sold_today*(sell_price - cost_price)
if (maxprofit(df) <= today_profit):
    cont = input("You're doing better than or equal to the possible max profit you can attain using the algorithm already, it is recommended you continue with this and document this data so that after a while the algorithm can be retrained for better predictions, if you want to exit now, enter 1:")
    if (cont):
        exit(0)

want_sell = input("Enter how many total units you want to sell, please enter a realistic number:(max units sold till now are 179 at 70Rs/unit according to the data):")
    
result = k_nearest_neighbors(df,want_sell,k=5)
percentage_discount = sell_price*10/int(result)

predicted_profit = want_sell*(int(result) - cost_price)

if (today_profit >= predicted_profit):
    print("You are already getting better or equal profit by using today's prices, increasing discount here will increase sales but reduce profit. Careful!")

print ("Max possible profit of the dataset is:",maxprofit(df))
print ("Today's profit is:", today_profit)
print ("Expected profit from new sales number:",predicted_profit)
print(str(percentage_discount) + "% is the required discount to increase sales")
