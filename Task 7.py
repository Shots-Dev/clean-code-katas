#Task 7

list_1 = [12,4,2,4,21,1]
list_2 = [1,2,3,4,6,2,45,21]

def combine(list_1,list_2):
    new_list = []
    max_length = max(len(list_1),len(list_2))

    for i in range(max_length):
        if i < len(list_1):
            new_list.append(list_1[i])
        if i < len(list_2):
            new_list.append(list_2[i])

    return new_list

print(combine(list_1,list_2))
    
    
