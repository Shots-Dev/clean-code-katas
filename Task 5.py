#Task 5

num = -4

def triangle(num):

    if num > 0:
        for hash in range(num):
            print('#' * (hash + 1))
    else:
        # num *= -1
        num = abs(num)   #Using abs() function will return positive number(absolute value)

        # for hash in range(num):
        #     print('#' * num)
        #     num -= 1

        for hash in range(num,0,-1):        # Using range(start,stop,step) to decrement/increment for loop. stop is not inclusive
            print('#' * hash)

triangle(num)