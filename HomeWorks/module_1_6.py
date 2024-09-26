my_dict={'Alex':1980, 'Den': 1975, 'Nick': 1995, 'Sam': 2000}
print("Dict: ", my_dict)
print("Existing value: ", my_dict['Sam'])
print("Not existing value: ", my_dict.get('Vlad'))
my_dict.update({'Ed': 1991, 'Marie': 1993})
a = my_dict['Den']
del my_dict['Den']
print('Deleted value: ', a)
print("Modified dictionary: ", my_dict)
my_set={1, 2, 3, 4, 'String', True, 1, 2, 4, "String", False}
print("Set: ", my_set)
my_set.update({7, 8, 0, 'Акробат', 98.154})
print(my_set)
my_set.remove('String')
print('Modified Set; ', my_set)

