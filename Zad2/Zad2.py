class Subscriber:
    def __init__(self, names=''):
        self.people = names

    def add_person(self, name):
        if type(name) is not str:
            raise Exception("its not string")
        if name in self.people:
            raise Exception("This person already exist!")
        self.people.append(name)
        return f"Person {name} added to list!"

    def delete_person(self, name):
        if type(name) is not str:
            raise Exception("its not string")
        if name not in self.people:
            raise Exception("This person doesn't exist!")
        self.people.remove(name)
        return f"Person ${name} deleted from list!"

    def send_message(self, name, message):
        if type(name) is not str:
            raise Exception("its not string")
        if type(message) is not str:
            raise Exception("its not string")
        if name not in self.people:
            raise Exception("This person doesn't exist!")
        for person in self.people:
            if person == name:
                return f"Message \"${message}\" sent to ${name}"