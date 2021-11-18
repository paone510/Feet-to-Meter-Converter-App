
from tkinter import Tk, Button, Label, DoubleVar, Entry

window = Tk()
window.title("feet to meter app")
window.configure(background="light green")
window.geometry("500x320")
window.resizable(width=False, height=False)

def convert():
    value = float(ft_entry.get())
    meter = value * 0.3048
    mt_value.set('%.4f' % meter)

def clear():
    ft_value.set('')
    mt_value.set('')
    
    
#feet
ft_lbl = Label(window, text='feet', bg='purple', fg='white', width=14)
ft_lbl.grid(column=0, row=0, padx=15, pady=15)

ft_value = DoubleVar()
ft_entry = Entry(window, textvariable=ft_value, width=14)
ft_entry.grid(column=2, row=0)
ft_entry.delete(0, 'end')

#meter
mt_lbl = Label(window, text='meter', bg='purple', fg='white', width=14)
mt_lbl.grid(column=0, row=1, padx=15, pady=30)

mt_value = DoubleVar()
mt_entry = Entry(window, textvariable=mt_value, width=14)
mt_entry.grid(column=2, row=1)
mt_entry.delete(0, 'end')

#button
convert_btn = Button(window, text='convert', bg='blue', fg='white', width=14, command=convert)
convert_btn.grid(column=0, row=3, padx=15)

#button
clear_btn = Button(window, text='clear', bg='black', fg='white', width=14, command=clear)
clear_btn.grid(column=2, row=3, padx=15)


window.mainloop()



