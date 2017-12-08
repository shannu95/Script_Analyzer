from tkinter import *
import tkinter as tk
import sys
from tkinter import ttk
from tkinter.filedialog import askopenfilename

root = tk.Tk()


def OpenFile():
    name = askopenfilename(initialdir="C:/Users/Documents/Programming/tkinter/",
                           filetypes=(("JavaScript file", "*.js"), ("PHP file", "*.php"),("Java file", "*.java"),("C++ file", "*.cpp"),("C# file", "*.cs")),
                           title="Choose a file"
                           )
    print ("The file path is -" + name + "\n\n")

    try:
        count = 1
        f = open(name, 'r')
        for line in f.xreadlines():

            # javascript & PHP Detector

            if "require('http')" in line:
                print (
                    "[" + str(count) + "] " + line + " Vulnerable parameter. Use HTTPS instead of HTTP request ")

            if "POST" in line:
                print "[" + str(count) + "] " + line + "Vulnerable parameter. Use GET instead of POST, to hide " \
                                                              "parameters "

            if "require('http')" in line:
                print "[" + str(
                    count) + "] " + line + " Vulnerable parameter. Use HTTPS instead of HTTP request "


            if "SCRIPT" in line:
                print "[" + str(count) + "] " + line + "Vulnerable TAG. Attacker can modify the tag manually"

            if "javascript:alert('XSS')" in line:
                print "[" + str(count) + "] " + line + "Alert box pop up to make the website look malicious."

            if "src=" in line:
                print "[" + str(count) + "]  " + line + "Any URL can be replaced inplace of current URL"

            if "email.value=" in line:
                print "[" + str(count) + "] " + line + "raw email ID is visible and it can be modified "

            if "jdbc:mysql:/" in line:
                print "[" + str(
                    count) + "] " + line + "if IP address, password and username are visble, Hacker can " \
                                                  "replace them "

            if "exposed()" in line:
                print "[" + str(count) + "] " + line + "Exposed to the Browser!"

            if "notExposed()" in line:
                print "[" + str(count) + "]  " + line + "Good! when to hide data from browser"

            if "File.append(" in line:
                print "[" + str(count) + "] " + line + "can detect the log file path directly"

            if "document.cookie" in line:
                print "[" + str(count) + "] " + line + "Hacker can determine information regarding cookies"

            #PHP

            if "include(" in line:
                print "[" + str(count) + "] Inclusion: " + line

            if "include_once(" in line:
                print "[" + str(count) + "] Inclusion: " + line

            if "require(" in line:
                print "[" + str(count) + "] Inclusion: " + line

            if "require_once(" in line:
                print "[" + str(count) + "] Inclusion: " + line

            if "eval(" in line:
                print "[" + str(count) + "] CmdExec: " + line

            if "preg_replace(" in line:
                print "[" + str(count) + "] CmdExec: " + line

            if "fwrite(" in line:
                print "[" + str(count) + "] CmdExec: " + line

            if "passthru(" in line:
                print "[" + str(count) + "] CmdExec: " + line

            if "file_get_contents(" in line:
                print "[" + str(count) + "] CmdExec: " + line

            if "shell_exec(" in line:
                print "[" + str(count) + "] CmdExec: " + line

            if "system(" in line:
                print "[" + str(count) + "] CmdExec: " + line

            if "mysql_query(" in line:
                print "[" + str(count) + "] SQL1: " + line

            if "fopen(" in line:
                print "[" + str(count) + "] File/Sys: " + line

            if "readfile(" in line:
                print "[" + str(count) + "] File/Sys: " + line

            if "glob(" in line:
                print "[" + str(count) + "] File/Sys: " + line

            if "file(" in line:
                print "[" + str(count) + "] File/Sys: " + line

            if "popen(" in line:
                print "[" + str(count) + "] File/Sys: " + line

            if "exec(" in line:
                print "[" + str(count) + "] File/Sys: " + line

            #C++

            if "gets(" in line:
                print "[" + str(count) + "] stdio: " + line + "This function does not check for buffer length and always results in a vulnerability."

            if "strcpy(" in line:
                print "[" + str(count) + "] Built-in function: " + line + "does not check the buffer boundaries and is vulnerable to overflows."

            if "sprintf(" in line:
                print "[" + str(count) + "] File/Sys: " + line

            if "fprintf(" in line:
                print "[" + str(count) + "] File/Sys: " + line

            if "snprintf(" in line:
                print "[" + str(count) + "] File/Sys: " + line

            #JAVA

            if "Statement" in line:
                print "[" + str(count) + "] SQL Injection: " + line + "Use PreparedStatement instead of Statement"

            if "http://" in line:
                print "[" + str(count) + "] URL Tampering: " + line

            #  C#

            if '"SELECT' in line:
                print "[" + str(count) + "] SQL Injection: " + line

            if 'searcher.Filter = string.Format("' in line:
                print "[" + str(count) + "] LDAP Injection: " + line









            count += 1

        #print("the code is free from vulnerabilities")
        f.close()

    except:
        print("No file exists")


Title = root.title("Script Analyzer")
frame1 = tk.Frame(root, width=400, height=40)
label = ttk.Label(root, text="Welcome to the Code Analyzer !!", foreground="blue", font=("Helvetica", 16))
B = tk.Button(root, compound=LEFT, text="Open", command=OpenFile)
label.pack()
frame1.pack(side=tk.BOTTOM)
B.pack()
tk.Button(root, compound=RIGHT, text='Exit', command=root.destroy).pack()


class StdRedirector():
    def __init__(self, text_widget):
        self.text_space = text_widget

    def write(self, string):
        self.text_space.config(state=tk.NORMAL)
        self.text_space.insert("end", string)
        self.text_space.see("end")
        self.text_space.config(state=tk.DISABLED)


class CoreGUI():
    def __init__(self, parent):
        text_box = tk.Text(parent, state=tk.DISABLED, wrap=NONE, height=20, width=70, borderwidth=0)
        text_box.pack()

        vscroll = Scrollbar(parent, orient=VERTICAL, command=text_box.yview)
        text_box['yscroll'] = vscroll.set

        vscroll.pack(side="right", fill="y")
        text_box.pack(side="left", fill="both", expand=True)

        sys.stdout = StdRedirector(text_box)
        sys.stderr = StdRedirector(text_box)

    def main(self):
        print ("Std Output")
        raise ValueError("Std Error")


CoreGUI(root)
root.mainloop()


# By: Shanmukha & Chinmay
# Date: 04/26/2017
# Subject info.: Computer Security CS - 410 / 591
# Project Topic: Script Analyzer
# Short info about project : Code is written for JavaScript and PHP analysis.
# Southern Illinois University Carbondale Spring 2017