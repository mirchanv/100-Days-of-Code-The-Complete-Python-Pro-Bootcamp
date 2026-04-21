import math
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#CC1B61"
GREEN = "#06C413"
YELLOW = "#FCCB05"
OLD_PURPLE = "#9D8FA8"
LIGHT_GRAY = "#BAB4BF"
DARK_PURPLE = "#191B35"
FONT_NAME = "Arial"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 20
INFO = "Free Pomodoro Timer for Deep Work."
POMODORO = "pomodoro"
SHORT_BREAK = "short_break"
LONG_BREAK = "long_break"
app_mode = None
reps = 0
timer = None
work_sessions_completed = 0
empty_circle = "\u2B55"
filled_circle = "\U0001F534"

# ---------------------------- MODE ------------------------------- #
def set_mode(mode):
    # Reset all to default first
    pomodoro_label.config(fg=LIGHT_GRAY)
    short_break_label.config(fg=LIGHT_GRAY)
    long_break_label.config(fg=LIGHT_GRAY)

    global app_mode
    app_mode = mode

    if mode == POMODORO:
        pomodoro_label.config(fg=PINK)
        timer_label.config(fg=PINK)
        status_label.config(text="FOCUS")
    elif mode == SHORT_BREAK:
        short_break_label.config(fg=GREEN)
        timer_label.config(fg=GREEN)
        status_label.config(text="BREAK")
    elif mode == LONG_BREAK:
        long_break_label.config(fg=YELLOW)
        timer_label.config(fg=YELLOW)
        status_label.config(text="LONG BREAK")

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer(event):
    global timer, reps
    window.after_cancel(timer)
    update_timer_label(f"{format_time(0)}:{format_time(0)}")
    timer_label.config(fg=LIGHT_GRAY)
    progress_label.config(text=f"{empty_circle}{empty_circle}{empty_circle}{empty_circle}")
    set_mode(None)
    reps = 0
    start_btn.bind("<Button-1>", start_timer)

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer(event):
    start_btn.unbind("<Button-1>")
    global app_mode, reps, work_sessions_completed

    if app_mode == SHORT_BREAK:
        work_sessions_completed += 1
        add_progress_circle()

    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 9 == 0:
        set_mode(LONG_BREAK)
        countdown(long_break_sec)
    elif reps % 2 != 0:
        set_mode(POMODORO)
        countdown(work_sec)
    else:
        set_mode(SHORT_BREAK)
        countdown(short_break_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def format_time(time):
    global app_mode
    return "{:02d}".format(time)

def countdown(seconds_left):
    global timer
    count_min = math.floor(seconds_left / 60)
    count_sec = seconds_left % 60

    update_timer_label(f"{format_time(count_min)}:{format_time(count_sec)}")

    if seconds_left > 0:
        timer = window.after(1000, countdown, seconds_left - 1)
    else:
        start_timer(None)
        window.bell()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro App")
window.config(padx=5, pady=10, background=DARK_PURPLE)

for i in range(3):
    window.grid_columnconfigure(i, weight=1)

pomodoro_label = Label(text="Pomodoro", width=15, font=(FONT_NAME, 18), fg=PINK, bg=DARK_PURPLE)
pomodoro_label.grid(row=0, column=0)

short_break_label = Label(text="Short Break", width=15, font=(FONT_NAME, 18), fg=OLD_PURPLE, bg=DARK_PURPLE)
short_break_label.grid(row=0, column=1)

long_break_label = Label(text="Long Break", width=15, font=(FONT_NAME, 18), fg=OLD_PURPLE, bg=DARK_PURPLE)
long_break_label.grid(row=0, column=2)

status_label = Label(text="FOCUS", font=(FONT_NAME, 16, "bold"), fg=LIGHT_GRAY, bg=DARK_PURPLE)
status_label.grid(row=1, column=0, columnspan=3, pady=(45, 20))

timer_label = Label(text=f"{format_time(WORK_MIN)}:00", font=("DS-DIGITAL", 72, "bold"), fg=LIGHT_GRAY, bg=DARK_PURPLE)
timer_label.grid(row=2, column=0, columnspan=3, rowspan=2)

progress_label = Label(text=f"{empty_circle}{empty_circle}{empty_circle}{empty_circle}", bg=DARK_PURPLE)
progress_label.grid(row=5, column=0, columnspan=3, pady=(20, 20))

button_frame = Frame(bg=DARK_PURPLE)
button_frame.grid(row=6, column=0, columnspan=3, pady=(25, 10))

start_border = Frame(button_frame, bg="#456882", padx=2, pady=2)
start_border.pack(side="left", padx=10)

start_btn = Label(
    start_border,
    text="START",
    font=(FONT_NAME, 14, "bold"),
    bg=DARK_PURPLE,
    fg="#456882",
    padx=10,
    pady=10,
    cursor="hand1",
    highlightbackground=PINK
)
start_btn.pack()

reset_border = Frame(button_frame, bg="#456882", padx=2, pady=2)
reset_border.pack(side="left", padx=10)

reset_btn = Label(
    reset_border,
    text="RESET",
    font=(FONT_NAME, 14, "bold"),
    bg=DARK_PURPLE,
    fg="#456882",
    padx=10,
    pady=10,
    cursor="hand1"
)
reset_btn.pack()

info_label = Label(text=INFO, font=(FONT_NAME, 16), fg=LIGHT_GRAY, bg=DARK_PURPLE)
info_label.grid(row=7, column=0, columnspan=3, pady=(10, 10))


def update_timer_label(time_left):
    timer_label.config(text=time_left)

def enable_hover_effect(event):
    event.widget.config(fg=PINK)

def disable_hover_effect(event):
    event.widget.config(fg="#456882")

def add_progress_circle():
    global work_sessions_completed
    current_progress = progress_label["text"][:work_sessions_completed].replace(empty_circle, filled_circle)
    left_progress = progress_label["text"][work_sessions_completed:]
    full_progress = current_progress + left_progress
    progress_label.config(text=full_progress)


# ---------------------------- HOVER EVENTS ------------------------------- #
start_btn.bind("<Enter>", enable_hover_effect)
start_btn.bind("<Leave>", disable_hover_effect)
reset_btn.bind("<Enter>", enable_hover_effect)
reset_btn.bind("<Leave>", disable_hover_effect)

# ---------------------------- CLICK EVENTS ------------------------------- #
start_btn.bind("<Button-1>", start_timer)
reset_btn.bind("<Button-1>", reset_timer)

window.mainloop()
