#PF-Exer-32

def human_pyramid(no_of_people):
    #pass #remove pass and place the recursive code the you had written earlier for this function
    if no_of_people==1:
        return 50
    else:
        return no_of_people*(50)+human_pyramid(no_of_people-2)


def find_maximum_people(max_weight):
    no_of_people=0
    #write your logic here. You may invoke recursive function human_pyramid() wherever applicable 
    count=0
    for i in range(1,max_weight+1,2):
        if human_pyramid(i)>max_weight:
            break
        else:
            count=i
    no_of_people=count
    
    return no_of_people

#Provide different values for max_weight and test your program
max_people=find_maximum_people(1000)
print(max_people)
