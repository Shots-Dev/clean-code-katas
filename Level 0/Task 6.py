#Task 6

num_1 = 94
num_2 = 8
num_3 = 3

def max_number(num_1,num_2,num_3):

    max = num_1

    if(num_2>max):
        max = num_2
    if(num_3>max):
        max = num_3

    print(f"The maximum number is {max}")

max_number(num_1,num_2,num_3)

#Bonus

num_1 = 94
num_2 = 8
num_3 = 3
num_4 = 887
num_5 = 33

def max_number(*numbers):                   #Use variable-length arguments (*args)

    max = numbers[0]

    for num in numbers:

        if(num>max):
            max = num

    print(f"The maximum number is {max}")

max_number(num_1,num_2,num_3,num_4,num_5)