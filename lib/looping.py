#!/usr/bin/env python3

from attr import s


def happy_new_year():
    # code goes here!
    counter = 10
    while counter > 0:
        print(counter)
        counter -= 1
    print("Happy New Year!")

    pass

def square_integers(int_list):
    return [num ** 2 for num in int_list]
def reversed_str(s):
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str
print(square_integers([1, 2, 3, 4]))
print(reversed_str("Hello"))
    
    
    
    # code goes here!
pass

def fizzbuzz():
    # code goes here!
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i) 
            
        
            
    
    pass
