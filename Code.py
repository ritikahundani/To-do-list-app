import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QListWidget 

class ToDoApp (QWidget):
	def __init__(self):

		super().__init__()
		self.setWindowTitle("To-Do List App")
		self.setGeometry (200, 200, 400, 300)
		self.tasks = []
		self.layout = QVBoxLayout ()
		self.input_field = QLineEdit ()
		self.add_button = QPushButton("Add Task")
		self.delete_button=QPushButton("Delete Task")
		self.task_list = QListWidget()
		self.layout.addWidget(self.input_field)
		self.layout.addWidget(self.add_button)
		self.layout.addWidget(self.delete_button)
		self.layout.addWidget(self.task_list)
		self.add_button.clicked.connect(self.add_task)
		self.delete_button.clicked.connect(self.delete_task) 
		self.setLayout (self.layout)

	def add_task (self):

		task = self.input_field.text()

		if task:

			self.tasks.append(task)

			self.task_list.addItem(task)

			self.input_field.clear()

	def delete_task(self):

		task=self.task_list.currentRow()

		self.task_list.takeItem(task)

if __name__ == "__main__":

	app = QApplication(sys.argv)

	window = ToDoApp ()

	window.show()

	sys.exit(app.exec_())