#task1
def divide_numbers(num1, num2):
    try:
        result = num1 / num2
        return result
    except ZeroDivisionError:
        return "you cant divide 0 "


num1 = 10
num2 = 2
print(f"{num1} / {num2} = {divide_numbers(num1, num2)}")
#task2
def access_list_element(my_list, index):
    try:
        return my_list[index]
    except IndexError:
        return "mistake"

example_list = [1, 2, 3]
print(access_list_element(example_list, 5))
#task3
