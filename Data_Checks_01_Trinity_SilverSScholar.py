##############################
#Python Data Check 01 Fall 2022
#Trinity Prichard
#SilverSScholar
#############################

import os
os.system('clear')


print ("Hello World!") 

############################
#List of First n Integers
############################
n = 25
p = list(range(25))
print(p)

############################
#Dictionary
############################
Dict = {1: 'Games', 2: 'For', 3: 'Two'}
print(Dict)

#Creating an Empty Dictionary
Dict = {}
print("Empty Dictionary")
print(Dict)

#Adding Elements one at a time
Dict[0] = 'Games'
Dict[2] = 'For'
Dict[3] = 2
print("\nDictionary after adding 3 elements: ")
print(Dict)

#Adding set of Values
#to a single key
Dict['Value_set'] =2,3,4
print("n\Dictionary after adding 3 elements: ")
print(Dict)

#Updating exisiting Key's Value
Dict[2] = 'Welcome'
print("\nUpdated key value: ")

#Adding Nested Key Valye to Dictionary
Dict[5] = {'Nested': {'1': 'Life', '2': 'Games'}}
print("n\Adding a Nested Key: ")
print(Dict)

#List example

print("List Example")
prime_numbers = [2,3,5,7,11,13,17]
#Tuple example
print ("Tuple Example")
perfect_squares = (1,4,9,16,25,36)
#Display Lenghts
print("Display Lengths")
print("# Primes =", len(prime_numbers))
print("#Squares =", len(perfect_squares))


