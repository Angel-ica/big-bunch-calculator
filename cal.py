import math

# numbers=[]
def addition():
    numbers=[]
    while True:
        user_input=int(input('>>: '))
        numbers.append(user_input)
        all_num=sum(numbers)
        print(all_num)

def subtract():
    max_user_input =int(input('>>'))
    while True:
        max_user_input-=int(input('>'))
        print(max_user_input)



# addition()
#subtract()
