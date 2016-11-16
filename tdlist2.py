from Tkinter import*
from tkMessageBox import *
from PIL import ImageTk, Image
import random
import tkFont

#functions
def blah():
    pass

def URGENT():
    pass 
def butnS1Yes(wndSave1):
    global wnd
    global txt1
    txt1.configure(state=DISABLED)
    #changing button save to SAVED
    btnSaved1=Button(wnd,text="Saved :)",background='purple',foreground='pink',command=blah)
    fontYes = tkFont.Font(family='Helvetica',size=13, weight='bold')
    btnSaved1.configure(width=10,height=1,font=fontYes, relief=RAISED)
    btnSaved1.pack()
    btnSaved1.place(x=700,y=360)

    wndSave1.destroy()

def butnS1No(wndSave1):
    wndSave1.destroy()
def butnS2Yes(wndSave2):
    global wnd
    global txt2
    txt2.configure(state=DISABLED)
    #changing button save to SAVED
    btnSaved2=Button(wnd,text="Saved :)",background='purple',foreground='pink',command=blah)
    fontYes = tkFont.Font(family='Helvetica',size=13, weight='bold')
    btnSaved2.configure(width=10,height=1,font=fontYes, relief=RAISED)
    btnSaved2.pack()
    btnSaved2.place(x=700,y=400)

    wndSave2.destroy()

def butnS2No(wndSave2):
    wndSave2.destroy()
def butnS3Yes(wndSave2):
    global wnd
    global txt3
    txt2.configure(state=DISABLED)
    #changing button save to SAVED
    btnSaved3=Button(wnd,text="Saved :)",background='purple',foreground='pink',command=blah)
    fontYes = tkFont.Font(family='Helvetica',size=13, weight='bold')
    btnSaved3.configure(width=10,height=1,font=fontYes, relief=RAISED)
    btnSaved3.pack()
    btnSaved3.place(x=700,y=440)

    wndSave3.destroy()

def butnS3No(wndSave3):
    wndSave3.destroy()
def butnU1Yes(wndU1):
    global wnd3
    global wnd
##    buttonURGENT=Button(wnd,text="URGENT",background='purple',foreground='dark red',command=URGENT)
    btnU1U=Button(wnd,text="URGENT!!!",background='purple',foreground='red',command=blah)
    fontYes = tkFont.Font(family='Helvetica',size=13, weight='bold')
    btnU1U.configure(width=10,height=1,font=fontYes, relief=RAISED)
    btnU1U.pack()
    btnU1U.place(x=800,y=360)
    newImage=ImageTk.PhotoImage(Image.open("priority.jpg"))
    bullet_label.configure(image=newImage)
    bullet_label.image=newImage
##    newImage_label=Label(wnd,image=newImage)  ######Problem here...image not showing
##    newImage_label.pack()
##    newImage_label.place(x=20,y=355)
def butnU1No(wndU1):
    
    wndU1.destroy()

    
    

def butn1U():
    wndU1=Tk()
    wndU1.geometry("400x100")
    wndU1.configure(background='pink')
    wndU1.title("Shopping List")
    fontYes = tkFont.Font(family='Helvetica',size=13, weight='bold')
    labelshop1=Label(wndU1,text="Do you want to save it?",foreground='purple',background='pink',font=fontYes)
    labelshop1.pack()
    labelshop1.place(x=120,y=3)
    
    '''bulletReplace=ImageTk.PhotoImage(Image.open("urgent.png"))
    bullet_label=Label(wnd,image=bulletReplace)
    bullet_label.pack()
    bullet_label.place(x=20,y=360)'''

    #button yes in dialog for URGENT BUTTON

    fontYes = tkFont.Font(family='Helvetica',size=13, weight='bold')
    btnU1Yes=Button(wndU1,text="Yes",background='purple',foreground='pink',command=lambda:butnU1Yes(wndU1))
    fontYes = tkFont.Font(family='Helvetica',size=13, weight='bold')
   

    btnU1Yes.configure(width=10,height=1,font=fontYes,relief=RAISED)
    btnU1Yes.pack()
    btnU1Yes.place(x=100,y=60)

    
    #button no in dialog for URGENT BUTTON
    btnU1No=Button(wndU1,text="No",background='purple',foreground='pink',command=lambda:butnU1No(wndU1))
    btnU1No.configure(width=10,height=1,font=fontYes, relief=RAISED)
    btnU1No.pack()
    btnU1No.place(x=220,y=60)

    
    
    
    
    


    #showinfo(title="Shopping List",message="Do you want to save it?")
