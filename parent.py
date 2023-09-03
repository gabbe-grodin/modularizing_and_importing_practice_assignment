local_val = "magical unicorns"
def square(x):
    return x * x

class User:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        return "hello"

print(square(5))
user = User("Anna")
print(user.name)
print(user.say_hello())

"""Namespace refers to which variables, functions, and classes are accessible to us at any given time during a program’s execution. Namespace is important because we have to know what variables we have access to. To see what variables are available in any given place, add the line print(locals()) and see what variables are in your current namespace. The object that prints will be a dictionary where the variable names are keys and the objects they reference are the values. Understanding namespace will help you understand the next portion, where we will use namespace to control the functionality that is imported with our document.

Whenever we create a new file and execute it, the Python interpreter automatically creates several variables. We’ll look closer at one of them: the variable __name__. To learn how to use this variable in your own code, follow the steps below:"""

print(__name__)

if __name__ == "__main__":
    print("the file is being executed directly")
else:
    print("The file is being executed because it is imported by another file. The file is called: ", __name__)
  
