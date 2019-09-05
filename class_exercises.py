class Person: 
    def __init__(self, name, email, phone): 
        self.name = name 
        self.email = email 
        self.phone = phone 
        self.friends = []
        self.greeting_count = 0

    def greet(self, other_person): 
        return('Hello {}, I am {}!'.format(other_person.name, self.name))
    def print_contact_info(self):
        return "{}'s email is {} and Sonny's phone number is {}.".format(self.name, self.email, self.phone)
    def add_friend(self, friend): 
        self.friends.append(friend)
    def num_friends(self): 
        return len(self.friends)
    def greeting_count(self): 
        if self.greet(): 
            self.greeting_count += 1
        return greeting_count
    
        
sonny = Person("Sonny", "sonny@hotmail.com", "483-485-4948")
jordan = Person("Jordan", "jordan@aol.com", "495-586-3456")

print(sonny.greet(jordan))
print(sonny.greeting_count())


class Vehicle: 
    def __init__(self, make, model, year):
        self.make = make 
        self.model = model 
        self.year = year 
    def print_info(self): 
        return "{} {} {}".format(self.year, self.make, self.model)

car = Vehicle('Nissan', 'Leaf', 2015)

print(car.make, car.model, car.year)
print(car.print_info())

