from tkinter import *
import random
import string

class App(Tk):
    def __init__(self):
        super().__init__()
        self.title("Text Encryption")
        self.geometry("530x300")
        self.resizable(False,False)
        self.canva = Canvas(self,bg="#418c4c",width=530,height=60,highlightthickness=0)
        self.canva.pack(pady=12)
        self.labeltitle = Label(self,text="Text Encryption App V1",font=("Arial",17,"bold"),bg="#418c4c",fg="white")
        self.labeltitle.place(relx=0.5, y=37, anchor="center")
        self.topframe = Frame(self)
        self.topframe.pack(side="top",pady=5)
        self.buttonconvert = Button(self.topframe,borderwidth=1,relief="solid",text="Convert",width=12,command=self.shufflealgorithm)
        self.buttonconvert.grid(column=0,row=0)
        self.buttonclear = Button(self.topframe,borderwidth=1,relief="solid",text="Clear Field",width=12,command=self.delete)
        self.buttonclear.grid(column=1,row=0,padx=7)
        self.frameone = Frame(self)
        self.frameone.pack(side="left",pady=12)
        self.l1 = Label(self.frameone,text="Input:",font=("Arial",13,"bold"))
        self.l1.pack(anchor="nw",padx=15)
        self.input = Text(self.frameone,height=11,borderwidth=1,relief="solid",width=30)
        self.input.pack(padx=15,anchor="nw")
        self.frametwo = Frame(self)
        self.frametwo.pack(side="left",pady=12)
        self.l2 = Label(self.frametwo,text="Output:",font=("Arial",13,"bold"))
        self.l2.pack(anchor="nw",padx=15)
        self.input1 = Text(self.frametwo,height=11,borderwidth=1,relief="solid",state="disabled")
        self.input1.pack(padx=15)
    def shufflealgorithm(self):
        thetext = ""
        z = self.input.get("1.0", "end-1c")
        list1 = list(" " + string.ascii_letters + string.digits + string.ascii_lowercase + string.ascii_uppercase)
        keys = list1.copy()
        random.shuffle(keys)
        for i in z:
            lindexe = list1.index(i)
            thetext += keys[lindexe]
        self.input1.config(state="normal")
        self.input1.delete("1.0","end")
        self.input1.insert(END,thetext)
        self.input1.config(state="disabled")
    def delete(self):
        self.input1.config(state="normal")
        self.input1.delete("1.0","end")
        self.input.delete("1.0","end")
        self.input1.config(state="disabled")



if __name__ == "__main__":
    app = App()
    app.mainloop()


