num=int(input('enter a number:'))
first=0
sec=1
print(first,',',sec,end=',')
for i in range(2,num):
    next=first+sec
    print(next,end=',')
    first=sec
    sec=next
    
