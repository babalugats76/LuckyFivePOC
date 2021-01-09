'''
@see https://docs.python.org/3/library/tkinter.html
@see https://effbot.org/tkinterbook
'''
from tkinter import Frame, Button, Tk, Label, font
from TicketGenerator import TicketGenerator

class LuckyFive(Frame):

    def __init__(self, master=None, title="Lucky Five"):
        super().__init__(master)
        self.pack(fill='both', expand=True, padx=5, pady=5)
        self.create_widgets()
        self.master.title(title)
        self.master.minsize(width=250,height=80)

    def create_widgets(self):
        
        # Add "Generate" Button
        self.generate = Button(self)
        self.generate["text"] = "Generate Ticket"
        self.generate["command"] = self.generateTicket
        self.generate.pack(fill='both', expand=True, padx=5, pady=5, side='top')

        # All Ticket Label
        labelStyle = font.Font(family='monospace', size=20)
        self.ticket = Label(self, font=labelStyle)
        self.ticket["text"] = ""
        self.ticket.pack(fill='both', expand=True, padx=5, pady=5, side='bottom')

        # Add "Quit" Button
        self.quit = Button(self, text="QUIT", fg="red", command=self.master.destroy)
        self.quit.pack(fill='both', expand=True, padx=5, pady=5, side='bottom')

    def generateTicket(self):
        # Generate ticket and update label
        self.ticket["text"] = ""
        newTicket = TicketGenerator.generate()
        print(newTicket)
        self.ticket["text"] = " ".join(str(n) for n in newTicket)

root = Tk()
app = LuckyFive(master=root)
app.mainloop()