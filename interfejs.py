import tkinter as tk
import time
class Application(tk.Frame):
    def __init__(self,wideo ,audio ,samples = 100,master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
        self.samples = samples
        self.wideo = wideo
        self.audio = audio
        self.index = 0
        self.union_list = []
        self.current_list = []
        self.which = "x"
         



    def create_widgets(self):
        self.button1 = tk.Button(self, text="wideo", command=lambda: self.start_selection(self.wideo,"w"))
        self.button1.pack(side="left")
        self.button2 = tk.Button(self, text="audio", command=lambda: self.start_selection(self.audio,"a"))
        self.button2.pack(side="right")


    def start_selection(self, lst, which):
        
        self.current_list = lst
        self.which = which

        # Bind the mouse button down event to the corresponding button
        if which == "w":
            self.button1.bind("<Button-1>", self.on_button_down)
            self.button1.bind("<ButtonRelease-1>", self.on_button_up)
        elif which == "a":
            self.button2.bind("<Button-2>", self.on_button_down)
            self.button2.bind("<ButtonRelease-2>", self.on_button_up)

    def on_button_down(self, event):
        
        while((self.index <= self.samples)):
            self.index += 10
            time.sleep(0.01)
            if self.index >= self.samples:
                break        
        
        
        
        # Determine the index of the item that the user clicked on
        #index = self.current_list.index(int(event.widget["text"]))
        # Add the clicked item to the selected numbers list
        #self.selected_number = self.current_list[index]

    def on_button_up(self, event):
        # Add the selected number to the union list and display it in the listbox
        for i in range(self.index):
            self.union_list.append(self.current_list[i])
        

        # Unbind the mouse button down and up events from the corresponding button
        if self.which == "w":
            self.button1.unbind("<Button-1>")
            self.button1.unbind("<ButtonRelease-1>")
        elif self.which == "a":
            self.button2.unbind("<Button-1>")
            self.button2.unbind("<ButtonRelease-1>")
        
        if self.index >= self.samples:
            self.master.destroy()

root = tk.Tk()
app = Application([],[],1,master = root)
app.mainloop()