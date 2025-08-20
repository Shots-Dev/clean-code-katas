#Task 9

message = "Umuzi" 

def find_vowels(message):

    vowels = {char.lower() for char in message if char in "a,e,i,o,u"}          
        #use set data type because it stores unique values 
        #first expression(is the datatype you want the set to store)

    print(f"Vowels: ",", ".join(sorted(vowels)))
        #use .join() to convert set into string so it prints without braces
        #it is seperated by the ' "," '
        #sorted() function gives us output sorted in alphabetical order

find_vowels(message)