#userWnd.destroy()
from Tkinter import*
from Tkinter import*
from tkMessageBox import *
from PIL import ImageTk, Image
import random
import tkFont
import speech_recognition as sr
import calendar

##try:
import Tkinter
import tkFont
from PIL import ImageTk, Image
##except ImportError: # py3k
##    import tkinter as Tkinter
##    import tkinter.font as tkFont
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from Tkinter import Tk
#from Tkinter.filedialog import askopenfilename



import ttk
import main1
##def press_btnEBACK(userWnd,DiaryWnd):
##    DiaryWnd.destroy()

    
    
##    userWnd=Tk() #creating the window
##    userWnd.title("Handy App welcomes you :)")
##    userWnd.geometry("1100x600")
##    lstOfImages=["bgUser1.jpg","bgUser2.gif","bgUser3.jpg","bgUser4.jpg","bgUser5.jpg","bgUser6.jpg","bgUser7.jpg","bgUser8.jpg","bgUser9.jpg","bgUser10.jpg"]
##    bgUser=ImageTk.PhotoImage(Image.open(random.choice(lstOfImages)))
##    bgUser_label=Label(userWnd,image=bgUser)
##    bgUser_label.pack()
##    bgUser_label.place(x=0,y=0)
##
##    #putting picture of td before the td button
##    btnUserTDpic=ImageTk.PhotoImage(Image.open("logo.png"))
##    btnUserTDpic_label=Label(userWnd,image=btnUserTDpic)
##    btnUserTDpic_label.pack()
##    btnUserTDpic_label.place(x=30,y=200)
##
##
##
##    #creating td button
##    helv20 = tkFont.Font(family='Helvetica',size=20, weight='bold', slant='italic')
##
##    btnTD=Button(text="To-Do List",relief=RAISED,font=helv20,width=20,height=2,state=NORMAL, background='pink', foreground='purple',command=ToDo)
##    btnTD.pack()
##    btnTD.place(x=200,y=200)
##    userWnd.after(2000,pics)
##
##    #putting picture of calculator before cal button
##
##    btnUserCalpic=ImageTk.PhotoImage(Image.open("calcUser.jpg"))
##    btnUserCalpic_label=Label(userWnd,image=btnUserCalpic)
##    btnUserCalpic_label.pack()
##    btnUserCalpic_label.place(x=30,y=300)
##
##    #creating calculator button
##
##    btnC=Button(text="Calculator",relief=RAISED,font=helv20,width=20,height=2,state=NORMAL, background='pink', foreground='purple')
##    btnC.pack()
##    btnC.place(x=200,y=300)
##
##    #putting picture of diary before diary button
##
##    btnUserDiapic=ImageTk.PhotoImage(Image.open("diaryUser.jpg"))
##    btnUserDiapic_label=Label(userWnd,image=btnUserDiapic)
##    btnUserDiapic_label.pack()
##    btnUserDiapic_label.place(x=30,y=400)
##
##    #creating diary button
##
##    btnC=Button(text="Diary",relief=RAISED,font=helv20,width=20,height=2,state=NORMAL, background='pink', foreground='purple',command=lambda:diary7.diary_create(userWnd))
##    btnC.pack()
##    btnC.place(x=200,y=400)
##
##    #putting picture of calendar before calendar button
##
##    btnUserCalepic=ImageTk.PhotoImage(Image.open("calendar.jpg"))
##    btnUserCalepic_label=Label(userWnd,image=btnUserCalepic)
##    btnUserCalepic_label.pack()
##    btnUserCalepic_label.place(x=30,y=500)
##
##    #creating calendar button
##
##    btnC=Button(text="Mini Calendar",relief=RAISED,font=helv20,width=20,height=2,state=NORMAL, background='pink', foreground='purple',command=CalendarWnd)
##    btnC.pack()
##    btnC.place(x=200,y=500)
##
##    wnd=0
##    bullet_label=0
##    txt1=0
##
##
##
##
##
##
##
##
##
##
##    userWnd.after(2000,pics)
##
##
##    userWnd.mainloop()

