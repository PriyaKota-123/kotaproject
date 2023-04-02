'''1.prime number'''
##def fun(a):
##    def fun1():
##        n=int(input("enter a number"))
##        count=0
##        for i in range(1,n+1):
##            if n%i==0:
##                count=count+1
##
##        if count==2:
##            print("it is prime")
##        else:
##            print("not a prime")
##    return fun1
##@fun
##def fun3():
##    pass
##fun3()


'''2.WAP armstrong number'''

##def fun(a):
##    def fun1():
##        n=int(input("enter a number"))
##        sum=0
##        b=len(str(n))
##        temp=n
##        while(temp>0):
##            c=temp%10
##            sum=sum+c**b
##            temp=temp//10
##        if n==sum:
##            print("it is an armstrong number")
##        else:
##            print("not an armstrong")
##    return fun1
##@fun
##def fun3():
##    pass
##fun3()

'''3.WAP in strong number using outer and inner function'''

##def fun(a):
##    def fun1():
##        n=int(input("enter a number"))
##        sum=0
##        temp=n
##        while(n):
##            i=1
##            fact=1
##            rem=n%10
##            while(i<=rem):
##                fact=fact*i
##                i=i+1
##                sum=sum+fact
##                n=n//10
##                if(sum==temp):
##                    print("it is a strong number")
##                else:
##                    print("it is not strong number")
##    return fun1()
##@fun
##def fun3():
##    pass
##fun3()

'''4.WAP palindrome for intergers'''
##def fun(a):
##    def fun():
##        n=int(input("enter a number"))
##        temp=n
##        sum=0
##        while(temp>0):
##            c=temp%10
##            sum=sum*10+c
##            temp=temp//10
##        if sum==n:
##            print("it is palindrome")
##        else:
##            print("not a palindrome")
##    return fun
##@fun
##def fun3():
##    pass
##fun3()


'''5.WAP perfect number '''

##def fun(a):
##    def fun1():
##        n=int(input("enter a number"))
##        i=1
##        sum=0
##        while(i<n):
##            if n%i==0:
##                sum=sum+i
##            i=i+1
##        if n==sum:
##            print("it is perfect")
##        else:
##            print("it is not perfect")
##    return fun1
##@fun
##def fun2():
##    pass
##fun2()

'''6.WAP factorial number'''
##def fun(a):
##    def fun1():
##        n=int(input("enter a number"))
##        fact=1
##        for i in range(1,n+1):
##            fact=fact*i
##        print(fact)
##    return fun1
##@fun
##def fun2():
##    pass
##fun2()

'''7.WAP even or odd'''
##def fun(a):
##    def fun1():
##        n=int(input("enter a number"))
##        if n%2==0:
##            print("it is even")
##        else:
##            print("it is odd")
##    return fun1
##@fun
##def fun3():
##    pass
##fun3()

'''8.WAP odd and even'''

##def fun(a):
##    def fun1():
##        n=int(input("enter a number"))
##        if n%2!=0:
##            print("it is odd")
##        else:
##            print("it is even")
##    return fun1
##@fun
##def fun3():
##    pass
##fun3()
##


'''9.WAP converting octal to decimal'''
##def fun(a):
##    def fun1():
##        n=int(input("enter a number"))
##        sum=0
##        i=1
##        while(n):
##            c=n%10
##            n=int(n/10)
##            sum=sum+c*i
##            i=i*8
##        print(sum)
##    return fun1
##@fun
##def fun2():
##    pass
##fun2()

'''10.WAP lcm'''
def fun(n):
    def fun1():
        a=int(input("enter a number"))
        b=int(input("enter a number"))
        if a>b:
            great=a
        else:
            great=b
        lcm=False
        for i in range(great(a*b+1)):
            if not lcm:
                if((i%a)==0 &(i%b)==0):
                    lcm=True
                    great=i
        print(great)
    return fun1()
@fun
def fun3():
    pass
fun3()

