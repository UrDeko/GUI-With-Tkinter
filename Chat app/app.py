import tkinter as tk

from tkinter import ttk

from frames import Chat

COLOUR_BACKGROUND = "#dcecff"
COLOUR_MESSAGE_BUBBLE = "#dbe9f8"
COLOUR_NIGHT_BLUE = "#027ebd"
COLOUR_PRIMARY = "#074869"
COLOUR_FONT = "#ffffff"


class Messenger(tk.Tk):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        style = ttk.Style(self)
        style.theme_use('clam')
        style.configure('TButton', background=COLOUR_NIGHT_BLUE, foreground=COLOUR_FONT)
        style.configure('Background.TFrame', background=COLOUR_PRIMARY)
        style.configure('TLabel', background=COLOUR_MESSAGE_BUBBLE, foreground=COLOUR_PRIMARY)

        self.title('Messenger')
        self.geometry("800x500+300+100")
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        main_frame = Chat(self)
        main_frame.grid(row=0, column=0, sticky=tk.E+tk.W+tk.N+tk.S)


if __name__ == "__main__":
    app = Messenger()
    app.mainloop()