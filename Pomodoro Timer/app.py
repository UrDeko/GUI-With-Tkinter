import tkinter as tk

from collections import deque
from tkinter import ttk

from frames import Settings, Timer

COLOUR_LIGHT = "#fcfcfc"
COLOUR_NIGHT_BLUE = "#027ebd"
COLOUR_PRIMARY = "#074869"
COLOUR_SECONDARY = "#293846"


class PomodoroApp(tk.Tk):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        style = ttk.Style()
        style.theme_use('clam')

        style.configure('Background.TFrame', background=COLOUR_PRIMARY)
        style.configure('Timer.TFrame', background=COLOUR_LIGHT)
        style.configure('Counter.TLabel', background=COLOUR_LIGHT, foreground=COLOUR_NIGHT_BLUE)
        style.configure('Description.TLabel', background=COLOUR_PRIMARY, foreground=COLOUR_LIGHT, font=("TkDefaultFont", 16))
        style.configure('PomodoroButton.TButton', background=COLOUR_PRIMARY, foreground=COLOUR_LIGHT)

        style.map('PomodoroButton.TButton',
                  background=[(tk.ACTIVE, COLOUR_PRIMARY), (tk.DISABLED, COLOUR_LIGHT)],
                  foreground=[(tk.ACTIVE, COLOUR_LIGHT), (tk.DISABLED, COLOUR_PRIMARY)])

        self.title('Pomodoro')
        self.geometry('+600+200')
        self.resizable(width=True, height=False)
        self.columnconfigure(0, weight=1)

        self.timer_order = ["Pomodoro", "Short Break", "Pomodoro", "Short Break", "Pomodoro", "Long Break"]
        self.timer_schedule = deque(self.timer_order)
        self.pomodoro = tk.StringVar(value='25')
        self.long_break = tk.StringVar(value='15')
        self.short_break = tk.StringVar(value='5')

        container = ttk.Frame(self, padding=(0, 10), style='Background.TFrame')
        container.columnconfigure(0, weight=1)
        container.grid(row=0, column=0, sticky=tk.E+tk.W+tk.N+tk.S)

        timer = Timer(container, self, lambda: self._show_frame(Settings))
        timer.grid(row=0, column=0, sticky=tk.E+tk.W+tk.N+tk.S)
        settings = Settings(container, self, lambda: self._show_frame(Timer), style='Background.TFrame')
        settings.grid(row=0, column=0, sticky=tk.E+tk.W+tk.N+tk.S)

        self.frames = dict()
        self.frames[Timer] = timer
        self.frames[Settings] = settings

        self._show_frame(Timer)

    def _show_frame(self, frame):
        """Switch between frames"""

        self.frames[frame].lift()


if __name__ == "__main__":
    app = PomodoroApp()
    app.mainloop()