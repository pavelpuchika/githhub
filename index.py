class person:
    __a=[1,2,4,3,2,1,-40,30,85,-1]
    __b=[1,3,22,-67,35,34,68,2,3,4]
    def m(self):
        a=sum(self.__a)
        b=sum(self.__b)
        print(a,b)
        print(a>b)
i=person()
i.m()

