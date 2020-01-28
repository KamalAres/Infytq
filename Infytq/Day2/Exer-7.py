#PF-Exer-7

def calculate_total_ticket_cost(no_of_adults, no_of_children):
    total_ticket_cost=0
    #Write your logic here
    rate_per_adult=37550.0
    rate_per_child=rate_per_adult/3
    adult_ticket_cost=no_of_adults*rate_per_adult
    child_ticket_cost=no_of_children*rate_per_child
    total=adult_ticket_cost+child_ticket_cost
    tax=(total*7)/100
    total=tax+total
    discount=(total*10)/100
    total_ticket_cost=total-discount

    return total_ticket_cost


#Provide different values for no_of_adults, no_of_children and test your program
total_ticket_cost=calculate_total_ticket_cost(5,2)
print("Total Ticket Cost:",total_ticket_cost)
