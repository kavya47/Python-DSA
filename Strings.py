
#https://www.chase2learn.com/hackerrank-algorithms-solutions/
#https://www.geeksforgeeks.org/python-code-print-common-characters-two-strings-alphabetical-order/

# Removing duplicate letters as per the input without order T.C =o(n*n)    S.c=o(n)
def removeduplicates(s):
    res=[]
    for ch in s:
        if ch not in res:
            res.append(ch)
    return ''.join(res)


s="Protiijaayiiii"
# print("first====",removeduplicates(s))

# using set() method   T.C =o(n)    S.c=o(n)
def removeduplicates_1(s):
    se=set() # set doesn't contain duplicate values  , doesn't maintain order
    res=[]
    for ch in s:
        if ch not in res:
            se.add(ch)
            # print(se)
            res.append(ch)
    return ''.join(res)

s="Protiijaayiiii"
# print("second====",removeduplicates_1(s))

#remove duplicates uing Dict 
def removeduplicates_2(s):
    se={} # set doesn't contain duplicate values  , doesn't maintain order
    print(type(se))
    res=[]
    for index,ch in enumerate(s):
        if ch not in res:
            se[ch]=index
            # print(se)
            res.append(ch)
    return ''.join(res)

s="Protiijaayiiii"
# print("Third====",removeduplicates_2(s))

# remove dupplicates in lexographical order 

def removedupes(s):
    d={char:index for index,char in enumerate(s)}
    print(d)
    result=[]
    for index,char in enumerate(s):
        if char not in result:
            while result and index < d[result[-1]] and char < result[-1]:
                result.pop()
            result.append(char)
    return ''.join(result)

s="bcaba"
# print("fourth====",removedupes(s))

#duplicates in a array  Time Complexity: O(n)  Auxiliary Space: O(1)
def duplicate(input_list):
    new_dict, new_list = {}, []
    print(new_dict.items())
    for i in input_list:
        if not i in new_dict:
            new_dict[i] = 1
            # print(new_dict)
        else:
            new_dict[i] += 1
            # print("elseee",new_dict)
    for key, values in new_dict.items():
        if values > 1:
            new_list.append(key)
 
    return new_list

input_list=[1, 2, 1, 2, 3, 4, 5, 1, 1, 2, 5, 6, 7, 8, 9, 9]
# print("fourth====",duplicate(input_list))

# COUNT FREQUENCY OF  all the WORDS IN A STRING

def stri_freq(s):
    all_freq = {}
    for i in s:
        if i in all_freq:
            all_freq[i] += 1
        else:
            all_freq[i] = 1 
    return all_freq

s="so,what can i do"
# print("count==",stri_freq(s))

#Maximum frequency character in String TC and SC o(n)
def max_stri_freq(s):
    all_freq = {}
    for i in s:
        if i in all_freq:
            all_freq[i] += 1
        else:
            all_freq[i] = 1 
    print(all_freq)
    return max(all_freq, key = all_freq.get)
    

s="cheatsheet"
print("count=jj=",max_stri_freq(s))

#WORD IS AN ANAGRAM OF OTHER  using Hash map Time Complexity: O(N) 
# Auxiliary Space: O(1), constant space is used
def isanagram(a,b):
    if (len(a)!=len(b)): #Check if length of both strings is same or not
        return False
    map={}#   # Create a HashMap containing Character as Key and
    # Integer as Value. We will be storing character as
    # Key and count of character as Value.
    for i in range(len(a)):## Loop over all character of String a and put in
    # HashMap.
        if (a[i] in map):## Check if HashMap already contain current
        # character or not
            map[a[i]] += 1
        else:# # else set that character in map and set
            # count to 1 as character is encountered
            # first time
            
            map[a[i]] =1
    for i in range(len(b)):#loop over string b
        if(b[i] in map):## Check if current character already exists in
        # HashMap/map
            map[b[i]] -= 1#if exists reduce the count 
        else:
            False
    keys=map.keys()#extract all the keys of hashMap
    for key in keys:
        if(map[key]!=0):#check if all keys are 0
            return False
    return True
a="llisen"
b="silent"
if(isanagram(a,b)):
    print("True")
else:
    print("False")


