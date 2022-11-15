a=10
b=9

try:
    print(a/b)
    k=int(input("Ebter number"))
    print(k)    

except ZeroDivisionError as e:
    print("This is a Zero division errr")

except ValueError as e:
    print("Va1ue error")

except Exception as e:
    print("This operation cannot be happened",e)

finally:
    print("close")