from tkinter import *
import tkinter as tk
from PIL import Image
from PIL import ImageTk
from PIL import ImageEnhance
from tkinter import filedialog
import cv2
import numpy as np
#from filedialog import askopenfilename,asksaveasfilename
from PIL import Image, ImageTk, ImageFilter, ImageEnhance, ImageOps
from PIL.ImageFilter import (
   BLUR, CONTOUR, DETAIL, EDGE_ENHANCE, EDGE_ENHANCE_MORE,
   EMBOSS, FIND_EDGES, SMOOTH, SMOOTH_MORE, SHARPEN
)


fw=Tk()
fw.title("Photo Editor")
canvas=Canvas(fw,width=600,height=400)
canvas.pack()


img=ImageTk.PhotoImage(Image.open("DIVAlogo.jpg"))
canvas.create_image(20,20,anchor=NW,image=img)

def  openButton_callback():
  
    root=Toplevel()
    root.geometry("600x550")
    root.title("Photo Editor")
    #top frame
    topframe=Frame(root,bg="gray",width=600,height=40).pack(side=TOP)
    #left frame 
    leftframe=Frame(root,bg="gray",width=100,height=500).pack(side=LEFT)

    def dispayImage(displayImage):
        ImagetoDisplay = displayImage.resize((400,400), Image.ANTIALIAS)
        ImagetoDisplay = ImageTk.PhotoImage(ImagetoDisplay)
        showWindow.config(image=ImagetoDisplay)
        showWindow.photo_ref = ImagetoDisplay
        showWindow.pack

    def newButton_callback():
        global originalImage
        filename = filedialog.askopenfilename()
        originalImage =Image.open(filename)
        dispayImage(originalImage)

    def saveasButton_callback():
        savefile = filedialog.asksaveasfile(defaultextension=".jpg")
        outputImage.save(savefile)

    def brightnessButton_callback():
        brightWindow=Tk()
        brightWindow.geometry("230x50")
        brightWindow.title("Brightness")

        def brightness_callback(brightness_pos):
            brightness_pos = float(brightness_pos)
            print(brightness_pos)
            global outputImage
            enhancer = ImageEnhance.Brightness(originalImage)
            outputImage = enhancer.enhance(brightness_pos)
            dispayImage(outputImage)

        brightScale=tk.Scale(brightWindow, from_=0, to=2, orient=tk.HORIZONTAL, length=200,
                            resolution=0.1, command=brightness_callback)
        brightScale.set(1)
        brightScale.pack()

    def contrastButton_callback():
        contrastWindow=Tk()
        contrastWindow.geometry("230x50")
        contrastWindow.title("Contrast")

        def contrast_callback( contrast_pos):
            contrast_pos = float( contrast_pos)
            print(contrast_pos)
            global outputImage
            enhancer = ImageEnhance.Brightness(originalImage)
            outputImage = enhancer.enhance( contrast_pos)
            dispayImage(outputImage)

        contrastScale=tk.Scale(contrastWindow, from_=0, to=2, orient=tk.HORIZONTAL, length=200,
                            resolution=0.1, command=contrast_callback)
        contrastScale.set(1)
        contrastScale.pack()

    def flipButton_callback():
        #img_flipped = np.flip(originalImage, axis=1)
        global outputImage
        outputImage= ImageOps.flip(originalImage)
        #outputImage = Image.fromarray(img_flipped)
        dispayImage(outputImage)

    def mirrorButton_callback():
        global outputImage
        outputImage=ImageOps.mirror(originalImage)
        dispayImage(outputImage)

    def rotateButton_callback():
        global outputImage
        #outputImage= originalImage.rotate(45)
        #Image.ROTATE_90, Image.ROTATE_180 and Image.ROTATE_270.
        outputImage= originalImage.transpose(Image.ROTATE_90)
        dispayImage(outputImage)

    def redButton_callback():#blue
        opencvImage = cv2.cvtColor(np.array(originalImage), cv2.COLOR_RGB2BGR)
        opencvImage[:, :, 0] = 10
        global outputImage
        outputImage = Image.fromarray(cv2.cvtColor(opencvImage, cv2.COLOR_BGR2RGB))
        dispayImage(outputImage)

    def yellowButton_callback():
        opencvImage = cv2.cvtColor(np.array(originalImage), cv2.COLOR_RGB2BGR)
        opencvImage[:, :, 0] = 20
        global outputImage
        outputImage = Image.fromarray(cv2.cvtColor(opencvImage, cv2.COLOR_BGR2RGB))
        dispayImage(outputImage)

    def blueButton_callback():#lightblue
        opencvImage = cv2.cvtColor(np.array(originalImage), cv2.COLOR_RGB2BGR)
        opencvImage[:, :, 2] = 20
        global outputImage
        outputImage = Image.fromarray(cv2.cvtColor(opencvImage, cv2.COLOR_BGR2RGB))
        dispayImage(outputImage)

    def orangeButton_callback():
        opencvImage = cv2.cvtColor(np.array(originalImage), cv2.COLOR_RGB2BGR)
        opencvImage[:, :, 2] = 200
        global outputImage
        outputImage = Image.fromarray(cv2.cvtColor(opencvImage, cv2.COLOR_BGR2RGB))
        dispayImage(outputImage)

    def pinkButton_callback():## pink
        opencvImage = cv2.cvtColor(np.array(originalImage), cv2.COLOR_RGB2BGR)
        opencvImage[:, :, 1] = 20
        global outputImage
        outputImage = Image.fromarray(cv2.cvtColor(opencvImage, cv2.COLOR_BGR2RGB))
        dispayImage(outputImage)

    def greenButton_callback():## green
        opencvImage = cv2.cvtColor(np.array(originalImage), cv2.COLOR_RGB2BGR)
        opencvImage[:, :, 1] = 1000
        global outputImage
        outputImage = Image.fromarray(cv2.cvtColor(opencvImage, cv2.COLOR_BGR2RGB))
        dispayImage(outputImage)

    def FIND_EDGESButton_callback():
        global outputImage
        outputImage=originalImage.filter(FIND_EDGES)
        dispayImage(outputImage)

    def SHARPENButton_callback():
        global outputImage
        outputImage=originalImage.filter(SHARPEN)
        dispayImage(outputImage)

    def CONTOURButton_callback():
        global outputImage
        outputImage=originalImage.filter(CONTOUR)
        dispayImage(outputImage)

    def SMOOTH_MOREButton_callback():
        global outputImage
        outputImage=originalImage.filter(SMOOTH_MORE)
        dispayImage(outputImage)
    
    def EMBOSSButton_callback():
        global outputImage
        outputImage=originalImage.filter(EMBOSS)
        dispayImage(outputImage)

    def DETAILButton_callback():
        global outputImage
        outputImage=originalImage.filter(DETAIL)
        dispayImage(outputImage)
    

    def medianBlurButton_callback():
        global outputImage
        outputImage=originalImage.filter(ImageFilter.MinFilter(3))
        dispayImage(outputImage)#boxImage = OriImage.filter(ImageFilter.BoxBlur(5))

    def redborder_callback():
        global outputImage
        color = "red"
        # top, right, bottom, left
        border = (20, 10, 20, 10)
        outputImage = ImageOps.expand(originalImage, border=border, fill=color)
        dispayImage(outputImage)

    def yellowborder_callback():
        global outputImage
        color = "yellow"
        # top, right, bottom, left
        border = (20, 10, 20, 10)
        outputImage = ImageOps.expand(originalImage, border=border, fill=color)
        dispayImage(outputImage)
    
    def greenborder_callback():
        global outputImage
        color = "green"
        # top, right, bottom, left
        border = (20, 10, 20, 10)
        outputImage = ImageOps.expand(originalImage, border=border, fill=color)
        dispayImage(outputImage)
    
    def orangeborder_callback():
        global outputImage
        color = "orange"
        # top, right, bottom, left
        border = (20, 10, 20, 10)
        outputImage = ImageOps.expand(originalImage, border=border, fill=color)
        dispayImage(outputImage)
    
    def pinkborder_callback():
        global outputImage
        color = "pink"
        # top, right, bottom, left
        border = (20, 10, 20, 10)
        outputImage = ImageOps.expand(originalImage, border=border, fill=color)
        dispayImage(outputImage)
    
    def blueborder_callback():
        global outputImage
        color = "blue"
        # top, right, bottom, left
        border = (20, 10, 20, 10)
        outputImage = ImageOps.expand(originalImage, border=border, fill=color)
        dispayImage(outputImage)
    
    def purpleborder_callback():
        global outputImage
        color = "purple"
        # top, right, bottom, left
        border = (20, 10, 20, 10)
        outputImage = ImageOps.expand(originalImage, border=border, fill=color)
        dispayImage(outputImage)
    
    def whiteborder_callback():
        global outputImage
        color = "white"
        # top, right, bottom, left
        border = (20, 10, 20, 10)
        outputImage = ImageOps.expand(originalImage, border=border, fill=color)
        dispayImage(outputImage)
    
    def blackborder_callback():
        global outputImage
        color = "black"
        # top, right, bottom, left
        border = (20, 10, 20, 10)
        outputImage = ImageOps.expand(originalImage, border=border, fill=color)
        dispayImage(outputImage)
    
    def blackandwhiteButton_callback():
        global outputImage
        outputImage = originalImage.convert("L")
        dispayImage(outputImage)
    
    def blackandwhiteButton2_callback():
        global outputImage
        outputImage=originalImage.convert("1")
        dispayImage(outputImage)
    
    def blurButton_callback():
        global outputImage
        outputImage=originalImage.filter(ImageFilter.BLUR)
        dispayImage(outputImage)#boxImage = OriImage.filter(ImageFilter.BoxBlur(5))
    
    def exitButton_callback():
        root.destroy()
        fw.destroy()


    ############### Top Frame ###################
    #new button
    new_button=Button(root,text="New",command=newButton_callback, width=7,height=1).place(x=15,y=10)
    #save as button
    save_as_button=Button(root,text="Save as",command=saveasButton_callback, width=7,height=1).place(x=100,y=10)  
    #Add color Button
    mb=Menubutton(root,text="Add color", width=9,height=1)
    mb.place(x=200,y=10) #position  
    mb.menu=Menu(mb) # sub-menu
    mb["menu"]=mb.menu # tempr
    option1=IntVar() # check 1
    option2=IntVar() 
    option3=IntVar() 
    option4=IntVar() 
    option5=IntVar() 
    option6=IntVar()
    #mb.menu.add_checkbutton(label="Red",variable=option1,command=redButton_callback) # chk btn1
    mb.menu.add_checkbutton(label="Yellow",variable=option2,command=yellowButton_callback) 
    mb.menu.add_checkbutton(label="Green",variable=option3,command=greenButton_callback) 
    mb.menu.add_checkbutton(label="Orange",variable=option4,command=orangeButton_callback) 
    mb.menu.add_checkbutton(label="Pink",variable=option5,command=pinkButton_callback) 
    mb.menu.add_checkbutton(label="Blue",variable=option6,command=blueButton_callback) 
    
    #add filters
    Mb=Menubutton(root,text="Add Filter",width=9,height=1)
    Mb.place(x=300,y=10) #position
    Mb.menu=Menu(Mb) # sub-menu
    Mb["menu"]=Mb.menu # tempr
    option1=IntVar() # check 1
    option2=IntVar() 
    option3=IntVar() 
    option4=IntVar() 
    option5=IntVar() 
    option6=IntVar()
    option7=IntVar()
    option8=IntVar()
    option9=IntVar()
    Mb.menu.add_checkbutton(label="FIND_EDGES",variable=option1,command=FIND_EDGESButton_callback) # chk btn1
    Mb.menu.add_checkbutton(label="SHARPEN",variable=option2,command=SHARPENButton_callback) 
    Mb.menu.add_checkbutton(label="CONTOUR",variable=option3,command=CONTOURButton_callback) 
    Mb.menu.add_checkbutton(label="SMOOTH_MORE",variable=option4,command=SMOOTH_MOREButton_callback)   
    Mb.menu.add_checkbutton(label="DETAIl",variable=option5,command= DETAILButton_callback)   
    Mb.menu.add_checkbutton(label="EMBOSS",variable=option6,command=EMBOSSButton_callback) 
    Mb.menu.add_checkbutton(label="MedianBlur",variable=option7,command=medianBlurButton_callback) 
    Mb.menu.add_checkbutton(label="Black And White",variable=option8,command=blackandwhiteButton_callback)
    Mb.menu.add_checkbutton(label="Black And White(1-bit)",variable=option9,command=blackandwhiteButton2_callback) 

    
    #add border  Button
    menubar=Menubutton(root,text="Border",width=9,height=1) 
    menubar.place(x=400,y=10) #position
    menubar.menu=Menu(menubar) # sub-menu
    menubar["menu"]=menubar.menu # tempr
    option1=IntVar() # check 1
    option2=IntVar() 
    option3=IntVar() 
    option4=IntVar() 
    option5=IntVar() 
    option6=IntVar()
    option7=IntVar()
    option8=IntVar()
    option9=IntVar()
    menubar.menu.add_checkbutton(label="Red",variable=option1,command=redborder_callback) # chk btn1
    menubar.menu.add_checkbutton(label="Yellow",variable=option2,command=yellowborder_callback)  
    menubar.menu.add_checkbutton(label="Green",variable=option3,command=greenborder_callback) 
    menubar.menu.add_checkbutton(label="orange",variable=option4,command=orangeborder_callback) 
    menubar.menu.add_checkbutton(label="Pink",variable=option5,command=pinkborder_callback) 
    menubar.menu.add_checkbutton(label="Blue",variable=option6,command=blueborder_callback) 
    menubar.menu.add_checkbutton(label="Purple",variable=option7,command=purpleborder_callback) 
    menubar.menu.add_checkbutton(label="White",variable=option8,command=whiteborder_callback) 
    menubar.menu.add_checkbutton(label="Black",variable=option9,command=blackborder_callback) 

    #Exit button
    exit_button=Button(root,text="Exit",command=exitButton_callback,width=7,height=1).place(x=500,y=10)  

    ############### Left Frame ###################  
    #brightness button
    brightness_button=Button(root,text="Brightness" ,command=brightnessButton_callback,background="white", width=10,height=2).place(x=10,y=50)
    #contrast button
    contrast_button=Button(root,text="Contrast",command=contrastButton_callback,background="white", width=10,height=2).place(x=10,y=100) 
    #flip Button
    flip_button=Button(root,text="Flip",command=flipButton_callback,background="white", width=10,height=2).place(x=10,y=150)
    #mirror Button
    mirror_button=Button(root,text="Mirror",command=mirrorButton_callback,background="white", width=10,height=2).place(x=10,y=200)
    #rotate Button
    rotate_button=Button(root,text="Rotate",command=rotateButton_callback,background="white", width=10,height=2).place(x=10,y=250)
    #blur Button
    blur_button=Button(root,text="Blur",command=blurButton_callback,background="white", width=10,height=2).place(x=10,y=300)
    
   
    showWindow = Label(root)
    showWindow.place(x=101,y=50)
    root.mainloop()

 
  

open_Button=Button(fw,text="Next", bd=5,font=("Times New Roman", 15, "bold"),command=openButton_callback).pack(side=BOTTOM)

fw.mainloop()
