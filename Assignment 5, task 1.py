dict_1 = {'Alice':85, 'Janice': 91, 'Lisa': 76}
stud= input("Please enter the name of the student")
if stud=='Alice':
    print("Hello Alice, ", "Your marks are:", dict_1[stud])
elif stud=='Janice':
    print("Hello Janice, ", "Your marks are:", dict_1[stud])
elif stud=='Lisa':
    print("Hello Lisa, ", "Your marks are:",  dict_1[stud])
else:
    print("Please enter a valid student")
