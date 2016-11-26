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

import ttk
import diary7

#functions associated with Calendar
def get_calendar(locale, fwday):
    # instantiate proper calendar class
    if locale is None:
        return calendar.TextCalendar(fwday)
    else:
        return calendar.LocaleTextCalendar(fwday, locale)

class Calendar(ttk.Frame):
    # XXX ToDo: cget and configure

    datetime = calendar.datetime.datetime
    timedelta = calendar.datetime.timedelta

    def __init__(self, master=None, **kw):
        """
        WIDGET-SPECIFIC OPTIONS
            locale, firstweekday, year, month, selectbackground,
            selectforeground
        """
        # remove custom options from kw before initializating ttk.Frame
        fwday = kw.pop('firstweekday', calendar.MONDAY)
        year = kw.pop('year', self.datetime.now().year)
        month = kw.pop('month', self.datetime.now().month)
        locale = kw.pop('locale', None)
        sel_bg = kw.pop('selectbackground', '#ffc4ff')
        sel_fg = kw.pop('selectforeground', '#05640e')

        self._date = self.datetime(year, month, 1)
        self._selection = None # no date selected

        ttk.Frame.__init__(self, master, **kw)

        self._cal = get_calendar(locale, fwday)

        self.__setup_styles()       # creates custom styles
        self.__place_widgets()      # pack/grid used widgets
        self.__config_calendar()    # adjust calendar columns and setup tags
        # configure a canvas, and proper bindings, for selecting dates
        self.__setup_selection(sel_bg, sel_fg)

        # store items ids, used for insertion later
        self._items = [self._calendar.insert('', 'end', values='')
                            for _ in range(6)]
        # insert dates in the currently empty calendar
        self._build_calendar()

        # set the minimal size for the widget
        self._calendar.bind('<Map>', self.__minsize)

    def __setitem__(self, item, value):
        if item in ('year', 'month'):
            raise AttributeError("attribute '%s' is not writeable" % item)
        elif item == 'selectbackground':
            self._canvas['background'] = value
        elif item == 'selectforeground':
            self._canvas.itemconfigure(self._canvas.text, item=value)
        else:
            ttk.Frame.__setitem__(self, item, value)

    def __getitem__(self, item):
        if item in ('year', 'month'):
            return getattr(self._date, item)
        elif item == 'selectbackground':
            return self._canvas['background']
        elif item == 'selectforeground':
            return self._canvas.itemcget(self._canvas.text, 'fill')
        else:
            r = ttk.tclobjs_to_py({item: ttk.Frame.__getitem__(self, item)})
            return r[item]

    def __setup_styles(self):
        # custom ttk styles
        style = ttk.Style(self.master)
        style.configure("BW.TLabel", foreground="black", background="white")
        arrow_layout = lambda dir: (
            [('Button.focus', {'children': [('Button.%sarrow' % dir, None)]})]
        )
        style.layout('L.TButton', arrow_layout('left'))
        style.layout('R.TButton', arrow_layout('right'))

    def __place_widgets(self):
        # header frame and its widgets
        hframe = ttk.Frame(self)
        #hframe.Style(foreground="pink", background="purple")
        lbtn = ttk.Button(hframe, style='L.TButton', command=self._prev_month)
        rbtn = ttk.Button(hframe, style='R.TButton', command=self._next_month)
        self._header = ttk.Label(hframe, width=15, anchor='center')
        # the calendar
        self._calendar = ttk.Treeview(show='', selectmode='none', height=10)

        # pack the widgets
        hframe.pack(in_=self, side='top', pady=4, anchor='center')
        lbtn.grid(in_=hframe)
        self._header.grid(in_=hframe, column=1, row=0, padx=12)
        rbtn.grid(in_=hframe, column=2, row=0)
        self._calendar.pack(in_=self, expand=1, fill='both', side='bottom')

    def __config_calendar(self):
        cols = self._cal.formatweekheader(3).split()
        self._calendar['columns'] = cols
        self._calendar.tag_configure('header', background='violet')
        self._calendar.insert('', 'end', values=cols, tag='header')
        # adjust its columns width
        font = tkFont.Font(family='Helvetica',size=30, weight='bold', slant='italic')
        maxwidth = max(font.measure(col) for col in cols)
        for col in cols:
            self._calendar.column(col, width=maxwidth, minwidth=maxwidth,
                anchor='e')

    def __setup_selection(self, sel_bg, sel_fg):
        self._font = tkFont.Font(family='Helvetica',size=30, weight='bold', slant='italic')
        self._canvas = canvas = Tkinter.Canvas(self._calendar,
            background=sel_bg, borderwidth=5, highlightthickness=0)
        canvas.text = canvas.create_text(0, 0, fill=sel_fg, anchor='w')
        

        canvas.bind('<ButtonPress-1>', lambda evt: canvas.place_forget())
        self._calendar.bind('<Configure>', lambda evt: canvas.place_forget())
        self._calendar.bind('<ButtonPress-1>', self._pressed)

    def __minsize(self, evt):
        width, height = self._calendar.master.geometry().split('x')
        height = height[:height.index('+')]
        self._calendar.master.minsize(width, height)

    def _build_calendar(self):
        year, month = self._date.year, self._date.month

        # update header text (Month, YEAR)
        header = self._cal.formatmonthname(year, month, 0)
        self._header['text'] = header.title()

        # update calendar shown dates
        cal = self._cal.monthdayscalendar(year, month)
        for indx, item in enumerate(self._items):
            week = cal[indx] if indx < len(cal) else []
            fmt_week = [('%02d' % day) if day else '' for day in week]
            self._calendar.item(item, values=fmt_week)

    def _show_selection(self, text, bbox):
        """Configure canvas for a new selection."""
        x, y, width, height = bbox

        textw = self._font.measure(text)

        canvas = self._canvas
        canvas.configure(width=width, height=height)
        canvas.coords(canvas.text, width - textw, height / 2 - 1)
        canvas.itemconfigure(canvas.text, text=text)
        canvas.place(in_=self._calendar, x=x, y=y)

    # Callbacks

    def _pressed(self, evt):
        """Clicked somewhere in the calendar."""
        x, y, widget = evt.x, evt.y, evt.widget
        item = widget.identify_row(y)
        column = widget.identify_column(x)

        if not column or not item in self._items:
            # clicked in the weekdays row or just outside the columns
            return

        item_values = widget.item(item)['values']
        if not len(item_values): # row is empty for this month
            return

        text = item_values[int(column[1]) - 1]
        if not text: # date is empty
            return

        bbox = widget.bbox(item, column)
        if not bbox: # calendar not visible yet
            return

        # update and then show selection
        text = '%02d' % text
        self._selection = (text, item, column)
        self._show_selection(text, bbox)

    def _prev_month(self):
        """Updated calendar to show the previous month."""
        self._canvas.place_forget()

        self._date = self._date - self.timedelta(days=1)
        self._date = self.datetime(self._date.year, self._date.month, 1)
        self._build_calendar() # reconstuct calendar

    def _next_month(self):
        """Update calendar to show the next month."""
        self._canvas.place_forget()

        year, month = self._date.year, self._date.month
        self._date = self._date + self.timedelta(
            days=calendar.monthrange(year, month)[1] + 1)
        self._date = self.datetime(self._date.year, self._date.month, 1)
        self._build_calendar() # reconstruct calendar

    # Properties

    @property
    def selection(self):
        """Return a datetime representing the current selected date."""
        if not self._selection:
            return None
        

        year, month = self._date.year, self._date.month
        return self.datetime(year, month, int(self._selection[0]))
        

    
        



