'''
list1=[12,3,490]
for i in range(len(list1)):
    #print(i)
    print(i," ",list1[i])

for i in range(1,8):
    print(i)
print("\n")
for i in range(1,8,2):
    print(i)


x=0
while(x<9):
    print(x)
    x=x+1
    if(x==3):
        break

x=0
while(x<9):
    x=x+1
    if(x==3):
        continue
    print(x)

for x in range(10):
    if(x==3):
        continue
    print(x)

for x in range(10):
    if(x==3):
        break
    print(x)


x={}
print(type(x))
x={1:23,5:89}
x={1:"Hello",8:69.67}
x={1:"hello","ok":[1,2,3,4,5]}
#print(x)
#print(x.keys())
#print(x.values())
#print(x[1])
#print(x['hello'])
#x[1]="python"
x['hello']='CDAC'
print(x)


x=dict([(1,23),(2,45),("Hello","cdac")])
print(x)
print(x.keys())
print(x.values())
print(x[2])


x={1:23,4:"cdac","location":"noida"}
#x["location"]="pune"
#x.update({'course':'python'})
x[56]="noida"
print(x)
x[56]=800
print(x)


dict1={1:34,5:67,9:87}
dict2={"name":"cdac","location":"noida"}
dict1.update(dict2)
print(dict1)

dict1={1:34,5:67,9:87}
#print(dict1.pop(9))#delete the pair with key 1
#print(dict1.popitem())#delete the last inserted item
del dict1

print(dict1)

x={}.fromkeys(['math','science'],90)
print(x)
'''

x={1,2,3,4,"hello",1,2}
x=set([1,2,3])
x={}
print(type(x))
y=set()
print(type(y))
#print(x)














                 
                


































































































































    

























