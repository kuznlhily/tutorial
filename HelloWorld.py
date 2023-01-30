print("Hello World!")
list=[]
for i in range(20):
    list.append(i)
    print(i)
duou=[]
puou=[]
for t in list:
    if(t%2==0):
        duou.append(t)
    else:
        puou.append(t*2)
print(duou)
print(puou) 