from asyncio import exceptions
FILEPATH="myfile.txt"
def get_data(filepath=FILEPATH):
    """
    Gets the data from the file and returns as a todo list
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
        return  todos_local
#print(help(get_data))
def write_data(todos_arg,filepath=FILEPATH):
    """
    Writes the data into the todo file
    """
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)

if __name__=="__main__":
    print("Hello")