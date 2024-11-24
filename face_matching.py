#importing desired modules/libraries
from tkinter import *
from tkinter import filedialog
import face_recognition



#function command for first variable; gives path for first choice
def browsingPIC1():
    fileVarPIC1=filedialog.askopenfilename( filetypes=(("Alaina's stuff",".gif"),("All files","*.*")))
    global enc1
    enc1=pictureDisplay(fileVarPIC1,0,0)
    x=enc1
    
#function command for second variable; gives path for second choice
def browsingPIC2():
    fileVarPIC2=filedialog.askopenfilename( filetypes=(("Alaina's stuff",".gif"),("All files","*.*")))
    global enc2
    enc2 = pictureDisplay(fileVarPIC2,700,0)
    y=enc2

#displaying picture; providing face encodings   
def pictureDisplay(fileVarPIC,x,y):
  
    pic=face_recognition.load_image_file(fileVarPIC)
    
    
    tkpic=PhotoImage(file=fileVarPIC)
    contestant1=canvas.create_image((x,y),image=tkpic,anchor='nw')
    
    
    label=Label()
    label.image=tkpic
    label.pack()
    
    contestant_face_encodings=face_recognition.face_encodings(pic)
    return contestant_face_encodings[0]

#comparing both choices
def compare_choices():
    result=face_recognition.compare_faces([enc1],enc2,0.5)
    if result==[True]:
        canvas.create_text(400,400,text='The images are of the same person!!!', fill='green',font=('Helvetica',30))
    else:
        canvas.create_text(400,400,text='The images are not of the same person!!!', fill='red',font=('Helvetica',30))

def clear():
    canvas.delete("all")

#customizing tkinter window
window=Tk()
window.title('face_matcher')

#creating canvas to expand window
canvas=Canvas(window,width=1280,height=680)
canvas.pack()

#creating first browse button
browse=Button(window, text='Browse',command=browsingPIC1)
browse.pack()

#creating second browse button
browse2=Button(window, text='Browse2',command=browsingPIC2)
browse2.pack()

#creating compare button
compare=Button(window, text='Compare',command=compare_choices)
compare.pack()

#reset button
reset=Button(window,text='Reset',command=clear)
reset.pack()

#creating area to display
display_area=Label(window, text="")
display_area.pack()

#creating app title
title=canvas.create_text(200,200, text='The face matcher',fill='blue',font=('Helvetica',30))

#mandatory line
window.mainloop()
    
