# x = 1 #assignment statement - get a value and put in some variable that get a slot in the memory
# print(x) # show what's in the variable in the terminal

# x = x + 1 #assignment with expression 
# print(x) #print func tion

# #if you write anything wrong you'll get a SYNTAX ERROR

# # CONDITIONAL STEPS

# x = 5
# if x < 10:
#     print('Smaller')
# if X > 20: 
#     print('Bigger')

# print('Finis')


# #REPEATED StEPS - LOOPS 

# n = 5
# while n > 0:
#     print(n)
#     n = n - 1
# print('Blastoff')

# #usb drive is the same of a secondary memory in a PC - the CPU is the oe
# # who runs the codes in the script - 
# x = int(98.9)
# print(x)


# a = input('Enter a number')

# try:
#     b = int(a)
# except:
#     b = 0

# print(b)


# hours = int(input("How many hours? "))
# rate = float(input("What's the rate per hour? "))

# if hours <= 40:
#     hourRate = hours * rate
# else:
#     moreHours = hours - 40
#     hourRate = (40 + (moreHours * 1.5))* rate

# print(hourRate)

# number = True
# while number != False:
#     try:
#         hours = input("How many hours? ")
#         if hours == "quit":
#             break
#         ihours = int(hours)
#         rate = float(input("What's the rate per hour? "))
#         number = False 
#     except:
#         print('You got to type just numbers! But if you want to leave type \'quit\'')




# score = float(input("What's your score? "))

# if score < 0.6:
#     print('F')
# elif score <= 0.7:
#     print('D')
# elif score <= 0.8:
#     print('C')
# elif score <= 0.9:
#     print('B')
# elif score <= 1:
#     print('A')
# else:
#     print('Error')


# def computepay(hours, rate):
#     if hours <= 40:
#         return hours * rate
#     else:
#         aboveForty = (hours - 40) * 1.5
#         return (40 + aboveForty) * rate
    
# hours = float(input('Hours: '))
# rate = float(input('Rate: '))

# print(f'Pay {computepay(hours, rate)}')

a = None 

print("Hello", a)