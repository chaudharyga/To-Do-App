def get_todos(filepath='todos.txt'):
  with open(filepath,'r') as file1:
        todo=file1.readlines()
  return todo

def write_todos(args,filepath='todos.txt'):
  with open(filepath,'w') as file1:
    file1.writelines(args)