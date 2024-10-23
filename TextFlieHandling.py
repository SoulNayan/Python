# a=open("ppt.txt",'r')     #This is read File 
# for i in a:
#     print(i)



# a=open("ppt.txt",'w')    #This is To write and Edit In File
# a.write("Hello this is Soul")
# a.close()  



a=open("ppt.txt",'r')    #delete (task) 
for i in a:
    print(i)
    a=open("ppt.txt",'w')
    a.write("")
    a.close()
