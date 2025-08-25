#Task 5(kata level 1)

# num = 4

# def triangle(num):

#     if num > 0:
#         for hash in range(num):
#             print('#' * (hash + 1))
#     else:
#         ## num *= -1
#         num = abs(num)   #Using abs() function will return positive number(absolute value)

#         # for hash in range(num):
#         #     print('#' * num)
#         #     num -= 1

#         for hash in range(num,0,-1):        ## Using range(start,stop,step) to decrement/increment for loop. stop is not inclusive
#             print('#' * hash)

# triangle(num)

#Task 2(kata level 2)

num = -4
mode = "rit"

def triangle(num,mode):

    if mode == "right" or mode == "left" or mode == "isosceles":
        if num > 0:
            for hash in range(1,num+1):
                if mode == "left":
                    print('#' * (hash + 1))
                elif mode == "right":
                    print((" " * (num - 1)) + ('#' * (hash + 1)))
                elif mode == "isosceles":
                    print(' ' * (num - hash) + '#' * (2 * hash - 1))

        else:
            # num *= -1
            num = abs(num)   #Using abs() function will return positive number(absolute value)

            # for hash in range(num):
            #     print('#' * num)
            #     num -= 1

            for hash in range(num,0,-1):        # Using range(start,stop,step) to decrement/increment for loop. stop is not inclusive
                if mode == "left":
                    print('#' * hash)
                elif mode == "right":
                    print((" " * (num - hash)) + ('#' * (hash)))
                elif mode == "isosceles":
                    print(' ' * (num - hash) + '#' * (2 * hash - 1))
    
    else:
        error()

def error():
    print("ERROR!!!\nIncorrect mode inputed")

triangle(num,mode)
