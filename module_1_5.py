immutable_var = 1, 2, 3, ['peach', 'pear', 'melon'], False
print(immutable_var)
immutable_var[3][1]= 'banana'
print(immutable_var)
#immutable_var[4]=True  данная команда не сработает, т.к. указанный элемент, является частью кортежа, т.е. он не может быть изменён.
mutable_list = [1, 3, 8, 'apple', 'banana', True]
print(mutable_list)
mutable_list[1]= 4
mutable_list[5]=False
mutable_list[4]='pear'
print(mutable_list)