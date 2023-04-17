# Day 17: Classes

# Pascal case for the name
class User:
    def __init__(self, user_id, username)  -> None:
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1

user_1 = User("bla", "bloop")
user_2 = User("bloop", "blip")

print(user_1.username)
print(user_1.followers)
print(user_1.following)

print(user_2.username)
user_1.follow(user_2)
print(user_2.followers)
print(user_2.following)


class Car:
    def __init__(self, seats):
        self.seats = seats

    def enter_race_mode(self):
        self.seats = 2

my_car = Car(5)
print(my_car.seats)

my_car.enter_race_mode()
print(my_car.seats)
