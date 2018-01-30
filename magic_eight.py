import random
answers = ["It is certain", "As I see it, yes", "It is decidedly so", "Without a doubt", "Yes definitely", "You may rely on it", "Most likely", "Outlook good", "Yes", "Signs point to yes", "Reply hazy try again", "Ask again later", "Better not tell you now", "Cannot predict now", "Concentrated and ask again", "Don't count on it", "My reply is no", "My sources say no", "Outlook not so good", "Very Doubtful"]
def question():
    user_input = ""
    while user_input != "quit":
        user_input = input("What is your question? Or, enter 'quit' to exit.")

        if user_input == "quit":
            break
        elif user_input[-1] != "?":
            print("I’m sorry, I can only answer questions ended with '?'.")
	else:
	    print(random.choice(answers))

question()
	

