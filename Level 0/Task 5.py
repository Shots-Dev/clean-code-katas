#Task 5

import math

length_1 = 4
length_2 = 5
length_3 = 2

def triangle_area(length_1,length_2,length_3):

    semiperem = 0.5 * (length_1 + length_2 + length_3)                     #Using the Semiperemeter to find the area
    area = math.sqrt(semiperem * ((semiperem - length_1) * (semiperem - length_2) * (semiperem - length_3)))
    
    print(area)

triangle_area(length_1,length_2,length_3)