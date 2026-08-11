t1=n1=int(input("enter a 1st number: "))
t2=n2=int(input("enter a 2nd number: "))
while True:
     if n1==n2:
         print(f'Two number:{t1},{t2}=GCD:{n1}')
         break
     elif n1>n2:
            n1=n1-n2
     else:
            n2-=n1
    
