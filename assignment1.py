
my_name = "Colin"
my_age = 27


def greeting(my_name,my_age):
    print("Hello, my name is " + my_name + " and I am " + str(my_age) + " years old.")

greeting(my_name,my_age)

user_name = input("What is your name: ")
user_age = input("What is your age: ")

def advanced_greeting():
    print("Hello, my name is " + str(user_name) + " and I am " + str(user_age) + " years old.")

advanced_greeting()


def decades_lived(new_age):
    decades = new_age // 10
    print("you have lived for " + str(decades) + " decades")

decades_lived(27)
