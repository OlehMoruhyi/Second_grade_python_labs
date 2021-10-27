from re import match


class Product:
    def __init__(self, pr, des, dim):
        if not isinstance(des, str) or not isinstance(dim, str):
            raise Exception
        if not isinstance(pr, (int, float)) or (pr <= 0):
            raise Exception
        self.__description = des
        self.__dimensions = dim
        self.__price = pr

    def __str__(self):
        return f'Prise: {self.price}, description: {self.description}, dimensions: {self.dimensions};'

    @property
    def description(self):
        return self.__description

    @property
    def dimensions(self):
        return self.__dimensions

    @property
    def price(self):
        return self.__price

    @description.setter
    def description(self, des):
        if not isinstance(des, str):
            raise Exception
        self.__description = des

    @dimensions.setter
    def dimensions(self, dim):
        if not isinstance(dim, str):
            raise Exception
        self.__dimensions = dim

    @price.setter
    def price(self, pr):
        if not isinstance(pr, (int, float)):
            raise Exception
        self.__price = round(pr, 2)


class Customer:
    def __init__(self, surname, name, patronymic, number):
        self.surname = surname
        self.name = name
        self.patronymic = patronymic
        self.number = number

    def __str__(self):
        return f'Surname: {self.surname}, name: {self.name}, patronymic: {self.patronymic}, number: {self.number};'

    @property
    def surname(self):
        return self.__surname

    @property
    def name(self):
        return self.__name

    @property
    def patronymic(self):
        return self.__patronymic

    @property
    def number(self):
        return self.__number

    @surname.setter
    def surname(self, surname):
        if not isinstance(surname, str):
            raise Exception
        self.__surname = surname

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise Exception
        self.__name = name

    @patronymic.setter
    def patronymic(self, patronymic):
        if not isinstance(patronymic, str):
            raise Exception
        self.__patronymic = patronymic

    @number.setter
    def number(self, number):
        if not isinstance(number, str):
            raise Exception
        if len(number) != 13 or not match(r'^\+380[0-9]{9}', number):
            raise Exception
        self.__number = number


class Order:
    def __init__(self, cus, products=[]):

        if not isinstance(cus, Customer) or not isinstance(products, list):
            raise Exception
        if not all(isinstance(x, Product) for x in products):
            raise Exception
        self.__products = []
        self.__customer = cus
        self.__products += products

    @property
    def customer(self):
        return self.__customer

    @property
    def products(self):
        return self.__products

    @customer.setter
    def customer(self, cus):
        if not isinstance(cus, Customer):
            raise Exception
        self.__customer = cus

    @products.setter
    def products(self, products):
        if not isinstance(products, list) or not all(isinstance(x, Product) for x in products):
            raise Exception
        self.__products = products

    def total_value(self):
        tv = 0
        for prod in self.__products:
            tv += prod.price
        return round(tv, 2)

    def __str__(self):
        kk = "\n\t"
        return f'Customer: \n\t{self.customer} \nOrder:\n\t{kk.join(map(str, self.products))}'

    def add_product(self, products):
        if all(isinstance(x, Product) for x in products):
            self.__products += products
        else:
            raise Exception

    def del_product(self, num):
        if isinstance(num, int) and 0 < num <= len(self.__products):
            self.__products.pop(num-1)
        else:
            raise Exception


try:
    customer = Customer('a', 's', 'd', '+380739963137')
    product = [Product(2.38, 'wer', 'est'), Product(2.14, 'w', 'e'), Product(2.38, 'wer', 'est')]
    order = Order(customer)
    order.add_product(product)
    order.add_product([Product(2.14, 'wer', 'est')])
    print(order)
    order.del_product(1)
    print(order)
    print('Total value:', order.total_value())
except Exception:
    print('Error!')
