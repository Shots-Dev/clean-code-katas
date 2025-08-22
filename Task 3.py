#Task 3

num_1 = 32.5
num_2 = 32.5

def is_sixty_five(num_1,num_2):
    if num_1 == 65 or num_2 == 65:
        return True
    elif (num_1 + num_2) == 65:
        return True
    else:
        return False
    
result = is_sixty_five(num_1,num_2)

print(result)