##    root = Tk()
##    tl = Toplevel(root)
##    tl.title("Languages")
##
##    frame = Frame(tl)
##    frame.grid()
##
##    canvas = Canvas(frame, width=100, height=130)
##    canvas.grid(row=1, column=0)
##    imgvar = PhotoImage(file="dnt4get.jgp")
##    canvas.create_image(50,70, image=imgvar)
##    canvas.image = imgvar
##
##   # msgbody1 = Label(frame, text="The", font=("Times New Roman", 20, "bold"))
##    #msgbody1.grid(row=1, column=1, sticky=N)
##    lang = Label(frame, text="language(s)", font=("Times New Roman", 20, "bold"), fg='blue')
##    lang.grid(row=1, column=2, sticky=N)
##    #msgbody2 = Label(frame, text="of this country is: Arabic", font=("Times New Roman", 20, "bold"))
##    #msgbody2.grid(row=1, column=3, sticky=N)
##
##    #cancelbttn = Button(frame, text="Cancel", command=lambda: choosefunc("cancel"), width=10)
##    #cancelbttn.grid(row=2, column=3)
##
##    #okbttn = Button(frame, text="OK", command=lambda: choosefunc("ok"), width=10)
##    #okbttn.grid(row=2, column=4)
def save1():
    wndSave1=Tk()
    wndSave1.geometry("400x100")
    wndSave1.configure(background='pink')
    wndSave1.title("Shopping")
    fontYes = tkFont.Font(family='Helvetica',size=13, weight='bold')
    labelshop1=Label(wndSave1,text="Do you want to save it?",foreground='purple',background='pink',font=fontYes)
    labelshop1.pack()
    labelshop1.place(x=120,y=3)

    #putting picture in dialog box

    '''dialogImage=ImageTk.PhotoImage(Image.open("btnshop.jpg"))
    dialog_label=Label(wnd2,image=dialogImage)
    dialog_label.pack()
    dialog_label.place(x=20,y=3)'''     ###not working




    fontYes = tkFont.Font(family='Helvetica',size=13, weight='bold')
    btnS1Yes=Button(wndSave1,text="Yes",background='purple',foreground='pink',command=lambda:butnS1Yes(wndSave1))

    btnS1Yes.configure(width=10,height=1,font=fontYes,relief=RAISED)
    btnS1Yes.pack()
    btnS1Yes.place(x=100,y=60)

    btnS1No=Button(wndSave1,text="No",background='purple',foreground='pink',command= lambda: butnS1No(wndSave1))
    btnS1No.configure(width=10,height=1,font=fontYes, relief=RAISED)
    btnS1No.pack()
    btnS1No.place(x=220,y=60)




    txt1=Text(wnd,relief=RAISED,font=helv20,width=40,height=1,state=DISABLED, background='pink', foreground='purple')

def save2():
    wndSave2=Tk()
    wndSave2.geometry("400x100")
    wndSave2.configure(background='pink')
    wndSave2.title("Shopping")
    fontYes = tkFont.Font(family='Helvetica',size=13, weight='bold')
    labelshop2=Label(wndSave2,text="Do you want to save it?",foreground='purple',background='pink',font=fontYes)
    labelshop2.pack()
    labelshop2.place(x=120,y=3)

    #putting picture in dialog box

    '''dialogImage=ImageTk.PhotoImage(Image.open("btnshop.jpg"))
    dialog_label=Label(wnd2,image=dialogImage)
    dialog_label.pack()
    dialog_label.place(x=20,y=3)'''     ###not working




    fontYes = tkFont.Font(family='Helvetica',size=13, weight='bold')
    btnS2Yes=Button(wndSave2,text="Yes",background='purple',foreground='pink',command=lambda:butnS2Yes(wndSave2))

    btnS2Yes.configure(width=10,height=1,font=fontYes,relief=RAISED)
    btnS2Yes.pack()
    btnS2Yes.place(x=100,y=60)

    btnS2No=Button(wndSave2,text="No",background='purple',foreground='pink',command= lambda: butnS2No(wndSave2))
    btnS2No.configure(width=10,height=1,font=fontYes, relief=RAISED)
    btnS2No.pack()
    btnS2No.place(x=220,y=60)




    #txt2=Text(wnd,relief=RAISED,font=helv20,width=40,height=1,state=DISABLED, background='pink', foreground='purple')

