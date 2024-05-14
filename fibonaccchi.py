#0,1,1,2,3,5,8,13,....

a=0
b=1
sum=0

for i in range(1,15):
    next_number=a+b
    a=b
    b=next_number

    print(next_number)
