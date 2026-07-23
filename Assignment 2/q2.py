#################################################
# CS03B - Summer 2026
# Assignment 2 - Question 2
# Student Name: Rayaan Riyaz
# SID: 20691965
#################################################

def run():
    """
    Students should implement their code for Question 2 inside this function.
    """
    # TODO: Write your code here

    # 2A

    x = {"key1": 1, "key2": 3, "key3": 2}
    y = {"key1": 1, "key2": 2}

    for key, value in x.items():
        if key in y:
            if value == y[key]:
                print(f"{key}: {value} is present in both x and y")
        
    # 2B

    subjects = {"Math": 81, "Physics": 83, "Chemistry": 87}
    subject_pairs = subjects.items()

    def get_score(pair):
        return pair[1]

    sorted_subjects = sorted(subject_pairs, key=get_score, reverse=True)
    print(sorted_subjects)


    # Example logic:
    # result = 5 + 5
    # print(f"Result: {result}")

if __name__ == "__main__":
    # This allows students to run this specific file 
    # individually for testing (e.g., `python q1.py`)
    run()
