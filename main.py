from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    canvas.itemconfig(timer, text=count)
    if count > 0:
        window.after(1000, count_down, count - 1)



# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 52))
title_label.grid(row=0, column=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_img)
timer = canvas.create_text(100, 130, text='00:00', fill='white', font=(FONT_NAME, 36, "bold"))
canvas.grid(row=1,column=1)

count_down(10)

start_button= Button(text="Start", fg='blue', bg=YELLOW, highlightthickness=0)
start_button.grid(row=2, column=0)

reset_button= Button(text="Reset", fg='blue', bg=YELLOW, highlightthickness=0)
reset_button.grid(row=2, column=2)

check_marks = Label(text="✓", fg=GREEN, bg=YELLOW)
check_marks.grid(row=3, column=1)

window.mainloop()