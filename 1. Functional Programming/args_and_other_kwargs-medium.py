# Proper format
# {
#   index: argument
#   name: keyword_argument,
# }
# if parameter is unnamed, it's index is key
#


def list_parameters(*args, **kwargs):
    new_dict = {index: value for index, value in enumerate(args)}
    return new_dict | kwargs


print(list_parameters(1, 2, 3, 4, 5, name='Zbigniew', surname='Ziobr', age=35))
