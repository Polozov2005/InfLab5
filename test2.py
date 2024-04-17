from tkinter import *
from PIL import ImageTk, Image
from pylatexenc.latex2text import LatexNodes2Text

root = Tk()
root.geometry("1100x500")
root['bg'] = 'grey'

equation = r'$\frac{1}{2} \times 3 = \frac{3}{2}$' 
equation_text = LatexNodes2Text().latex_to_text(equation)
label = Label(root, text=equation_text, height=100, width=100)
label.pack()

root.mainloop()