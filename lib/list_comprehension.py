#!/usr/bin/env python3
def return_evens(num_list):
    evens = [n for n in num_list if n % 2 == 0]
    return evens

# Define num_list in the same scope
num_list = range(1, 10, 2)

# Call the function with num_list
result = return_evens(num_list)
print(result)
  

def make_exclamation(sentence_list):
    return [string + "!" for string in sentence_list]
