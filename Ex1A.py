# ???????? ?????????, ??????? ????? ???????? ? ??????? ?????? ???????? ??????

while(True):
    res=input("Enter your number: ")
    try:
        num=int(res)
        if(int(res)>0):
            break
        else:
            print("Number must be positive!")
    except ValueError:
        print("That's not a number!")
for i in range(1, num+1):
    print("^"*i)