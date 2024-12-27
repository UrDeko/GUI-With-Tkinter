import tkinter.font as font
import tkinter as tk

from tkinter import ttk

from converters import MetersToFeet, FeetToMeters

POSITIONING = ("+800+200")
COLOUR_BACKGROUND = "#ffffff"
COLOUR_NIGHT_BLUE = "#027ebd"


class Converter(tk.Tk):
    """Converter App"""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        style = ttk.Style(self)
        style.theme_use('clam')
        style.configure('FrameColour.TFrame', background=COLOUR_NIGHT_BLUE)
        style.configure('TButton', background=COLOUR_NIGHT_BLUE, foreground=COLOUR_BACKGROUND)
        style.configure('TFrame', background=COLOUR_BACKGROUND)
        style.configure('TLabel', background=COLOUR_BACKGROUND, foreground=COLOUR_NIGHT_BLUE)
        style.map('TButton',
                  background=[(tk.ACTIVE, COLOUR_BACKGROUND), (tk.DISABLED, COLOUR_NIGHT_BLUE)],
                  foreground=[(tk.ACTIVE, COLOUR_NIGHT_BLUE), (tk.DISABLED, COLOUR_BACKGROUND)])
        font.nametofont('TkDefaultFont').configure(size=20, family='Courier')
        font.nametofont('TkTextFont').configure(size=20, family='Courier')

        self.title("Converter")
        self.geometry(POSITIONING)
        self.resizable(width=True, height=False)
        self.columnconfigure(0, weight=1)

        container = ttk.Frame(self, padding=5, style='FrameColour.TFrame')
        container.columnconfigure(0, weight=1)
        container.grid(row=0, column=0, sticky=tk.E+tk.W+tk.N+tk.S)

        miles_to_feet = MetersToFeet(container, self, padding=10)
        miles_to_feet.grid(row=0, column=0, sticky=tk.E+tk.W)

        feet_to_miles = FeetToMeters(container, self, padding=10)
        feet_to_miles.grid(row=0, column=0, sticky=tk.E+tk.W)

        self.converters = dict()
        self.converters[MetersToFeet] = miles_to_feet
        self.converters[FeetToMeters] = feet_to_miles

        self._switch(MetersToFeet)

    def _switch(self, converter):
        """Switch between converters"""

        self.bind("<Return>", self.converters[converter].calculate)
        self.converters[converter].clear()
        self.converters[converter].lift()


converter = Converter()
converter.mainloop()
