from tkinter import *
from questions import data
from education_quiz import Education_Quiz

window = Tk()
window.minsize(800, 500)
window.maxsize(800, 500)
window.title("Пожарная безопасность. Учебный тренажер")

quiz = Education_Quiz(window, data)

window.mainloop()