# hacker rank Time and Space of O(N)
def anagram(s):
    if len(s) % 2 != 0:
        return -1

    dict = {}

    for val in s[len(s)//2:]:
        if val not in dict:
            dict[val] = 0
        dict[val] += 1

    count = 0
    for val in s[:len(s)//2]:
        if val in dict and dict[val] != 0:
            dict[val] -= 1

    for val in dict.values():
        count += val

    return count

#
def anagram(s):
    if len(s) % 2: return -1
    
    from collections import Counter
    d1 = Counter(s[:len(s)//2])
    d2 = Counter(s[len(s)//2:])
    return sum( (d1-d2).values())

# string with unique characters(when case insesntive)
def uniqueCharacters(str):
     
    # If at any time we encounter 2
    # same characters, return false
    for i in range(len(str)):
        for j in range(i + 1,len(str)):
            if(str[i] == str[j]):
                return False
 
    # If no duplicate characters
    # encountered, return true
    return True
 
 
# Driver Code
str = "GEeks" # yes
 
if(uniqueCharacters(str)):
    print("Yes")
else:
    print("No")

#Approach 4 – Without Extra Data Structure: The approach is valid for strings having alphabet as a-z. This approach is a little tricky. Instead of maintaining a boolean array, we maintain an integer value called checker(32 bits). As we iterate over the string, we find the int value of the character with respect to ‘a’ with the statement int bitAtIndex = str.charAt(i)-‘a’; 
# Then the bit at that int value is set to 1 with the statement 1 << bitAtIndex . 
# Now, if this bit is already set in the checker, the bit AND operation would make the checker > 0. Return false in this case. 
# Else Update checker to make the bit 1 at that index with the statement checker = checker | (1 <<bitAtIndex); 

def uniqueCharacters(string):
	
	# Assuming string can have characters
	# a-z this has 32 bits set to 0
	checker = 0
	
	for i in range(len(string)):
		bitAtIndex = ord(string[i]) - ord('a')

		# If that bit is already set in
		# checker, return False
		if ((bitAtIndex) > 0):
			if ((checker & ((1 << bitAtIndex))) > 0):
				return False
				
			# Otherwise update and continue by
			# setting that bit in the checker
			checker = checker | (1 << bitAtIndex)

	# No duplicates encountered, return True
	return True

str = "I aAm wonder" # yes
 
if(uniqueCharacters(str)):
    print("Yessss")
else:
    print("No")

# nTH FIBONACCI NUMBER Time Complexity: O(N) Auxiliary Space: O(1)
def fibonacci(n):
    a = 0
    b = 1
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return a
    elif n == 1:
        return b
    else:
        for i in range(2, n):
            c = a + b
            a = b
            b = c
        return b
 
# Driver Program
 
print(fibonacci(9))

# common characters in 2 strings 
def twoStrings(s1, s2):
    for char in s1:
        if char in s2:
            return 'YES'
        else:
            continue
    return 'NO'

# count of common characters in 2 strings 
def count_substring(string, sub_string):
    counter = 0
    for i in range(len(string)):
        if i == string.find(sub_string,i,len(string)):
            counter += 1
        else:
            pass
    return counter

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    # print(count)

# Reverse of string 

# Function to reverse a entire string Tc o(n) SC 0(1)
def reverse(string):
    string = string[::-1]
    return string
  
s = "2"
print(reverse(s))

# REVERSE WORDS in a guven string **hello world to world hello TC and SC o(n)
string = "Hello World"
# reversing words in a given string
s = string.split()[::-1]
l = []
for i in s:
    # apending reversed words to l
    l.append(i)
# printing reverse words
print(" ".join(l))

#mutliplaciation 
def myfun(a,b):
    if b<0:
        return -myfun(a,-b)
    
    elif b==0:
        return 0
    elif b==1:
        return a
    else:
        return a+ myfun(a,b-1)
a=3
b=8       
print("mul of 2 numbers",myfun(a,b))

# consecutive number Here, in each loop, I check if the current element is equal to the previous element.
def check(lst):
    last = lst[0]
    for num in lst[1:]:
        if num == last:
            return True
        last = num
    return False
lst = [1, 2, 3, 5, 6]
print (check(lst))

#2d array 
from array import *

T = [[11, 12, 5, 2], [15, 6,10], [10, 8, 12, 5], [12,15,8,6]]
for r in T:
   for c in r:
      print(c,end = " ")
   print()

# using list comhersion
rows, cols = (5, 5)
arr = [[0 for i in range(cols)] for j in range(rows)]
print(arr)

#fizz buzz
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print ('FizzBuzz')
    elif i % 3 == 0:
        print ('Fizz')
    elif i % 5 == 0:
        print ('Buzz')
    else:
        print (str(i))