#PF-Assgn-61
def validate_name(name):
    #Start writing your code here
    if len(name)>0 and len(name)<16:
        if name.isalpha():
            return True
    return False

def validate_phone_no(phno):
    #Start writing your code here
    if len(phno)==10 and phno.isdigit():
        if phno.count(phno[0])!=10:
            return True
    return False

def validate_email_id(email_id):
    #Start writing your code here
    domain_name=["gmail","yahoo","hotmail"]
    if email_id.find("@") and email_id.find(".com"):
        if email_id.count("@")>1:
            return False
        if email_id.count(".com")>1:
            return False
        temp=email_id.split("@")
        temp=temp[-1]
        temp=temp[:-4]
        #print(temp)
        if temp in domain_name:
            return True
    return False

def validate_all(name,phone_no,email_id):
    #Start writing your code here
    # Use the below given print statements to display appropriate messages
    # Also, do not modify them for verification to work
    if validate_name(name)==False:
        print("Invalid Name")
    elif validate_phone_no(phone_no)==False:
        print("Invalid phone number")
    elif validate_email_id(email_id)==False:    
        print("Invalid email id")
    else:
        print("All the details are valid")


#Provide different values for name, phone_no and email_id and test your program
validate_all("Tom@123", "9994599998", "tina@yahoo.com")
