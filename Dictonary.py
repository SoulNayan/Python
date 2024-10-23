# dictonary==>key value,name:sdfsd
# a={"name":"nayan"}
# print(type(a))
# print(a.items())
# print(a.values())
# print(a.keys())


# a={"name":"Nayan","Number":"09282354736","course":"Web dev"}
# print(a.keys())


# s1=dict({"name":"jaydip","number":"897867","course":"web design"})  #create dictionary using dict function
# print(s1)


# s1=dict([("name","jaydip"),("number","897867"),("course","web design")])
# print(s1)


# s1={"name":"jaydip","number":[1234,4556,678]}
# print(s1)

# s1={"name":"jaydip","number":[1234,4556,678]}
# print(s1["name"])

# s1={"name":"jaydip","number":[1234,4556,678]}
# print(s1.get('name'))


# s1={"name":"jaydip","number":[1234,4556,678]}
# print(s1.keys())
# print(s1.values())
# print(s1.items())


# s1={"name":"jaydip","number":[1234,4556,678]}
# for i in s1:
#     print(i,s1[i])


# s1={"name":"jaydip","number":[1234,4556,678],"course":"web design"}
# for i in s1.items():
#     print(i[0],i[1]) 


# s1={"name":"jaydip","number":[1234,4556,678],"course":"web design"}
# s1['fees']=35000
# s1.update({"job":"yes"})
# print(s1)


# s1={"name":"jaydip","number":[1234,4556,678],"course":"web design"}
# s1.update({"weight": 50, "height": 6})
# print(s1)


# s1={"name":"jaydip","number":[1234,4556,678],"course":"web design"}
# s1.update([("weight", 50), ("height", 6)])
# print(s1)


# s1={"name":"jaydip","number":3245546,"course":"web design"}
# s1.update([("weight", 50), ("height", 6)])
# s1.update({'state':'raj'})
# for i,j in s1.items():
#     print(i,":",j)


# s1={"name":"jaydip","number":3245546,"course":"web design"}
# # using pop('key')
# s1.pop('name')
# print(s1)


# s1={"name":"jaydip","number":3245546,"course":"web design"}
# s1.popitem()
# print(s1)


# s1={"name":"jaydip","number":3245546,"course":"web design"}
# del s1['number']
# print(s1)


# s1={"name":"jaydip","number":3245546,"course":"web design"}
# s1.clear()
# print(s1)


# s1={"name":"jaydip","number":3245546,"course":"web design"}
# del s1
# print(s1)


# s1={"name":"jaydip","number":3245546,"course":"python",'fees':50000}
# keyname="name"
# if keyname in s1.keys():
#     print('name is ',s1[keyname])
# else:
#     print('key not found')


# s1={"name":"jaydip","number":3245546,"course":"python",'fees':50000}
# s2={'education':'bca','result':'pass'}
# s1.update(s2)
# print(s1)


# s1={"name":"jaydip"}
# s2={'education':'bca'}
# s3={'result':'pass'}
# s={**s1,**s2,**s3}
# print(s)


# s1={"name":"jaydip",'number':54656}
# s2={'education':'bca','number':60000}
# s1.update(s2)
# print(s1)



# s1={"name":"jaydip","number":3245546,"course":"python",'fees':50000}
# s2=s1.copy()
# print(s2)


# s1={"name":"jaydip","number":3245546,"course":"python",'fees':50000}
# # sorting dictionary by keys
# print(sorted(s1.items()))


# s1={"name":50,"number":30,"course":20,'fees':10}
# # sorting dictionary by keys
# print(sorted(s1.values()))


# s1={"name":"jaydip","number":3245546,"course":"python",'fees':50000}
# s1["name"]+="nayan"
# # a=[]
# # b="nayan"
# # keyname="name"
# # for i,j in s1.items():
# #     if(i=="name"):
# #         a.append(s1[keyname])
# #         a.append(b)
# #         s1[keyname]=a
# print(s1)