def test():
    import sys
    #global userWnd
    #userWnd.destroy()
    root = Tk()
    root.title('Handy Calendar')
    #root.configure(background="grey")
    background=ImageTk.PhotoImage(Image.open("backgroundtd.jpg"))
    background_label=Tkinter.Label(root,image=background)
    background_label.pack()
    background_label.place(x=0,y=0)
    
    ttkcal = Calendar(root,firstweekday=calendar.SUNDAY)
    ttkcal.pack(expand=1, fill='both')

    if 'win' not in sys.platform:
        style = ttk.Style()
        style.theme_use('clam')

    root.mainloop()

##    wndSelection=Tkinter.Tk()
##    wndSelection.title("You selected")
##    labelSelection=Tkinter.Label(text="You selected"+ttkcal.selection)

    #wndSelection.mainloop()
def CalendarWnd(userWnd):
    userWnd.destroy()
    #lambda:test(userWnd)
    test()
    
##    if __name__ == '__main__':
##        test()
    
#functions associated with to-do list

def butnA():
    global txt1
    r = sr.Recognizer()
    with sr.Microphone() as source:
        wndSay1=Tk()
        wndSay1.geometry("400x100")
        wndSay1.configure(background='pink')
        wndSay1.title("Shopping")
        fontYes = tkFont.Font(family='Helvetica',size=13, weight='bold')
        labelSay1=Label(wndSay1,text="Please say something",foreground='purple',background='pink',font=fontYes)
        labelSay1.pack()
        labelSay1.place(x=120,y=3)
        
        #print("Say something!")
        audio = r.listen(source)
        wndSay1.destroy()
        wndProcess1=Tk()
        wndProcess1.geometry("400x100")
        wndProcess1.configure(background='pink')
        wndProcess1.title("Shopping")
        fontYes = tkFont.Font(family='Helvetica',size=13, weight='bold')
        labelProcess1=Label(wndProcess1,text="Processing",foreground='purple',background='pink',font=fontYes)
        labelProcess1.pack()
        labelProcess1.place(x=120,y=3)
        
