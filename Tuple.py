# a=(50,40,60,10,15,30)     #tuple is unmutable 
# print(type(a))


# a=(45,33,21,78,55,60,10)
# sum=0
# for i in range(0,len(a)):
#     sum+=a[i]
#     print("a(",i,")=",a[i])
# print("SUM==",sum)



# a=(45,33,21,78,55,60,10)
# c=a[0]
# for i in range(0,len(a)):
#     if(a[i]>c):
#         c=a[i]
# print("Max Value==",c)


# a=(45,33,21,78,55,60,10)
# c=a[0]
# for i in range(0,len(a)):
#     if(a[i]<c):
#         c=a[i]
# print("Min Value==",c)


# a=(45,33,21,78,55,60,10)
# a=list(a)
# for i in range(0,len(a)):
#     for j in range(0,len(a)):
#         if(a[i]>a[j]):
#             min=a[i]
#             a[i]=a[j]
#             a[j]=min
# a=tuple(a)
# print("",a)


# a=(45,33,21,78,55,60,10)
# a=list(a)
# for i in range(0,len(a)):
#     for j in range(0,len(a)):
#         if(a[i]<a[j]):
#             min=a[i]
#             a[i]=a[j]
#             a[j]=min
# a=tuple(a)
# print("",a)


# a=(45,33,21,78,55,60,10)
# a=list(a)
# b=int(input("Enter index Number::"))
# cnt=0
# for i in range(0,len(a)):
#     if(i==b):
#         c=int(input("Enter replace Value::"))
#         a[i]=c
#         cnt=cnt+1
# if(cnt==0):
#     print("Invalid Index")
# a=tuple(a)
# print("",a)


# a = ["cdmi", "creative", "true", "surat", "adajan", "kamrej"]
# b=[]
# n=input("value==")
# for i in range(0,len(a)):
#     if(n==a[i][0]):
#         b.append(a[i])
# print(tuple(b))


# a=(45,33,21,78,33,60,33)
# b=len(a)
# print(sum(a))
# print(max(a))
# print(min(a))
# b=a.count(33)
# b=a.index(33)
# print(list(a))
# print(a)


