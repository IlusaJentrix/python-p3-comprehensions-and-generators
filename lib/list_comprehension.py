#!/usr/bin/env python3
def return_evens(num_list):
    evens = [n for n in num_list if n % 2 == 0]
    return evens

# Define num_list 
num_list = range(1, 10, 2)


result = return_evens(num_list)
print(result)
  

def make_exclamation(sentence_list):
    return [string + "!" for string in sentence_list]
