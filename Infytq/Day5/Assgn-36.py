#PF-Assgn-36
def create_largest_number(number_list):
    #pass
    #remove pass and write your logic here
    number_list.sort()
    number_list.reverse()
    largest_number=""
    for i in number_list:
        largest_number=largest_number+str(i)
    largest_number=int(largest_number)
    return largest_number

number_list=[23,45,67]
largest_number=create_largest_number(number_list)
print(largest_number)
