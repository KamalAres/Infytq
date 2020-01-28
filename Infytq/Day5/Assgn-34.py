#PF-Assgn-34
def find_pairs_of_numbers(num_list,n):
    #pass
    #Remove pass and write your logic here
    sum=0
    count=0
    num_list.sort()
    #print(num_list)
    for i in num_list:
        for j in num_list:
            #print(i,j)
            if i==j:
                #print("Hi")
                continue
                #print("Hi")
            sum=i+j
            if sum>=n:
                count=count+1
                #print(num_list,i,j)
                
                index=num_list.index(i)
                num_list[index]=0
                index=num_list.index(j)
                num_list[index]=0
                #print(num_list)
                #continue
            
            
        #print(num_list)
    #print(num_list,count)
    return count

num_list=[0,1,2,3,4,5,6,7,8]
n=8
print(find_pairs_of_numbers(num_list,n))
