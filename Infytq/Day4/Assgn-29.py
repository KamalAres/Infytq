#PF-Assgn-29
def calculate(distance,no_of_passengers):
    #pass
    #Remove pass and write your logic here
    millage=10
    distance_covered=distance/millage
    cost=distance_covered*70
    #print(cost)
    passenger_cost=no_of_passengers*80
    #print(passenger_cost)
    if passenger_cost>=cost:
        return passenger_cost-cost
    return -1



#Provide different values for distance, no_of_passenger and test your program
distance=25
no_of_passengers=25
print(calculate(distance,no_of_passengers))
