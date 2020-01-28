#PF-Exer-35

def count_names(name_list):
    count1=0
    count2=0
    s=[]
    #start writing your code here
    #Populate the variables: count1 and count2

    # Use the below given print statements to display the output
    # Also, do not modify them for verification to work
    #print("_at -> ",count1)
    #print("%at% -> ",count2)
    for i in name_list:
        if i.find("at")>=0:
            count2=count2+1
            s=i.split("at")
            if len(s[0])==1 and i.endswith("at"):
                count1=count1+1
    print("_at -> ",count1)
    print("%at% -> ",count2)

           


#Provide different names in the list and test your program
name_list=['at', 'dats']
count_names(name_list)
