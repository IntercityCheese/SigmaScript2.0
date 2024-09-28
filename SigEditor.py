# Whaaat it's Sigma Script Editor???

# Gui Modules
from tkinter import *
from tkinter import simpledialog
from tkinter import filedialog
import customtkinter as CT
from tklinenums import TkLineNumbers

# SS2.0 Executable Path
exePath = ""
SSexe = None

# Other Variables
OutputLine = 0

# Saving Stuff
CurrentFileName = ""
def SelInt():
    global exePath
    file_path = filedialog.askopenfilename(title = "Open .exe files", filetypes= [("Sigma Script Code", "*.exe")])
    if file_path:
        current_file = file_path
        with open(file_path, 'r') as file:
            typezone.delete("1.0", END)
            typezone.insert(END, file.read())
            root.title(f"Sigma Script - {current_file}")

def Load():
    global current_file
    file_path = filedialog.askopenfilename(title = "Open .sig files", filetypes= [("Sigma Script Code", "*.sig")])
    if file_path:
        current_file = file_path
        with open(file_path, 'r') as file:
            typezone.delete("1.0", END)
            typezone.insert(END, file.read())
            root.title(f"Sigma Script - {current_file}")
            
def Save():
        file_path = current_file
        if file_path != "":
            try:
                with open(file_path, 'w') as file:
                    text_content = typezone.get("1.0", END)
                    file.write(text_content)
                    print("File Saved")
                    root.title(f"Sigma Script - {current_file}")
            except Exception as e:
                print(f"Error saving file: {str(e)}")
        else:
            SaveAs()

def SaveAs():
    global current_file
    file_path = filedialog.asksaveasfilename(defaultextension = ".sig", filetypes = [("Sigma Script Code", "*.sig")])
    if file_path:
        current_file = file_path
        root.title(f"Sigma Script - {current_file}")
        Save()

current_file = ""

# Highlighting Stuff
SyntaxClasses = {
    "Statements" : ["print", "make", "var ",  'input', "cast_to", "math"],
    "Loops&Ifs" : ["while", "for ","if","else", "void"],
    "Castings" : ["string.", "string ", "num.", "num "],
    "Determiners" : [" in ", "not "],
    "Comment" : ['> ']
    }

def text_edited(e):
    HighLightSyntax()

def find(sub, clas, col):
    

    s = sub

    if s:
        idx = '1.0'
        while 1:
            idx = typezone.search(s, idx, nocase=1, stopindex=END)

            if not idx: break

            lastidx = '%s+%dc' % (idx, len(s))

            typezone.tag_add(clas, idx, lastidx)
            idx = lastidx

        typezone.tag_config(clas, foreground = col)
    typezone.focus_set()


def HighLightSyntax():
    typezone.tag_remove('Statements', '1.0' ,END)
    typezone.tag_remove('Loops&Ifs', '1.0' ,END)
    typezone.tag_remove('Castings', '1.0', END)
    typezone.tag_remove('Determiners', '1.0' ,END)
    typezone.tag_remove('Comments', '1.0', END)
    
    #Statements
    for Statement in SyntaxClasses["Statements"]:
        find(Statement, "Statements", "purple1")
    for Loop in SyntaxClasses["Loops&Ifs"]:
        find(Loop, "Loops", "green3")
    for Caster in SyntaxClasses["Castings"]:
        find(Caster, "Castings", "dodger blue")
    for Determiner in SyntaxClasses["Determiners"]:
        find(Determiner, "Determiners", "DarkOrange1")
    find('>', "Comments", "red")

# Refresh Text
CodeStartStuff = '''
Refresh =============================================================

'''

# Runtime Operations:
def Output(text, tagcol):
    global OutputLine
    responsezone.insert(END, f"{text}\n")
    OutputLine += 1
    if tagcol != "None":
        responsezone.tag_add(tagcol, f"{OutputLine}.0", END)
        responsezone.tag_config(tagcol, foreground = tagcol)

def ShellRun():
     # Check for SS Runtime .exe
     if exePath == "" or SSexe.name != "SigmaScript2-0.exe":
          Output("Error - Please select a SigmaScript2-0.exe file to run you're code. Go to File>Select Interpreter and selct the file.", "red")

def RunCode():
     # Check for SS Runtime .exe
     if exePath == "" or SSexe.name != "SigmaScript2-0.exe":
          Output("Error - Please select a SigmaScript2-0.exe file to run you're code. Go to File>Select Interpreter and selct the file.", "red")
          

# Help Situations
helptext = '''
What??? You need help with syntax? If only there was a dedicated documentation file in the SS 2.0 folder...        
'''
credsyeah = '''
ALFIE LITTLESTONE - EVERYTHING
DAWID N. - TRIED SADTIONS
ALFIE LITTLESTONE - PROJECT MANAGER
ALFIE LITTLESTONE - SPECIAL MENTION
JAMIE HANSEN - JAMIE HANSEN'''
IDETEXT = '''Resize this window to make it easier to read!

Welcome to Sigma script. As it seems you have no clue
what you are doing. Don't worry, I got you covered.

If you look at the screen there is 3 boxes and some drop down menus.
The Top box is the code window
The Middle box is the output window
The Bottom box is for one line code (Like printing variables after a program is run to see if it worked, all variables used in the previously run code work here, so you can change, print or assign variables).

What about the dropdowns?

The dropdowns were based off of IDLE (The thing you code python in) so it should be pretty straight forward to get around..

Good Luck (you'll need it...)'''

