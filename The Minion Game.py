# your code start here
s= input("enter a word  :")
Stuart=0
kevin = 0

length = len(s)

for i in range(length):
    if s[i] in ["a","E","I","O","U"]:
        kevin  += length-i
    else:
        Stuart += length-i
if (Stuart> kevin):
    print("Stuart", Stuart)
elif (Stuart< kevin):
    print("Kevin", kevin)
elif (Stuart==kevin):
        print("Draw")
else:
        print("Draw")