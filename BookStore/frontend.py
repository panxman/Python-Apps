import tkinter as tk
import backend


# Get Selected Row
def getSelectedRow(event):
    try:
        global selected_tuple
        index = list1.curselection()[0]
        selected_tuple = list1.get(index)
        e1.delete(0, tk.END)
        e1.insert(tk.END, selected_tuple[1])
        e2.delete(0, tk.END)
        e2.insert(tk.END, selected_tuple[2])
        e3.delete(0, tk.END)
        e3.insert(tk.END, selected_tuple[3])
        e4.delete(0, tk.END)
        e4.insert(tk.END, selected_tuple[4])
    except IndexError:
        pass


# View all Books
def viewBooks():
    list1.delete(0, tk.END)
    for row in backend.view():
        list1.insert(tk.END, row)


# Search for a specific Book
def searchBook():
    list1.delete(0, tk.END)
    for row in backend.search(title_text.get(), author_text.get(),
                              year_text.get(), isbn_text.get()):
        list1.insert(tk.END, row)


# Add Book
def addBook():
    backend.insert(title_text.get(), author_text.get(),
                   year_text.get(), isbn_text.get())
    list1.delete(0, tk.END)
    list1.insert(tk.END, (title_text.get(), author_text.get(),
                          year_text.get(), isbn_text.get()))


# Update Book
def updateBook():
    backend.update(selected_tuple[0],
                   title_text.get(), author_text.get(),
                   year_text.get(), isbn_text.get())


# Delete a Book
def deleteBook():
    backend.delete(selected_tuple[0])


window = tk.Tk()
window.title("Books I have read")
window.geometry("400x200")

# Labels
l1 = tk.Label(window, text="Title")
l1.grid(row=0, column=0)
l2 = tk.Label(window, text="Author")
l2.grid(row=0, column=2)
l3 = tk.Label(window, text="Year")
l3.grid(row=1, column=0)
l4 = tk.Label(window, text="ISBN")
l4.grid(row=1, column=2)

# entries
title_text = tk.StringVar()
e1 = tk.Entry(window, textvariable=title_text)
e1.grid(row=0, column=1)
author_text = tk.StringVar()
e2 = tk.Entry(window, textvariable=author_text)
e2.grid(row=0, column=3)
year_text = tk.StringVar()
e3 = tk.Entry(window, textvariable=year_text)
e3.grid(row=1, column=1)
isbn_text = tk.StringVar()
e4 = tk.Entry(window, textvariable=isbn_text)
e4.grid(row=1, column=3)

# Listbox and Scrollbar
list1 = tk.Listbox(window, height=6, width=35)
list1.grid(row=2, column=0, rowspan=6, columnspan=2)
sb1 = tk.Scrollbar(window)
sb1.grid(row=2, column=2, rowspan=6)
list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)
# Bind method - Show info of selected item
list1.bind('<<ListboxSelect>>', getSelectedRow)

# Buttons
b1 = tk.Button(window, text="View all", width=12, command=viewBooks)
b1.grid(row=2, column=3)
b2 = tk.Button(window, text="Search Entry", width=12, command=searchBook)
b2.grid(row=3, column=3)
b3 = tk.Button(window, text="Add Entry", width=12, command=addBook)
b3.grid(row=4, column=3)
b4 = tk.Button(window, text="Update Selected", width=12, command=updateBook)
b4.grid(row=5, column=3)
b5 = tk.Button(window, text="Delete Selected", width=12, command=deleteBook)
b5.grid(row=6, column=3)
b6 = tk.Button(window, text="Close", width=12, command=window.destroy)
b6.grid(row=7, column=3)

window.mainloop()
