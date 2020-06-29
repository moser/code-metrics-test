class A:
    def subject(self):
        return 1

class BB:
    pass

class B(BB):
    pass

class C(B, A):
    def subject(self):
        res = super(C, self).subject()
        return res
