#################################################
# CS03B - Summer 2026
# Assignment 1 - Question 3
# Student Name: Rayaan Riyaz
# SID: 20691965
#################################################


class Employee:
    def __init__(self, name, number):
        self.name = name
        self.number = number
    def getName(self):
        return self.name
    def getNumber(self):
        return self.number
    def setName(self, name):
        self.name = name
    def setNumber(self, number):
        self.number = number
class ProductionWorker(Employee):
    def __init__(self, name, number, shift_number, hourly_pay_rate):
        super().__init__(name, number)
        self.shift_number = shift_number
        self.hourly_pay_rate = hourly_pay_rate
    def getShiftNumber(self):
        return self.shift_number
    def getHourlyPayRate(self):
        return self.hourly_pay_rate
    def setShiftNumber(self, shift_number):
        self.shift_number = shift_number
    def setHourlyPayRate(self, hourly_pay_rate):
        self.hourly_pay_rate = hourly_pay_rate


def run():
    """
    Students should implement their code for Question 3 inside this function.
    """
    # TODO: Write your code here

    name = input("Employee Name: ")
    number = int(input("Employee Number: "))
    shift_number = int(input("Shift Number: "))
    if shift_number != 1 and shift_number != 2:
        print("Invalid Shift Number")
        return
    hourly_pay_rate = float(input("Hourly Pay Rate: "))

    worker = ProductionWorker(name, number, shift_number, hourly_pay_rate)
    print()
    print("Employee Name:", worker.getName())
    print("Employee Number:", worker.getNumber())
    print("Shift Number:", worker.getShiftNumber())
    print("Hourly Pay Rate:", worker.getHourlyPayRate())

    # Example logic:
    # result = 5 + 5
    # print(f"Result: {result}")

if __name__ == "__main__":
    # This allows students to run this specific file 
    # individually for testing (e.g., `python q1.py`)
    run()