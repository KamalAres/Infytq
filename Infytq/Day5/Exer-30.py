#PF-Exer-30

def find_average(mark_list):
    try:
	    total=0
	    print("Hi",mark_list,len(mark_list))
	    for i in range(0, len(mark_list)):
		    total+=mark_list[i]
		    #print("Hi")
	    marks_avg=total/len(mark_list)
	    return marks_avg
    except TypeError:
        print("Incompatiable Datatype")
    except IndexError:
        print("Index out of range")
    except TabError:
        print("No idea")
    except ZeroDivisionError:
        print("Found zero Division Error")
        
try:
    
    m_list=[15, 26, 34, 24]
    print("Average marks:", find_average(m_list))
except NameError:
    print("Name Error")
except ValueError:
    print("Value Error")
except:
    print("Some Error")
