'''import matplotlib.pyplot as plt

def chatbot():
    print("Hello! I'm your marks graphing chatbot.")
    print("Let's plot your subject marks for different examinations.")

    try:
        num_subjects = int(input("Enter the number of subjects: "))
        subjects = []
        all_marks = {}

        for _ in range(num_subjects):
            subject = input("Enter subject name: ")
            num_tests = int(input(f"Enter the number of tests for {subject}: "))

            marks = []
            for i in range(1, num_tests + 1):
                test_mark = float(input(f"Enter marks for {subject} - Test {i}: "))
                marks.append(test_mark)

            all_marks[subject] = marks
            subjects.append(subject)

        plot_marks(subjects, all_marks)

    except ValueError:
        print("Invalid input. Please enter a valid number of subjects, tests, and marks.")

def plot_marks(subjects, all_marks):
    for subject, marks in all_marks.items():
        plt.plot(range(1, len(marks) + 1), marks, label=subject, marker='o')

    plt.xlabel('Tests')
    plt.ylabel('Marks')
    plt.title('Marks Graph for Different Subjects')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    chatbot()'''

import matplotlib.pyplot as plt

def greet():
    print("Hello! I'm your performance tracker chatbot.")
    print("I can help you visualize your performance over multiple tests.")
    print("Let's get started!")

def chat():
    greet()

    try:
        num_subjects = int(input("How many subjects did you have tests for? "))
        subjects = []
        all_marks = {}
        max_marks = {}

        for _ in range(num_subjects):
            subject = input(f"Enter the name of subject {_ + 1}: ")
            num_tests = int(input(f"How many tests did you have for {subject}? "))
            max_mark = float(input(f"What is the maximum marks for {subject}? "))

            marks = []
            for i in range(1, num_tests + 1):
                test_mark = float(input(f"Enter marks for {subject} - Test {i}: "))
                marks.append(test_mark)

            all_marks[subject] = marks
            subjects.append(subject)
            max_marks[subject] = max_mark

        plot_pie_chart(subjects, all_marks, max_marks)

    except ValueError:
        print("Oops! Something went wrong. Please enter valid numbers and marks.")

def plot_pie_chart(subjects, all_marks, max_marks):
    for subject, marks in all_marks.items():
        percentages = [mark / max_marks[subject] * 100 for mark in marks]
        plt.pie(percentages, labels=[f"Test {i}" for i in range(1, len(marks) + 1)], autopct='%1.1f%%', startangle=90)
        plt.title(f'Marks Distribution for {subject}')
        plt.show()

if __name__ == "__main__":
    chat()

