#PF-Tryout
#Start writing your code here
import random
def toss_coin():
    dict_coin={0:"H",1:"H",2:"H",3:"H",4:"H",5:"H",6:"H",7:"T",8:"T",9:"T"}
    result=random.randrange(0,10)
    return dict_coin.get(result)
    
print(toss_coin())
