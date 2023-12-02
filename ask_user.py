command = {
    "how are you" : 'good',
    "what do you do" : "programming",
    "who are you" : "program"
}

def ask_user():
    while True:
        try:
            print("If you want to quit press 'q'") 
            user_input = input("User: ")
            if user_input.lower() == 'q':
                break
            elif user_input in command.keys():
                print(f"Program: {command[user_input]}")
            else:
                print(f"Program: you input {user_input}")
            print()
        except KeyboardInterrupt:
            print("Bye!")
            break
ask_user()