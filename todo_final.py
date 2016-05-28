import sys

marked = '[ ]'
command = ""
input_mark = ""

while command != 'exit':
    new_data = []
    data = []
    f = open('todo.txt', 'r')
    text = f.readlines()
    for line in text:
        line = line.strip()
        status = line[0]
        todo = line[1:]
        data.append([status, todo])
        f.close()
    if len(data) == 0:
        print("you don't have any task saved")
# --------------------------------------------outputs

    def output_new_data(new_data):
        with open('todo.txt', 'w') as output:
            for i in new_data:
                output.write("".join(i)+'\n')

    def output_append_data(data):
        with open('todo.txt', 'a') as output:
            output.write("u"+new_idea+'\n')

    def output_mark_data(data):
        with open('todo.txt', 'w') as output:
            for i in data:
                output.write("".join(i)+'\n')
# ---------------------------------------------it lists and marks the item

    def mark(data):
        if item[0] == "m":
            marked = '[x]'
        else:
            marked = '[ ]'
        print(idx+1, marked, item[1])
# --------------------------------------------done
    command = input("Please specify a command [list, add, mark, archive]: ")  # user parameter
# --------------------------------------------list all item
    if command == "list":
        for idx, item in enumerate(data):
            mark(data)
# --------------------------------------------done
# --------------------------------------------add an item
    if command == "add":
        new_idea = input("Add an item: ")
        output_append_data(data)
        print("Item added\n")
# --------------------------------------------done
# --------------------------------------------mark an item
    if command == "mark":
        print("You saved the following to-do items:")
        for idx, item in enumerate(data):
            mark(data)
        input_mark = int(input("Which one you want to mark as completed:  "))
        for i in range(len(data)):
            i = input_mark+1
            data[input_mark-1][0] = "m"
        for i in range(len(data)):
            if i == input_mark:

                print(data[i-1][1])
        output_mark_data(data)

        # print(input_mark,"is completed")
# ---------------------------------------------done
# ---------------------------------------------archive the marked items
    if command == "archive":
        for i in data:
            if i[0] == 'u':
                new_data1 = i[0]
                new_data2 = i[1:]
                new_data.append([new_data1, "".join(new_data2)])
                output_new_data(new_data)
            else:
                del i
                output_new_data(new_data)
        print("All completed tasks got deleted.\n")
# ----------------------------------------------done
