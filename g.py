list=[5,3,2,4,1]
print('Unsorted list:',list)
i=len(list)-1
while i !=0:
    j=0
    while j<i:
        if list[0]>list[j+1]:
            t=list[j]
            list[j]=list[j+1]
            list[j+1]=t
        j+=1
    i-=1
print('shorted list:',list)
