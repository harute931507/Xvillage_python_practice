gui = input("GUI mode ? [y/n] ")
SUP = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")
function = "ax2+bx+c=d".translate(SUP)

if gui == "y":
    import tkinter as tk
    win = tk.Tk()

    win.title("Solution")
    win.geometry("480x270")

    fun = tk.Label(win, text=function, font=("Helvetica", 24))
    a = tk.Label(win, text="a is ", font=("CourierNew", 16))
    b = tk.Label(win, text="b is ", font=("CourierNew", 16))
    c = tk.Label(win, text="c is ", font=("CourierNew", 16))
    d = tk.Label(win, text="d is ", font=("CourierNew", 16))
    answer1 = tk.Label(win, text="answer1", font=("Helvetica", 20))
    answer2 = tk.Label(win, text="answer2", font=("Helvetica", 20))

    aVar = tk.Entry(win, text="a")
    bVar = tk.Entry(win, text="b")
    cVar = tk.Entry(win, text="c")
    dVar = tk.Entry(win, text="d")

    def cal():
        A = int(aVar.get())
        B = int(bVar.get())
        C = int(cVar.get())
        D = int(dVar.get())

        x1 = (B+(B*B-4*A*C)**(1/2))/(2*A)
        x2 = (B-(B*B-4*A*C)**(1/2))/(2*A)
        X1 = '({0.real:.2f} + {0.imag:.2f}i)'.format(x1)
        X2 = '({0.real:.2f} + {0.imag:.2f}i)'.format(x2)
        answer1.config(text=X1)
        answer2.config(text=X2)

    solve = tk.Button(win, text="Solve", command=cal)

    fun.grid(row=0, column=3)

    a.grid(row=2, column=1)
    b.grid(row=3, column=1)
    c.grid(row=4, column=1)
    d.grid(row=5, column=1)

    aVar.grid(row=2, column=2)
    bVar.grid(row=3, column=2)
    cVar.grid(row=4, column=2)
    dVar.grid(row=5, column=2)

    solve.grid(row=6, column=3)
    answer1.grid(row=7, column=1)
    answer2.grid(row=8, column=1)

    win.mainloop()

else:

    print(function)
    a = int(input("a = ? "))
    b = int(input("b = ? "))
    c = int(input("c = ? "))
    d = int(input("d = ? "))
    c = c - d
    x1 = (-b+(b*b-4*a*c)**(1/2))/(2*a)
    x2 = (-b-(b*b-4*a*c)**(1/2))/(2*a)
    print(x1, x2)
