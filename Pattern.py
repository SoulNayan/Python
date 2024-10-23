# 1
# 21
# 321
# 4321
# 54321
# 4321
# 321
# 21
# 1
# for i in range(1,6):
#     j=i
#     for j in range(j,0,-1):
#         print("",j,end="")
#     print(" ")
# for i in range(4,0,-1):
#     j=i
#     for j in range(j,0,-1):
#         print("",j,end="")
#     print(" ")


#     1
#    12
#   123
#  1234
# 12345
#  2345
#   345
#    45
#     5
# for i in range(1,6):
#     for b in range(0,5-i):
#         print(" ",end=" ")
#     for j in range(1,i+1):
#         print("",j,end="")
#     print(" ")
# for i in range(2,6):
#     for b in range(0,1-i,-1):
#         print(" ",end=" ")
#     j=i    
#     for j in range(j,6):
#         print("",j,end="")
#     print(" ")


# 1        1
# 12      21
# 123    321
# 1234  4321
# 1234554321
# for i in range(1,6):
#     for j in range(1,i+1):
#         print("",j,end="")
#     for s in range(1,11-2*i):
#         print(" ",end=" ")
#     b=i    
#     for b in range(b,0,-1):
#         print("",b,end="")
#     print(" ")


# 1234554321
# 1234  4321
# 123    321
# 12      21
# 1        1
# for i in range(6,1,-1):
#     for j in range(1,i):
#         print("",j,end="")
#     for s in range(1,11-2*i+2):
#         print(" ",end=" ")
#     b=i-1   
#     for b in range(b,0,-1):
#         print("",b,end="")
#     print(" ")


# 1234554321
# 1234  4321
# 123    321
# 12      21
# 1        1
# 1        1
# 12      21
# 123    321
# 1234  4321
# 1234554321
# for i in range(6,1,-1):
#     for j in range(1,i):
#         print("",j,end="")
#     for s in range(1,11-2*i+2):
#         print(" ",end=" ")
#     b=i-1   
#     for b in range(b,0,-1):
#         print("",b,end="")
#     print(" ")
# for i in range(2,6):
#     for j in range(1,i+1):
#         print("",j,end="")
#     for s in range(1,11-2*i):
#         print(" ",end=" ")
#     b=i    
#     for b in range(b,0,-1):
#         print("",b,end="")
#     print(" ")


# 1
# 11
# 121
# 1331
# 14641
# for i in range(0,5):
#     n=1
#     for j in range(i+1):
#         print("",n,end="")
#         n=n*(i-j)//(j+1)
#     print(" ")


# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15
# c=1
# for i in range(1,6):
#     for j in range(i):
#         print("",c,end="")
#         c=c+1
#     print(" ")


# 1
# 10
# 101
# 1010
# 10101
# for i in range(1,6):
#     c=0
#     for j in range(i):
#         if(c==1):
#             c=0
#         else:
#             c=1    
#         print("",c,end="")
#     print(" ")


# 1
# 1 2
# 1 2 4  
# 1 2 4 7
# 1 2 4 7 11
# for i in range(1,6):
#     c=1
#     for j in range(1,i+1):
#         print("",c,end="")
#         c=c+j
#     print(" ")


# 1
# 2 4
# 3 6 9
# 4 8 12 16
# 5 10 15 20 25
# for i in range(1,6):
#     for j in range(1,i+1):
#         c=i
#         c=c*j
#         print("",c,end="")
#     print(" ")


