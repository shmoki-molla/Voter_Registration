from tkinter import *
from requests import get_unique_values, get_values_by_year_and_states
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

root = Tk()
root.title('Voters registration')
root.geometry('1280x720')
root.resizable(width=False, height=False)
root.config(bg='blue')
states = get_unique_values('Jurisdiction')
months = get_unique_values('Month')

class Data:
    def __init__(self, year=None, states=None, votes=None):
        self.year = year
        self.states = states
        self.votes = votes
    def set_year(self, year):
        self.year = year

    def set_states(self, states):
        self.states = states

    def set_votes(self, votes):
        self.votes = votes

    def get_all(self):
        print(self.year, self.states, self.votes)


data = Data()




def on_button_clicked(text, selected_states):
    if text in selected_states:
        selected_states.remove(text)
    else:
        selected_states.append(text)

def knopki():
    selected_states = []
    for word in states:
        chk = Checkbutton(root, text=word,
                          font=('Times New Roman', 10, 'bold'),
                          bg='green'
                          )
        chk['command'] = lambda w=word: on_button_clicked(w, selected_states)
        chk.pack()
    data.set_states(selected_states)
    btn_start.pack()

def start():
    data.set_votes(get_values_by_year_and_states(data.year, data.states))
    data.get_all()
    num_months = len(months)
    num_states = len(data.states)
    fig, ax = plt.subplots()
    width = 0.35

    x = np.arange(num_months)

    for i in range(num_states):
        state_votes = np.array(data.votes[i])
        ax.bar(x + i*width, state_votes, width, label=data.states[i])
    ax.set_xticks(x + width*num_states/2)
    ax.set_xticklabels(months)
    ax.legend()
    for widget in root.winfo_children():
        widget.destroy()
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().pack()



label_year = Label(root,
                   text='Выберите год',
                   font=('Times New Roman', 30, 'bold'),
                   bg = 'white')
label_year.pack()

btn_2016 = Button(root,
                text='2016',
                font=('Times New Roman', 30, 'bold'),
                bg = 'orange',
                activebackground = 'yellow',
                fg = 'white',
                activeforeground = 'black'
                  )
btn_2016.pack()
btn_2020 = Button(root,
                  text = '2020',
                  font=('Times New Roman', 30, 'bold'),
                    bg = 'orange',
                    activebackground = 'yellow',
                    fg = 'white',
                activeforeground = 'black'
                  )
btn_2020.pack()

btn_2016.bind('<ButtonPress-1>', lambda e: [data.set_year(2016), btn_2016.pack_forget(), label_year.pack_forget(), btn_2020.pack_forget(), knopki()])
btn_2020.bind('<ButtonPress-1>', lambda e: [data.set_year(2020), btn_2020.pack_forget(), label_year.pack_forget(), btn_2016.pack_forget(), knopki()])


btn_start = Button(root, text="Запуск", command=start,
                   font=('Times New Roman', 20, 'bold'),
                   bg='orange'
                   )



