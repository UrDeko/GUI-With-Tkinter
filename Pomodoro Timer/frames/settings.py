import tkinter as tk
from tkinter import ttk


class Settings(ttk.Frame):

    def __init__(self, container, controller, show_timer, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        settings_frame = ttk.Frame(self, padding=10, style='Background.TFrame')
        settings_frame.columnconfigure(0, weight=1)
        settings_frame.columnconfigure(1, weight=1)
        settings_frame.grid(row=0, column=0, sticky=tk.E+tk.W)

        pomodoro_lbl = ttk.Label(settings_frame, text='Pomodoro:', style='Description.TLabel')
        pomodoro_lbl.grid(row=0, column=0, sticky=tk.W)
        long_break_lbl = ttk.Label(settings_frame, text='Long Break:', style='Description.TLabel')
        long_break_lbl.grid(row=1, column=0, sticky=tk.W)
        short_break_lbl = ttk.Label(settings_frame, text='Short Break:', style='Description.TLabel')
        short_break_lbl.grid(row=2, column=0, sticky=tk.W)

        pomodoro_spb = tk.Spinbox(settings_frame, from_=0, to=120, increment=1, justify=tk.CENTER, textvariable=controller.pomodoro, width=10, highlightbackground='#074869')
        pomodoro_spb.grid(row=0, column=1, sticky=tk.E)
        long_break_spb = tk.Spinbox(settings_frame, from_=0, to=40, increment=1, justify=tk.CENTER, textvariable=controller.long_break, width=10, highlightbackground='#074869')
        long_break_spb.grid(row=1, column=1, pady=10, sticky=tk.E)
        short_break_spb = tk.Spinbox(settings_frame, from_=0, to=20, increment=1, justify=tk.CENTER, textvariable=controller.short_break, width=10, highlightbackground='#074869')
        short_break_spb.grid(row=2, column=1, sticky=tk.E)

        button_frame = ttk.Frame(self, padding=5, style='Background.TFrame')
        button_frame.columnconfigure(0, weight=1)
        button_frame.grid(row=1, column=0, columnspan=2, sticky=tk.E+tk.W+tk.S)

        back_btn = ttk.Button(button_frame, text='<- Back', command=show_timer, style='PomodoroButton.TButton')
        back_btn.grid(row=0, column=0, sticky=tk.E+tk.W)