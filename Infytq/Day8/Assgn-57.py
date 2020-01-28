#PF-Assgn-57
def check_prime(number):
    #pass #remove pass and write your logic here. if the number is prime return true, else return false
    if number>1:
        for i in range(2,number):
            if number%i==0:
                return False
        else:
            return True
    else:
        return False

def rotations(num):
    #pass #remove pass and write your logic here. It should return the list of different combinations of digits of the given number.
	#Rotation should be done in clockwise direction. For example, if the given number is 197, the list returned should be [197, 971, 719]
	num_list=[num]
	digit=len(str(num))
	power=10**(digit-1)
	for i in range(digit):
	    first=num//power
	    #print(first)
	    left=((num * 10) + first)-(first * power * 10)
	    num_list.append(left)
	    num=left
	return num_list[:-1]

def get_circular_prime_count(limit):
    #pass #remove pass and write your logic here.It should return the count of circular prime numbers below the given limit.
    count=0
    for i in range(limit):
        rotate=rotations(i)
        for j in rotate:
            if check_prime(j):
                flag=True
            else:
                flag=False
                break
        if flag:
            count+=1
    return count
        

#Provide different values for limit and test your program
print(get_circular_prime_count(1000))
