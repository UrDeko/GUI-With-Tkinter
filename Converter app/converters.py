import tkinter as tk

from tkinter import ttk

FONT = ("Helvetica", 18, "normal")
MULTIPLE = 3.28084


class MetersToFeet(ttk.Frame):
    """Meters to Feet Converter"""

    def __init__(self, container, controller, **kwargs):
        super().__init__(container, **kwargs)
        
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        self.meters = tk.StringVar()
        self.feet = tk.StringVar()

        meters_lbl = ttk.Label(self, text="Meters:", anchor=tk.E)
        meters_lbl.grid(row=0, column=0)
        meters_in = ttk.Entry(self, textvariable=self.meters)
        meters_in.grid(row=0, column=1)
        meters_in.focus()

        feet_lbl = ttk.Label(self, text="Feet:", anchor=tk.E)
        feet_lbl.grid(row=1, column=0)
        feet_out = ttk.Entry(self, textvariable=self.feet)
        feet_out.grid(row=1, column=1)

        convert_btn = ttk.Button(self, text="Convert", command=self.calculate)
        convert_btn.grid(row=2, column=0, columnspan=2)
        switch_btn = ttk.Button(self, text="Switch", command=lambda: controller._switch(FeetToMeters))
        switch_btn.grid(row=3, column=0, columnspan=2)

        for widget in self.winfo_children():
            widget.grid_configure(padx=10, pady=5, sticky=tk.E+tk.W)
            # widget.config(font=FONT)

        convert_btn.grid_configure(pady=(15, 5))

    def calculate(self, *args):
        """Convert the meters to feet"""

        try:
            input_ = float(self.meters.get())
            result = round(input_ * MULTIPLE, 2)
            self.feet.set(result)
        except ValueError:
            pass

    def clear(self):
        """Clear entry widgets"""

        self.meters.set("")
        self.feet.set("")


class FeetToMeters(ttk.Frame):
    """Feet to Meters Converter"""

    def __init__(self, container, controller, **kwargs):
        super().__init__(container, **kwargs)
        
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        self.feet = tk.StringVar()
        self.meters = tk.StringVar()

        feet_lbl = ttk.Label(self, text="Feet:", anchor=tk.E)
        feet_lbl.grid(row=0, column=0)
        feet_in = ttk.Entry(self, textvariable=self.feet)
        feet_in.grid(row=0, column=1)
        feet_in.focus()

        meters_lbl = ttk.Label(self, text="Meters:", anchor=tk.E)
        meters_lbl.grid(row=1, column=0)
        meters_out = ttk.Entry(self, textvariable=self.meters)
        meters_out.grid(row=1, column=1)


        convert_btn = ttk.Button(self, text="Convert", command=self.calculate)
        convert_btn.grid(row=2, column=0, columnspan=2)
        switch_btn = ttk.Button(self, text="Switch", command=lambda: controller._switch(MetersToFeet))
        switch_btn.grid(row=3, column=0, columnspan=2)

        for widget in self.winfo_children():
            widget.grid_configure(padx=10, pady=5, sticky=tk.E+tk.W)
            # widget.config(font=FONT)

        convert_btn.grid_configure(pady=(15, 5))

    def calculate(self, *args):
        """Convert the feet to meters"""

        try:
            input_ = float(self.feet.get())
            result = round(input_ / MULTIPLE, 2)
            self.meters.set(result)
        except ValueError:
            pass

    def clear(self):
        """Clear entry widgets"""

        self.feet.set("")
        self.meters.set("")