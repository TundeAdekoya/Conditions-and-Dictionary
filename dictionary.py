my_dict={"key":"This is the value", "Key2":"This is is another key"} #EMPTY DICTIONARY

#my_Dict = dict() #EMPTY DICTIONARY

#my_set = set() #eMPTY SET 

#print(type(my_Dict)) 

#you can change, add key to a dictionary

my_dict["_key"] = "This is the new value"
my_dict[3] = "This is the new value"


#to update key : TO ADD MULTIPLE KEYS TO A DICTIONARY
# a = {"key7":"This is the new new value", "key5":"This is another new key"}
# my_dict.update(a)
# popped = my_dict.pop("key7")
# print(popped)
# print(my_dict)

#TOFIND THE KEY
#print(my_dict["Key2"])

#TO FIND THE VALUE
#print(my_dict.get("xyz"))

#TO PRINT NOT FOUND INSTEAD OF NONE
#print(my_dict.get("xyz","not found"))

#TO PRINT ALL THE KEYS 
#print((my_dict).keys())

#TO PRINT ALL THE VALUES
#print((my_dict).values())

#TO PRINT ALL THE ITEMS
#print((my_dict).items())

#b = ([('key', 'This is the value'), ('Key2', 'This is is another key'), ('_key', 'This is the new value'), (3, 'This is the new value'), ('key7', 'This is the new new value'), ('key5', 'This is another new key')])

#TURN SET IN PEARS TO A DICTIONARY 

#b = {('key', 'This is the value'), ('Key2', 'This is is another key'), ('_key', 'This is the new value'), (3, 'This is the new value'), ('key7', 'This is the new new value'), ('key5', 'This is another new key')}

#print(dict(b))

#CLASS WORK 
#CHANGE KEY TO ANOTHER KEY
data = {"name":"Chuks", "location":"Aba", "Job":"Senior Developer", "Salary":"£50,000"}
data ['City'] = data.pop('location')
print(data)




