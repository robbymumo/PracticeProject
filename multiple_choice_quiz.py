class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer


questions_prompts = (
    "What is the color of the Bananas? \n a) Blue \n b) Red \n c) Yellow \n\n",
    "What is the color of Apples? \n a) Yellow \b) Red/Green \n c) Purple\n\n",
    "What is the color of Oranges \n a) Oranges \b) Yellow \n c) Purple\n\n",
    "What is the color of ripe Tomatoes? \n a) Green \b) Yellow \n c) Red\n\n",
)

questions = [
    Question(questions_prompts[0], "c"),
    Question(questions_prompts[1], "a"),
    Question(questions_prompts[2], "a"),
    Question(questions_prompts[3], "c")
]


def run_test(questions):
    score = 0
    for question in questions:
        answer = input(questions_prompts)
        if answer == question.answer:
            score += 1
    print(f'You got {score} correct!')


run_test(questions)
