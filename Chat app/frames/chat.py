import requests
import tkinter as tk

from tkinter import ttk

from frames.message_window import MessageWindow

GET_URL_ADDRESS = "api_address"
POST_URL_ADDRESS = "api_address"

messages_info = [{'date': 1715768278.425697, 'message': "Hello world asdagidsgf;uefhoeufhepofuHOUDFHDJVNDJKV;dfh;OEDHUEFHSJVBSKHVsfh;ekFGkdaghasbCKHSABCASHKBeqfgfuhwe"}]


class Chat(ttk.Frame):

    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        self.messages_section = MessageWindow(self)
        self.messages_section.grid(row=0, column=0, sticky=tk.E+tk.W+tk.N+tk.S)
        scroll_bar = tk.Scrollbar(self, orient=tk.VERTICAL, command=self.messages_section.yview)
        scroll_bar.grid(row=0, column=1, sticky=tk.N+tk.S)
        self.messages_section.configure(yscrollcommand=scroll_bar.set)

        input_section = ttk.Frame(self, padding=(10, 10), style='Background.TFrame')
        input_section.grid(row=1, column=0, columnspan=2, sticky=tk.E+tk.W)
        self.text_field = tk.Text(input_section, height=3)
        self.text_field.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 5))
        send_button = ttk.Button(input_section, text='Send', command=self.post_message)
        send_button.pack(pady=(0, 5), fill=tk.BOTH, expand=True)
        fedge_button = ttk.Button(input_section, text='Fedge', command=self.get_messages)
        fedge_button.pack(fill=tk.BOTH, expand=True)

        self.get_messages()

    def post_message(self):
        """Post messages in the chat"""

        body = self.text_field.get('1.0', tk.END).strip()
        # requests.post(POST_URL_ADDRESS, json={'message': body})
        self.text_field.delete('1.0', tk.END)
        self.get_messages()

    def get_messages(self):
        """Fedge messages from a database"""
        global messages_info
        
        # messages_info = requests.get(GET_URL_ADDRESS).json()
        self.messages_section._update_messages_section(messages_info)
        self.messages_section.after(50, lambda: self.messages_section.yview_moveto(1))