def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params( b = 25 )
print_params( c = [1,2,3] )
print_params( b = 18,a='fist' )
print_params(548,[5,11,17],False)
print_params()
values_list=[5,'test',False]
values_dict={'a':25, 'b': 'dictionary','c':0.25}
print_params(*values_list)
print_params(**values_dict)
values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_2, 42)
