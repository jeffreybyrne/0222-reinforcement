# Exercise 1
# Create a Task class with a description and due_date (both strings). Define an
# __init__ method, then try creating three instances of this class.


class Task:

    def __init__(self, desc, due_date):
        self.description = desc
        self.due_date = due_date


task1 = Task("do this assignment", "today")
task2 = Task("get enough sleep", "tonight")
task3 = Task("go back to work", "April 29")

# Exercise 2
# Create a TodoList class with a tasks list (which will contain instances of
# the Task class). Create an __init__ method and an add_task method that allows
# you to pass in an instance of your Task class. Try creating a todo list and
# adding your three tasks to it.


class TodoList:

    def __init__(self):
        self.task_list = []

    def __str__(self):
        ret_string = ""
        for num, task in enumerate(self.task_list, 1):
            ret_string = ret_string + task.description + "\n"
        return ret_string

    def add_task(self, task):
        self.task_list.append(task)


list1 = TodoList()
list1.add_task(task1)
list1.add_task(task2)
list1.add_task(task3)
print(list1)
