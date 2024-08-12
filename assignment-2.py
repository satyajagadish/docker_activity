# write a program which can filter even numbers in a list by using filter function. The list is 1 to 10.

l = [1,2,3,4,5,6,7,8,9,10]
def fil(x):
    if x%2 == 0:
        return x
new = list(filter(fil,l))
print(new)

# write a program which can map() to make a list whose elements are square of elements in [1,2,3,4,5,6,7,8,9,10]

input_list = [1,2,3,4,5,6,7,8,9,10]
def square(x):
    return x * x
result_list = list(map(square,input_list))
print(result_list)


# write a program which can map() and filter() to make a list whose elements are square of numbers in [1,2,3,4,5,6,7,8,9,10]

input_list = [1,2,3,4,5,6,7,8,9,10]
def numbers(x):
    if x%2 == 0:
        return x 
def even_squares(x):
    return x * x
even_numbers = filter(numbers,input_list)
squares_evens = map(even_squares,even_numbers)
result_list = list(squares_evens)
print(result_list)


# write a program which can filter() to make a list whose elements are even numbers 1 and 20.

numbers = range(1,21)
def filters(x):
    if x%2 == 0:
        return x