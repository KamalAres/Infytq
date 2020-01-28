#PF-Exer-22

def generate_ticket(airline,source,destination,no_of_passengers):
    ticket_number_list=[]
    #Write your logic here
    for i in range(0,no_of_passengers):
        source=source[0:3]
        destination=destination[0:3]
        t_no=101+i
        ticket=airline+":"+source+":"+destination+":"+str(t_no)
        ticket_number_list.append(ticket)
    if len(ticket_number_list)>5:
        #print(ticket_number_list)
        ticket_number_list=ticket_number_list[-5:]
    

    #Use the below return statement wherever applicable
    return ticket_number_list

#Provide different values for airline,source,destination,no_of_passengers and test your program
print(generate_ticket("AI","Bangalore","London",7))
