#PF-Assgn-55

#Sample ticket list - ticket format: "flight_no:source:destination:ticket_no"
#Note: flight_no has the following format - "airline_name followed by three digit number

#Global variable
ticket_list=["AI567:MUM:LON:014","AI077:MUM:LON:056", "BA896:MUM:LON:067", "SI267:MUM:SIN:145","AI077:MUM:CAN:060","SI267:BLR:MUM:148","AI567:CHE:SIN:015","AI077:MUM:SIN:050","AI077:MUM:LON:051","SI267:MUM:SIN:146"]

def find_passengers_flight(airline_name="AI"):
    #This function finds and returns the number of passengers travelling in the specified airline.
    count=0
    for i in ticket_list:
        string_list=i.split(":")
        if(string_list[0].startswith(airline_name)):
            count+=1
    return count

def find_passengers_destination(destination):
    #Write the logic to find and return the number of passengers traveling to the specified destination
    #pass
    #Remove pass and write your logic here
    count=0
    for i in ticket_list:
        string_list=i.split(":")
        if(string_list[2].startswith(destination)):
            count+=1
    return count

def find_passengers_per_flight():
    '''Write the logic to find and return a list having number of passengers traveling per flight based on the details in the ticket_list
    In the list, details should be provided in the format:
    [flight_no:no_of_passengers, flight_no:no_of_passengers, etc.].'''
    #pass
    #Remove pass and write your logic here
    pass_list=[]
    for i in ticket_list:
        flight_no=i[:5]
        no_of_passengers=find_passengers_flight(i[:5])
        flight_no=flight_no+":"+str(no_of_passengers)
        pass_list.append(flight_no)
    #print(pass_list)
    return list(set(pass_list))
        
    

def sort_passenger_list():
    #Write the logic to sort the list returned from find_passengers_per_flight() function in the descending order of number of passengers
    #pass
    #Remove pass and write your logic here
    sort_list=find_passengers_per_flight()
    
    
    new=[]
    for i in sort_list:
        i=i.split(":")
        #print(i)
        
        #new.append(i
        l=i[::-1]
        #print(l)
        new.append(l)
    new.sort(reverse=True)
    sort_list=new
    new=[]
    for i in sort_list:
        new.append(i[::-1])
    temp=""
    sort_list=[]
    for i in new:
        temp=i[0]+":"+i[1]
        sort_list.append(temp)
        
    #print(new)
    return sort_list

#Provide different values for airline_name and destination and test your program.
#print(find_passengers_per_flight())
#print(find_passengers_flight("AI"))
#print(find_passengers_destination("LON"))
print(sort_passenger_list())
