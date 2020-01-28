#PF-Assgn-56

def max_frequency_word_counter(data):
    word=""
    frequency=0
    data=data.lower()
    list=data.split(" ")
    #print(list)
    for i in list:
        if list.count(i)>frequency:
            frequency=data.count(i)
            word=i
    #start writing your code here
    #Populate the variables: word and frequency


    # Use the below given print statements to display the output
    # Also, do not modify them for verification to work
    print(word,frequency)


#Provide different values for data and test your program.
data="Listen to the big clock Tick tock tick"
max_frequency_word_counter(data)