def press_Okay(dialog_EmailWnd3):
    dialog_EmailWnd3.destroy()
    
    
    
def Send_toGmail(subject_entry,from_entry,to_entry,msg_box,passwd_entry):
    print "hi"
    
    msg=MIMEMultipart()
    subject=subject_entry.get()
    my_email=from_entry.get()
    addrto=to_entry.get()
    msg['Subject']=subject
    print "hello"
    msg["From"]=my_email
    msg["To"]=addrto

    text=MIMEText(msg_box.get("1.0",END))
    msg.attach(text)
    passwd=passwd_entry.get()

    print "connecting"
    #create a dialog box to show that it is connecting to the server
    dialog_EmailWnd1=Tk()
    dialog_EmailWnd1.title("Email")
    dialog_EmailWnd1.geometry("400x2100")
    dialog_EmailWnd1.configure(bg="pink")
    fontYes = tkFont.Font(family='Helvetica',size=13, weight='bold')
    label_dialog1=Label(dialog_EmailWnd1,text="Connecting to Gmail server.Please be patient",fg="purple",bg="pink")
    label_dialog1.pack()
    label_dialog1.place(x=120,y=3)
        
    
    s=smtplib.SMTP("smtp.gmail.com",587)
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login(my_email,passwd)
    print "connected"
    #destroy previous dialog box 
    dialog_EmailWnd1.destroy()
    #create another dialog box
    dialog_EmailWnd2=Tk()
    dialog_EmailWnd2.title("Email")
    dialog_EmailWnd2.geometry("400x200")
    dialog_EmailWnd2.configure(bg="pink")
    fontYes = tkFont.Font(family='Helvetica',size=13, weight='bold')
    label_dialog2=Label(dialog_EmailWnd2,text="Connected to Gmail server.",fg="purple",bg="pink")
    label_dialog2.pack()
    label_dialog2.place(x=120,y=3)
   
    
    
    
    s.sendmail(my_email,addrto,msg.as_string())
    print "sent"
    #creating another dialog box to indicate "Sent"
    #we fisrt destroy previous dialog box
    dialog_EmailWnd2.destroy()
    #send_emailWnd.destroy()
    
    
    dialog_EmailWnd3=Toplevel()
    dialog_EmailWnd3.title("Email")
    dialog_EmailWnd3.geometry("400x100")
    dialog_EmailWnd3.configure(bg="pink")
    fontYes = tkFont.Font(family='Helvetica',size=13, weight='bold')
    label_dialog3=Label(dialog_EmailWnd3,text="Your Email Has Been Sent Successfully!",fg="purple",bg="pink")
    label_dialog3.pack()
    label_dialog3.place(x=120,y=3)
    #putting a picture in dialog box
    dialogEmail_pic=ImageTk.PhotoImage(Image.open("smiley_emailDialog.jpeg"))
    dialogEmail_pic_label=Label(dialog_EmailWnd3,image=dialogEmail_pic)
    dialogEmail_pic_label.image=dialogEmail_pic
    dialogEmail_pic_label.pack()
    dialogEmail_pic_label.place(x=200,y=8) ##not working

    #adding a button "Ok" to this window
    btn_Okay=Button(dialog_EmailWnd3,text="Okay",bg="purple",fg="pink",command=lambda:press_Okay(dialog_EmailWnd3))
    btn_Okay.pack()
    btn_Okay.place(x=200,y=30)

    
    s.quit()
    
    
    
def Send_Email(Emails_listbox):
    selected_email=Emails_listbox.get(ACTIVE)
    #destroy the userinterface window
    
    send_emailWnd=Toplevel()
    send_emailWnd.title("Send Email")
    send_emailWnd.geometry("600x400")
    bgEmail=ImageTk.PhotoImage(Image.open("bgEmail.png"))
    bgEmail_label=Label(send_emailWnd,image=bgEmail)
    bgEmail_label.pack()
    bgEmail_label.place(x=0,y=0)

    #send_emailWnd.configure(bg="VioletRed4")
    #creating Label "To" of email
    '''To_label=Label(send_emailWnd,text="To",bg="hot pink",fg="VioletRed4")
    To_label.pack()
    To_label.place(x=40,y=40)'''
    #creating the entry box next to the Label "To"
    from_entry=Entry(send_emailWnd, bg="pink",fg="VioletRed4",width=50)
