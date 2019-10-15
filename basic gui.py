from tkinter import *
import tkinter.messagebox as tmsg

root = Tk()


def get_entry():
    a = title_text.get()
    b = author_text.get()
    c = year_text.get()
    d = price_text.get()
    if d.isdigit() and c.isdigit():
        listbox.insert(END, f'Title: {a}, Author: {b}, Year: {c}, Price: ${d}')
        title_text.set('')
        author_text.set('')
        year_text.set('')
        price_text.set('')
    else:
        tmsg.showinfo('Incorrect Input', 'Please give price/year value in numbers')
        if d.isdigit():
            year_text.set('0')
        else:
            price_text.set('0')


# TODO : the same problem .  the get() value gives empty value inside a  inner func. Have to find a sol
#  for it
def update_selected():
    update_pos = listbox.curselection()  # this takes in the cursor selection
    listbox.delete(ANCHOR)  # this deletes the object at the pos
    rooted = Tk()
    rooted.geometry('300x300')
    label = Label(rooted, text='i am a pop up window for updating selection', bg='grey22', fg='white')
    label.pack(fill=X)
    lab1 = Label(rooted, text='Title')
    lab1.pack(side=TOP, anchor='w')
    update_text = StringVar()
    ent1 = Entry(rooted, textvariable=update_text)
    ent1.pack()
    insert_text = update_text.get()
    print(insert_text)  # getting empty value here . have to fix the issue

    def click():
        global insert_text
        a = but1.cget('text')

        if a == 'Submit':
            listbox.insert(update_pos, insert_text + '<--this has to appear')  # this adds the new data

    but1 = Button(rooted, text='Submit', command=click)
    but1.pack()

    rooted.mainloop()


def delete():
    listbox.delete(ANCHOR)


def deleteall():
    ask_del = tmsg.askquestion("WARNING", 'Are you sure you want to delete all')
    if ask_del == 'yes':
        listbox.delete(0, END)


# TODO check for the values of inner func as why are they not getting value. Plus fix it cant get why
#  they are not in tuple range
t_txt = StringVar()
a_txt = StringVar()
y_txt = StringVar()
p_txt = StringVar()


def submit():
    global t_txt, a_txt, y_txt, p_txt
    print(t_txt)
    a1 = t_txt.get()
    a2 = a_txt.get()
    a3 = y_txt.get()
    a4 = p_txt.get()
    print('submit clicked')
    print(a1 + 'for a1')
    print(a2 + 'for a2')
    print(a3 + 'for a3')
    print(a4 + 'for a4')
    print(p_txt.get() + 'for p_txt.get()')
    try:
        lb = listbox.get(END, 0).index(
            f'Title: {t_txt.get()}, Author: {a_txt.get()}, Year: {y_txt.get()}, Price: ${p_txt.get()}')
        print(lb)
    except Exception as e:
        print('its not working ')
        print(e)


def search():
    global p_txt, a_txt, y_txt, p_txt
    root1 = Tk()
    root1.geometry('300x300')
    root1.title('Search')
    # labels
    l5 = Label(root1, text='Title')
    l5.pack(side=TOP, anchor='w')
    # t_txt = StringVar()
    e5 = Entry(root1, textvariable=t_txt)
    e5.pack(side=TOP, anchor='w')
    l6 = Label(root1, text='Author')
    l6.pack(side=TOP, anchor='w')

    # a_txt = StringVar()
    e6 = Entry(root1, textvariable=a_txt)
    e6.pack(side=TOP, anchor='w')

    l7 = Label(root1, text='Year')
    l7.pack(side=TOP, anchor='w')
    # y_txt = StringVar()
    e7 = Entry(root1, textvariable=y_txt)
    e7.pack(side=TOP, anchor='w')
    l8 = Label(root1, text='Price')
    l8.pack(side=TOP, anchor='w')
    # p_txt = StringVar()
    e8 = Entry(root1, textvariable=p_txt)
    e8.pack(side=TOP, anchor='w')

    button_submit = Button(root1, text='Submit', command=submit)
    button_submit.pack()

    root1.mainloop()


def viewall():
    root = Tk()
    root.geometry('300x300')
    label = Label(root, text='i am a pop up window for viewing all', bg='grey22', fg='white')
    label.pack(fill=X)

    root.mainloop()


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
listbox = Listbox(root, height=10, width=35, selectmode=EXTENDED, activestyle=DOTBOX, )
# dotbox is the selection is surrounded by doted line
listbox.grid(row=3, column=0, columnspan=3, rowspan=5)

# scroll bar

scrollbar = Scrollbar(root)
scrollbar.grid(row=3, column=3, rowspan=5, sticky='nsw', )  # here you can see used 'nsw' so that
# it stretches in north and south and also putts in west
scrollbar.config(command=listbox.yview)
listbox.config(yscrollcommand=scrollbar.set)

scrollbar1 = Scrollbar(root, orient=HORIZONTAL)
scrollbar1.grid(row=7, column=0, columnspan=3, sticky='ews')
scrollbar1.config(command=listbox.xview)
listbox.config(xscrollcommand=scrollbar1.set)

# buttons

button1 = Button(root, text='View All', width=12, command=viewall)
button1.grid(row=3, column=3, sticky='e')
button2 = Button(root, text='Search Entry', width=12, command=search)
button2.grid(row=4, column=3, sticky='e')
button3 = Button(root, text='Add Entry', width=12, command=get_entry)
button3.grid(row=5, column=3, sticky='e')
button4 = Button(root, text='Update Selected', width=12,
                 command=update_selected)  # see how i imported the file  new_window
button4.grid(row=6, column=3, sticky='e')
button5 = Button(root, text='Delete Selected', width=12, command=delete)
button5.grid(row=7, column=3, sticky='e')
button6 = Button(root, text='Delete All', width=12, command=deleteall)
button6.grid(row=8, column=3, sticky='e')
button7 = Button(root, text='Close', width=12, command=quit)
button7.grid(row=9, column=3, sticky='e')


def name_position():
    n_pos = listbox.curselection()
    print(n_pos)

    root2 = Tk()

    try:
        lab1 = Label(root2, text=f'The position of the selection is {n_pos[0] + 1}', bg='grey22', fg='white',
                     font='lucida 20 bold')
        lab1.pack(fill=BOTH, )
    except IndexError as i:
        print(i)
        lab1 = Label(root2, text='Nothing is Selected!!', bg='grey22', fg='white',
                     font='lucida 15 bold')
        lab1.pack(fill=BOTH, )
        print('value of tuple index for n_pos is out range')

    root2.mainloop()


button7 = Button(root, text='Get Position', width=12, command=name_position)
button7.grid(row=10, column=3, sticky='e')

root.mainloop()
