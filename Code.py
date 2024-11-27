import tkinter as tk
import sqlite3

# Connect to database or create it
conn = sqlite3.connect("tasks.db")
cursor = conn.cursor()

# Create table if it doesn't exist
cursor.execute("CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY, task TEXT, completed BOOLEAN)")

# Add a task to the database
def add_task():
    task = entry.get()
    if task:
        cursor.execute("INSERT INTO tasks (task, completed) VALUES (?, ?)", (task, False))
        conn.commit()
        update_listbox()
        entry.delete(0, tk.END)

# Mark selected task as completed
def mark_as_completed():
    selected_task_index = listbox.curselection()
    if selected_task_index:
        task_id = listbox.get(selected_task_index).split(" | ")[0]  # Extract task ID
        cursor.execute("UPDATE tasks SET completed = ? WHERE id = ?", (True, task_id))
        conn.commit()
        update_listbox()

# Delete a task from the database
def delete_task():
    selected_task_index = listbox.curselection()
    if selected_task_index:
        task_id = listbox.get(selected_task_index).split(" | ")[0]  # Extract task ID
        cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
        conn.commit()
        update_listbox()

# Update the listbox display
def update_listbox():
    listbox.delete(0, tk.END)
    cursor.execute("SELECT id, task, completed FROM tasks")
    for task in cursor.fetchall():
        display_text = f"{task[0]} | {task[1]}"  # Display task with its ID
        if task[2]:  # Check if the task is completed
            display_text += " ✓"  # Add checkmark
        listbox.insert(tk.END, display_text)

# Initialize the app
root = tk.Tk()
root.title("To-Do List")

# Entry for new tasks
entry = tk.Entry(root, width=40)
entry.pack(pady=10)

# Add Task Button
add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack(pady=5)

# Task Listbox
listbox = tk.Listbox(root, width=50, height=15)
listbox.pack(pady=10)

# Populate listbox with tasks from the database
update_listbox()

# Mark as Completed Button
complete_button = tk.Button(root, text="Mark as Completed", command=mark_as_completed)
complete_button.pack(pady=5)

# Delete Task Button
delete_button = tk.Button(root, text="Delete Task", command=delete_task)
delete_button.pack(pady=5)

root.mainloop()

# Close database connection when the app closes
conn.close()
