import tkinter as tk

from datetime import datetime
from tkinter import ttk

COLOUR_BACKGROUND = "#ffffff"
existing_labels = []


class MessageWindow(tk.Canvas):

    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        self.container = container
        self.config(bg=COLOUR_BACKGROUND, highlightthickness=0)

        self.messages_frame = ttk.Frame(container)
        self.messages_frame.columnconfigure(0, weight=1)
        messages_window = self.create_window((0, 0), window=self.messages_frame, anchor=tk.N+tk.W, width=self.winfo_width())

        def configure_message_window(event):
            self.itemconfig(messages_window, width=self.winfo_width())

            for message_buble in self.messages_frame.winfo_children():
                for label in message_buble.winfo_children():
                    label.config(wraplength=self.winfo_width() - 10)

        def configure_scroll_region(event):
            self.config(scrollregion=self.bbox(tk.ALL))

        def on_mouse_wheel(event):
            self.yview_scroll(-event.delta, 'units')

        self.bind_all('<MouseWheel>', on_mouse_wheel)
        self.bind('<Configure>', configure_message_window)
        self.messages_frame.bind('<Configure>', configure_scroll_region)

    def _update_messages_section(self, messages_info):
        """Update messages section"""

        for message in messages_info:
            time_stamp = datetime.fromtimestamp(message['date']).strftime('%d-%m-%Y %H:%M:%S')
            text = message['message']

            if (time_stamp, text) not in existing_labels:
                existing_labels.append((time_stamp, text))
                self._create_message_bubble(time_stamp, text)

    def _create_message_bubble(self, time_stamp, text):
        """Create new message bubble"""

        message_bubble = ttk.Frame(self.messages_frame)
        message_bubble.grid(sticky=tk.E+tk.W)
        message_bubble.columnconfigure(0, weight=1)

        time_stamp_label = ttk.Label(message_bubble, text=time_stamp)
        time_stamp_label.grid(sticky=tk.E+tk.W)

        text_label = ttk.Label(message_bubble, text=text)
        text_label.grid(sticky=tk.E+tk.W)