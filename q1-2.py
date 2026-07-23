#################################################
# CS03B - Summer 2026
# Assignment 2 - Question 1
# Student Name: Rayaan Riyaz
# SID: 20691965
#################################################

def run():
    """
    Students should implement their code for Question 1 inside this function.
    """
    # TODO: Write your code here

    # 1A

    color_names = ["Black", "Red", "Maroon", "Yellow"]
    color_codes = ["#000000", "#FF0000", "#800000", "#FFFF00"]
    dictionaries = []
    for i in range(len(color_names)):
        color_dictionary = {
            "color_name": color_names[i],
            "color_code": color_codes[i],

        }
        dictionaries.append(color_dictionary)

    print(dictionaries)

    # 1B

    classes = ["Class-V", "Class-VI", "Class-VII", "Class-VIII"]
    numbers = [1, 2, 2, 3]
    
    combination = {}
    
    for i in range(len(classes)):
        combination[classes[i]] = {numbers[i]}

    print(combination)
    
    # Example logic:
    # result = 5 + 5
    # print(f"Result: {result}")

if __name__ == "__main__":
    # This allows students to run this specific file 
    # individually for testing (e.g., `python q1.py`)
    run()