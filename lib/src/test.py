class Class2:

    class Labels:
        c2l1 = 'label 1'
        c2l2 = 'label 2' 

    class Params:
        pass 
        # p1 = None
        # p2 = None
        # p3 = None

    Params.p1 = Labels.c2l2
    Params.p2 = 1234


print(Class2.Params.p1)
print(Class2.Params.p2)
# print(Class2.Params.p3)