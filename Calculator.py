import tkinter as tk

class Calculator :

    def __init__(self):

        self.root = tk.Tk()
        
        self.root.minsize(450, 740)                                                                           # fixing the window size 
        self.root.maxsize(450, 740)
        self.root.configure(background='black')                                                                
        self.root.title("Calculator")
        #insert a calculator icon self.root.wm_iconbitmap("")

        self.entry = tk.StringVar()
        self.entry.set("")
        
        self.screen =tk.Entry(self.root, textvar = self.entry, font="lucida 35 bold", justify='right', bg='cyan', fg='black', relief='ridge')
        self.screen.pack(side='top', fill='x', ipady=20, pady=10, padx=10)

        buttons = [["AC", "C", "%", "/"],                                            # creating a list for all the buttons
                   ["7", "8", "9", "*"],
                   ["4", "5", "6", "-"],
                   ["1", "2", "3", "+"],
                   ["e", "0", ".", "="]]
        

        for row in buttons:                                                          # iterating through the list

            frame = tk.Frame(self.root, bg="black", borderwidth=2)
            frame.pack(side='top')
            
            for btn in row:

                if btn in ("C", "AC"):
                    button = tk.Button(frame, text=btn, font=("times new roman", 28, "bold"), relief='raised',
                   width=3, height=1, pady=15, bg="grey", fg="black", activebackground="red", activeforeground="white")
                    
                elif btn == "=" :
                    button = tk.Button(frame, text=btn, font=("times new roman", 28, "bold"), relief='raised',
                   width=3, height=1, pady=15, bg='cyan', fg='white', activebackground="red", activeforeground="black")
                    
                else:
                    button = tk.Button(frame, text=btn, font=("times new roman", 28, "bold"), relief='raised',
                   width=3, height=1, pady=15, bg="grey", fg="black",
                   activebackground="cyan", activeforeground="white")
                    
                button.pack(side='left', padx=10, pady=10)
                button.bind("<Button-1>", self.click)


        self.root.mainloop()



    def click(self, event) :

        text=event.widget.cget("text")

        if text == '=' :                                               # evaluate the expression on the display
            if self.entry.get().isdigit():
                value = int(self.entry.get())

            else:                                                      # when the evaluating expression is not valid
                try:
                    value = eval(self.screen.get())
                except Exception as e:
                    value = "Error"
                    print(e)

            self.entry.set(value)                                   
            self.screen.update()                                        # updating the display with the result
        
        elif text == 'C' :                                              # erase the last character of expression on the display
            self.entry.set(self.entry.get()[:-1])
            self.screen.update()

        elif text == 'AC' :                                             # clear the display
            self.entry.set("")
            self.screen.update()
        
        else :                                                          # apart from the other mentioned, if any other button is clicked, it will be appended to the expression on the display
            self.entry.set(self.entry.get() + text)
            self.screen.update()

        
        if self.screen.get() == "Error":                                # automatically clear the display if Error is generated in previous calculations
            self.entry.set("")
            self.screen.update()



calc = Calculator()    