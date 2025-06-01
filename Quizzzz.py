questions = [
 {
    "prompt": "What is captial city of Kerala?",
    "options": ["A. Trivandrum", "B. Palakkad", "C. Idukki"],
    "answer": "a",
 },
 {
    "prompt": "What is captial city of Rajasthan?",
    "options": ["A. Jodhpur", "B. Jaipur", "C. Jamshedpur"],
    "answer": "b",
 },
 {
    "prompt": "What is captial city of West Bengal?",
    "options": ["A. Sealdah", "B. Howrah", "C. Kolkata"],
    "answer": "c",
 }
]
def quiz(questions):
    points = 0
    for question in questions:
        print("\n" + question["prompt"])
        for option in question["options"]:
            print(option)
        you= input("\nWhat is your answer?:").upper()
        if you == question["answer"]:
            points += 1
        else:
            print("Sorry, you didn't answer correctly.")
        print("\n You finished the Quizzzz")
        print("\n You scored " + str(points) + " points.")
quiz(questions)
