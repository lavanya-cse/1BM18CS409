def Fibonacci(n):
    a=0
    b=1
    if(n<0):
        print("incorrect input\n")
    elif(n==0):
        return a
    else:
        for i in range(0,n):
            print(a)
            c=a+b
            a=b
            b=c
        
def main():
    size=int(input("enter the size:"))
    Fibonacci(size)

main()
