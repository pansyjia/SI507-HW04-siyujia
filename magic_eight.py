def question():
    user_input = ""
    while user_input != "quit":
        user_input = input("What is your question? Or, enter 'quit' to exit.")

        if user_input == "quit":
            break
        elif user_input[-1] != "?":
            print("I’m sorry, I can only answer questions ended with '?'.")

question()
