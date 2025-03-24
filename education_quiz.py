import random
from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
from utils import round_rectangle, change_on_hover

class Education_Quiz():
	def __init__(self, window, data):
		self.window = window
		self.data = data
		self.selected_answers = {}
		self.start()
		
	def start(self):
		self.generate_questions()
		self.qno = 0
		self.total_size=len(self.questions)
		self.correct=0
		self.display_start()
		self.selected_answers.clear()
	
	def render_background(self):
		canva = Canvas(self. window, bg='#dda15e', width=800, height=500)
		round_rectangle(canva, 50, 50, 750, 450, radius=150, fill="#fefae0")
		canva.pack()

	def generate_questions(self):
		self.questions = []
		self.options = []
		self.answers=[]

		questions_list = random.sample(self.data, 10)
		for question in questions_list:
			self.questions.append(question["вопрос"])
			self.options.append(question["варианты"])
			self.answers.append(question["ответ"])

	def display_results(self):
		self.correct = self.check_ans()
		self.clear()
		self.render_background()

		text = Label(
			self.window, 
            text="Результаты", 
            width=20,
			height=3,
            font=( 'ariel', 20, 'bold' ), 
            anchor= 'w',
			justify="center",
			background="#fefae0",
			foreground="#283618"
		)
		text.place(x=315, y=100)
		
		wrong_count = self.total_size - self.correct
		correct = f"Правильно: {self.correct}"
		wrong = f"Неправильно: {wrong_count}"
		
		score = int(self.correct / self.total_size * 100)
		result = f"{score}%"
		progress_bar = ttk.Progressbar(
			self.window,
			length=200,
			mode="determinate"
		)
		progress_bar['value'] = score
		progress_bar.place(x=300, y=200)
		
		result_text = Label(
			self.window, 
            text=f"{result}\n\n{correct}\n{wrong}", 
            width=20,
			height=4,
            font=( 'ariel', 20, 'bold' ), 
            anchor= 'w',
			justify="center",
			background="#fefae0",
			foreground="#283618"
		)
		result_text.place(x=289, y=230)
		
		start_btn = Button(
			self.window, 
            text="Начать заново",
            command=self.start,
            width=20,
            bg="#606c38",
            fg="#fefae0",
            font=("ariel",16,"bold"),
			relief="flat"
		)
		change_on_hover(start_btn) 
		start_btn.place(x=265, y=390)

	def display_start(self):
		self.clear()
		self.render_background()
		start_label = Label(
			self.window, 
            text="Учебный тренажер\nпо теме\n\"Пожарная безопасность\"", 
            width=25,
			height=3,
            font=( 'ariel', 20, 'bold' ), 
            anchor= 'w',
			justify="center",
			background="#fefae0",
			foreground="#283618"
		)
		start_label.place(x=230, y=140)

		start_button = Button(
			self.window, 
            text="Начать",
            command=self.display_question,
            width=15,
            bg="#606c38",
            fg="#fefae0",
            font=("ariel",16,"bold"),
			relief="flat"
		)
		change_on_hover(start_button) 
		start_button.place(x=310, y=290)

	def check_ans(self):
		correctAnswers = 0
		for questionNumber, answer in self.selected_answers.items():
			if answer == self.answers[questionNumber][1]:
				correctAnswers += 1
		return correctAnswers
  
		
	def clear(self):
		for widget in self.window.winfo_children():
			widget.destroy() 

	def next_btn(self):
		self.clear()

		self.selected_answers[self.qno] = self.opt_sel.get()
		
		self.qno += 1
		
		if self.qno==self.total_size:
			self.display_results()
		else:
			self.display_question()

	def show_hint(self):
		mb.showinfo("Подсказка", self.answers[self.qno][0])
		
	def back_btn(self):
		self.clear()
		if self.qno == 0:
			self.display_start()
		else:
			self.qno -= 1
			self.display_question()

	def buttons(self):
		next_button = Button(
            self.window, 
            text="Следующий вопрос",
            command=self.next_btn,
            width=20,
            bg="#606c38",
            fg="white",
            font=("ariel",16,"bold"),
			relief="flat"
            )
		change_on_hover(next_button) 
		next_button.place(x=265,y=380)
		back_btn = Button(
			self.window, 
            text="<", 
            command=self.back_btn,
            width=3,
            bg="#606c38", 
            fg="white",
            font=("ariel",16," bold"),
			relief="flat"
        )
		change_on_hover(back_btn) 
		back_btn.place(x=100,y=380)
		hint_button = Button(
            self.window, 
            text="?", 
            command=self.show_hint,
            width=3,
            bg="#606c38", 
            fg="white",
            font=("ariel",16," bold"),
			relief="flat"
            )
		change_on_hover(hint_button) 
		hint_button.place(x=640,y=380)

	def display_opt(self):
		self.render_background()
		self.opt_sel=IntVar()
		self.opts=self.radio_buttons()
		val=0

		if self.qno in self.selected_answers:
			self.opt_sel.set(self.selected_answers[self.qno])
		else:
			self.opt_sel.set(0)

		for opt in self.options[self.qno]:
			self.opts[val]['text']=opt
			val+=1

	def display_question(self):
		self.clear()
		
		self.render_background()
		self.display_title()
		self.display_text()
		self.display_opt()
		self.buttons()


	def display_text(self):
		qno = Label(
            self.window, 
            text=self.questions[self.qno], 
            width=48,
			height=5,
            font=( 'ariel' ,16, 'bold' ), 
            anchor= 'w',
			background="#fefae0",
			foreground="#283618",
			justify="left",
			wraplength=600
            )
		qno.place(x=100, y=90)

	def display_title(self):
		title = Label(
            self.window, 
            text="Пожарная безопасность",
            width=40,
			height=1,
			background="#dda15e",
			foreground="#283618", 
            font=("ariel", 20, "bold")
            )
		title.place(x=60, y=2)


	def radio_buttons(self):
		q_list = []
		y_pos = 190
		while len(q_list) < 4:
			radio_btn = Radiobutton(
                self.window,
                text=" ",
                variable=self.opt_sel,
                value = len(q_list)+1,
                font = ("ariel",14),
				background="#fefae0",
			    foreground="#283618"
                )
			q_list.append(radio_btn)
			radio_btn.place(x = 100, y = y_pos)
			y_pos += 40
		return q_list
