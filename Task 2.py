#Task 2

num_1 = 6
num_2 = 7

def has_three(num_1,num_2):
    if num_1 == 3 or num_2 == 3:
        return True
    elif num_1 + num_2 == 3:
        return True
    else:
        return False
    

result = has_three(num_1, num_2)

print(result)