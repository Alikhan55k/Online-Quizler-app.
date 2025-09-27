import tkinter
import html

window=tkinter.Tk()
window.title("Quizzler")
window.configure(padx=50, pady=50,bg="black")


class Quiz():
    import requests
    response = requests.get('https://opentdb.com/api.php?amount=10&category=18&type=boolean')
    response.status_code
    response = response.json()
    response = response['results']

    def __init__(self):
        self.score = 0
        self.question_no = 0
    def ask(self):
        q=self.response[self.question_no]
        question=html.unescape(q['question'])
        label2.configure(text=question,bg='white')
        def right_clicked():
            self.ans="True"

            if self.ans == q["correct_answer"]:
                label2.config(bg="green")
                self.score += 1
                label1.config(text=f'Score: {self.score}/10')
            else:
                label2.config(bg="red")
            if self.question_no == 9:
                label2.config(text="Game_end", bg="yellow")
            else:
                self.question_no += 1
                window.after(1000, self.ask)
        def wrong_clicked():

            self.ans="False"
            if self.ans == q["correct_answer"]:
                label2.config(bg="green")
                self.score += 1
                label1.config(text=f'Score: {self.score}/10')

            else:
                label2.config(bg="red")

            if self.question_no == 9:
                label2.config(text="Game_end",bg="yellow")
            else:
                self.question_no += 1
                window.after(1000, self.ask)

        button1.configure(command=right_clicked)
        button2.configure(command=wrong_clicked)


#Creating Labels buttons and canvas

label1=tkinter.Label(window, text="Score=0",bg="black",fg="white")
label2=tkinter.Label(window, text="Score=0/10",width=70,height=20)
true_button='Day34/images/true.png'
false_button='Day34/images/false.png'
photo1=tkinter.PhotoImage(file=true_button)
photo2=tkinter.PhotoImage(file=false_button)
button1=tkinter.Button(window, text="Quit", image=photo1)
button2=tkinter.Button(window, text="Quit", image=photo2)


#Apply all these things

label1.grid(row=0, column=2)
label2.grid(row=1, column=0,columnspan=3)
button1.grid(row=2, column=0)
button2.grid(row=2, column=2)


s1=Quiz()
s1.ask()
window.mainloop()