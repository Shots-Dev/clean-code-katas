#Task 1

num = 11

def multiples(num):
    sum = 0
    for number in range(num):
        if number % 3 == 0 or number % 5 == 0:
            sum += number
        
    print(f"The sum is: {sum}")

multiples(num)
