from tkinter import Tk


# we are using inheritance so the parent of this class will be Tk (we mentioned in the main comments that this is form )
class Window(Tk):
    def __init__(self, title="User Management Application "):
        # Warning : the parent has an init method so the child should call the parents's init method
        # this can be done by using super().
        super().__init__()
        # its parent has this title
        self.title(title)
        self.geometry("500x300")
        # Responsive
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

    def show(self):
        self.mainloop()
