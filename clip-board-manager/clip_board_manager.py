"""Clipboard Manager

This script creates a simple GUI application that monitors your clipboard
and displays its contents in a listbox. You can double-click on an item
to copy it back to the clipboard.
"""

import tkinter as tk
import pyperclip


def update_listbox():
    """Checks the clipboard for new content and updates the listbox.

  This function retrieves the current clipboard content and compares it
  with the internal list. If a new item is found, it's added to the list
  and displayed in the listbox. A separator line is also added for clarity.
  The listbox is then scrolled to the bottom to show the latest entry.
  Finally, the function schedules itself to run again after 1 second
  to continuously monitor the clipboard.
  """
    new_item = pyperclip.paste()
    if new_item not in X:
        X.append(new_item)
        listbox.insert(tk.END, new_item)
        listbox.insert(tk.END, "----------------------")
    listbox.yview(tk.END)
    root.after(1000, update_listbox)


def copy_to_clipboard():
    """Copies the selected item from the listbox to the clipboard.

  This function retrieves the currently selected item from the listbox
  and copies it to the clipboard using the pyperclip module. The function
  checks if an item is selected before attempting to copy.
  """
    selected_item = listbox.get(listbox.curselection())
    if selected_item:
        pyperclip.copy(selected_item)


X = []

root = tk.Tk()
root.title("Clipboard Manager")
root.geometry("500x500")
root.configure(bg="#f0f0f0")

frame = tk.Frame(root, bg="#f0f0f0")
frame.pack(padx=10, pady=10)

label = tk.Label(frame, text="Clipboard Contents:", bg="#f0f0f0")
label.grid(row=0, column=0)

scrollbar = tk.Scrollbar(root)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

listbox = tk.Listbox(root, width=150, height=150, yscrollcommand=scrollbar.set)
listbox.pack(pady=10)
scrollbar.config(command=listbox.yview)

update_listbox()

listbox.bind("<Double-Button-1>", copy_to_clipboard)

root.mainloop()