##        wndAudio1=Tk()
##        wndAudio1.geometry("400x100")
##        wndAudio1.configure(background='pink')
##        wndAudio1.title("Shopping")
##        fontYes = tkFont.Font(family='Helvetica',size=13, weight='bold')
##        labelAudio1=Label(wndAudio1,text="What do you have to buy?",foreground='purple',background='pink',font=fontYes)
##        labelAudio1.pack()
##        labelAudio1.place(x=120,y=3)


    #print "hmm.. I wonder what you said"
    # recognize speech using Google Speech Recognition
    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        txt1.insert(END, r.recognize_google(audio))
        txt1.configure(state=DISABLED)
    except sr.UnknownValueError:
        wndProcess1.destroy()
        wndAudio1=Tk()
        wndAudio1.geometry("400x100")
        wndAudio1.configure(background='pink')
        wndAudio1.title("Shopping")
        fontYes = tkFont.Font(family='Helvetica',size=13, weight='bold')
        labelAudio1=Label(wndAudio1,text="Could not understand audio",foreground='purple',background='pink',font=fontYes)
        labelAudio1.pack()
        labelAudio1.place(x=120,y=3)
        #print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

def blah():
    pass

def URGENT():
    pass 
def butnS1Yes(wndSave1):
    #global wnd
    #global txt1
    txt1.configure(state=DISABLED)
    #changing button "save" to "SAVED :)"
    btnSaved1=Button(wnd,text="Saved :)",background='purple',foreground='pink',command=blah)#remove the command
    fontYes = tkFont.Font(family='Helvetica',size=13, weight='bold')
    btnSaved1.configure(width=10,height=1,font=fontYes, relief=RAISED)
    btnSaved1.pack()
    btnSaved1.place(x=700,y=360)

    wndSave1.destroy()

def butnS1No(wndSave1):
    wndSave1.destroy()
def butnS2Yes(wndSave2):
    global wnd #################
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
    #global wnd3
    global wnd
    #global bullet_label
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
    wndU1.destroy()
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
    global txt1
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

      
           
        


   
      
           



