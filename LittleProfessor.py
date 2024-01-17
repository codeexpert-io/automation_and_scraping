#Little Professor
import random
#allows user choose valid difficulty
def main():
    while True:
        try:
            level=int(input("level: "))
            if level<1 or level>3:
                print("",end="")
            else:
                break
        except ValueError:
            print("",end="")
    game(level)

#gives game of chosen difficulty
def game(level):
    total=0
    while True:
        if level==1:
            a=1
            b=9
        elif level == 2:
            a = 10
            b = 99
        elif level == 3:
            a = 100
            b = 999
        for i in range(10):
            x=random.randint(a,b)
            y=random.randint(a,b)
            z=x+y
            try:
                ans=int(input(str(x)+"+"+str(y)+"="))
            except ValueError:
                ans = int(input(str(x) + "+" + str(y) + "="))
            if ans==z:
                total=total+1
            else:
                print("EEE")
                q=0
                while q<2:
                    ans = int(input(str(x) + "+" + str(y) + "="))
                    q=q+1
                    if ans==z:
                        total=total+1
                        break
                    elif q<2:
                        print("EEE")
                print(str(x) + "+" + str(y) + "="+str(z))
        print(total,"/10",sep="")
        break

if __name__=='__main__':
    main()


