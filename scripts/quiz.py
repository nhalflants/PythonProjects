import json

with open("../files/questions.json", "r") as file:
    content = file.read()
data = json.loads(content)

score = 0
for question in data:
    print(question["question"])
    for index, answer in enumerate(question["answers"]):
        print(index + 1, "-", answer)
    user_choice = int(input("Enter your answer: "))
    question["user_choice"] = user_choice


for index, question in enumerate(data):
    if question["user_choice"] == question["correctIndex"]:
        score = score + 1
        result = "Correct Answer"
    else:
        result = "Wrong Answer"
    message = f"{index + 1} {result} - Your answer: {question['user_choice']}, Correct answer: {question['correctIndex']}"
    print(message)

print("score:", score, "/", len(data))
