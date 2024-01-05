import csv
import matplotlib.pyplot as plt

def greet():
    print("Hello! I'm your versatile marks graphing chatbot.")
    print("I can help you visualize your performance over multiple tests.")
    print("Let's get started!")

def save_data_to_csv(subjects, all_marks, max_marks):
    with open(r'C:/Users/Student/Desktop/marks_data.csv', 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)

        # Write header
        csv_writer.writerow(['Subject', 'Test', 'Marks', 'Max Marks'])

        # Write data
        for subject, marks in all_marks.items():
            max_mark = max_marks[subject]
            for i, mark in enumerate(marks, start=1):
                csv_writer.writerow([subject, f'Test {i}', mark, max_mark])

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

        save_data_to_csv(subjects, all_marks, max_marks)
        plot_combined_graph(subjects, all_marks, max_marks)

        # TensorFlow model training can be added here for more advanced chatbot functionalities

    except ValueError:
        print("Oops! Something went wrong. Please enter valid numbers and marks.")

if __name__ == "__main__":
    chat()
