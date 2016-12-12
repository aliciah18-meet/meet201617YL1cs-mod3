class student:
    def __init__ (self, name, hometown, age, height, favicecream)
        self.name=name
        self.hometown=hometown
        self.age=age
        self.height=height
        self.favicecream=favicecream
        
    def print_summary(self):
        print('Your name is ' + str(name))
        print('Your hometown is ' + str(self.hometown))
        print('Your age is ' + str(self.age))
        print('Your height is ' + str(self.height))
        print('Your favorite ice cream is ' + str(self.favicecream))

    def get_girrafe_gap(self):
        girrafe_height= 500
        return (girrafe_height-self.height)
