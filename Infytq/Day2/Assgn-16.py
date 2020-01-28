#PF-Assgn-16
def make_amount(rupees_to_make,no_of_five,no_of_one):
    five_needed=0
    one_needed=0

    #Start writing your code here
    #Populate the variables: five_needed and one_needed
    #print(no_of_one)
    #print(no_of_five)
    temp5=rupees_to_make//5
    if temp5<=no_of_five:
        five_needed=temp5
        temp1=rupees_to_make-(five_needed*5)
        if temp1<=no_of_one:
            one_needed=temp1
        else:
            one_needed=no_of_one
        
    else: 
        five_needed=no_of_five
        temp1=rupees_to_make-(five_needed*5)
        if temp1<=no_of_one:
            one_needed=temp1
        else:
            one_needed=no_of_one
        
    total=five_needed*5+one_needed
    if total==rupees_to_make:
        print("No. of Five needed :", five_needed)
        print("No. of One needed  :", one_needed)
    else:
        print(-1)
    
        

        
    


    # Use the below given print statements to display the output
    # Also, do not modify them for verification to work

    #print("No. of Five needed :", five_needed)
    #print("No. of One needed  :", one_needed)
    #print(-1)


#Provide different values for rupees_to_make,no_of_five,no_of_one and test your program
make_amount(105,20,5)
