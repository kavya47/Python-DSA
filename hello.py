
# List comprehensions

""" lst = [1,2,3,4,5,6,7,8,9,10] """
#a = [x+1 for x in lst] increment of list
#a = [x for x in lst if x>2 if x%2==0] #2 if conditions inside a list
#a=[x  if x>5 else 'hi is 4' for x in lst] # if else statements inside a list 
#a =['two' if x%2==0 else 'three' if x%3==0 else "not 2 or 3" for x in lst] # multiple if statements inside a list comprehension

## NESTED LIST COMPREHENSION
""" lst1=[1,2]
lst2=[3,4]
a=[(x,y) for x in lst1 for y in lst2]
print(a)
 """
# Lambda expresions 
""" 
x= lambda a:a+5
print(x(5)) """
"""
c=tuple("abc")
print("TUPLE======",c)

c=list("abc")
print("LIST=====",c)"""

# width=15
# height=12.0
# print(width//3)

cur_result=['bc']
print(cur_result[-1])