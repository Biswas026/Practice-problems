a=100
def xyz():
    global b
    b=10# enclosed scope 
    def abc():
        c=1123
        print(c)
    abc()
    print(a)
    print(b)

print(a)
xyz()
print(b)

#built in scope : print(),input(),
