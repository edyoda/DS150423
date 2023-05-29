class A:
    def a(self):
        print("a")
        
class B(A):
    def b(self):
        print("b")
        
class C(A):
    def c(self):
        print("c")
        
class D(B):
    def d(self):
        print("d")

class E(B):
    def e(self):
        print("e")
        
class F(C):
    def f(self):
        print("f")
        
class G(E,F):
    def g(self):
        print("g")
        
obj1 = G()
obj2 = D()
obj1.g()
obj1.e()
obj1.f()
obj1.b()
obj2.b()
obj1.c()
obj1.a()
obj2.a()