#################################################
# CS03B - Summer 2026
# Assignment 2 - Question 3
# Student Name: Rayaan Riyaz
# SID: 20691965
#################################################


def run():
    """
    Students should implement their code for Question 4 inside this function.
    """
    # TODO: Write your code here

    def k_grammar(N, K):
        row = "0"
        for i in range(N-1):
            new_row = ""
            for symbol in row:
                if symbol == "0":
                    new_row += "01"
                else:
                    new_row += "10"
            row = new_row
        return row[K-1]

    print(k_grammar(4, 5))

    # Example logic:
    # result = 5 + 5
    # print(f"Result: {result}")

if __name__ == "__main__":
    # This allows students to run this specific file 
    # individually for testing (e.g., `python q1.py`)
    run()