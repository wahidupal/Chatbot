from tkinter import *
import os
import os.path
import datetime
import win32com.client as wincl
import random
import webbrowser
from PIL import Image, ImageTk
import tkinter.simpledialog as simpledialog
import csv
 
text_to_speech = wincl.Dispatch("SAPI.SpVoice")
text_to_speech.Voice = text_to_speech.GetVoices().Item(2)
bot_state = 1
is_user_question = True
# name = simpledialog.askstring('hi', prompt='What is your name?')
 
my_path = os.path.dirname(__file__)
 
 
class Window(Frame):
 
    # Define settings upon initialization. Here you can specify
    def __init__(self, master=None):
        # parameters that you want to send through the Frame class.
        Frame.__init__(self, master)
 
        # reference to the master widget, which is the tk window
        self.master = master
 
        # with that, we want to then run init_window, which doesn't yet exist
        self.init_window()
 
    # Creation of init_window
    def init_window(self):
        # changing the title of our master widget
        self.master.title("Simple Bot")
 
        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)
 
        # tbx_output = Text(self, height=15, width=60)
        # tbx_output.place(x=40, y=10)
 
        # create a Frame for the Text and Scrollbar
        txt_frm = Frame(self.master, height=15, width=60)
        txt_frm.pack(fill="both", expand=True)
        # ensure a consistent GUI size
        txt_frm.grid_propagate(False)
        # implement stretchability
        txt_frm.grid_rowconfigure(0, weight=1)
        txt_frm.grid_columnconfigure(0, weight=1)
 
        # create a Text widget
        self.tbx_output = Text(txt_frm, borderwidth=3, relief="sunken")
        self.tbx_output.config(font=("consolas", 12), undo=True, wrap='word')
        self.tbx_output.grid(row=0, column=0, sticky="nsew", padx=2, pady=2)
 
        # create a Scrollbar and associate it with txt
        scrollb = Scrollbar(txt_frm, command=self.tbx_output.yview)
        scrollb.grid(row=0, column=1, sticky='nsew')
        self.tbx_output['yscrollcommand'] = scrollb.set
 
        txt_frm2 = Frame(self.master, height=15, width=60)
        txt_frm2.pack(fill="both", expand=True)
        # ensure a consistent GUI size
        txt_frm2.grid_propagate(False)
        # implement stretchability
        txt_frm2.grid_rowconfigure(0, weight=1)
        txt_frm2.grid_columnconfigure(0, weight=1)
 
        # create a Text widget
        self.tbx_input = Text(txt_frm2, borderwidth=3, relief="sunken")
        self.tbx_input.config(font=("consolas", 12), undo=True, wrap='word')
        self.tbx_input.grid(row=0, column=0, sticky="nsew", padx=2, pady=2)
 
        # create a Scrollbar and associate it with txt
        scrollb = Scrollbar(txt_frm2, command=self.tbx_input.yview)
        scrollb.grid(row=0, column=1, sticky='nsew')
        self.tbx_input['yscrollcommand'] = scrollb.set
 
        # ScrollBar = Scrollbar(tbx_output)
        # ScrollBar.config(command=tbx_output.yview)
        # tbx_output.config(yscrollcommand=ScrollBar.set)
        # ScrollBar.pack(side=RIGHT, fill=Y)
        # tbx_output.pack(expand=YES, fill=BOTH)
 
        # tbx_input = Text(self, height=15, width=60)
        # tbx_input.place(x=40, y=300)
 
        # creating a button instance
       # btn1 = Button(self, text="talk")#, command=lambda: self.retrieve_input(tbx_input.get("1.0", "end-1c")))
        # self.tbx_output = tbx_output
        # self.tbx_input = tbx_input
 
        # , self.bot_speak)
        self.master.bind("<Return>", lambda x: self.addchat(name))
 
        # placing the button on my window
        # btn1.place(x=0, y=0)
        my_path = os.path.dirname(__file__)
 
        # load = Image.open(my_path + "\\rechal1.png")
        # render = ImageTk.PhotoImage(load)
 
        # # labels can be text or images
        # img = Label(self, image=render)
        # img.image = render
        # # img.place(x=200, y=600)
        # img.pack()
 
        text_to_speech.Speak("hello what is your name?")
        name = simpledialog.askstring('hello', prompt='What is your name?')
        if name == None:
            name = "ronen"
        self.tbx_input.focus_set()
 
    def bot_speak(self, answer):
        if answer:
            # print('Bot: ' + answer + '\n')
            self.tbx_output.insert(END, f"Bot: {answer.upper()}\n\n")
            text_to_speech.Speak(answer)
 
    def addchat(self, name):
        txt = self.tbx_input.get("1.0", "end-1c").lower().rstrip()
        # gets everything in your textbox
 
        self.tbx_output.insert(END, f"You: {txt}" + "\n\n")
        # # tosses txt into textarea on a new line after the end
        self.tbx_input.delete('1.0', END)  # deletes your textbox text
        self.tbx_output.see(END)
 
        if is_user_question:
            self.user_question(txt, name)
        else:
            self.bot_question(txt, name)
 
    def user_question(self, txt, name):
        global is_user_question
        global bot_state
        # global name
        troubled_mind = ["i'm feeling down", "i feel sad",
                         "i feel fear", "panic", "crying"]
        troubled_mind_replay = [
            "don't feel bad remember thing are not as bad as they seems",
            "don't lose hope dear friend... you are loved and cared by people around you",
            "i understand and i wish i could help you feel better " +
            name + " remember thing are not as bad as you imagine"
        ]
 
        alone = ["i don't feel good", "help me", "stress", "no one to talk to"]
        alone_replays = [
            "there is no reasons to worry you are not alone in the world people love and care about you... please try to remember that",
            "as much as you feel fear and panic right now i promiss you you will return to feel better and relaxed and that you will have better days of joy",
            "it's just a hard time your going through but thing will get better i promiss you just hold on don't let fear or sadness or anger control your life"
        ]
 
        sickness = ["i feel sick", "i'm sick",
                    "pain", "fever", "toothache", "the flue"]
        sickness_replays = [
            "be strong " + name + " you will get well don't worry. if you have the flue you will get better and if your tooth hurts the dentist will help you",
            "don't be angry or judge yourself or blame yourself don't be hard on yourself cause that's how life goes remember that it's not your fualt",
            "believe thing will get better they usually do and you will be well again and everything will be alright try to be positive dear " +
            name + " remember you are loved and cherished by your dear ones"
        ]
 
        scared = ["i am scared", "what will be", "the cold", "will i die"]
        scared_replays = [
            "don't be afraid you will not die and everything will turned to the best",
            "try to relax and don't bring fear over you i know things may look hard right now but they'll get better and better",
            "you will live long and you will prosper don't let fear or anger or sadness gain control over you"
        ]
 
        insomnia = ["i haven't slept all night",
                    "can't sleep", "up all night", "didn't sleep"]
        insomnia_replays = [
            "it's okay to be awake at night from time to time",
            "some people like to stay up at night... so there is nothing wrong with that",
            "you are learning to program it's okay you'll be fine"
        ]
        # hi = ['hi ']
        # ex = ['exit']
        # fly = ['fly']
 
        # end_word = ['i wish to exit']
 
        bother = ['something is bothering me']
        friend = ['meet my friend']
 
        if txt == "hi":
            # if any(s in txt for s in hi):
            self.bot_speak('hi! how are you ' + name)
        # elif any(s in txt for s in ex):
        #     self.bot_speak('goodbye')
        elif any(s in txt for s in troubled_mind):
            self.bot_speak(random.choice(troubled_mind_replay))
        elif any(s in txt for s in alone):
            self.bot_speak(random.choice(alone_replays))
        elif any(s in txt for s in sickness):
            self.bot_speak(random.choice(sickness_replays))
        elif any(s in txt for s in bother):
            self.bot_speak("what is bothering you?")
            bot_state = 1
            is_user_question = False
        elif any(s in txt for s in friend):
            self.bot_speak("what is your friend's name?")
            bot_state = 3
            is_user_question = False
        elif any(s in txt for s in scared):
            self.bot_speak(random.choice(scared_replays))
        elif any(s in txt for s in insomnia):
            self.bot_speak(random.choice(insomnia_replays))
        elif txt == 'fly':  # any(s in txt for s in fly):
            webbrowser.open_new("https://www.youtube.com/watch?v=UGQqYS38DLE")
        elif txt == 'i wish to exit':
            mycsv = os.path.join(my_path, 'ChatLog.csv')
            if not os.path.exists(mycsv):
                saveFile = open(mycsv, 'w')
                saveFile.write(
                    f"""{datetime.datetime.now().strftime("%d/%m/%Y")}, {self.tbx_output.get(1.0,'end-1c')}\n""")
                saveFile.close()
            else:
                appendFile = open(mycsv, 'a')
                for row in self.tbx_output.get(1.0, 'end-1c'):
                    appendFile.write(row)
                appendFile.close()
 
                # appendFile.write(f"""{datetime.datetime.now().strftime("%d/%m/%Y")}, {self.tbx_output.get(1.0,'end-1c')}\n""")
                # appendFile.close()
                # with open('employee_file.csv', mode='w') as employee_file:
                #     employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                #
                #     employee_writer.writerow(self.tbx_output.get(1.0,'end-1c'))
            exit()
        else:
            self.bot_speak("it's nice to talk to you")
 
    def bot_question(self, txt, name):
        global is_user_question
        global bot_state
        if bot_state == 1:
            bother = txt
            self.bot_speak("i'm sorry that " + bother +
                           " is bothering you i wish i could help")
            is_user_question = True
        elif bot_state == 3:
            friend = txt
            self.bot_speak("nice to meet you " +
                           friend + " " + name + " friend")
            is_user_question = True
 
    # def retrieve_input(self, user_input):
    #     print(user_input)
 
        # if not os.path.exists('DiaryLog.csv'):
        #     saveFile = open('DiaryLog.csv', 'w')
        #     saveFile.write(f"""{datetime.datetime.now().strftime("%d/%m/%Y")}, {user_input}\n""")
        #     saveFile.close()
        # else:
        #     appendFile = open('DiaryLog.csv', 'a')
        #     appendFile.write(f"""{datetime.datetime.now().strftime("%d/%m/%Y")}, {user_input}\n""")
        #     appendFile.close()
 
 
# root window created. Here, that would be the only window, but
# you can later have windows within windows.
root = Tk()
 
root.geometry("600x850")
 
# creation of an instance
app = Window(root)
 
# mainloop
root.mainloop()