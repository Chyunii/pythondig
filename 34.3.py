class Person:
    def __init__(self, name, age, address, wallet):
        self.name=name
        self.age=age
        self.address=address
        self.__wallet=wallet

    def pay(self, amount):
        if amount>self.__wallet:
            print('돈이 모자라네...')
            return
        self.__wallet-=amount

maria=Person('마리아', 20, '서울시 서초구 반포동', 10000)

maria.pay(3000)