def save3():
    wndSave3=Tk()
    wndSave3.geometry("400x100")
    wndSave3.configure(background='pink')
    wndSave3.title("Shopping")
    fontYes = tkFont.Font(family='Helvetica',size=13, weight='bold')
    labelshop3=Label(wndSave3,text="Do you want to save it?",foreground='purple',background='pink',font=fontYes)
    labelshop3.pack()
    labelshop3.place(x=120,y=3)

    #putting picture in dialog box

    '''dialogImage=ImageTk.PhotoImage(Image.open("btnshop.jpg"))
    dialog_label=Label(wnd2,image=dialogImage)
    dialog_label.pack()
    dialog_label.place(x=20,y=3)'''     ###not working




    fontYes = tkFont.Font(family='Helvetica',size=13, weight='bold')
    btnS3Yes=Button(wndSave3,text="Yes",background='purple',foreground='pink',command=lambda:butnS3Yes(wndSave3))

    btnS3Yes.configure(width=10,height=1,font=fontYes,relief=RAISED)
    btnS3Yes.pack()
    btnS3Yes.place(x=100,y=60)

    btnS3No=Button(wndSave3,text="No",background='purple',foreground='pink',command= lambda: butnS3No(wndSave3))
    btnS3No.configure(width=10,height=1,font=fontYes, relief=RAISED)
    btnS3No.pack()
    btnS3No.place(x=220,y=60)

      
           
        

wnd=Tk()
wnd.title("To-Do List")
wnd.geometry("1100x800")
background=ImageTk.PhotoImage(Image.open("backgroundtd.jpg"))
background_label=Label(wnd,image=background)
background_label.pack()
background_label.place(x=0,y=0)

background_image=ImageTk.PhotoImage(Image.open("bg.jpg"))
image_label=Label(wnd,image=background_image)
image_label.pack()
image_label.place(x=20,y=20)

top=ImageTk.PhotoImage(Image.open("tdlist.jpg"))
top_label=Label(wnd,image=top)
top_label.pack()
top_label.place(x=20,y=20)

shop_image=ImageTk.PhotoImage(Image.open("scartoon2.gif"))
top_label1=Label(wnd,image=shop_image)
top_label1.pack()
top_label1.place(x=20,y=140)

shop_image1=ImageTk.PhotoImage(Image.open("shopping.png"))
shop_label=Label(wnd,image=shop_image1)
shop_label.pack()
shop_label.place(x=320,y=140)

shop_image2=ImageTk.PhotoImage(Image.open("box.jpg"))
shop_label=Label(wnd,image=shop_image2)
shop_label.pack()
shop_label.place(x=620,y=140)

shop_image3=ImageTk.PhotoImage(Image.open("grocerystore.jpg"))
shop_label=Label(wnd,image=shop_image3)
shop_label.pack()
shop_label.place(x=820,y=140)






#putting bullet

bullet=ImageTk.PhotoImage(Image.open("flower.png"))
bullet_label=Label(wnd,image=bullet)
bullet_label.pack()
bullet_label.place(x=20,y=355)


#creating textbox

helv20 = tkFont.Font(family='Helvetica',size=20, weight='bold', slant='italic')
txt1=Text(wnd,relief=RAISED,font=helv20,width=40,height=1,state=NORMAL, background='pink', foreground='purple')
txt1.pack()
txt1.place(x=90,y=360)

