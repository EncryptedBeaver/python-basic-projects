import random

ANSWERS = [
    "Outlook good", "100% yes, go for it!", "Reply hazy, try again", "Ask again later",
    "Better not tell you now", "Cannot predict now", "Concentrate and ask again",
    "My coffee hasn't kicked in yet", "Ask your mom instead", "Don't count on it",
    "My reply is no", "My sources say no", "Very doubtful", "Outlook not so good",
    "Not in a million years", "Error 404: Hope not found"
]

PROMPTS = [
    "What is on your mind?",
    "What is your burning question?",
    "Ask away! The orb is listening...",
    "What do you wish to know?",
    "Type your question here:",
    "Seek and you shall find. What’s your question?",
    "What secret shall I reveal today?",
    "What does your heart desire to ask?",
    "Consult the magic orb: What is your question?",
    "Ready for answers? Ask your question!"
]


def one_more_question():
    aks_again = input("\nDo you want to ask anything else? Enter 'yes' or 'no' ").lower().strip()
    while aks_again not in ('yes', 'no'):
        print("\nYou are supposed to enter only 'yes' or 'no'")
        aks_again = input("\nDo you want to ask anything else? Enter 'yes' or 'no' ").lower().strip()

    if aks_again == 'no':
        print("\nOK, come back if you need to ask anything ")

    return aks_again == 'yes'


print("\nHello I'm a magic ball and I know the answer to any of your questions")
user_name = input("\nWhat's your name? ").capitalize()
print(f"\nNice to meet you, {user_name}")


while True:
    question = input(f"{random.choice(PROMPTS)} ")
    print(f" -> {random.choice(ANSWERS)}")
    
    if not one_more_question():
        break



