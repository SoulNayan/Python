# a=[12,34,45,45]
# # print(type(a))
# print(a)
# print(a[1])
# for i in range(0,len(a)):
#     print("a[",i,"]=",a[i])


# a=[32,55,65,80,12,10,44]
# sum=0
# for i in range(0,len(a)):
#     sum+=a[i]
#     print("a[",i,"]=",a[i])
# print("Sum=",sum) 


# a=[320,55,65,8,12,10,44]
# c=a[0]
# for i in range(0,len(a)):
#     if(a[i]>c):
#         c=a[i]
# print("Max=",c)


# a=[320,55,65,8,12,10,44]
# c=a[0]
# for i in range(0,len(a)):
#     if(a[i]<c):
#         c=a[i]
# print("Min=",c)


# a=[50,40,60,10,15,30]
# for i in range(0,len(a)):
#    for j in range(0,len(a)):
#       if(a[i]>a[j]):
#          min=a[i]
#          a[i]=a[j]
#          a[j]=min
# print("",a)


# b=int(input("Enter index Number::"))
# a=[50,40,60,10,15,30]
# cnt=0
# for i in range(0,len(a)):
#     if(i==b):
#         c=int(input("Enter replace Value::"))
#         a[i]=c
#         cnt=cnt+1
# if(cnt==0):
#     print("Invalid Index")
# print("",a)   


# a=[]
# c=int(input("Enter Size=="))
# for i in range(0,c):
#     b=input()
#     a.append(b)
# print(a)


# a=[]
# c=int(input("Enter List size::"))
# for i in range(0,c):
#     b=int(input())
#     a.append(b)
# print(a)
# print("Sum of List::",sum(a))



# a=[23,34,3,4,3]
# b=[12,34,34]
# print(sum(a))
# print(min(a))
# print(min(a))
# a.append(b)
# a.extend(b)
# b=a.count(34)
# b=a.index(3)
# a.insert(2,45)
# print(tuple(a))
# a.pop(-2)
# a.remove(23)
# print(a)



# a=[]
# c=int(input("Enter List size::"))
# for i in range(0,c):
#     b=int(input())
#     a.append(b)
# print(a)
# print("Max Number::",max(a))


# a=[20,22,52,60,1,20]
# a.insert(4,100)
# print(a)


# a=[20,22,52,60,1,20]
# a.remove(20)
# print(a)



# a=[20,30,40,10,30,55]
# a=sum(a)
# print("sum",a)