from tkinter import *
from tkinter import ttk
import urllib.request
def go():
	text.delete(1.0, END)
	print(entry.get())
	with urllib.request.urlopen(entry.get()) as response:
		received_html = response.read()
	text.insert(1.0, received_html)
	
def __init__(self,parent,**kwargs):
        Canvas.__init__(self,parent,**kwargs)
        self.bind("<Configure>", self.on_resize)
        self.height = self.winfo_reqheight()
        self.width = self.winfo_reqwidth()

def on_resize(self,event):
        # determine the ratio of old width/height to new width/height
        wscale = float(event.width)/self.width
        hscale = float(event.height)/self.height
        self.width = event.width
        self.height = event.height
        # resize the canvas 
        self.config(width=self.width, height=self.height)
        # rescale all the objects tagged with the "all" tag
        self.scale("all",0,0,wscale,hscale)

browser_window = Tk()

browser_window.configure(background='black')
#browser

leftFrame = Frame(browser_window)
leftFrame.pack(side=LEFT,fill="both", expand=True)
 
rightFrame = Frame(browser_window)
rightFrame.pack(side=RIGHT)
 
label1 = Label(leftFrame, text="History")
label1.pack()
 
label3 = Label(leftFrame, text="More On It")
label3.pack()

''' Scrollbar and History tab'''
scrollbar = Scrollbar(leftFrame, orient="vertical")
lb = Listbox(leftFrame, width=50, height=20, yscrollcommand=scrollbar.set)
scrollbar.config(command=lb.yview)

scrollbar.pack(side="right", fill="both")
lb.pack(side="left",fill="both", expand=True)
for i in range(0,100):
    lb.insert("end", "item #%s" % i)
    '''Scrollbar and History Tab End Here'''
    
browser_window.title('Grail')
TAB_CONTROL = ttk.Notebook(browser_window)
TAB1 = ttk.Frame(TAB_CONTROL)
TAB_CONTROL.add(TAB1, text='Tab 1')
'''Configure style directly into browser'''
#style = ttk.Style()
#style.configure("BW.TLabel", foreground="black", background="white")
#l1 = ttk.Label(TAB1,text="Test", style="BW.TLabel").grid(column=1, row=0, padx=10, pady=10)


TAB2 = ttk.Frame(TAB_CONTROL)
TAB_CONTROL.add(TAB2, text='Tab 2')

TAB3 = ttk.Frame(TAB_CONTROL)
TAB_CONTROL.add(TAB3, text='Tab 3')
TAB_CONTROL.winfo_children()
browser_window.resizable(height = None, width = None)
label = Label(browser_window, text= 'Enter URL:')

ADD_BUTTON=ttk.Button(TAB_CONTROL,command=go)
TAB_CONTROL.add(ADD_BUTTON,text='+')
ttk.Label(TAB1, text="This is Tab 1").grid(column=0, row=0, padx=10, pady=10)
ttk.Label(TAB2, text="This is Tab 2").grid(column=0, row=0, padx=10, pady=10)
ttk.Label(TAB3, text="This is Tab 3").grid(column=0, row=0, padx=10, pady=10)

ttk.Button(TAB3, text='Go',command=go).grid(column=0, row=0, padx=10, pady=10)

ttk.Entry(TAB2).grid(column=1, row=0, padx=10, pady=10,ipadx=200)
#TAB2 Input Field
print(ttk.Entry(TAB2).get())
#TAB_CONTROL.add(Button, text='Tab 2')
TAB_CONTROL.pack(expand=1, fill="both")
#Tab Name Labels

#label.resizable(height = None, width = None)
#url label
scrollbar1 = Scrollbar(browser_window, orient="vertical")
entry = Entry(browser_window)
height=browser_window.winfo_height()
width=browser_window.winfo_width()

#entry.geometry("{}x{}".format(height,width))

browser_window.overrideredirect(False)
entry.insert(END, "http://knowpapa.com")
print(entry.get())
button = Button(browser_window, text='Go', command = go)

text = Text(browser_window,yscrollcommand=scrollbar1.set)
scrollbar1.config(command=text.yview)
scrollbar1.pack(side="right", fill="y")


label.pack(side=TOP,fill="both", expand=True)
entry.pack(side=TOP,fill="both", expand=True)
button.pack(side=TOP,fill="both", expand=False)
text.pack(side= TOP,fill="both", expand=True)

browser_window.mainloop()
