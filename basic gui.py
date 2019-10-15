from tkinter import *

root = Tk()
# Main Text
l1 = Label(root, text='Title')
l1.grid(row=0, column=0)

l2 = Label(root, text='Author')
l2.grid(row=0, column=2)

l3 = Label(root, text='Year')
l3.grid(row=1, column=0)

l4 = Label(root, text='Price')
l4.grid(row=1, column=2)

# Entry
title_text = StringVar()
e1 = Entry(root, textvariable=title_text)
e1.grid(row=0, column=1)
print(f'{e1.get()} is the value of the entry')

author_text = StringVar()
e2 = Entry(root, textvariable=author_text)
e2.grid(row=0, column=3)

year_text = StringVar()
e3 = Entry(root, textvariable=year_text)
e3.grid(row=1, column=1)

price_text = StringVar()
e4 = Entry(root, textvariable=price_text)
e4.grid(row=1, column=3)

# list box
listbox = Listbox(root, height=6, width=35)
listbox.grid(row=2, column=0, columnspan=3, rowspan=5)

# scroll bar

scrollbar = Scrollbar(root)
scrollbar.grid(row =2 , column=3 , rowspan = 6,sticky = 'nsw',) # here you can see used 'nsw' so that
# it stretches in north and south and also putts in west
scrollbar.config(command = listbox.yview)
listbox.config(yscrollcommand = scrollbar.set)

# buttons

button = Button(root,text = 'View All',width = 12)
button.grid(row = 3,column =3, sticky = 'e')
button = Button(root,text = 'Search Entry',width = 12)
button.grid(row = 4,column =3, sticky = 'e')
button = Button(root,text = 'Add Entry',width = 12)
button.grid(row = 5,column =3, sticky = 'e')
button = Button(root, text = 'Update Selected',width = 12)
button.grid(row = 6,column =3, sticky = 'e')
button = Button(root,text = 'Delete Selected',width = 12)
button.grid(row = 7,column =3, sticky = 'e')
button = Button(root, text = 'Close',width = 12)
button.grid(row = 8,column =3, sticky = 'e')


root.mainloop()

