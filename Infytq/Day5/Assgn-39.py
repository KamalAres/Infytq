#PF-Assgn-39
#This verification is based on string match.     

#Global variables
menu=('Veg Roll','Noodles','Fried Rice','Soup')
quantity_available=[2,200,3,0]

'''This method accepts the item followed by the quantity required by a customer in the format item1, quantity_required, item2, quantity_required etc.'''
def place_order(*item_tuple):
    #pass
    #Remove pass and write your logic here
    item=[]
    quantity=[]
    for i in range(0,len(item_tuple)):
        if i%2==0:
            item.append(item_tuple[i])
        else:
            quantity.append(item_tuple[i])
    #print(item)
    #print(quantity)
    for i in item:
        if i in menu:
            index1=menu.index(i)
            index2=item.index(i)
            if(check_quantity_available(index1,quantity[index2])):
                print(i,"is available")
            else:
                print(i,"stock is over")
        else:
            print(i,"is not available")
    #for i in quantity:
        
            

    #Populate the item name in the below given print statements
    #Use it to display the output wherever applicable
    #Also, do not modify the text in it for verification to work
    
    #print("<item name>is not available")
    #print("<item name>stock is over")
    #print ("<item name>is available")
    
  


'''This method accepts the index position of the item requested by the customer in the quantity_available list, and the requested quantity of the item.'''

def check_quantity_available(index,quantity_requested):
    #pass
    #Remove pass and write your logic here to return an appropriate boolean value.
    if quantity_requested<=quantity_available[index]:
                #print(menu[index],"is available")
                quantity_available[index]-= quantity_requested
                return True
    
    return False

#Provide different values for items ordered and test your program
#place_order("Veg Roll",2,"Noodles",2)
place_order("Fried Rice",2,"Soup",1)
#print("<item name>is not available")
#print("<item name>stock is over")
'''print ("Veg Roll is available")
print ("Noodles is available")    
print ("Soup is available") 
print("Veg Roll stock is over")
print("Fried Rice1 is not available")'''

#print(False)