#creating buttons
fontYes = tkFont.Font(family='Helvetica',size=13, weight='bold')
btn1=Button(relief=RIDGE, text='Save?',width=4,height=1, background='purple',foreground='pink',command=save1)
btn1.configure(width=10,height=1,font=fontYes, relief=RAISED)
btn1.pack()
btn1.place(x=700,y=360)

#button URGENT
btnU=Button(wnd,text="Urgent?",background='purple',foreground='pink',command=butn1U)
fontYes = tkFont.Font(family='Helvetica',size=13, weight='bold')
btnU.configure(width=10,height=1,font=fontYes, relief=RAISED)
btnU.pack()
btnU.place(x=800,y=360)
###2#####

#Creting bullet2
bullet2=ImageTk.PhotoImage(Image.open("flower.png"))
bullet2_label=Label(wnd,image=bullet2)
bullet2_label.pack()
bullet2_label.place(x=20,y=400)

#creating txbox2
helv20 = tkFont.Font(family='Helvetica',size=20, weight='bold', slant='italic')
txt2=Text(wnd,relief=RAISED,font=helv20,width=40,height=1,state=NORMAL, background='pink', foreground='purple')
txt2.pack()
txt2.place(x=90,y=400)

#creating buttons
fontYes = tkFont.Font(family='Helvetica',size=13, weight='bold')
btn2=Button(relief=RIDGE, text='Save?',width=4,height=1, background='purple',foreground='pink',command=save2)
btn2.configure(width=10,height=1,font=fontYes, relief=RAISED)
btn2.pack()
btn2.place(x=700,y=400)
btn2U=Button(wnd,text="Urgent?",background='purple',foreground='pink',command=butn1U)
fontYes = tkFont.Font(family='Helvetica',size=13, weight='bold')
btn2U.configure(width=10,height=1,font=fontYes, relief=RAISED)
btn2U.pack()
btn2U.place(x=800,y=400)

###3####
#Creting bullet3
bullet3=ImageTk.PhotoImage(Image.open("flower.png"))
bullet3_label=Label(wnd,image=bullet2)
bullet3_label.pack()
bullet3_label.place(x=20,y=440)

#creating txbox2
helv20 = tkFont.Font(family='Helvetica',size=20, weight='bold', slant='italic')
txt3=Text(wnd,relief=RAISED,font=helv20,width=40,height=1,state=NORMAL, background='pink', foreground='purple')
txt3.pack()
txt3.place(x=90,y=440)

#creating buttons
fontYes = tkFont.Font(family='Helvetica',size=13, weight='bold')
btn3=Button(relief=RIDGE, text='Save?',width=4,height=1, background='purple',foreground='pink',command=save3)
btn3.configure(width=10,height=1,font=fontYes, relief=RAISED)
btn3.pack()
btn3.place(x=700,y=440)
btn3U=Button(wnd,text="Urgent?",background='purple',foreground='pink',command=butn1U)
fontYes = tkFont.Font(family='Helvetica',size=13, weight='bold')
btn3U.configure(width=10,height=1,font=fontYes, relief=RAISED)
btn3U.pack()
btn3U.place(x=800,y=440)
###4###
#Creting bullet4
bullet4=ImageTk.PhotoImage(Image.open("flower.png"))
bullet4_label=Label(wnd,image=bullet4)
bullet4_label.pack()
bullet4_label.place(x=20,y=480)

#creating txbox2
helv20 = tkFont.Font(family='Helvetica',size=20, weight='bold', slant='italic')
txt4=Text(wnd,relief=RAISED,font=helv20,width=40,height=1,state=NORMAL, background='pink', foreground='purple')
txt4.pack()
txt4.place(x=90,y=480)

#creating buttons
fontYes = tkFont.Font(family='Helvetica',size=13, weight='bold')
btn4=Button(relief=RIDGE, text='Save?',width=4,height=1, background='purple',foreground='pink',command=save2)
btn4.configure(width=10,height=1,font=fontYes, relief=RAISED)
btn4.pack()
btn4.place(x=700,y=480)
btn4U=Button(wnd,text="Urgent?",background='purple',foreground='pink',command=butn1U)
fontYes = tkFont.Font(family='Helvetica',size=13, weight='bold')
btn4U.configure(width=10,height=1,font=fontYes, relief=RAISED)
btn4U.pack()
btn4U.place(x=800,y=480)

