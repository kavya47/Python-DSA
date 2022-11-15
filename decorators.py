#https://www.educative.io/answers/how-to-use-decorators-in-python

#can handle zerodivision using decorator 

def zero_logic(func):

    def inner(a,b):
        if b==0:
            return "not divisible"
        return func(a,b)
    return inner


@zero_logic #decorators method  1 way
def div(a,b):
    print (a/b)

#div=zero_logic(div) # 2 way 

# print(div(2,0))
div(2,0)


