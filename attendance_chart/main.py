import tkinter as tk
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

def create_pie_chart():
    # Get input from user
    present = int(present_entry.get())
    absent = int(absent_entry.get())
    total_students = present + absent

    # Data
    labels = ['Present', 'Absent']
    sizes = [present, absent]

    # Plot
    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')
    ax.set_title('Attendance in My Class')

    # Show plot
    plt.show()

# Create window
window = tk.Tk()
window.title("Attendance in My Class")

# Present label and entry
present_label = tk.Label(window, text="Number of students present:")
present_label.pack()
present_entry = tk.Entry(window)
present_entry.pack()

# Absent label and entry
absent_label = tk.Label(window, text="Number of students absent:")
absent_label.pack()
absent_entry = tk.Entry(window)
absent_entry.pack()

# Button to create pie chart
create_button = tk.Button(window, text="Create Pie Chart", command=create_pie_chart)
create_button.pack()

# Run window
window.mainloop()