####5#####

#Creting bullet4
bullet5=ImageTk.PhotoImage(Image.open("flower.png"))
bullet5_label=Label(wnd,image=bullet5)
bullet5_label.pack()
bullet5_label.place(x=20,y=520)

#creating txbox2
helv20 = tkFont.Font(family='Helvetica',size=20, weight='bold', slant='italic')
txt5=Text(wnd,relief=RAISED,font=helv20,width=40,height=1,state=NORMAL, background='pink', foreground='purple')
txt5.pack()
txt5.place(x=90,y=520)

#creating buttons
fontYes = tkFont.Font(family='Helvetica',size=13, weight='bold')
btn5=Button(relief=RIDGE, text='Save?',width=4,height=1, background='purple',foreground='pink',command=save2)
btn5.configure(width=10,height=1,font=fontYes, relief=RAISED)
btn5.pack()
btn5.place(x=700,y=520)
btn5U=Button(wnd,text="Urgent?",background='purple',foreground='pink',command=butn1U)
fontYes = tkFont.Font(family='Helvetica',size=13, weight='bold')
btn5U.configure(width=10,height=1,font=fontYes, relief=RAISED)
btn5U.pack()
btn5U.place(x=800,y=520)

####6####
#Creting bullet4
bullet6=ImageTk.PhotoImage(Image.open("flower.png"))
bullet6_label=Label(wnd,image=bullet6)
bullet6_label.pack()
bullet6_label.place(x=20,y=560)

#creating txbox2
helv20 = tkFont.Font(family='Helvetica',size=20, weight='bold', slant='italic')
txt6=Text(wnd,relief=RAISED,font=helv20,width=40,height=1,state=NORMAL, background='pink', foreground='purple')
txt6.pack()
txt6.place(x=90,y=560)

#creating buttons
fontYes = tkFont.Font(family='Helvetica',size=13, weight='bold')
btn6=Button(relief=RIDGE, text='Save?',width=4,height=1, background='purple',foreground='pink',command=save2)
btn6.configure(width=10,height=1,font=fontYes, relief=RAISED)
btn6.pack()
btn6.place(x=700,y=560)
btn6U=Button(wnd,text="Urgent?",background='purple',foreground='pink',command=butn1U)
fontYes = tkFont.Font(family='Helvetica',size=13, weight='bold')
btn6U.configure(width=10,height=1,font=fontYes, relief=RAISED)
btn6U.pack()
btn6U.place(x=800,y=560)

###7###
#Creting bullet4
bullet7=ImageTk.PhotoImage(Image.open("flower.png"))
bullet7_label=Label(wnd,image=bullet7)
bullet7_label.pack()
bullet7_label.place(x=20,y=600)

#creating txbox2
helv20 = tkFont.Font(family='Helvetica',size=20, weight='bold', slant='italic')
txt7=Text(wnd,relief=RAISED,font=helv20,width=40,height=1,state=NORMAL, background='pink', foreground='purple')
txt7.pack()
txt7.place(x=90,y=600)

#creating buttons
fontYes = tkFont.Font(family='Helvetica',size=13, weight='bold')
btn7=Button(relief=RIDGE, text='Save?',width=4,height=1, background='purple',foreground='pink',command=save2)
btn7.configure(width=10,height=1,font=fontYes, relief=RAISED)
btn7.pack()
btn7.place(x=700,y=600)
btn7U=Button(wnd,text="Urgent?",background='purple',foreground='pink',command=butn1U)
fontYes = tkFont.Font(family='Helvetica',size=13, weight='bold')
btn7U.configure(width=10,height=1,font=fontYes, relief=RAISED)
btn7U.pack()
btn7U.place(x=800,y=600)


##insereting emoji at bottom

emoji=ImageTk.PhotoImage(Image.open("pencil.png"))
emoji_label=Label(wnd,image=emoji)
emoji_label.pack()
emoji_label.place(x=980,y=500)




wnd.mainloop()
