#PF-Assgn-3
#This verification is based on string match.

mileage=12
amount_per_litre=40
distance_one_way=190
per_head_cost=0
divisible_by_five=False

#Start writing your code from here
#Populate the variables: per_head_cost and divisible_by_five
distance_one_way=distance_one_way*2
total=distance_one_way/mileage
cost=total*amount_per_litre
per_head_cost=cost/4
if per_head_cost%5==0:
    divisible_by_five=True



#Do not modify the below print statements for verification to work
print(per_head_cost)
print(divisible_by_five)