def ToDo(userWnd):
    #global wndUser
    #global bullet_label
    userWnd.destroy()
    
    #wnd=Toplevel()
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
    btn1=Button(wnd,relief=RIDGE, text='Save?',width=4,height=1, background='purple',foreground='pink',command=save1)
    btn1.configure(width=10,height=1,font=fontYes, relief=RAISED)
    btn1.pack()
    btn1.place(x=700,y=360)

    #button URGENT
    btnU=Button(wnd,text="Urgent?",background='purple',foreground='pink',command=butn1U)
    fontYes = tkFont.Font(family='Helvetica',size=13, weight='bold')
    btnU.configure(width=10,height=1,font=fontYes, relief=RAISED)
    btnU.pack()
    btnU.place(x=800,y=360)

    #creating button for audio
    btnA=Button(wnd,text="Speak",background='purple',foreground='pink',command=butnA)
    fontYes = tkFont.Font(family='Helvetica',size=13, weight='bold')
    btnA.configure(width=10,height=1,font=fontYes, relief=RAISED)
    btnA.pack()
    btnA.place(x=900,y=360)
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
    btn2=Button(wnd,relief=RIDGE, text='Save?',width=4,height=1, background='purple',foreground='pink',command=save2)
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
    btn3=Button(wnd,relief=RIDGE, text='Save?',width=4,height=1, background='purple',foreground='pink',command=save3)
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
    btn4=Button(wnd,relief=RIDGE, text='Save?',width=4,height=1, background='purple',foreground='pink',command=save2)
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
    btn5=Button(wnd,relief=RIDGE, text='Save?',width=4,height=1, background='purple',foreground='pink',command=save2)
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
    btn6=Button(wnd,relief=RIDGE, text='Save?',width=4,height=1, background='purple',foreground='pink',command=save2)
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
    btn7=Button(wnd,relief=RIDGE, text='Save?',width=4,height=1, background='purple',foreground='pink',command=save2)
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

    

def pics(userWnd,bgUser,btnUserTDpic,btnUserCalpic,btnUserDiapic,btnUserCalepic):
    #global userWnd
    #global bgUser
    #global btnUserTDpic
    #global btnUserCalpic
    #global btnUserDiapic
    #global btnUserCalepic
    
    #global wnd
    lstOfImages=["bgUser1.jpg","bgUser2.gif","bgUser3.jpg","bgUser4.jpg","bgUser5.jpg","bgUser6.jpg","bgUser7.jpg","bgUser8.jpg","bgUser9.jpg","bgUser10.jpg"]
    bgUser=ImageTk.PhotoImage(Image.open(random.choice(lstOfImages)))
    bgUser_label=Label(userWnd,image=bgUser)
    bgUser_label.pack()
    bgUser_label.place(x=0,y=0)

    #putting picture of td before the td button
    #btnUserTDpic=ImageTk.PhotoImage(Image.open("logo.png"))
    btnUserTDpic_label=Label(userWnd,image=btnUserTDpic)
    btnUserTDpic_label.pack()
    btnUserTDpic_label.place(x=30,y=200)

    #creating td button
    helv20 = tkFont.Font(family='Helvetica',size=20, weight='bold', slant='italic')

    btnTD=Button(text="To-Do List",relief=RAISED,font=helv20,width=20,height=2,state=NORMAL, background='pink', foreground='purple',command=lambda:ToDo(userWnd))
    btnTD.pack()
    btnTD.place(x=200,y=200)
    #userWnd.after(2000,pics)
