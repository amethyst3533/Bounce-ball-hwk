class Car():
    brand = "Ford"
    speed = 20

    def __init__(self):
        print("Your Car")
    def change(self):
        self.brand = input("What brand is your car? ")
        self.speed = int(input("What speed is your car? "))
    def acceleration(self):
            self.speed += 10
    def display(self):
            print(self.brand)
            print(self.speed)


Van = Car()
Van.change()
Van.acceleration()
Van.display()

#acceleration = self.speed+10

#def on_key_down(key):
    #if key == keys.SPACE:
        #acceleration = +10