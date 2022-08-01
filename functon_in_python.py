#function to return variable
# def maximum(a,b,c):
#     return max(a,b,c)

# a = int(input('enter number: '))
# b = int(input('enter number: '))
# c = int(input('enter number: '))

# max_num = maximum(a,b,c)

# print('maximum number is' +   str (max_num)


def trip_welcome():
    print("welcome to trip app")
    print("seems like you're going to lagos today")
#calling my function
trip_welcome()

# #types ofArguments
# #positional argument
# #example 1

def trip_app(name,origin,destination):
    #name,origin,destination are called parameters
    print("Hello " + name +" how are you doing today?")
    print("i hope you have a smooth journey from " + origin +" to "+ destination +" today")
    
name = input("enter your name:")
origin = input("enter your current location:")
destination = input("enter your destination:")

trip_app(name,origin,destination)

# keyword statement
# Example 2


def trip_app(name,origin,destination):
    #name,origin,destination are called parameters
    print("Hello " + name +" how are you doing today?")
    print("i hope you have a smooth journey from " + origin +" to "+ destination +" today")
    
trip_app(name = input("Enter your name:"),
 destination = input("Enter your destination:"), 
 origin = input("Enter your current location:"))

#default argument
#example 3

def trip_app(name,destination,origin = "lagos"):
    #name,origin,destination are called parameters
    print("Hello " + name +" how are you doing today?")
    print("i hope you have a smooth journey from " + origin +" to "+ destination +" today")

name = input("Enter your name:")
destination = input("Enter your destination:")

welcome_speech = trip_app(name,destination)

print(welcome_speech)

#Return statement
#example 4

def trip_app(name,destination,origin = "lagos"):
    #name,origin,destination are called parameters
    greet = ("Hello " + name +" how are you doing today?")
    greet_2 = ("i hope you have a smooth journey from " + origin +" to "+ destination +" today")
    
    return greet, greet_2
name = input("Enter your name:")
origin = input("Enter your current location:")
destination = input("Enter your destination:")  