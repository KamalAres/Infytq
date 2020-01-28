#PF-Assgn-32
def max_visited_speciality(patient_medical_speciality_list,medical_speciality):
    # write your logic here
    count1=0
    count2=0
    count3=0
    for i in patient_medical_speciality_list:
        if i=='P':
            count1=count1+1
        elif i=='O':
            count2=count2+1
        elif i=="E":
            count3=count3+1
        else:
            continue
    if count1>count2 and count1>count3:
        speciality="Pediatrics"
    elif count2>count3:
        speciality="Orthopedics"
    else:
        speciality="ENT"
        

    return speciality

#provide different values in the list and test your program
patient_medical_speciality_list=[301,'P',302, 'P' ,305, 'P' ,401, 'E' ,656, 'E']
medical_speciality={"P":"Pediatrics","O":"Orthopedics","E":"ENT"}
speciality=max_visited_speciality(patient_medical_speciality_list,medical_speciality)
print(speciality)
