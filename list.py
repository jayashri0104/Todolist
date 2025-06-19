def abs():
    print("1.list all task")
    print("2.add a task")
    print("3.delete a task ")
    print("4.mark a task as completed")
    print("99.Exit")


def set_list(abc):
    for i in abc:
        if i['done']:
            print( abc .index(i), i['abc'], "--->", "complete")
        else: 
            print(abc .index(i), i['abc'], "--->", "incomplete")
        