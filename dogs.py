class pets:
    dogs=[]
    def __init__(self, dogs):
        self.dogs = dogs

class Dogs:
    species = 'mammals'
    def __init__(self, name, age):
        self.name= name
        self.age= age

    def desc(self):
        return '{} is {} years old'.format(self.name, self.age)

    def speak(self, sound):
        return '{} makes {} sound'.format(self.name, sound)

class RusselT(Dogs):
    def run(self, speed):
        return '{} runs {}'.format(self.name, speed)

class Other(Dogs):
    def run(self, speed):
        return '{} runs {}'.format(self.name, speed)

my_dogs=[RusselT('Tim',5), Other('Fred','7'), RusselT('Russ',6)]

my_pets=pets(my_dogs)

print('I have {} dogs.'.format(len(my_pets.dogs)))
for dog in my_dogs:
    print('{} is {} years old.'.format(dog.name, dog.age))

print('And they are all mammals, ofc')
