from tkinter import *
from PIL import ImageTk, Image
from tkinter.ttk import Combobox, Checkbutton
from tkinter import filedialog, messagebox
import os
import json
from matplotlib import pyplot as plt
import numpy as np
import smtplib
import imghdr
from email.message import EmailMessage
import webbrowser


def root():

    root = Tk()
    root.geometry("904x604")
    root.title("Graph Builder")
    root.resizable(False, False)
    load = Image.open('WpUser.png')
    render = ImageTk.PhotoImage(load)
    img = Label(root, image=render)
    img.place(x=0, y=0)

    def using():
        global loggedin
        loggedin = []


    def openSign():
        Sign = Toplevel(root)
        Sign.geometry("304x304")
        Sign.resizable(False, False)
        Sign.title("Sign in")
        Sign.configure(bg='RoyalBlue3')
        load2 = Image.open('log-sign.png')
        render2 = ImageTk.PhotoImage(load2)
        img2 = Label(Sign, image=render2)
        img2.place(x=0, y=0)

        labelName = Label(Sign, text="Enter Name", bg='LightBlue1', font=("arial", 10, "bold"))
        labelMail = Label(Sign, text='Enter e-mail', bg='LightBlue1', font=("arial", 10, "bold"))
        labelPass = Label(Sign, text="Enter Password", bg='LightBlue1', font=("arial", 10, "bold"))
        labelPassAgain = Label(Sign, text="Enter Password Again", bg='LightBlue1', font=("arial", 10, "bold"))


        labelName.place(x=10, y=70)
        labelMail.place(x=10, y=100)
        labelPass.place(x=10, y=130)
        labelPassAgain.place(x=10, y=160)




        name = Entry(Sign, bg='LightBlue1')
        email = Entry(Sign, bg='LightBlue1')
        password = Entry(Sign,show='*', bg='LightBlue1')
        passagain = Entry(Sign,show='*', bg='LightBlue1')
        name.place(x=170, y=72)
        email.place(x=170, y=102)
        password.place(x=170, y=132)
        passagain.place(x=170, y=162)


        def buttonClick():

            def signin(usr):


                if str(name.get()) in usr.keys():
                    messagebox.showinfo('Error', 'Username already taken!')

                elif str(name.get()) not in usr.keys():
                    flag = True
                    for x in range (len(list(usr.values()))):
                        if  str(email.get()) in list(usr.values())[x]:
                            messagebox.showinfo('Error', 'E-mail already used!')

                            flag = False
                            break
                    if flag:
                        if str(password.get()) == str(passagain.get()):
                            usr[str(name.get())] = [str(password.get()),str(email.get())]
                            messagebox.showinfo('Success', 'User Saved!')
                        else:
                            messagebox.showinfo('Error', 'Passwords does not match!')

                    writeUsers(usr)
                return True

            def readUsers():
                try:
                    with open("users.json", "r") as f:
                        return json.load(f)
                except FileNotFoundError:
                    return {}

            def writeUsers(usr):
                with open("users.json", "w+") as f:
                    json.dump(usr, f)

            users = readUsers()
            success = signin(users)

            while not success:
                success = signin(users)

        btnEnter = Button(Sign, text="          Enter          ", bg='green', font=("arial", 10, "bold"), command=buttonClick)
        btnEnter.place(x=170, y=192)

        btnexit = Button(Sign, text="   Exit   ", bg='red', font=("arial", 10, "bold"), command=Sign.destroy)
        btnexit.place(x=230, y=250)

        Sign.mainloop()


    def openLog():
        global entryName,entryPass

        Log = Toplevel(root)
        Log.geometry("304x304")
        Log.resizable(False, False)
        Log.title("Log in")
        load3 = Image.open('log-sign.png')
        render3 = ImageTk.PhotoImage(load3)
        img3 = Label(Log, image=render3)
        img3.place(x=0, y=0)

        labelName = Label(Log, text="Name", font=("arial", 10, "bold"), bg='LightBlue1')
        labelPass = Label(Log, text="Password", font=("arial", 10, "bold"), bg='LightBlue1')


        labelName.place(x=10, y=70)
        labelPass.place(x=10, y=100)


        entryName = Entry(Log, bg='LightBlue1')
        entryPass = Entry(Log, show='*', bg='LightBlue1')




        entryName.place(x=100, y=70)
        entryPass.place(x=100, y=100)

        def buttonClick():

            def logIn(usr):

                if str(entryName.get()) in usr.keys() and usr[str(entryName.get())][0] == str(entryPass.get()):
                    using()
                    loggedin.append(str(entryName.get()))
                    loggedin.append(usr[str(entryName.get())][0])
                    loggedin.append(usr[str(entryName.get())][1])
                    messagebox.showinfo('Message', 'Log in Successful!')
                    Log.destroy()
                    root.withdraw()
                    Maincaller()


                    return True

                else:
                    messagebox.showinfo('Message', 'Log in Failed!')
                    return True

            def readUsers():
                try:
                    with open("users.json", "r") as f:
                        return json.load(f)
                except FileNotFoundError:
                    return {}

            users = readUsers()
            success = logIn(users)

            while not success:
                success = logIn(users)

        btnexit = Button(Log, text="   Exit   ", bg='red', font=("arial", 10, "bold") , command=Log.destroy)
        btnexit.place(x=230, y=250)

        btnenter = Button(Log, text="          Enter          ", bg='green', font=("arial", 10, "bold") , command=buttonClick)
        btnenter.place(x=100, y=130)

        Log.mainloop()





    def Maincaller():

        windowMain = Toplevel(root)
        windowMain.geometry("904x604")
        windowMain.title("Graph Builder")
        windowMain.resizable(0, 0)

        load1 = Image.open('WpMains.png')
        render1 = ImageTk.PhotoImage(load1)
        img1 = Label(windowMain, image=render1)
        img1.place(x=0, y=0)

        labelUser = Label(windowMain,fg='white',font='Times 12 italic',bg='blue' ,text="Welcome " + loggedin[0])
        labelUser.place(x=637, y=447)



        def dest():
            root.destroy()

        windowMain.protocol("WM_DELETE_WINDOW", dest)

        def fileDialog():
            Load = Toplevel(windowMain)
            Load.geometry("904x598")
            Load.title("Graph Builder")


            try:
                fileName = filedialog.askopenfilename(initialdir="/", title="Select A File", filetype=(("jpeg", ".jpg"), ("All Files",".*")))
                Label(Load, text=fileName).pack()
                Img = ImageTk.PhotoImage(Image.open(fileName))
                Label(Load, image=Img).pack()
            except AttributeError:
                pass

            Load.mainloop()


        def Share():

            mails_temp = []
            mails = []

            windowShare = Toplevel(windowMain)
            windowShare.geometry('304x304')
            windowShare.title("Graph Builder")
            windowShare.resizable(False, False)
            load4 = Image.open('log-sign.png')
            render4 = ImageTk.PhotoImage(load4)
            img4 = Label(windowShare, image=render4)
            img4.place(x=0, y=0)


            receiverL = Label(windowShare, text='Receiving e-mails: ', bg='LightBlue1')
            receiverL.place(x=10, y=70)
            passL = Label(windowShare, text='Your e-mail password: ', bg='LightBlue1')
            passL.place(x=10, y=100)
            fileL = Label(windowShare, text='File: ', bg='LightBlue1')
            fileL.place(x=10, y=130)


            varEntry = StringVar()
            receiver = Entry(windowShare, textvariable=varEntry, bg='LightBlue1')
            receiver.place(x=150, y=70)
            passw = Entry(windowShare, show='*', bg='LightBlue1')
            passw.place(x=150, y=100)
            file = Entry(windowShare, bg='LightBlue1')
            file.place(x=150, y=130)

            def conf():

                mails_temp.append(varEntry.get())
                for i in mails_temp:
                    sp = i.split()
                    mails.append(sp)

            def res():
                receiver.delete(0, 'end')
                mails_temp.clear()

            def send():

                print(mails[0])
                msg = EmailMessage()
                msg['Subject'] = 'Sent with Graphit'
                msg['From'] = loggedin[2]
                msg['To'] = ",".join(mails[0])

                with open(str(file.get()), 'rb') as f:
                    file_data = f.read()
                    file_type = imghdr.what(f.name)
                    file_name = f.name

                msg.add_attachment(file_data, maintype= 'image', subtype= file_type, filename= file_name)

                user = loggedin[2]
                password = str(passw.get())

                server = smtplib.SMTP('smtp.gmail.com', 465)
                server.starttls()
                server.login(user, password)
                server.sendmail(user, mails, msg)

            def openweb():
                webbrowser.open('http://gmail.com')

            btnConf = Button(windowShare, text="Confirm", command=conf, bg='green')
            btnConf.place(x=10, y=160)

            btnRes = Button(windowShare, text="Reset", command=res, bg='yellow')
            btnRes.place(x=100, y=160)

            btnEnter = Button(windowShare, text="Send", bg='green', command=send)
            btnEnter.place(x=60, y=220)

            btnexit = Button(windowShare, text="Exit", bg='red', command=windowShare.destroy)
            btnexit.place(x=230, y=220)

            btnWeb = Button(windowShare, text='Open Web', bg='grey', command=openweb)
            btnWeb.place(x=130, y=220)

            windowShare.mainloop()


        def AccountPage():
            Acc = Toplevel(windowMain)
            Acc.geometry("304x304")
            Acc.title("Graph Builder")
            Acc.resizable(False, False)
            load4 = Image.open('log-sign.png')
            render4 = ImageTk.PhotoImage(load4)
            img4 = Label(Acc, image=render4)
            img4.place(x=0, y=0)

            labelName = Label(Acc, text="Name: ", bg='LightBlue1')
            labelPass = Label(Acc, text="Password: ", bg='LightBlue1')
            labelMail = Label(Acc, text="E-Mail: ", bg='LightBlue1')
            labelName.place(x=20, y=70)
            labelPass.place(x=20, y=100)
            labelMail.place(x=20, y=130)

            labelName2 = Label(Acc, text=loggedin[0], bg='LightBlue1')
            labelName2.place(x=100, y=70)

            labelPass2 = Label(Acc, text=loggedin[1], bg='LightBlue1')
            labelPass2.place(x=100, y=100)

            labelMail2 = Label(Acc, text=loggedin[2], bg='LightBlue1')
            labelMail2.place(x=100, y=130)


            def logout():
                using()
                windowMain.destroy()
                root.deiconify()

            btnExit = Button(Acc, text='Log Out', command=logout, bg='red')
            btnExit.place(x=200, y=160)

            Acc.mainloop()


        def Build():

            window = Toplevel(windowMain)
            window.title("Graphit")
            window.geometry('350x200')
            window.resizable(0, 0)
            load5 = Image.open('907793.png')
            render5 = ImageTk.PhotoImage(load5)
            img5 = Label(window, image=render5)
            img5.place(x=0, y=0)

            frame1 = LabelFrame(window, text='General Information', bg='SteelBlue4')
            frame1.pack(side=LEFT, padx=2, pady=2, expand=True)

            frame2 = LabelFrame(window, text='Additional Settings')
            frame2.pack(side=RIGHT, padx=2, pady=2, expand=True)



            def list():
                global data_x, data_y, temp_x, temp_y, line_labels, temp_labels
                temp_x = []
                data_x = []
                if y_check.get() == 0:
                    temp_y = [[] for i in range(int(entry_y.get()))]
                    data_y = [[] for i in range(int(entry_y.get()))]
                    temp_labels = [[] for i in range(int(entry_y.get()))]
                    line_labels = [[] for i in range(int(entry_y.get()))]
                if y_check.get() == 1:
                    temp_labels = []
                    line_labels = []


            def data_window():
                list()
                dataWindow = Toplevel(window)
                dataWindow.title('Data Values')
                dataWindow.geometry('400x200')
                dataWindow.configure(bg='SteelBlue4')

                dataFrame = LabelFrame(dataWindow, text='X Values', bg='SteelBlue4')
                dataFrame.grid(row=0, column=0, rowspan=3, columnspan=2, sticky=W + E + N + S)

                dataFrame2 = LabelFrame(dataWindow, text='Y Values', bg='SteelBlue4')
                dataFrame2.grid(row=0, column=2, rowspan=3, columnspan=2, sticky=W + E + N + S)

                dataFrame3 = LabelFrame(dataWindow, text='Settings')
                dataFrame3.grid(row=5, column=0, rowspan=3, columnspan=2, sticky=W + E + N + S)

                dataFrame4 = LabelFrame(dataWindow, text='Line Labels', bg='SteelBlue4')
                dataFrame4.grid(row=5, column=2, rowspan=3, columnspan=2, sticky=W + E + N + S)

                z = 1
                for x in range(int(entry_x.get())):
                    x_data = Entry(dataFrame, width=7)
                    x_data.grid(row=x, column=0, pady=0, padx=5)
                    temp_x.append(x_data)
                if y_check.get() == 0:
                    for y in range(int(entry_y.get())):
                        for x in range(int(entry_x.get())):
                            y_data = Entry(dataFrame2, width=7)
                            y_data.grid(row=x, column=z, pady=0)
                            temp_y[y].append(y_data)
                        z += 1

                    # ENTRIES
                    for y in range(int(entry_y.get())):
                        legend_label = Entry(dataFrame4, width=7)
                        legend_label.grid(row=0, column=y, pady=0)
                        temp_labels[y].append(legend_label)
                if y_check.get() == 1:
                    for y in range(int(entry_x.get())):
                        entry_pielabel= Entry(dataFrame4, width=10)
                        entry_pielabel.grid(row=0, column=y, pady=0)
                        temp_labels.append(entry_pielabel)

                def confirmed():
                    for value in temp_x:
                        data_x.append(value.get())

                    x = 0
                    if y_check.get() == 0:
                        while x < int(entry_y.get()):
                            for value in temp_y[x]:
                                data_y[x].append(int(value.get()))
                            for value in temp_labels[x]:
                                line_labels[x].append(value.get())
                            x += 1
                    if y_check.get() == 1:
                        for value in temp_labels:
                            line_labels.append(value.get())
                    dataWindow.destroy()

                def reset():
                    list()
                    z = 1

                    for x in range(int(entry_x.get())):
                        x_data = Entry(dataFrame, width=7)
                        x_data.grid(row=x, column=0, pady=0, padx=5)
                        temp_x.append(x_data)
                    if y_check.get() == 0:
                        for y in range(int(entry_y.get())):
                            for x in range(int(entry_x.get())):
                                y_data = Entry(dataFrame2, width=7)
                                y_data.grid(row=x, column=z, pady=0)
                                temp_y[y].append(y_data)
                            z += 1
                        for y in range(int(entry_y.get())):
                            legend_label = Entry(dataFrame4, width=7)
                            legend_label.grid(row=0, column=y, pady=0)
                            temp_labels[y].append(legend_label)
                    if y_check.get() == 1:
                        for y in range(int(entry_x.get())):
                            entry_pielabel= Entry(dataFrame4, width=10)
                            entry_pielabel.grid(row=0, column=y, pady=0)
                            temp_labels.append(entry_pielabel)

                # BUTTONS
                dataButton = Button(dataFrame3, text='Confirm Values', command=confirmed, bg='green')
                dataButton.grid(column=0, row=0)

                button_clear = Button(dataFrame3, text='Reset', command=reset, bg='yellow')
                button_clear.grid(column=1, row=0)


            def clicked():
                graph_type = combo1.get()

                if grid_check.get() == 1:
                    plt.grid(True)

                if graph_type == 'Line Plot':
                    for x in range(int(entry_y.get())):
                        plt.plot(data_x, data_y[x], label=line_labels[x][0])
                        plt.xlabel(entry_xlabel.get())
                        plt.ylabel(entry_ylabel.get())
                        plt.title(entry_title.get())
                    plt.legend()
                    plt.show()
                elif graph_type == 'Bar Chart':
                    x_index = np.arange(len(data_x))

                    bars = int(entry_y.get())
                    width = 1 / (bars + 1)
                    sep = -(1 / (bars + 1)) * (bars - 1)
                    for x in range(bars):
                        if hor_check.get() == 0:
                            plt.bar(x_index + sep, data_y[x], width=width, label=line_labels[x][0])
                            plt.xlabel(entry_xlabel.get())
                            plt.ylabel(entry_ylabel.get())

                        else:
                            plt.barh(x_index + sep, data_y[x], height=width, label=line_labels[x][0])
                            plt.xlabel(entry_ylabel.get())
                            plt.ylabel(entry_xlabel.get())
                        sep += 1 / (bars + 1)
                    if hor_check.get() == 0:
                        plt.xticks(ticks=x_index - ((bars - 1) * (width / 2)), labels=data_x)
                    else:
                        plt.yticks(ticks=x_index - ((bars - 1) * (width / 2)), labels=data_x)
                    plt.title(entry_title.get())
                    plt.legend()
                    plt.show()
                elif graph_type == 'Pie Chart':
                    plt.pie(data_x, labels=line_labels, wedgeprops={'edgecolor':'black'},startangle=90, autopct='%1.1f%%')
                    plt.show()

                list()

            def disable():
                if y_check.get() == 1:
                    entry_y.config(state='disabled')
                    entry_xlabel.config(state='disabled')
                    entry_ylabel.config(state='disabled')
                else:
                    entry_y.config(state=NORMAL)
                    entry_xlabel.config(state=NORMAL)
                    entry_ylabel.config(state=NORMAL)

            # BUTTONS
            button1 = Button(frame1, text='Make Graph', command=clicked, bg='green')
            button1.grid(column=0, row=1)

            button_data = Button(frame1, text='Input Datas', command=data_window, bg='yellow')
            button_data.grid(column=1, row=6)

            # GRAPH TYPES
            combo1 = Combobox(frame1)
            combo1['values'] = ('Line Plot', 'Bar Chart', 'Pie Chart')
            combo1.current(0)
            combo1.grid(column=0, row=0)

            # ENTRIES
            entry_x = Entry(frame1, width=10, bg='LightBlue1')
            entry_x.grid(column=1, row=4)

            entry_y = Entry(frame1, width=10, bg='LightBlue1')
            entry_y.grid(column=1, row=5)

            entry_xlabel = Entry(frame1, width=10, bg='LightBlue1')
            entry_xlabel.grid(column=1, row=7)

            entry_ylabel = Entry(frame1, width=10, bg='LightBlue1')
            entry_ylabel.grid(column=1, row=8)

            entry_title = Entry(frame1, width=10, bg='LightBlue1')
            entry_title.grid(column=1, row=10)


            # LABELS
            lbl_x = Label(frame1, text='Total Data Values', bg='LightBlue1')
            lbl_x.grid(column=0, row=4)

            lbl_y = Label(frame1, text='Number of Lines', bg='LightBlue1')
            lbl_y.grid(column=0, row=5)

            lbl_ver = Label(frame1, text='Horizontal Label', bg='LightBlue1')
            lbl_ver.grid(column=0, row=7)

            lbl_hor = Label(frame1, text='Vertical Label', bg='LightBlue1')
            lbl_hor.grid(column=0, row=8)

            lbl_title = Label(frame1, text='Title', bg='LightBlue1')
            lbl_title.grid(column=0, row=10)

            # CHECKBOX
            grid_check = IntVar()
            chk_grid = Checkbutton(frame2, text='Add Grid', variable=grid_check)
            chk_grid.grid(column=2, row=3)

            hor_check = IntVar()
            chk_hor = Checkbutton(frame2, text='Horizontal Bar', variable=hor_check)
            chk_hor.grid(column=2, row=4)

            y_check = IntVar()
            chk_y = Checkbutton(frame2, text='Pie Chart Mode', variable=y_check,command=disable)
            chk_y.grid(column=2, row=5)

            window.mainloop()

        statusbar1 = Label(windowMain, text="Welcome to Free Graph builder GRAPHIT ", relief=SUNKEN, font='Times 12 italic')
        statusbar1.place(x=2, y=580)

        button1 = Button(windowMain, text="Build a Graph", fg='white', bg='blue', font=("Bahnschrift SemiBold", 20, "bold"),command=Build)
        button1.place(x=100, y=300)

        button2 = Button(windowMain, text="Load a Graph", fg='white', bg='blue', font=("Bahnschrift SemiBold", 20, "bold"), command=fileDialog)
        button2.place(x=320, y=300)

        button3 = Button(windowMain, text="Share", fg='white', bg='blue', font=("Bahnschrift SemiBold", 20, "bold"), command=Share)
        button3.place(x=542, y=300)

        button4 = Button(windowMain, text="Account", fg='white', bg='blue', font=("Bahnschrift SemiBold", 20, "bold"),command=AccountPage)
        button4.place(x=680, y=300)

        windowMain.mainloop()


    statusbar = Label(root, text="Welcome to Free Graph builder GRAPHIT ", relief=SUNKEN, font='Times 12 italic')
    statusbar.place(x=2, y=580)

    button1 = Button(root, text="Sign in", fg='white', bg='blue', font=("Bahnschrift SemiBold", 20, "bold"), command=openSign)
    button1.place(x=230, y=300)

    button2 = Button(root, text="Log in", fg='white', bg='blue', font=("Bahnschrift SemiBold", 20, "bold"), command=openLog)
    button2.place(x=540, y=300)

    root.mainloop()


root()