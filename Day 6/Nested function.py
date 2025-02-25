# Nested Function
a=10
def xyz ():
   # global a
   # print("a1",a)
    a=20
    print("a2",a)
    def pqr():
        global a
        print("a3",a)
        #a=30
        print("a4",a)
    pqr()
xyz()

