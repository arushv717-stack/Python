win_num=36
num=int(input("Enter a number  :"))
guess=1
while True:
    if win_num==num:
        print(f'{guess}')
        break
    else:
        if num < win_num:
            num=int(input("you guessed to 'low' number \n try again..."))
            guess+=1
        else:
            num=int(input("you guessed to 'high 'number \n try again..."))
            guess+=1
