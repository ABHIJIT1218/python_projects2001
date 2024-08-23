# # todos = []
# from functions import get_todos,write_todos
import functions
import time

now = time.strftime("%b %d,%Y %H:%M:%S")
print(now)
while True:
    user = input("type add or show or edit or complete :- ")
    user = user.strip()  #it removes the extra spaces

    if user.startswith('add'):
        todo = user[4:]     #List extraction


        # with open('todos.txt', 'r')as file:   #it makes the code shorter
        #     todos= file.readlines()
        todos= functions.get_todos()


        # file = open('todos.txt','r')
        # todos = file.readlines()  # returns as a list
        # if we write file.read() then it will return a normal string


        todos.append(todo + '\n')

        # file = open('todos.txt', 'w')
        # file.writelines(todos)

        # with open('todos.txt', 'w')as file:   #it makes the code shorter
        #     todos= file.writelines(todos)
        functions.write_todos(todos)

    elif user.startswith('show'):
        # file = open('todos.txt', 'r')
        # todos = file.readlines()
        # with open('todos.txt', 'r')as file:   #it makes the code shorter
        #     todos= file.readlines()
        todos = functions.get_todos()

        for index, items in enumerate(todos):  # using enumerate we can excess two variables
            # print(index, " - ", items)  # here we are getting extra spaces while printing the output.
            items = items.strip('\n')
            print(f"{index}-{items}")  # it will print as it is no extra spaces
            # print(type(todos))

        #       new_todos = []                               SAME THING WITHOUT USING lIST COMPREHENSION
        #
        #       for item in todos:
        #           new_item = item.strip("\n")
        #           new_todos.append(new_item)
        #       print(todos)

                        #LIST COMPREHENSION
        # new_todos= [item.strip('\n') for item in todos]

    elif user.startswith('edit'):
        try:
            number = user[5:]
            print(number)
            number = (int(number)) - 1

            # with open('todos.txt', 'r')as file:   #it makes the code shorter
            #     todos= file.readlines()
            todos = functions.get_todos()

            new_todo = input("enter new todo:- ")
            todos[number] = new_todo + '\n'

            # with open('todos.txt', 'w') as file:  # it makes the code shorter
            #     file.writelines(todos)
            functions.write_todos(todos)

        except ValueError:
            print("your command is not valid")
            continue


    elif user.startswith('complete'):
        try:
            number1 = int(user[9:])

            # with open('todos.txt', 'r') as file:  # it makes the code shorter
            #     todos = file.readlines()
            todos = functions.get_todos()

            todos.pop(number1)

            # with open('todos.txt', 'w') as file:  # it makes the code shorter
            #     file.writelines(todos)
            functions.write_todos(todos)

        except IndexError:
            print("index is not valid. ")
            continue

    elif user.startswith('exit'):
        print(f"your all task is over thank you...")
        break
    else:
        print("command is not valid")



# contents = ["My name is Abhijit paul","the carrot were reportedly sliced","vinod naam hai hamhara"]
# #
# # filenames = ["doc.txt","reports.txt","presentation.txt"]
# #
# # for contents, filenames in zip(contents, filenames):
# #     file = open(filenames,"w")
# #     file.write(contents)


# a = [1,2,3]
#
# b = [10,20,30]
#
# x =zip(a,b)

# a = "blaaaa blaa " \
#     "sadsad sadd" \
#     "wqqe wqeeqwe qw"
# print(a)

# str=""
# content = ["The true meaning of obscurity lies underneath the most delicate structures of viscosity. The idea "
#            "of changing that balance is obscure by itself."]
# for con in content:
#     str= str+ (con.capitalize())
#
# print(str)

# file1 = open('todos.txt','r')
# todo1 = file1.readlines()
# print(todo1)
#
# str=""
# for con in todo1:
#     str+= (con.title())
#
# print(str)


# file = open('todos.txt', 'r')
# var = file.read()
#
# count=0
# for i in var:
#     count+=1
#
# print(count)

# content = 'snail'
# file1 = open('file.txt','w')
# file1.write(content)

# Open the file named "file.txt" in write mode using a context manager
# The 'with' statement ensures that the file is properly closed after writing
    # with open("file.txt", "w") as file:
    #     # Write the string "snail" to the file
    #     file.write("snail")

# names = ["john smith", "jay santi", "eva kuki"]     #UISNG LIST COMPREHENSION
# capitalized_name = [name.title() for name in names]
# print(capitalized_name)

# colors = [11, 34, 98, 43, 45, 54, 54]
# for i in colors:
#     if i>50:
#         print(str(i))

# def func(str1):
#     str1 = str1.title()
#     return f"hi {str1}"
#
# result = func(" person")
# print(result)

# def func1(str1):
#     c=0
#     split1 = str1.split(',')
#     print(split1)
#     for i in split1:
#         c+=1
#     print(c)
#
#
# func1("vinod,naam,hai,hamhara")

# EXPERIMENT
# import webbrowser
#
# user = input("enter a search term:- ")
# webbrowser.open("https://www.google.com/search?q="+ user)

# EXPERIMENT
# import glob
# myfiles = glob.glob("*.txt")   #it returns all files as a list
# print(myfiles)

# EXPERIMENT
# import csv
#
# with open("weather.csv", 'r')as file:
#     data = list(csv.reader(file))
# print(data)  #it will print list of list as csv.reader data directly is not readable (its iterative type)