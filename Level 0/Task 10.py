#Task 10

message_1 = "house"
message_2 = "computers"

def common_letters(message_1,message_2):

    set_1 = set(message_1)
    set_2 = set(message_2)
    #Fisrt change the messages to sets e.g {h,o,u,s,e}

    common = set_1 & set_2
    #use the set operations to find the unions(the common elemens/letters)

    print("Common letters: ",",".join(sorted(common)))

common_letters(message_1,message_2)