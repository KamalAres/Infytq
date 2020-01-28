#PF-Assgn-26

def solve(heads,legs):
    error_msg="No solution"
    chicken_count=0
    rabbit_count=0

    #Start writing your code here
    if legs%2==0 and heads<legs:
        #print("Hi1")
        if heads*4==legs:
            rabbit_count=heads
        elif heads*2==legs:
            chicken_count=heads
        else:
            #print("Hi2")
            #if heads*2<legs:
                #print("HI")
                for i in range(heads,0,-1):
                    chicken_count=heads-i
                    rabbit_count=i
                    #print(chicken_count,rabbit_count)
                    if chicken_count*2+rabbit_count*4==legs:
                        break
        print(chicken_count,rabbit_count)
                
    
    else:
        print(error_msg)
        
    
    #Populate the variables: chicken_count and rabbit_count



    # Use the below given print statements to display the output
    # Also, do not modify them for verification to work

   
    #

#Provide different values for heads and legs and test your program
solve(20,10)