##    #inserting the email that we clicked on in the listbox of previous window
##    from_entry.insert(0,selected_email)
    
    
    
    from_entry.pack()
    from_entry.place(x=190,y=50)
    '''#creating Label "From" of email
    From_label=Label(send_emailWnd,text="From",bg="hot pink",fg="VioletRed4")
    From_label.pack()
    From_label.place(x=40,y=110)'''

    passwd_entry=Entry(send_emailWnd,show="*", bg="pink",fg="VioletRed4",width=50)
    
    passwd_entry.pack()
    passwd_entry.place(x=190,y=90)
    #creating the entry box next to the Label "From"
    to_entry=Entry(send_emailWnd, bg="pink",fg="VioletRed4",width=50)
    #inserting the email that we clicked on in the listbox of previous window
    to_entry.insert(0,selected_email)
    to_entry.pack()
    to_entry.place(x=190,y=130)
    
    
    #creating Label "Subject" of email
    '''subject_label=Label(send_emailWnd,text="Subject",bg="hot pink",fg="VioletRed4")
    subject_label.pack()
    subject_label.place(x=40,y=150)'''
    #creating the entry box next to the Label "Subject"
    subject_entry=Entry(send_emailWnd, bg="pink",fg="VioletRed4",width=50)
    subject_entry.pack()
    subject_entry.place(x=190,y=170)
    #creating the label"Password)
    '''passwd_label=Label(send_emailWnd,text="Password",bg="hot pink",fg="VioletRed4")
    passwd_label.pack()
    passwd_label.place(x=40,y=160)'''
    #creating "password" entry box
    '''passwd_entry=Entry(send_emailWnd, bg="pink",fg="VioletRed4",width=50)
    
    passwd_entry.pack()
    passwd_entry.place(x=180,y=190)'''
    

    #Creating big entry for message
    msg_box=Text(send_emailWnd,bg="pink",fg="VioletRed4",width=50,height=6)
    msg_box.pack()
    msg_box.place(x=80,y=250)
    #creating a button for "Send Email"
    btn_SendEmail=Button(send_emailWnd,bg="pink",fg="VioletRed4",text="Send Email",command=lambda:Send_toGmail(subject_entry,from_entry,to_entry,msg_box,passwd_entry))
    btn_SendEmail.pack()
    btn_SendEmail.place(x=80,y=350)
##    #creating the label"Password)
##    passwd_label=Label(send_emailWnd,text="Password",bg="hot pink",fg="VioletRed4")
##    passwd_label.pack()
##    passwd_label.place(x=40,y=160)
##    #creating "password" entry box
##    passwd_entry=Entry(send_emailWnd, bg="pink",fg="VioletRed4")
##    
##    passwd_entry.pack()
##    passwd_entry.place(x=120,y=160)
##    
    
    
    
    send_emailWnd.mainloop()
    

def Add_Email(AddEmail_entry,Emails_listbox):
    input_from_AddEmail=AddEmail_entry.get()
    #inserting the thing we got from the entry box to the listbox
    Emails_listbox.insert(END,input_from_AddEmail)
    file_Email=open("fileEmail.txt","a")
    file_Email.write(input_from_AddEmail+"\n")
    file_Email.close()
    
    
    
    
def Add_Contact(AddContact_entry,Contact_listbox):
    print AddContact_entry
    entry_Contact=AddContact_entry.get()
    print "just under entry_Contact"
    print entry_Contact
    Contact_listbox.insert(END,entry_Contact)
    file_Contact=open("fileContact.txt","a")
    file_Contact.write(entry_Contact+"\n")
    file_Contact.close()
    
    
