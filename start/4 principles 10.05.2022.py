# 4 Принципа ООП

# 1-2. Inheritance (Наследование) и Polymorphism (Полиморфизм)

class Crypto:
    name: str
    price: int

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self) -> str:
        return f"Crypto: {self.name}, price: {self.price}"

    @staticmethod
    def sing():
        print("XXX")

class Bitcoin(Crypto):

    @staticmethod
    def sing():
        print("BTC")

class Ethereum(Crypto):

    @staticmethod
    def sing():
        print("ETH")

crypto = Crypto("XXX", 0)
bitcoin = Bitcoin("Bitcoin", 30000)
ethereum = Ethereum("Ethereum", 2000)

print(crypto)
crypto.sing()
print(bitcoin)
bitcoin.sing()
print(ethereum)
ethereum.sing()

# 3. Abstraction (Абстракция)

class Bike:
    model: str
    year: int
    volume: int

    def __init__(self, model, year, volume):
        self.model = model
        self.year = year
        self.volume = volume

    def __str__(self) -> str:
        return f"Model: {self.model}, year: {self.year}, volume: {self.volume} см3"

suzuki = Bike("Suzuki SV", 2003, 650)
honda = Bike("Honda SBR", 2004, 600)
yamaha = Bike("Yamaha R1", 2005, 1000)

print(suzuki)
print(honda)
print(yamaha)

# 4. Encapsulation (Екапсуляция)

class User:
    username: str
    _email: str
    __password: str

    def __init__(self, nick, pwd, email):
        self.username = nick
        self.__password = pwd
        self._email = email

    def change_pass(self, pwd):
        self.__password = pwd

class MailUser(User):

    def p(self):
        print(self._email)
        print(self.__password)

user = MailUser("Khameta", "dx2010", "granat.maxim@yandex.by")
print(user._email)
print(user.__password)