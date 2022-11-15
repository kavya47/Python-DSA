#‘p’, ‘q’, ‘r’, 's', 't', ‘P’, ‘Q’, ‘R’, 'S', 'T', ‘1’, ‘2’, ‘3’, '4', ‘!’, ‘$’, '@'
#Let's use the following scoring scheme for setting up the password.

# 2 points if it’s p’, ‘q’, ‘r’, 's', or 't'

# 3 points if it’s ‘P’, ‘Q’, ‘R’, 'S', or 'T'

# 4 points if it’s ‘1’, ‘2’, ‘3’, or '4'

# 5 points if it’s ‘!’, ‘$’, or '@'

#Step 1: Create an appropriate dictionary linking characters (alphabets, numbers, and special characters) to respective weights listed above.

pswrd_dict={'p':2,'q':2,'r':2,'s':2,'t':2,'P':3,'Q':3,'R':3,'S':3,'T':3,'1':4,'2':4,'3':4,'4':4,'!':5,'$':5,'@':5}
# print(pswrd_dict['p']+pswrd_dict['@'])

#Step 2: Make a string called myPassWd and set it to a test value "p@Q!R3s$"
myPassWd="p@Q!R3s$"

#Step 3: Find the integer equivalent of the password string. Example: For the string in Step 2, you would get 2+5+3+5+3+4+2+5 = 29.
inte_value=pswrd_dict['p']+pswrd_dict['@']+pswrd_dict['Q']+pswrd_dict['!']+pswrd_dict['R']+pswrd_dict['3']+pswrd_dict['s']+pswrd_dict['$']
print("Equivalent value====",inte_value)

#Step 4: Calculate the password score by dividing the total numerical weight (from Step 3) by the length of the password string. 
# Round the result to two decimal places. For the example string in Step 2, the password score would be 29/8 = 3.63 
# (corrected to two decimal places).

paswrd_score=round(inte_value/len(myPassWd),2)
print("password score====",paswrd_score)

#Now, test your code using the following strings. In this step, your code reads each string as an input and prints its weight. 
# "rrQR23$!@"
# "QQr$$13!"
# "12333pqrPP"
# "pqrPQR123$!"

#Testing "rrQR23$!@"
myPassWd_test_1="rrQR23$!@"
inte_value_test_1=pswrd_dict['r']+pswrd_dict['r']+pswrd_dict['Q']+pswrd_dict['R']+pswrd_dict['2']+pswrd_dict['3']+pswrd_dict['$']+pswrd_dict['!']+pswrd_dict['@']
paswrd_score_test_1=round(inte_value_test_1/len(myPassWd_test_1),2)
print("password score test1====",paswrd_score_test_1)

#Testing "QQr$$13!"
myPassWd_test_2="QQr$$13!"
inte_value_test_2=pswrd_dict['Q']+pswrd_dict['Q']+pswrd_dict['r']+pswrd_dict['$']+pswrd_dict['$']+pswrd_dict['1']+pswrd_dict['3']+pswrd_dict['!']
paswrd_score_test_2=round(inte_value_test_2/len(myPassWd_test_2),2)
print("password score test2====",paswrd_score_test_2)

#Testing "12333pqrPP"
myPassWd_test_3="12333pqrPP"
inte_value_test_3=pswrd_dict['1']+pswrd_dict['2']+pswrd_dict['3']+pswrd_dict['3']+pswrd_dict['3']+pswrd_dict['p']+pswrd_dict['q']+pswrd_dict['r']+pswrd_dict['P']+pswrd_dict['P']
paswrd_score_test_3=round(inte_value_test_3/len(myPassWd_test_3),2)
print("password score test3====",paswrd_score_test_3)

#Testing "pqrPQR123$!"
myPassWd_test_4="pqrPQR123$!"
inte_value_test_4=pswrd_dict['p']+pswrd_dict['q']+pswrd_dict['r']+pswrd_dict['P']+pswrd_dict['Q']+pswrd_dict['R']+pswrd_dict['1']+pswrd_dict['2']+pswrd_dict['3']+pswrd_dict['$']+pswrd_dict['!']
paswrd_score_test_4=round(inte_value_test_4/len(myPassWd_test_4),2)
print("password score test4====",paswrd_score_test_4)




