from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
from questions import data
import random

class Education_Quiz:
	def __init__(self):
		self.qno=0
		self.disp_start()
		self.total_size=len(questions)
		self.correct=0

	def disp_res(self):
		for widget in ws.winfo_children():
			widget.destroy()
		text = Label(
			ws, 
            text="Результаты", 
            width=400,
            font=( 'ariel', 20, 'bold' ), 
            anchor= 'w',
			justify="center",
			wraplength=400
		)
		text.place(x=310, y=100)
		wrong_count = self.total_size - self.correct
		correct = f"Правильно: {self.correct}"
		wrong = f"Неправильно: {wrong_count}"
		score = int(self.correct / self.total_size * 100)
		result = f"{score}%"
		progress_bar = ttk.Progressbar(
			ws,
			length=200,
			mode="determinate"
		)
		progress_bar['value'] = score
		progress_bar.place(x=290, y=200)
		result_text = Label(
			ws, 
            text=f"{result}\n{correct}\n{wrong}", 
            width=400,
            font=( 'ariel', 20, 'bold' ), 
            anchor= 'w',
			justify="center",
			wraplength=400
		)
		result_text.place(x=280, y=230)

	def disp_start(self):
		self.start_label = Label(
			ws, 
            text="Учебный тренажер\nпо теме\n\"Пожарная безопасность\"", 
            width=400,
            font=( 'ariel', 20, 'bold' ), 
            anchor= 'w',
			justify="center",
			wraplength=400
		)
		self.start_label.place(x=220, y=100)

		self.start_button = Button(
			ws, 
            text="Начать",
            command=self.disp_ques,
            width=15,
            bg="#F2780C",
            fg="white",
            font=("ariel",16,"bold")
		)
		self.start_button.place(x=300, y=250)

	def check_ans(self, qno):
		if self.opt_sel.get() == answers[qno][1]:
			return True
    
	def next_btn(self):
		for widget in ws.winfo_children():
			widget.destroy()

		if self.check_ans(self.qno):
			self.correct += 1
		
		self.qno += 1
		
		if self.qno==self.total_size:
			self.disp_res()
		else:
			self.disp_ques()
			self.disp_opt()

	def show_hint(self):
		mb.showinfo("Подсказка", answers[self.qno][0])

	def buttons(self):
		next_button = Button(
            ws, 
            text="Следующий вопрос",
            command=self.next_btn,
            width=20,
            bg="#F2780C",
            fg="white",
            font=("ariel",16,"bold")
            )
		
		next_button.place(x=290,y=380)
		
		quit_button = Button(
            ws, 
            text="?", 
            command=self.show_hint,
            width=3,
            bg="black", 
            fg="white",
            font=("ariel",16," bold")
            )
		
		quit_button.place(x=40,y=380)


	def disp_opt(self):
		val=0
		self.opt_sel.set(0)
		for opt in options[self.qno]:
			self.opts[val]['text']=opt
			val+=1

	def disp_ques(self):
		self.start_button.destroy()
		self.start_label.destroy()

		self.disp_title()
		self.disp_text()
		self.opt_sel=IntVar()
		self.opts=self.radio_buttons()
		self.disp_opt()
		self.buttons()


	def disp_text(self):
		qno = Label(
            ws, 
            text=questions[self.qno], 
            width=60,
			height=2,
            font=( 'ariel' ,16, 'bold' ), 
            anchor= 'w',
			wraplength=650,
			justify="left"
            )
		qno.place(x=100, y=130)

	def disp_title(self):
		title = Label(
            ws, 
            text="Пожарная безопасность",
            width=50, 
			height=2,
            bg="green",
            fg="white", 
            font=("ariel", 20, "bold")
            )
		title.place(x=0, y=2)


	def radio_buttons(self):
		q_list = []
		y_pos = 190
		while len(q_list) < 4:
			radio_btn = Radiobutton(
                ws,
                text=" ",
                variable=self.opt_sel,
                value = len(q_list)+1,
                font = ("ariel",14)
                )
			q_list.append(radio_btn)
			radio_btn.place(x = 100, y = y_pos)
			y_pos += 40
		return q_list


ws = Tk()
ws.geometry("800x450")
ws.title("Пожарная безопасность. Учебный тренажер")

questions = []
options = []
answers=[]

questions_list = random.sample(data, 10)
for question in questions_list:
	questions.append(question["вопрос"])
	options.append(question["варианты"])
	answers.append(question["ответ"])

quiz = Education_Quiz()

ws.mainloop()
