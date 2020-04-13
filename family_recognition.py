#importing desired modules
from tkinter import *
from tkinter import filedialog
import face_recognition
import datetime
from PIL import Image, ImageTk


#loading family pics
Alaina=face_recognition.load_image_file('Alaina_Ahuja.gif')
Ayan=face_recognition.load_image_file('Ayan_Ahuja.gif')
Gauri=face_recognition.load_image_file('Gauri_Ahuja.gif')
Yogi=face_recognition.load_image_file('Yogi_Ahuja.gif')

#creating family encodings
Alaina_encodings=face_recognition.face_encodings(Alaina)[0]
Ayan_encodings=face_recognition.face_encodings(Ayan)[0]
Gauri_encodings=face_recognition.face_encodings(Gauri)[0]
Yogi_encodings=face_recognition.face_encodings(Yogi)[0]

#creating list of family members
family_members=[
    Alaina_encodings,
    Ayan_encodings,
    Gauri_encodings,
    Yogi_encodings
]
#function to browse for files
def browse():
    global fileVarPIC
    fileVarPIC=filedialog.askopenfilename( filetypes=(("Alaina's stuff",".gif"),("All files","*.*")))
    
    global enc1
    enc1=pictureDisplay(fileVarPIC,400,0)

def Check():
    a = datetime.datetime.now()
    print(a)
    choice=face_recognition.load_image_file(fileVarPIC)
    
    choice_encodings=face_recognition.face_encodings(choice)[0]
    
    result=face_recognition.compare_faces(family_members,choice_encodings,0.6)

    if True in result:
        canvas.create_text(400,400,text='this is your family member!',fill='green',font=('Helvetica',30))
    else:
        canvas.create_text(400,400,text='this is not your family member',fill='red',font=('Helvetica',30))
    
    b = datetime.datetime.now()
    delta = b - a
    print(int(delta.total_seconds() * 1000))

def clear():
    canvas.delete("all")

def pictureDisplay(fileVarPIC,x,y):
    #pic=ImageTk.PhotoImage(fileVarPIC)
    loaded_image = Image.open(fileVarPIC)
    pic=ImageTk.PhotoImage(loaded_image)
    #pic=PhotoImage(file=fileVarPIC)
    tkpic=canvas.create_image((x,y),image=pic,anchor='nw')
    label=Label()
    label.image=pic
    label.pack()


#making tkinter window
window=Tk()
window.title('family_recognition')

#creating tkinter canvas 
canvas=Canvas(window, width=1280, height=680)
canvas.pack()

#creating browsing button
browse=Button(window, text='Browse',command=browse,bg='blue')
browse.pack()

#creating check button
check=Button(window,text='Check',command=Check)
check.pack()

#creating reset button
reset=Button(window,text='Reset',command=clear)
reset.pack()



window.mainloop()