toplevel_window = None
toplevel_window2 = None
toplevel_window3 = None

def addhelp():
        global toplevel_window2
        if toplevel_window2 is None or not toplevel_window2.winfo_exists():
            toplevel_window2 = CT.CTkToplevel(master = root)  # create window if its None or destroyed
            toplevel_window2.title = "SS 2.0 IDE Help"
            toplevel_window2.grid_rowconfigure(0,weight=1)
            toplevel_window2.grid_columnconfigure(0,weight=1)
            text1 = CT.CTkTextbox(master=toplevel_window2)
            text1.insert("0.1", helptext)
            text1.grid(row=0,column=0,sticky="nsew")
            toplevel_window2.focus()
            Output("Documentation HELP - The help box has opened. Check the Taskbar if not visible.")
        else:
            toplevel_window2.focus()  # if window exists focus it
def credits():
        global toplevel_window3
        if toplevel_window3 is None or not toplevel_window3.winfo_exists():
            toplevel_window3 = CT.CTkToplevel(master = root)  # create window if its None or destroyed
            toplevel_window3.title = "SS 2.0 IDE Help"
            toplevel_window3.grid_rowconfigure(0,weight=1)
            toplevel_window3.grid_columnconfigure(0,weight=1)
            text1 = CT.CTkTextbox(master=toplevel_window3)
            text1.insert("0.1", credsyeah)
            text1.grid(row=0,column=0,sticky="nsew")
            toplevel_window3.focus()
            Output("Credits - The credits box has opened. Check the Taskbar if not visible.")
        else:
            toplevel_window3.focus()  # if window exists focus it
def open_IDE_window():
        global toplevel_window
        if toplevel_window is None or not toplevel_window.winfo_exists():
            toplevel_window = CT.CTkToplevel(master = root)  # create window if its None or destroyed
            toplevel_window.title = "SS 2.0 IDE Help"
            toplevel_window.grid_rowconfigure(0,weight=1)
            toplevel_window.grid_columnconfigure(0,weight=1)
            text1 = CT.CTkTextbox(master=toplevel_window)
            text1.insert("0.1", IDETEXT)
            text1.grid(row=0,column=0,sticky="nsew")
            toplevel_window.focus()
            Output("IDE HELP - The help box has opened. Check the Taskbar if not visible.")
        else:
            toplevel_window.focus()  # if window exists focus it

# Root Config
root = CT.CTk()
root.geometry("1050x750")
root.title("Sigma Script 2.0")

# Type Area Configs
typezone = CT.CTkTextbox(master = root, height = 500, width = 1000, yscrollcommand = True, font = ("Consolas", 15), fg_color= "gray16")
responsezone = CT.CTkTextbox(master = root, height = 150, width = 1000, yscrollcommand = True, fg_color = "gray16", font = ("Consolas", 15))
shellbox = CT.CTkEntry(master = root, fg_color = "gray16", width = 1000)
shellbox.bind("<Return>", lambda event: ShellRun())

# File Menu
menu_bar = Menu(root)
root.config(menu = menu_bar)
file_menu = Menu(menu_bar, tearoff = 0)
menu_bar.add_cascade(label = "File", menu = file_menu)
file_menu.add_command(label = "Open", command = Load)
file_menu.add_command(label = "Save", command = Save)
file_menu.add_command(label = "Save As", command = SaveAs)
file_menu.add_separator()
file_menu.add_command(label="Select Interpreter", command=SelInt)
file_menu.add_separator()
file_menu.add_command(label="Exit", command= root.destroy)

# Run Menu
run_menu = Menu(menu_bar, tearoff = 0)
menu_bar.add_cascade(label = "Run", menu = run_menu)
run_menu.add_command(label = "Run Code", command = RunCode)
run_menu.add_command(label = "Check Syntax", command = HighLightSyntax)

# Help Menu
alf = Menu(menu_bar, tearoff = 0)
menu_bar.add_cascade(label = "Help", menu = alf)
alf.add_command(label = "Documentation", command = addhelp)
alf.add_command(label = "IDE Help", command = open_IDE_window)
alf.add_command(label = "Credits", command = credits)

alf.add_command(label = "Made By Alfie Littlestone")
alf.add_command(label = "Made By Alfie Littlestone")
alf.add_command(label = "Made By Alfie Littlestone")
alf.add_command(label = "Made By Alfie Littlestone")

root.bind("<F5>", lambda event: RunCode()) # F5 Keybind

# Placing Type Areas
typezone.place(x = 25, y = 25)
responsezone.place(x = 25, y = 550)
shellbox.place(x=25, y=710)

# Syntax Highlighting Caller
typezone.bind('<Key>', text_edited)

# Startup message
Output("Type 'help' into the black box for help.", "yellow")


# Loop Starter (No Code Past Here)
root.mainloop()

print("Closed.") # Program Closed Indicator