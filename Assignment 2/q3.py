#################################################
# CS03B - Summer 2026
# Assignment 2 - Question 3
# Student Name: Rayaan Riyaz
# SID: 20691965
#################################################

def run():
    """
    Students should implement their code for Question 3 inside this function.
    """
    # TODO: Write your code here

    sentence = "Let's take LeetCode contest"
    words = sentence.split()
    reversed_words = []

    for word in words:
        reversed_word = word[::-1]
        reversed_words.append(reversed_word)

    reversed_sentence = " ".join(reversed_words)
    print(reversed_sentence)

    # Example logic:
    # result = 5 + 5
    # print(f"Result: {result}")

if __name__ == "__main__":
    # This allows students to run this specific file 
    # individually for testing (e.g., `python q1.py`)
    run()
