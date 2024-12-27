import tkinter as tk

from collections import deque
from tkinter import ttk


class Timer(ttk.Frame):

    def __init__(self, container, controller, show_settings, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        self.configure(style='Background.TFrame')
        self.time_decrement = None

        self.columnconfigure(0, weight=1)
        self.controller = controller

        self.current_timer_txt = tk.StringVar(value=self.controller.timer_schedule[0])
        self.current_time = tk.StringVar(value=f'{self.controller.pomodoro.get()}:00')

        self.timer_description = ttk.Label(self, padding=(5, 5), textvariable=self.current_timer_txt, anchor=tk.CENTER, style='Description.TLabel')
        self.timer_description.grid(row=0, column=0, padx=(5, 0), sticky=tk.W)

        settings_btn = ttk.Button(self, text='Settings', command=show_settings, style='PomodoroButton.TButton')
        settings_btn.grid(row=0, column=1, padx=(0, 5), pady=(0, 5), sticky=tk.E)

        timer_frame = ttk.Frame(self, height=100, style='Timer.TFrame')
        timer_frame.grid(row=1, column=0, columnspan=2, pady=5, sticky=tk.E+tk.W)
        self.time_counter = ttk.Label(timer_frame, textvariable=self.current_time, font='Courier 46', style='Counter.TLabel')
        self.time_counter.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        buttons = ttk.Frame(self, padding=5, style='Background.TFrame')
        buttons.columnconfigure(0, weight=1)
        buttons.columnconfigure(1, weight=1)
        buttons.columnconfigure(2, weight=1)
        buttons.grid(row=2, column=0, columnspan=2, sticky=tk.E+tk.W)
        self.start_btn = ttk.Button(buttons, text='Start', command=self._decrement_time, style='PomodoroButton.TButton')
        self.start_btn.grid(row=0, column=0, sticky=tk.E+tk.W)
        self.stop_btn = ttk.Button(buttons, text='Stop', command=self._stop, state=tk.DISABLED, style='PomodoroButton.TButton')
        self.stop_btn.grid(row=0, column=1, sticky=tk.E+tk.W, padx=5)
        self.reset_btn = ttk.Button(buttons, text='Reset', command=self._reset, state=tk.DISABLED, style='PomodoroButton.TButton')
        self.reset_btn.grid(row=0, column=2, sticky=tk.E+tk.W)

    def _decrement_time(self):
        """Decrement time by one"""
        
        self.start_btn.config(state=tk.DISABLED)
        self.stop_btn.configure(state=tk.NORMAL)
        self.reset_btn.configure(state=tk.NORMAL)

        if self.current_time.get() != "00:00":
            minutes = int(self.current_time.get().split(':')[0])
            seconds = int(self.current_time.get().split(':')[1])

            if seconds > 0:
                seconds -= 1
            else:
                seconds = 59
                minutes -= 1

            self.current_time.set(f'{minutes:02d}:{seconds:02d}')
        elif self.current_time.get() == "00:00":
            self.controller.timer_schedule.rotate(-1)
            next_up = self.controller.timer_schedule[0]

            self.current_timer_txt.set(next_up)

            match next_up:
                case "Pomodoro":
                    self.current_time.set(value=f'{int(self.controller.pomodoro.get()):02d}:00')
                case "Long Break":
                    self.current_time.set(value=f'{int(self.controller.long_break.get()):02d}:00')
                case "Short Break":
                    self.current_time.set(value=f'{int(self.controller.short_break.get()):02d}:00')

        self.time_decrement = self.after(1000, self._decrement_time)

    def _stop(self):
        """Stop timer"""

        self.stop_btn.configure(state=tk.DISABLED)
        self.start_btn.configure(state=tk.NORMAL)
        self.after_cancel(self.time_decrement)

    def _reset(self):
        """Reset timer"""

        self._stop()
        self.reset_btn.config(state=tk.DISABLED)
        self.controller.timer_schedule = deque(self.controller.timer_order)
        self.current_timer_txt.set(value=self.controller.timer_schedule[0])
        self.current_time.set(value=f'{int(self.controller.pomodoro.get()):02d}:00')