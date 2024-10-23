# def reverse(n):  #with argument-without return
#     sum=0
#     while(n!=0):
#         temp=n%10
#         sum=sum*10+temp
#         n=n//10
#     print(sum)

# n=int(input("valueee=="))
# reverse(n)


# def reverse():   #without argument-with return
#     sum=0
#     n=int(input("valueee=="))
#     while(n!=0):
#         temp=n%10
#         sum=sum*10+temp
#         n=n//10
#     return(sum) 

# print(reverse())



# def reverse(n):  #with argument-with return
#     sum=0
#     while(n!=0):
#         temp=n%10
#         sum=sum*10+temp
#         n=n//10
#     return(sum)

# n=int(input("valueee=="))
# print(reverse(n))



# def reverse():  #without argument-without return
#     sum=0
#     n=int(input("valueee=="))
#     while(n!=0):
#         temp=n%10
#         sum=sum*10+temp
#         n=n//10
#     print(sum)

# reverse()

# class -object==>oops
# collecttion of method and varaible
# blueprint of class,reprenative of class
# class demo:
#     def hello(self):
#         self.a=10
#         print("hello")
#     def hello1(self):
#         print(self.a)
# a=demo()
# a.hello()
# a.hello1()


# class sum:
#     def value(self):
#         self.a=[]
#         c=int(input("Enter List size::"))
#         for i in range(0,c):
#             b=int(input())
#             self.a.append(b)
#         sum.value1(self)
#     def value1(self):
#         b=self.a
#         sum=0
#         for i in range(0,len(b)):
#             sum+=b[i]
#         print("sum::",sum)
# a=sum()
# a.value()

# inheritence ===>inhete 
# base derive
# super sub
# perent child

# class demo:                    #single inheritence
#     def hello(self):
#         self.a=34
#         print("hello")
# class demo1(demo):    
#     def hello1(self):
#         print("hello1",self.a)
# a=demo1()
# a.hello()
# a.hello1()


# class demo:                           #multilevel inheritence
#     def hello(self):
#         self.a=30
#         print("Hello-A",self.a)
# class demo1:
#     def hello1(self):
#         self.b=35
#         print("Guys-B",self.b)
# class demo2((demo),(demo1)):
#     def hello2(self):
#         c=self.a+self.b
#         print("Sum of A and B::",c)
# a=demo2()
# a.hello()
# a.hello1()
# a.hello2()


# class demo:                           #multiple inheritence
#     def hello(self):
#         self.a=30
#         print("Hello",self.a)
# class demo1(demo):
#     def hello1(self):
#         self.b=35
#         print("Guys",self.b)
#         self.c=self.a+self.b
# class demo2(demo1):
#     def hello2(self):
#         print("Sum of A and B::",self.c)
# a=demo2()
# a.hello()
# a.hello1()
# a.hello2()



# class demo:                                  #Hierarchy inheritence
#     def hello(self):
#         self.a=35
#         print("This is main Class::",self.a)
# class demo1(demo):
#     def hello1(self):
#         b=40
#         c=self.a+b
#         print(b,"+",self.a)
#         print("This is 1st Child Class::",c)
# class demo2(demo):
#     def hello2(self):
#         b=80
#         c=b-self.a
#         print(b,"-",self.a)
#         print("This is 2nd Child Class::",c)
# a=demo1()
# b=demo2()
# a.hello()
# a.hello1()
# b.hello()
# b.hello2()



# class demo:                                  #Hybrid inheritence
#     def hello(self):
#         self.a=35
#         print("This is main Class::",self.a)
# class demo1(demo):
#     def hello1(self):
#         self.b=40
#         c=self.a+self.b
#         print(self.b,"+",self.a)
#         print("This is 1st Child Class::",c)
# class demo2(demo):
#     def hello2(self):
#         self.c=80
#         sum=self.c-self.a
#         print(self.c,"-",self.a)
#         print("This is 2nd Child Class::",sum)
# class demo3((demo1),(demo2)):
#     def hello3(self):
#         d=[]
#         d.append(self.a)
#         d.append(self.b)
#         d.append(self.c)
#         print("This Is 4th Class::",d)
# a=demo3()
# a.hello()
# a.hello1()
# a.hello2()
# a.hello3()



# class demo:
#     def getNO(self):
#         self.a=int(input("Enter Any Number::"))
#         print(self.a)
#         demo1.prime(self)
# class demo1(demo):
#     def prime(self):
#         cnt=0
#         for i in range(2,self.a):
#             if(self.a%i==0):
#                 cnt=cnt+1
#                 break
#         if(cnt==1):
#             print("Not Prime")
#         else:
#             print("Prime Number")
#         demo2.palindrome(self)
# class demo2(demo1):
#     def palindrome(self):
#         b=self.a
#         c=b
#         rev=0
#         while(b!=0):
#             rem=b%10
#             rev=rev*10+rem
#             b=b//10
#         if(c==rev):
#             print("palindrome Number")
#         else:
#             print("Not palindrome")
#         demo3.armstrong(self)
# class demo3(demo2):
#     def armstrong(self):
#         b=self.a
#         c=b
#         arm=0
#         while(b!=0):
#             rem=b%10
#             arm=rem*rem*rem+arm
#             b=b//10
#         if(c==arm):
#             print("Armstrong Number")
#         else:
#             print("Not Armstrong")
#         demo4.spynum(self)
# class demo4(demo3):
#     def spynum(self):
#         b=self.a
#         d=1
#         sum=0
#         while(b!=0):
#             rem=b%10
#             sum=sum+rem
#             d=d*rem
#             b=b//10
#         if(sum==d):
#             print("Spy Number")
#         else:
#             print("Not Spy Number")
# a=demo4()
# a.getNO()

#(Constructor):-"spacical type of method which is call autometic when we creat class object"
# class demo:
#     def __init__(self) :
#         print("hello")
# a=demo()


# def getno():
#     a=int(input("Enter Value::"))
#     return(palindrome(a))
# def palindrome(a):
#     b=a
#     rev=0
#     while(b!=0):
#         rem=b%10
#         rev=rev*10+rem
#         b=b//10
#     return(check(rev,a))
# def check(rev,a):
#     if(a==rev):
#         return("Palindrome Number")
#     else:
#         return("Not Palindrome Number")
# print(getno())