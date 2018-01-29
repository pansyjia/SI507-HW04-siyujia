import random
answers = ["It is certain", "As I see it, yes", "It is decidedly so", "Without a doubt", "Yes definitely", "You may rely on it", "Most likely", "Outlook good", "Yes", "Signs point to yes", "Reply hazy try again", "Ask again later", "Better not tell you now", "Cannot predict now", "Concentrated and ask again", "Don't count on it", "My reply is no", "My sources say no", "Outlook not so good", "Very Doubtful"]
def question():
	q = input("What is your question?")
	print(random.choice(answers))
