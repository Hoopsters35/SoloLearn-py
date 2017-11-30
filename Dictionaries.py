#Dictionaries are like maps in other languages
#can only take non-mutable objects as keys. -- no lists or dictionaries

dictionary = {"Justin": 19, "Nathan": 20}
dictionary[1] = "Hello" #how to add a new key/value pair
print(dictionary[1])
#using the same key overrides the previous
dictionary["Nathan"] = "Pitt Student"
print(dictionary)
print("Justin" in dictionary) #true, justin is a key
print(19 in dictionary) #false, only checks keys

print(dictionary.get("Justin"))
print(dictionary.get(19, "19 is not a key")) #second argument returns if the key doesnt exist (default None)
dictionary[True] = False # in python, 1 == True. so writing True overrides 1 
print(dictionary.get(1, "no 1"))