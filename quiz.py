print("🎯 Welcome to Quiz App")
score = 0

questions = [
    {
        "q": "What is the capital of India?",
        "options": ["A. Mumbai", "B. Delhi", "C. Kolkata", "D. Chennai"],
        "answer": "B"
    },
    {
        "q": "Which language is used for AI?",
        "options": ["A. Python", "B. HTML", "C. C", "D. PHP"],
        "answer": "A"
    },
    {
        "q": "2 + 2 = ?",
        "options": ["A. 3", "B. 4", "C. 5", "D. 6"],
        "answer": "B"
    }
]

for i in questions:
    print("\n", i["q"])
    for opt in i["options"]:
        print(opt)

    ans = input("Your answer (A/B/C/D): ")

    if ans.upper() == i["answer"]:
        print("Correct ✅")
        score += 1
    else:
        print("Wrong ❌")

print("\n🎉 Quiz Finished!")
print("Your Score:", score, "/", len(questions))
