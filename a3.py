class Parrot:
    species="bird"
    def __init__(self,name,age):
        self.name=name
        self.age=age
blu = Parrot ("Blu",18)
woo= Parrot("woo",15)
print("Blu is a {}".format(blu.age))
print("Woo is a {}".format(woo.age))