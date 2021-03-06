#PF-Assgn-19

def calculate_bill_amount(food_type,quantity_ordered,distance_in_kms):
    bill_amount=0
    #write your logic here
    delivery_charge=0
    if distance_in_kms>0 and distance_in_kms<=3:
        delivery_charge=0
    elif distance_in_kms>3 and distance_in_kms<=6:
        delivery_charge=(distance_in_kms-3)*3
    elif distance_in_kms>6:
        delivery_charge=(distance_in_kms-6)*6+9
    else:
        bill_amount=-1
        return bill_amount
    if food_type=="V":
        if quantity_ordered>0:
            bill_amount=quantity_ordered*120+delivery_charge
        else:
            bill_amount=-1
    elif food_type=="N":
        if quantity_ordered>0:
            bill_amount=quantity_ordered*150+delivery_charge
        else:
            bill_amount=-1
    else:
        bill_amount=-1
    return bill_amount

#Provide different values for food_type,quantity_ordered,distance_in_kms and test your program
bill_amount=calculate_bill_amount("N",2,0)
print(bill_amount)
