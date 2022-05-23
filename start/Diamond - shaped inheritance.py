# Ромбовидное наследование. Порядок иерархии в множественном наследовании
# простое

class A:
    def hi(self):
        print("A")

class B(A):
    def hi(self):
        print("B")

class C(A):
    def hi(self):
        print("C")

class D(C, B):
# вывод для нагладности
    def print_mro(T):
        print(*[c.__name__ for c in D.mro()], sep=' -> ')

class E(B, C):
# вывод для нагладности
    def print_mro(T):
        print(*[c.__name__ for c in E.mro()], sep=' -> ')

d = D()
d.hi()
print(D.mro())
print(D.print_mro(d))
e = E()
e.hi()
print(E.mro())
print(E.print_mro(e))

# Сложное

class O:
    def hi(self):
        print("O")

class A_1(O):
    def hi(self):
        print("A1")

class B_1(O):
    def hi(self):
        print("B1")

class C_1(O):
    def hi(self):
        print("C1")

class D_1(O):
    def hi(self):
        print("D1")

class E_1(O):
    def hi(self):
        print("E1")

class K1(A_1, B_1, C_1):
    pass

class K2(B_1, C_1):
    pass

class K3(C_1, D_1, E_1):
    pass

class Z(K1, K2, K3):
# вывод для нагладности
    def print_mro(T):
        print(*[z.__name__ for z in Z.mro()], sep=' -> ')

z = Z()
z.hi()
print(Z.mro())
print(Z.print_mro(z))

# Противоречие

class A_2:
    def hi(self):
        print("A")

class B_2(A_2):
    def hi(self):
        print("B")

class C_2(A_2):
    def hi(self):
        print("C")

class D_2(C_2, B_2):
    pass


class E_2(B_2, C_2):
    pass

class MyMro(type):
    def mro(cls):
        return (cls, B_2, C_2, A_2, object)


class X_2(D_2, E_2, metaclass=MyMro):
    pass
# вывод для нагладности
    def print_mro(T):
        print(*[c.__name__ for c in X_2.mro()], sep=' -> ')

x = X_2()
x.hi()
print(X_2.mro())
print(X_2.print_mro(x))
