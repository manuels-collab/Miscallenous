import math
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
reps = 1
timer = ''

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    text.config(text="Timer")
    check_marks.config(text="")
    global reps
    reps = 1


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global  reps
    if reps % 2 != 0:
        text.config(text="Work", fg=GREEN)
        count_down(60 * WORK_MIN)
    if reps == 2 or reps == 4 or reps == 6:
        text.config(text="Break", fg=PINK)
        count_down(60 * SHORT_BREAK_MIN)
    if reps == 8:
        text.config(text="Break", fg=RED)
        count_down(60 * LONG_BREAK_MIN)
        reps = 1
    else:
        count_down(60 * WORK_MIN)

    reps += 1


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global reps
    global timer
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✅"
        check_marks.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)


text = Label(text="Timer", font=(FONT_NAME, 24, "bold"), fg=GREEN, bg=YELLOW)
text.grid(row=0, column=1)

check_marks = Label(fg=GREEN, bg=YELLOW, width=5, height=5)
check_marks.grid(row=3, column=1)

start_button = Button(text="Start", highlightthickness=0, command= start_timer, font=(FONT_NAME, 15, "bold"), width=4, height=1, fg=GREEN, relief='groove')
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer, font=(FONT_NAME, 15, "bold"), width=4, height=1, fg=GREEN, relief='groove')
reset_button.grid(row=2, column=2)





window.mainloop()