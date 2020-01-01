from tkinter import *


def calc_button(num):
    global operator
    operator = operator + str(num)
    text_input.set(operator)


def calc_clear():
    global operator
    operator = ""
    text_input.set(operator)


def calc_result():
    global operator
    res = str(eval(operator))
    text_input.set(res)


root = Tk()
root.geometry("354x460")
root.title("Simple Calculator")
root.config(background='grey')

operator = ""  # this will hold on to any input.
text_input = StringVar()

txtDisplay = Entry(root, font="none 12 bold", textvariable=text_input,
                   bd=10, insertwidth=4, bg="white", justify="right", relief=SOLID).grid(columnspan=4)

# --------------------------------------------------------------------------------------------------------------------------------------
button_7 = Button(root, padx=16, pady=16, bd=8, fg="black",
                  font="none 12 bold", text="7", command=lambda: calc_button(7), bg="red").grid(row=1)
button_8 = Button(root, padx=16, pady=16, bd=8, fg="black",
                  font="none 12 bold", text="8", command=lambda: calc_button(8), bg="red").grid(row=1, column=1)
button_9 = Button(root, padx=16, pady=16, bd=8, fg="black",
                  font="none 12 bold", text="9", command=lambda: calc_button(9), bg="red").grid(row=1, column=2)
button_mult = button_1 = Button(root, padx=16, pady=16, bd=8, fg="black",
                                font="none 12 bold", text="X", command=lambda: calc_button("*")).grid(row=1, column=3)
# --------------------------------------------------------------------------------------------------------------------------------------
button_4 = Button(root, padx=16, pady=16, bd=8, fg="black",
                  font="none 12 bold", text="4", command=lambda: calc_button(4), bg="red").grid(row=2)
button_5 = Button(root, padx=16, pady=16,  bd=8, fg="black",
                  font="none 12 bold", text="5", command=lambda: calc_button(5), bg="red").grid(row=2, column=1)
button_6 = Button(root, padx=16, pady=16,  bd=8, fg="black",
                  font="none 12 bold", text="6", command=lambda: calc_button(6), bg="red").grid(row=2, column=2)
button_sub = Button(root, padx=16, pady=16, bd=8, fg="black",
                    font="none 12 bold", text="-", command=lambda: calc_button("-")).grid(row=2, column=3)
# --------------------------------------------------------------------------------------------------------------------------------------
button_1 = Button(root, padx=16, pady=16, bd=8, fg="black",
                  font="none 12 bold", text="1", command=lambda: calc_button(1), bg="red").grid(row=3)
button_2 = Button(root, padx=16, pady=16, bd=8, fg="black",
                  font="none 12 bold", text="2", command=lambda: calc_button(2), bg="red").grid(row=3, column=1)
button_3 = Button(root, padx=16, pady=16, bd=8, command=lambda: calc_button(3), fg="black",
                  font="none 12 bold", text="3", bg="red").grid(row=3, column=2)
button_add = Button(root, padx=16, pady=16, bd=8, fg="black",
                    font="none 12 bold", text="+", command=lambda: calc_button("+")).grid(row=3, column=3)
# --------------------------------------------------------------------------------------------------------------------------------------
button_signinverse = Button(root, padx=16, pady=16, bd=8, fg="black",
                            font="none 12 bold", text="+/-", bg="red").grid(row=4)
button_0 = Button(root, padx=16, pady=16, bd=8, command=lambda: calc_button(0), fg="black",
                  font="none 12 bold", text="0", bg="red").grid(row=4, column=1)
button_decimal = Button(root, padx=16, pady=16, bd=8, fg="black",
                        font="none 12 bold", text=".", command=lambda: calc_button("."), bg="red").grid(row=4, column=2)
button_div = Button(root, padx=16, pady=16, bd=8, fg="black",
                    font="none 12 bold", text="/", command=lambda: calc_button("/")).grid(row=4, column=3)
# --------------------------------------------------------------------------------------------------------------------------------------
button_clear = Button(root, padx=16, bd=8, pady=16, fg="black",
                      font="none 12 bold", text="C", command=lambda: calc_clear()).grid(row=5)
button_remainderdiv = Button(root, padx=16, pady=16, bd=8, fg="black",
                             font="none 12 bold", text="%", command=lambda: calc_button("%")).grid(row=5, column=1)

button_result = Button(root, padx=16, pady=16, bd=8, fg="black",
                       font="none 12 bold", text="=", command=lambda: calc_result()).grid(row=5, column=2)

root.mainloop()
