"""
To do list
"""
from list import abs, set_list

print("Welcome...welcome")
n = 100
abc=[
        {'abc': "write program", 'done': False}
    ]
while n != 99:
    abs()
    n = int(input(" select choise : "))  
    print("-"*20)
    if n == 1:
        set_list(abc)
    elif n == 2:
          t = input("Enter task:")
          abc.append({'abc': t, 'done': False})  
          set_list(abc)
    elif n == 3:
        t = int(input("enter task  to delete:"))
        abc.pop(t)
        print("dont! updated list")
        set_list(abc)
    elif n == 4:
        t = int(input("enter task to mark as complate:"))
        abc[t]['done'] = True
        set_list(abc)
    else:
        print("Exit!!")
        print("-"*20)