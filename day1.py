#Ask user for input and display todos

user_prompt = "Enter a todo:"
todo1 = input(user_prompt)
todo2 = input(user_prompt)
todo3 = input(user_prompt)

todos = [todo1, todo2, todo3]
print(todos)


title = "Enter the title: "
user_title = input(title)

print("The title length is " + str(len(user_title)))
