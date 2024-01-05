
import matplotlib.pyplot as plt

def greet():
    print("Hello! I'm your versatile marks graphing chatbot.")
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

        plot_combined_graph(subjects, all_marks, max_marks)

        # TensorFlow model training can be added here for more advanced chatbot functionalities

    except ValueError:
        print("Oops! Something went wrong. Please enter valid numbers and marks.")

def plot_combined_graph(subjects, all_marks, max_marks):
    # Plotting line graph for subject-wise performance
    for subject, marks in all_marks.items():
        plt.plot(range(1, len(marks) + 1), marks, label=subject, marker='o')

    plt.xlabel('Tests')
    plt.ylabel('Marks')
    plt.title('Marks Graph for Different Subjects')
    plt.legend()
    plt.show()

    # Plotting pie chart for marks distribution
    for subject, marks in all_marks.items():
        percentages = [mark / max_marks[subject] * 100 for mark in marks]
        plt.pie(percentages, labels=[f"Test {i}" for i in range(1, len(marks) + 1)], autopct='%1.1f%%', startangle=90)
        plt.title(f'Marks Distribution for {subject}')
        plt.show()

if __name__ == "__main__":
    chat()
