# Класс для работы с обыкновенными дробями и действия с ними

import math

class Fractions:
    numerator: int
    denominator: int

    def __init__(self, one, two):
        self.numerator = one
        if two == 0:
            print("Ошибка на ноль делить нельзя")
            self.denominator = 1
        self.denominator = two

    def __str__(self):
        return f"{self.numerator} / {self.denominator}"

# сложение
    def __add__(self, other):
        numerator_1 = self.numerator * other.denominator + self.denominator * other.numerator
        denominator_1 = self.denominator * other.denominator
        gcd = math.gcd(numerator_1, denominator_1)
        return Fractions(numerator_1 // gcd, denominator_1 // gcd)

# вычетания
    def __sub__(self, other):
        numerator_1 = self.numerator * other.denominator - self.denominator * other.numerator
        denominator_1 = self.denominator * other.denominator
        gcd = math.gcd(numerator_1, denominator_1)
        return Fractions(numerator_1 // gcd, denominator_1 // gcd)

# умножение
    def __mul__(self, other):
        numerator_1 = self.numerator * other.numerator
        denominator_1 = self.denominator * other.denominator
        gcd = math.gcd(numerator_1, denominator_1)
        return Fractions(numerator_1 // gcd, denominator_1 // gcd)
# деление
    def __truediv__(self, other):
        numerator_1 = self.numerator * other.denominator
        denominator_1 = self.denominator * other.numerator
        gcd = math.gcd(numerator_1, denominator_1)
        return Fractions(numerator_1 // gcd, denominator_1 // gcd)

# равенство
    def __eq__(self, other):
        numerator_1 = self.numerator * other.denominator
        denominator_1 = self.denominator * other.numerator
        return numerator_1 == denominator_1

# неравенство
    def __ne__(self, other):
        numerator_1 = self.numerator * other.denominator
        denominator_1 = self.denominator * other.numerator
        return numerator_1 != denominator_1

# больше
    def __gt__(self, other):
        numerator_1 = other.denominator * self.denominator / self.denominator * self.numerator
        denominator_1 = other.denominator * self.denominator / other.denominator * other.numerator
        return numerator_1 > denominator_1

# больше или равно
    def __ge__(self, other):
        numerator_1 = other.denominator * self.denominator / self.denominator * self.numerator
        denominator_1 = other.denominator * self.denominator / other.denominator * other.numerator
        return numerator_1 >= denominator_1

# меньше
    def __lt__(self, other):
        numerator_1 = other.denominator * self.denominator / self.denominator * self.numerator
        denominator_1 = other.denominator * self.denominator / other.denominator * other.numerator
        return numerator_1 < denominator_1

# меньше или равно
    def __le__(self, other):
        numerator_1 = other.denominator * self.denominator / self.denominator * self.numerator
        denominator_1 = other.denominator * self.denominator / other.denominator * other.numerator
        return numerator_1 <= denominator_1

x = Fractions(1, 5)
y = Fractions(2, 3)

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x > y)
print(x >= y)
print(x < y)
print(x <= y)
