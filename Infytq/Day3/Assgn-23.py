#PF-Assgn-23
def calculate_bill_amount(gems_list, price_list, reqd_gems,reqd_quantity):
    bill_amount=0
    #Write your logic here
    discount=0
    j=0
    for i in reqd_gems:
        if i in gems_list:
            index=gems_list.index(i)
            bill_amount+=price_list[index]*reqd_quantity[j]
            #print(bill_amount)
            j=j+1
        else:
            bill_amount=-1
            break
    if bill_amount>30000:
        discount=0.05*bill_amount
        bill_amount=bill_amount-discount
    return bill_amount

#List of gems available in the store
gems_list=["Emerald","Ivory","Jasper","Ruby","Garnet"]

#Price of gems available in the store. gems_list and price_list have one-to-one correspondence
price_list=[1760,2119,1599,3920,3999]

#List of gems required by the customer
reqd_gems=["Ivory","Emerald","Garnet"]

#Quantity of gems required by the customer. reqd_gems and reqd_quantity have one-to-one correspondence
reqd_quantity=[3,10,12]

bill_amount=calculate_bill_amount(gems_list, price_list, reqd_gems, reqd_quantity)
print(bill_amount)
