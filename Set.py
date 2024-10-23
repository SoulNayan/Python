# set=unique
# a={"jan","jan",12,45,56}
# print(type(a))

#Set Methods
#add()                            #add an element to set
#clear()                          #removes all the elements from the set
#copy()                           #return a copy of the set
#difference()                     #returns a set containg the difference between the two or more sets
#difference_update()              #remove the items in this set that are also insluded in another,specified set
#discard()                        #remove the specified item
#intersection()                   #return a set,that is the intersecion of two other set
#intersection_update()            #remove the items in this set that are not present in other,specified set(s)
#isdisjoint()                     #returns wjether two sets have a intersecton or not
#issubset()                       #return whether another set contain this set or not
#isuperset()                      #return whether another set contain this set or not
#pop()                            #removes an element from the set
#remove()                         #remove the specified element
#symmetric_difference()           #return a set with symmetric diffreence of two set
#symmetric_difference_update()    #insert the symmetric differences from this set and another
#union()                          #return a set containing the union of set
#update()                         #update the set with hte union of this set and others



# a={"jan","jan",12,45,56}  # to add value to set
# a.add(60)
# print(a)


# a={50,21,66,8,11,22,55}  #to add another set to current set(same value will displayed only once)
# b={10,20,30,40,51}
# a.update(b)
# print(a)


# a={50,21,66,8,11,22,55}  #to delete certain value
# a.remove(21)
# print(a)


# a={50,21,66,8,11,22,55}  # to delete certain value
# a.discard(21)
# print(a)


# a={50,21,66,8,11,22,55} #to delete last value but this is set so we don't know that which value will be deleted from last
# a.pop()
# print(a)


# a={50,21,66,8,11,22,55}  #to empty a set
# a.clear()
# print(a)


# a={50,21,66,8,11,22,55}  #to delete a set
# del a
# print(a)


# a={10,22,55,40}  
# b={10,22,40,50}
# print(a&b)


# a={10,22,55,40}  
# b={10,20,40,50}
# print(a.intersection(b))


# a={10,20,55,40}  
# b={10,20,40,50}
# a.intersection_update(b)
# print(a)


# a={10,22,55,40}  
# b={10,20,40,50}
# print(a-b)


# a={10,22,55,40}  
# b={10,20,40,50}
# print(a.difference(b))


# a={10,22,55,40}  
# b={10,20,40,50}
# c=a.symmetric_difference(b)
# print(c)


# a={10,22,55,40}  
# b={10,20,40,50}
# a.symmetric_difference_update(b)
# print(a)


# d1 = {"Monday", "Friday", "Saturday", "Sunday","Sunday"}
# d2={"Monday", "Tuesday", "Wednesday"}
# print(d1|d2)
 
 

# a={10,22,55,40}  
# b={10,20,40,50}
# a.isdisjoint(b)
# print(a)


# a={10,22,55,40}  
# b={10,20,40,50}
# a.issubset(b)
# print(a)


# a={10,22,55,40}  
# b={10,20,40,50}
# a.issuperset(b)
# print(a)