x = 0
for num in range(5):
    x+=1
print(x)
# x will print 5 because it is 0 + 5

x = 3
for num in range(5):
    x+=1
print(x)

x = 3
for num in range (5):
    x+=2
print(x)

x=0
for num in range(5):
    x+=num
    # x = num + x
print(x)

x=0
for num in range(5):
    x*=num
print(x)

x=1
for num in range (1,5):
    x*= num
    # from 1 to 5 but never includes the ending (5)
print(x)

x=0
for num in range (10,12):
    x+=num
print(x)

x=0
for num in range(7,15): #8, 10, 12, 14 
    if(num%2==0):
        x+=num
    print(x)

x=0
for num in range(7,15): #x = 0
    if(num%2==0):       # num = 7
        x+=1
    else:
        x+=2
    print(x)
