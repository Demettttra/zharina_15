class my_class():
    def __init__(self):
        pass
    def meth2(self, value):
        return len(str(value))
    def meth1(self, value):
        gl="аоуыэяёюие"
        gl_all=''
        sgl_all=''
        chet=[]
        if type(value) is str:
            for i in value.lower():
                if i in gl:    gl_all+=i
                elif i.isalpha():    sgl_all+=i
            if self.meth2(gl_all)*self.meth2(sgl_all)<=self.meth2(value):    print(gl_all)
            else:    print(sgl_all)
        if type(value) is int:
            for i in str(value):
                if int(i)%2==0:    chet.append(int(i))
            print(sum(chet)*self.meth2(value))
my_class().meth1(44835)
my_class().meth1('Жарина ?%; Оксана тзздб178')
