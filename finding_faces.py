#importing desired modules/libraries
from tkinter import *
from tkinter import filedialog
import face_recognition
from PIL import Image, ImageTk

class FamilyFaces:
    
    def __init__(self,canvas,enc1,fileVarPIC,family_members):
        #loading family images
        Alaina=face_recognition.load_image_file('Alaina_Ahuja.gif')
        Ayan=face_recognition.load_image_file('Ayan_Ahuja.gif')
        Gauri=face_recognition.load_image_file('Gauri_Ahuja.gif')
        Yogi=face_recognition.load_image_file('Yogi_Ahuja.gif')

        #calculating family encodings
        Alaina_encodings=face_recognition.face_encodings(Alaina)[0]
        Ayan_encodings=face_recognition.face_encodings(Ayan)[0]
        Gauri_encodings=face_recognition.face_encodings(Gauri)[0]
        Yogi_encodings=face_recognition.face_encodings(Yogi)[0]

        #creating list of known faces
        self.family_members=[
            Alaina_encodings,
            Ayan_encodings,
            Gauri_encodings,
            Yogi_encodings
        ]
        
        #creating tkinter window
        window=Tk()
        window.title('who is family?')

        #creating tkinter canvas
        
        self.canvas=Canvas(window, width=1280,height=680)
        self.canvas.pack()
        self.enc1=None
        self.fileVarPIC=None
        #creating button to browse for pic
        browse_btn=Button(window, text='Browse',command=self.browse)
        browse_btn.pack()

        #creating button to find and analyze faces
        go_btn=Button(window,text='Go!',command=self.go)
        go_btn.pack()

        #creating button to reset board
        reset=Button(window,text='Reset',command=self.clear)
        reset.pack()

        #mandatory tkinter line
        window.mainloop()

    #function to browse for pic
    def browse(self):
        #global fileVarPIC
        self.fileVarPIC=filedialog.askopenfilename( filetypes=(("Alaina's stuff",".gif"),("All files","*.*")))
        self.enc1=self.pictureDisplay(400,0)

    #function to find and analyze faces
    def go(self):
        choice=face_recognition.load_image_file(self.fileVarPIC)
        choice_encodings=face_recognition.face_encodings(choice)
        
        lenghth=len(choice_encodings)
        counter=0
        for x in range(lenghth):
            result=face_recognition.compare_faces(self.family_members,choice_encodings[x],0.6)
            if True in result:
                counter=counter+1
        
        fraction=counter,'/',lenghth,'are family'
        final=self.canvas.create_text(400,400,text=fraction,fill='pink',font=('Helvetica',30))
            
    #function to reset board
    def clear(self):
        self.canvas.delete('all')

    #function to display images
    def pictureDisplay(self,x,y):
        loaded_image = Image.open(self.fileVarPIC)
        pic=ImageTk.PhotoImage(loaded_image)
        tkpic=self.canvas.create_image((x,y),image=pic,anchor='nw')
        label=Label()
        label.image=pic
        label.pack()

obj=FamilyFaces(None,None,None,None)
