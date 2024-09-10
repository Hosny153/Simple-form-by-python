import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

root = tk.Tk()
root.title("Form")

# Global variable to keep track of current ID
current_id = 1

def Data():
    # This function retrieves data from the input fields,
    # displays the data in a message box, and inserts it
    # into the Treeview.

    global current_id
    # Get data from input fields
    All_Data = (Entry1.get() + "\n" +
                Entry2.get() + "\n" +
                Entry3.get() + "\n" +
                gender.get() + "\n" +
                Choose.get() + "\n" +
                Entry6.get("1.0", "end-1c"))
    
    # Show information in a message box
    messagebox.showinfo("Information", f'You Information: \n{All_Data}')
    
    # Insert data into Treeview
    Tree_Table.insert("", "end", text=str(current_id), values=(All_Data))
    current_id += 1

def Clear():
    # This function clears all the input fields.
    Entry1.delete(0, "end")
    Entry2.delete(0, "end")
    Entry3.delete(0, "end")
    gender.set("none")
    Choose.delete(0, "end")
    Entry6.delete("1.0", "end")

# Create GUI elements
Heading = tk.Label(root, text="Data Entry Form", font=("Arial", 20, "bold"))
Heading.grid(row=0, column=0, pady=5, columnspan=4)

label1 = tk.Label(root, text="First Name")
label1.grid(row=1, column=0, pady=10, padx=5, sticky="we")

Entry1 = tk.Entry(root, width=20)
Entry1.grid(row=1, column=1, pady=10, sticky="we")

label2 = tk.Label(root, text="Last Name")
label2.grid(row=1, column=2, pady=10, padx=5, sticky="we")

Entry2 = tk.Entry(root, width=20)
Entry2.grid(row=1, column=3, pady=10, sticky="we")

label3 = tk.Label(root, text="Birth Date")
label3.grid(row=2, column=0, pady=5, padx=5, sticky="w")

Entry3 = tk.Entry(root, width=20)
Entry3.grid(row=2, column=1, columnspan=3, pady=10, sticky="we")

label4 = tk.Label(root, text="Gender")
label4.grid(row=3, column=0, pady=5, padx=5, sticky="w")

gender = tk.StringVar()
gender.set("none")

Check1 = tk.Radiobutton(root, text="Male", variable=gender, value="Male")
Check1.grid(row=3, column=1, sticky="w")

Check2 = tk.Radiobutton(root, text="Female", variable=gender, value="Female")
Check2.grid(row=3, column=2, sticky="w")

label5 = tk.Label(root, text="Country")
label5.grid(row=4, column=0, pady=5, padx=5, sticky="w")

Choose = ttk.Combobox(root, values=["Egypt", "Morocco", "Algeria", "UAE"], width=20)
Choose.grid(row=4, column=1, pady=5, columnspan=3, padx=5, sticky="we")

label6 = tk.Label(root, text="Address")
label6.grid(row=5, column=0, pady=5, padx=5, sticky="nw")

Entry6 = tk.Text(root, width=20, height=5)
Entry6.grid(row=5, column=1, columnspan=3, pady=10, sticky="we")

Save_btn = tk.Button(root, text="Save", width=8, command=Data)
Save_btn.grid(row=6, column=1, sticky="e", pady=10)

Clear_btn = tk.Button(root, text="Clear", width=8, command=Clear)
Clear_btn.grid(row=6, column=3, sticky="w")

Heading2 = tk.Label(root, text="All Information", font=("Arial", 20, "bold"))
Heading2.grid(row=7, column=0, pady=5, columnspan=4)

Tree_Table = ttk.Treeview(root,show="headings")
Tree_Table.grid(row=8, column=1, columnspan=3, pady=5, padx=5)

# Define columns for Treeview
Tree_Table["columns"] = ("First Name", "Last Name", "Birth Date", "Gender", "Country", "Address")

# Set headings for Treeview columns
Tree_Table.heading("First Name", text="First Name")
Tree_Table.heading("Last Name", text="Last Name")
Tree_Table.heading("Birth Date", text="Birth Date")
Tree_Table.heading("Gender", text="Gender")
Tree_Table.heading("Country", text="Country")
Tree_Table.heading("Address", text="Address")

root.mainloop()
