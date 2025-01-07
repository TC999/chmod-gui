import json

def load_translations(language):
    with open('translations.json', 'r', encoding='utf-8') as f:
        translations = json.load(f)
    return translations.get(language, translations['en'])

# Load translations for the desired language
language = 'zh'  # Change this to 'en' for English or other language codes for other languages
translations = load_translations(language)

def _(text):
    return translations.get(text, text)
import tkinter as tk
from tkinter import messagebox, filedialog

# Function to generate chmod command
def generate_command():
    owner = owner_var.get()
    group = group_var.get()
    others = others_var.get()
    file_path = file_entry.get()

    # Convert symbolic permissions to numeric
    permissions = {
        'r': 4,
        'w': 2,
        'x': 1,
        '-': 0
    }

    owner_perm = sum([permissions[c] for c in owner])
    group_perm = sum([permissions[c] for c in group])
    others_perm = sum([permissions[c] for c in others])

    chmod_command = f"chmod {owner_perm}{group_perm}{others_perm} {file_path}"
    
    # Check for dangerous commands
    if "777" in chmod_command or ("-R 777" in chmod_command and "/usr" in chmod_command):
        result_label.config(text=f"{_('generated_command')}{chmod_command}", fg="red")
        messagebox.showwarning(_("Warning"), _("warning_message"))
    else:
        result_label.config(text=f"{_('generated_command')}{chmod_command}", fg="black")
    
    # Store the generated command for copying
    generated_command.set(chmod_command)

# Function to copy command to clipboard
def copy_command():
    root.clipboard_clear()
    root.clipboard_append(generated_command.get())
    messagebox.showinfo("Info", "Command copied to clipboard!")

# Function to show help message
def show_help():
    messagebox.showinfo(_("Help"), _("help_message"))

# Function to open file dialog
def select_file():
    filename = filedialog.askopenfilename()
    file_entry.delete(0, tk.END)  # Clear the entry box first
    file_entry.insert(0, filename)

# Load translations for the desired language
language = 'zh'  # Change this to 'en' for English or other language codes for other languages
translations = load_translations(language)

def _(text):
    return translations.get(text, text)

# Create the main window
root = tk.Tk()
root.title(_("Chmod Command Generator"))

# Create the grid layout
tk.Label(root, text=_("owner_permissions")).grid(row=0, column=0)
tk.Label(root, text=_("group_permissions")).grid(row=1, column=0)
tk.Label(root, text=_("others_permissions")).grid(row=2, column=0)
tk.Label(root, text=_("file_directory_name")).grid(row=3, column=0)

owner_var = tk.StringVar(value="---")
group_var = tk.StringVar(value="---")
others_var = tk.StringVar(value="---")

tk.Entry(root, textvariable=owner_var).grid(row=0, column=1)
tk.Entry(root, textvariable=group_var).grid(row=1, column=1)
tk.Entry(root, textvariable=others_var).grid(row=2, column=1)

file_entry = tk.Entry(root)
file_entry.grid(row=3, column=1)

file_button = tk.Button(root, text=_("select_file"), command=select_file)
file_button.grid(row=3, column=2)

generate_button = tk.Button(root, text=_("generate_command"), command=generate_command)
generate_button.grid(row=4, column=0, columnspan=3)

help_button = tk.Button(root, text=_("help"), command=show_help)
help_button.grid(row=5, column=0, columnspan=3)

result_label = tk.Label(root, text=_("generated_command"))
result_label.grid(row=6, column=0, columnspan=3)

# Add a variable to store the generated command
generated_command = tk.StringVar()

# Add a button to copy the command
copy_button = tk.Button(root, text=_("copy_command"), command=copy_command)
copy_button.grid(row=7, column=0, columnspan=3)

# Run the application
root.mainloop()
