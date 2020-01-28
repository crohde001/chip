
from chatterbot import ChatBot
bot = ChatBot('Chip', trainer='chatterbot.trainers.ListTrainer')
from chatterbot.trainers import ListTrainer

conversation = [
    "Hello", "Hi there!",
    "What's Your name?", "My name is Chip",
    "How are you doing?", "I'm doing great.",
    "I need help", "How May I help?"
]

trainer = ListTrainer(bot)

trainer.train(conversation)

response = bot.get_response("Hello")
print(response)