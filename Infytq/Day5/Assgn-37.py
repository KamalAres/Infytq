#PF-Assgn-37

#Global variables
child_id=(10,20,30,40,50)
chocolates_received=[12,5,3,4,6]

def calculate_total_chocolates():
    #pass
    #Remove pass and write your logic here to find and return the total number of chocolates
    total=0
    for i in chocolates_received:
        total=total+i
    return total

def reward_child(child_id_rewarded,extra_chocolates):
    #pass
    #Remove pass and write your logic here
    if child_id_rewarded in child_id:
        if extra_chocolates>0:
            
            index=child_id.index(child_id_rewarded)
            chocolates_received[index]=chocolates_received[index]+extra_chocolates
            print(chocolates_received)
        else:
            print("Extra chocolates is less than 1")
    else:
        print("Child id is invalid")
        
    


    # Use the below given print statements to display the output
    # Also, do not modify them for verification to work

    #print("Extra chocolates is less than 1")
    #print("Child id is invalid")
    #print(chocolates_received)


print(calculate_total_chocolates())
#Test your code by passing different values for child_id_rewarded,extra_chocolates
reward_child(20,2)
