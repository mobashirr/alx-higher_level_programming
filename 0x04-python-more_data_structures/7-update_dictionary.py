#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):

    a_dictionary[key] = value
    return (a_dictionary)


'''
# test cases :
prnt_sortd = __import__('6-prnt_sortd').prnt_sortd

a_dictionary = { 'language': "C", 'number': 89, 'track': "Low level" }
new_dict = update_dictionary(a_dictionary, 'language', "Python")
prnt_sortd(new_dict)
print("--")
prnt_sortd(a_dictionary)

print("--")
print("--")

new_dict = update_dictionary(a_dictionary, 'city', "San Francisco")
prnt_sortd(new_dict)
print("--")
prnt_sortd(a_dictionary)
'''
