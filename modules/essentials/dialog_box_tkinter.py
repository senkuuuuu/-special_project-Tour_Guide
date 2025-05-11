import tkinter as tk
from tkinter import messagebox

class DialogBox:
    def show_popup(self, type, error_message):
        root = tk.Tk()
        root.withdraw()
        result = None
        if type == 'error':
            messagebox.showerror('error', error_message)
        elif type == 'yesno':
            result = messagebox.askyesno("Confirmation", error_message)
        elif type == 'info':
            messagebox.showinfo('Notification', error_message)
        return result