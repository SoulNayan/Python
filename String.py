# a="jkhj"
# print("ghfh",a[1])
# for i in a:
#     print(i)


# str1='hello'
# print(type(str1))

# str2="world"
# print(type(str2))

# str3='''nayan'''   #triple quotes are genrally used for represent the multiline or docstring
# print(type(str3))




# str="Creative Multimedia"
#":" is slice operator
# print(str[0:])  #start with index 0 to end
# print(str[1:5]) #start with index 1 to 4th index
# print(str[2:4]) #star with index 2 to 3rd index
# print(str[:3])  #start with index 0 to 2nd index
# print(str[4:7]) #start with index 4 to 6th index



# str="Creative Multimedia"
# #with the help of slice operator ":" we can reverse the string by printing the negative index
# print(str[-1])
# print(str[-3])
# print(str[-2:])
# print(str[-4:-1])
# print(str[-7:-2])
# print(str[::-1]) #to reverser the given string


#string is immutable in python
# the current string can be assigned a completely toa new content as specified
# str="creative"
# str="design"
# print(str)



#String Operator:

#"+" it is known as concatenation operator to join the strings given either side of the operator
# str1="creative"
# str2="design"
# str1+=str2
# print(str1)

#"*" it is known as repetition operator.this operator is used for repetiton of string or to unpacking
# str="Hello"
# # str1=str*3
# # print(str1)
# #Unpacking: *str unpacks the string into individual characters,useful in function arguments.
# print(*str)

#"in" in python,'in' operator used to check if a sub-string exists within astring.it returns true if the substring is found and false otherwise.
# str="Hello World"
# str1= "Hello" in str
# print(str1)

#"not in" in python,'not in' operator used to check if a sub-string not exists within a string.it returns flase if the substring is found and true otherwise.
# str="Hello World"
# str1= "hello" not in str
# print(str1)

# str="hello World"      #to capitalized First Letter in String
# str=str.capitalize()
# print(str)

# str="HELLO WORLD"      #it returns string in lowercase
# str=str.casefold()
# print(str)


# str="Hello World Hello New Here"
# str=str.count("Hello",0,len(str))
# print(str)


# str="Hello World"
# str=str.endswith("Hello",0,5)
# print(str)