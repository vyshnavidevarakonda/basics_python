import rand
print("🚩"*25,"HILL CLIMB FALL","🚩"*25)
a = input("enter player_1 name:")
b = input("enter player_2 name:")
list_a = []
list_b = []
i = 0
while(sum(list_a)!=10 and sum(list_b)!=10):
    if(i%2==0 and input("player_1 enter p to play:")=='p'):
        if(sum(list_a)<10):
            diceno = rand.diceroll()
            print("\ndice no. -->",diceno)
            list_a.append(diceno)
        else:
            list_a.clear()
        print("step no.-->",sum(list_a))
        i+=1
    elif(i%2!=0 and input("player_2 enter p to play:")=='p'):
        if(sum(list_b)<10):
            diceno = rand.diceroll()
            print("/ndiceno,-->",diceno)
            list_b.append(diceno)
        else:
           list_b.clear()
        print("step no. -->",sum(list_b))
        i+=1
    else: 
        print("Thankyou...")
        break
if(sum(list_a)==10):
    print("🏁"*10,f"{a} is the winner...😊","🏁"*10)
elif(sum(list_b)==10):
    print("🏁"*10,f"{b} is the winner...😊","🏁"*10)
else:
   print("Thankyou...")