def diary_create(userWnd):
    userWnd.destroy()

    #DiaryWnd=Toplevel()
    DiaryWnd=Tk()
    DiaryWnd.title("Diary")
    DiaryWnd.geometry("1100x600")
    Dbackground=ImageTk.PhotoImage(Image.open("backgroundtd.jpg"))
    Dbackground_label=Label(DiaryWnd,image=Dbackground)
    Dbackground_label.pack()
    Dbackground_label.place(x=0,y=0)

    Dbackground_image=ImageTk.PhotoImage(Image.open("dia4.jpg"))
    Dimage_label=Label(DiaryWnd,image=Dbackground_image)
    Dimage_label.pack()
    Dimage_label.place(x=20,y=20)

    #creating the Label "Add Contact"

    AddContact_label=Label(DiaryWnd,text="Contact",background="pink",foreground="VioletRed4")
    AddContact_label.pack()
    AddContact_label.place(x=30,y=100)


    #creating the entry box for "Add Contact"
    AddContact_entry=Entry(DiaryWnd)
    AddContact_entry.pack()
    AddContact_entry.place(x=30,y=130)

    #creating the buttton "Add"
    btn_AddContact=Button(DiaryWnd,text="Add",bg="black",fg="white",command=lambda:Add_Contact(AddContact_entry,Contact_listbox))
    btn_AddContact.pack()
    btn_AddContact.place(x=160,y=130)

    #creating the Label "Add Email"

    AddContact_label=Label(DiaryWnd,text="Email",background="pink",foreground="VioletRed4")
    AddContact_label.pack()
    AddContact_label.place(x=30,y=160)
    #creating the entry box for "Add Email"
    AddEmail_entry=Entry(DiaryWnd)
    AddEmail_entry.pack()
    AddEmail_entry.place(x=30,y=190)

    #creating the label "CONTACTS"

    Contacts_label=Label(DiaryWnd,text="CONTACTS",bg="black",fg="white")
    Contacts_label.pack()
    Contacts_label.place(x=130,y=230)


    #Creating listbox for Contacts names 
    Contact_listbox=Listbox(DiaryWnd,width=50, height=20)
    Contact_listbox.pack()
    Contact_listbox.configure(bg="hot pink",fg="VioletRed4")
    file_Contact=open("fileContact.txt","r")
    line=file_Contact.readline()
    while line:
        Contact_listbox.insert(END,line)
        line=file_Contact.readline()
    file_Contact.close()
    
        
        
    
    
    Contact_listbox.place(x=60,y=260)

    #Creating the label "EMAIL ID"  

    Emails_label=Label(DiaryWnd,text="EMAILS",bg="black",fg="white")
    Emails_label.pack()
    Emails_label.place(x=420,y=230)
    #Creating listbox for EMAIL IDS  
    Emails_listbox=Listbox(DiaryWnd, width=50, height=20)
    Emails_listbox.configure(bg="hot pink",fg="VioletRed4")
    file_Email=open("fileEmail.txt","r")
    line=file_Email.readline()
    while line:
        Emails_listbox.insert(END,line)
        line=file_Email.readline()
    file_Email.close()
    
    Emails_listbox.pack()
    Emails_listbox.place(x=320,y=260)
    #getting what we wrote in the entry box and adding it to the listbox
    ##entry_get=AddContact_entry.get()
    ##Contact_listbox.insert(END,entry_get)
    #creating the "Add" button for the EMAIL ID
    btn_AddEmail=Button(DiaryWnd,text="Add",bg="black",fg="white",command=lambda:Add_Email(AddEmail_entry,Emails_listbox))
    btn_AddEmail.pack()
    btn_AddEmail.place(x=160,y=190)

    #creating button "Send" inderneath the email listbox
    btn_SendEmail=Button(DiaryWnd,text="Send Email",bg="black",fg='white',command=lambda:Send_Email(Emails_listbox))
    btn_SendEmail.pack()
    btn_SendEmail.place(x=320,y=580)

    #creating button "BACK"
    btnE_BACK=Button(DiaryWnd,text="BACK",bg="black",fg="white",width=15,command=lambda:main1.recreateWnd(DiaryWnd))
    #btnE_BACK=Button(DiaryWnd,text="BACK",bg="black",fg="white",width=15)
    btnE_BACK.pack()
    btnE_BACK.place(x=950,y=20)
                         

    







    DiaryWnd.mainloop()
