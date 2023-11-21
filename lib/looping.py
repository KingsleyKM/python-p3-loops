#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    i = 10
    while i > 0 :
        print(i)
        i -= 1
    print("Happy New Year")  

def square_integers(int_list):
    # code goes here
    new = list()
    for num in int_list :
        new.append(num ** 2)
        print(new)

print(square_integers([1,2,3,4,5]))        

def fizzbuzz(num):
    # code goes here!
    if num % 3 == 0 and num % 5 == 0 :
        return "FizzBuzz";
    elif num % 3 == 0 :
        return "Fizz";
    elif num % 5 == 0 :
        return "Buzz";
    else :
        return num;

def fizzbuzz_printer():
    num = 1 
    while num <= 100 :
        print(fizzbuzz(num))
        num += 1

def reverse_string(str):
    new_string =""
    for x in range(len(str)-1,-1,-1) :
            new_string += str[x]
    return new_string