##
##    #putting picture of calculator before cal button
##
##    #btnUserCalpic=ImageTk.PhotoImage(Image.open("calcUser.jpg"))
##    btnUserCalpic_label=Label(userWnd,image=btnUserCalpic)
##    btnUserCalpic_label.pack()
##    btnUserCalpic_label.place(x=30,y=300)
##
##    #creating calculator button
##
##    btnC=Button(text="Calculator",relief=RAISED,font=helv20,width=20,height=2,state=NORMAL, background='pink', foreground='purple')
##    btnC.pack()
##    btnC.place(x=200,y=300)

    #putting picture of diary before diary button

    #btnUserDiapic=ImageTk.PhotoImage(Image.open("diaryUser.jpg"))
    btnUserDiapic_label=Label(userWnd,image=btnUserDiapic)
    btnUserDiapic_label.pack()
    btnUserDiapic_label.place(x=30,y=300)

    #creating diary button

    btnC=Button(text="Diary",relief=RAISED,font=helv20,width=20,height=2,state=NORMAL, background='pink', foreground='purple',command=lambda:diary7.diary_create(userWnd))
    btnC.pack()
    btnC.place(x=200,y=300)

    #putting picture of calendar before calendar button

    #btnUserCalepic=ImageTk.PhotoImage(Image.open("calendar.jpg"))
    btnUserCalepic_label=Label(userWnd,image=btnUserCalepic)
    btnUserCalepic_label.pack()
    btnUserCalepic_label.place(x=30,y=400)

    #creating calendar button

    btnC=Button(text="Mini Calendar",relief=RAISED,font=helv20,width=20,height=2,state=NORMAL, background='pink', foreground='purple')
    btnC.pack()
    btnC.place(x=200,y=400)

    


    userWnd.after(3000,lambda:pics(userWnd,bgUser,btnUserTDpic,btnUserCalpic,btnUserDiapic,btnUserCalepic))

    




def recreateWnd(DiaryWnd):
    DiaryWnd.destroy()
    userWnd=Tk() #creating the window
    userWnd.title("Handy App welcomes you :)")
    userWnd.geometry("1100x600")
    lstOfImages=["bgUser1.jpg","bgUser2.gif","bgUser3.jpg","bgUser4.jpg","bgUser5.jpg","bgUser6.jpg","bgUser7.jpg","bgUser8.jpg","bgUser9.jpg","bgUser10.jpg"]
    bgUser=ImageTk.PhotoImage(Image.open(random.choice(lstOfImages)))
    bgUser_label=Label(userWnd,image=bgUser)
    bgUser_label.pack()
    bgUser_label.place(x=0,y=0)

    #putting picture of td before the td button
    btnUserTDpic=ImageTk.PhotoImage(Image.open("logo.png"))
    btnUserTDpic_label=Label(userWnd,image=btnUserTDpic)
    btnUserTDpic_label.pack()
    btnUserTDpic_label.place(x=30,y=200)



    #creating td button
    helv20 = tkFont.Font(family='Helvetica',size=20, weight='bold', slant='italic')

    btnTD=Button(text="To-Do List",relief=RAISED,font=helv20,width=20,height=2,state=NORMAL, background='pink', foreground='purple',command=lambda:ToDo(userWnd))
    btnTD.pack()
    btnTD.place(x=200,y=200)
    #userWnd.after(2000,pics)  #####HERE

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

    #putting picture of diary before diary button

    btnUserDiapic=ImageTk.PhotoImage(Image.open("diaryUser.jpg"))
    btnUserDiapic_label=Label(userWnd,image=btnUserDiapic)
    btnUserDiapic_label.pack()
    btnUserDiapic_label.place(x=30,y=300)

    #creating diary button

    btnC=Button(text="Diary",relief=RAISED,font=helv20,width=20,height=2,state=NORMAL, background='pink', foreground='purple',command=lambda:diary7.diary_create(userWnd))
    btnC.pack()
    btnC.place(x=200,y=300)

    #putting picture of calendar before calendar button

    btnUserCalepic=ImageTk.PhotoImage(Image.open("calendar.jpg"))
    btnUserCalepic_label=Label(userWnd,image=btnUserCalepic)
    btnUserCalepic_label.pack()
    btnUserCalepic_label.place(x=30,y=400)

    #creating calendar button

    btnC=Button(text="Mini Calendar",relief=RAISED,font=helv20,width=20,height=2,state=NORMAL, background='pink', foreground='purple',command=lambda:CalendarWnd(userWnd))
    btnC.pack()
    btnC.place(x=200,y=400)

    wnd=0
    bullet_label=0
    txt1=0










    userWnd.after(2000,lambda:pics(userWnd,bgUser,btnUserTDpic,btnUserCalpic,btnUserDiapic,btnUserCalepic))


    userWnd.mainloop()
