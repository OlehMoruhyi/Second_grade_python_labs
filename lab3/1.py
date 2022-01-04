import json
import datetime


class Ticket:
    id_generator = 0

    def __init__(self):
        with open("IT-event.json", 'r') as f:
            event = json.load(f)
        self.price = event['event']['price']
        Ticket.id_generator = event['event']['number_of_tickets']

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        if not isinstance(value, int):
            raise TypeError("ID must be int")
        if value > Ticket.id_generator:
            raise ValueError("ID generation failure")
        self.__id = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Price must be numeric")
        if value <= 0:
            raise ValueError("Price must be larger than 0")
        self.__price = value

    def __str__(self):
        return f'{self.__class__.__name__} {self.price} {self.id}'


class AdvanceTicket(Ticket):

    def __init__(self):
        super().__init__()
        with open("IT-event.json", 'r') as f:
            t = json.load(f)['event']['Advance']
            if not isinstance(t, float):
                raise TypeError
            self.price *= t



class LateTicket(Ticket):
    def __init__(self):
        super().__init__()
        with open("IT-event.json", 'r') as f:
            t = json.load(f)['event']['Late']
            if not isinstance(t, float):
                raise TypeError
            self.price *= t


class StudentTicket(Ticket):
    def __init__(self):
        super().__init__()
        with open("IT-event.json", 'r') as f:
            t = json.load(f)['event']['Student']
            if not isinstance(t, float):
                raise TypeError
            self.price *= t


class Event:
    def __init__(self):
        with open("IT-event.json", 'r') as f:
            event = json.load(f)
        self.date = datetime.datetime(*list(event["event"]["date"]))
        self.regular = Ticket()
        self.student = StudentTicket()
        self.advanced = AdvanceTicket()
        self.late = LateTicket()

    def show_tickets(self):
        date_dif = (self.date - datetime.datetime.now()).days
        if date_dif < 0:
            return f"too late"
        with open("IT-event.json", 'r') as f:
            event = json.load(f)
        if not event['event']['number_of_tickets']:
            return f"too late"
        if date_dif > 60:
            return f"Ticket price: {self.advanced.price}$\nFor students: " \
                   f"{self.student.price}$\n{event['event']['number_of_tickets']}" \
                   f" tickets left\n\n"
        elif 0 <= date_dif < 10:
            return f"Ticket price: {self.late.price}$\nFor students: " \
                   f"{self.student.price}$\n{event['event']['number_of_tickets']}" \
                   f" tickets left\n\n"
        else:
            return f"Ticket price: {self.regular.price}$\nFor students: " \
                   f"{self.student.price}$\n{event['event']['number_of_tickets']}" \
                   f" tickets left\n\n"

    def buy_ticket(self, is_student):
        date = datetime.datetime.now()
        with open("IT-event.json", 'r') as f:
            event = json.load(f)
        if event["event"]["number_of_tickets"] <= 0:
            raise ValueError("Tickets sold out!")
        date_dif = (self.date - datetime.datetime.now()).days
        if date_dif < 0:
            raise TimeoutError("Time to buy tickets is up. Event ended.")
        event["event"]["number_of_tickets"] -= 1
        with open("IT-event.json", 'w') as f:
            json.dump(event, f)
        if is_student:
            ticket = self.student
        elif date_dif > 60:
            ticket = self.advanced
        elif 0 <= date_dif < 10:
            ticket = self.late
        else:
            ticket = self.regular
        ticket.id = Ticket.id_generator
        Ticket.id_generator -= 1
        with open("data.json", 'r') as f:
            data = json.load(f)
        if 'event' not in data:
            data['event'] = {}
        if not str(ticket.id) in data['event']:
            data['event'][str(ticket.id)] = {}
            data['event'][str(ticket.id)]['price'] = ticket.price
            data['event'][str(ticket.id)]['purchase_date'] = str(date)
        with open("data.json", 'w') as f:
            json.dump(data, f)
        return f"You successfully bought your ticket!\n"\
               f"Id:{ticket.id}\n\n"

    @staticmethod
    def search_ticket(ticket_id):
        with open("data.json", 'r') as f:
            data = json.load(f)
        if "event" not in data:
            raise KeyError("There is no events in data")
        if ticket_id not in data["event"]:
            raise KeyError("There is no tickets in data")
        price = data["event"][ticket_id]["price"]
        date = data["event"][ticket_id]["purchase_date"]
        return f"YOUR TICKET:\nTicket id: {ticket_id}\n" \
               f"Price: {price}\nPurchase date: {date}"


responce = ""
event = Event()
print(event.show_tickets())
print(event.date)
while not responce.upper() == "Q":
    responce = input("Do you want to search or buy tickets? S/B\nq - to quit\n")
    try:
        if responce.upper() == "S":
            id = input("Enter id ")
            print(event.search_ticket(id))
        elif responce.upper() == "B":
            responce = input("Are you a student? Y/N\n")
            try:
                if responce.upper() == "Y":
                    st = True
                elif responce.upper() == "N":
                    st = False
                else:
                    raise TypeError("Incorrect data")
                print(event.buy_ticket(st))
            except TypeError:
                print("Something went wrong")
        else:
            raise TypeError("Incorrect data")
        print(event.show_tickets())
    except TypeError:
        print("Something went wrong")
    except KeyError as er:
        print(er)
