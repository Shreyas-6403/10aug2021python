#declare list type which carry 10 elements
lst = [1,2,3,4,5,6,7,8,9,0]
print("\n List",(lst))

#extract all list
x=lst[0:9]
print("\n extracted all list",(x))

#extract index number 2 to 5
y=lst[2:5]
print("\n Extracted index ",(y))

#print list element reverse
def Reverse(lst):
    new_lst = lst[::-1]
    return new_lst
print("\nReversed",Reverse(lst))

#using append, insert add elemenent in list

#Append
lst.append('new')
print("\n List with Append",(lst))

#insert
lst.insert(3, 'A')
print('\n Now with Insert:',(lst))

#add
lsttuple = ("Sample1", "Sample2")
lst.extend(lsttuple)
print("\n List with Add",(lst)) 

#Pop element
removed_element = lst.pop(2)
print('\n Removed Element:', removed_element)

#Clear List
lst.clear()

# Updated prime_numbers List
print('\n List after clear():', lst)
print("\n")
