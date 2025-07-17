my_list = list(input("Please enter 10 numbers "))
print("this is the original list: ", my_list)
new_list = my_list[:5]
print("Extracted first five elements: ", new_list)
rev_list = new_list[::-1]
print("Extracted last five elements: ", rev_list)