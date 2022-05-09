from encodings import utf_8
from fileinput import filename
from fileinput import *
import PIL.Image
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
filenamo = "pas"
def browseFiles():
    global filenamo
    filenamo = filedialog.askopenfilename(initialdir = "/",
                                          title = "Select a File",
                                          filetypes = (("Photos",
                                                        "*.jpg*"),
                                                        ("Photos",
                                                        "*.png*"),
                                                       ("all files",
                                                        "*.*")))
    label.configure(text="Choosed file : "+filenamo)

def sortie():
    global repertoire
    repertoire = filedialog.askdirectory(title = "Select an output directory" , mustexist = True )

def action():
    tab_mona=PIL.Image.open(filenamo)
    taille=tab_mona.size
    canva=PIL.Image.new("RGB", (taille[0],taille[1]), "white")
    quotient = 0
    sortie()
    output_name = repertoire+"/"+(str(text.get(1.0, 'end-1c')))
    print(output_name)
    elfichier = value.get()
    choisi(elfichier,tab_mona,canva,output_name,taille)

fenetre = Tk()
fenetre.geometry("500x500")
fenetre.title("Photo Color Changer v.1.42")
label = Label(fenetre, text="Choose the input picture")
label.place(relx=0.5, rely=0, anchor=N)
button_explore = Button(fenetre,
                        text = "Browse files",
                        command = browseFiles)
button_explore.place(relx=0.5, rely=0.05, anchor=N)
labeldest = Label(fenetre, text="Choose the name of the output file (include the extension!) :")
labeldest.place(relx=0.5, rely=0.45, anchor=N)
text = Text(fenetre,height=3,width=40)
text.place(relx=0.5, rely=0.5, anchor=N)

button_launch = Button(fenetre,
                        text = "Start !",
                        command = action)
button_launch.place(relx=0.5, rely=0.6, anchor=N)

value = StringVar() 
bouton1 = Radiobutton(fenetre, text="Red Effect", variable=value, value=1)
bouton2 = Radiobutton(fenetre, text="Invert Colors", variable=value, value=2)
bouton3 = Radiobutton(fenetre, text="Shadows Boost", variable=value, value=3)
bouton4 = Radiobutton(fenetre, text="Pointillism", variable=value, value=4)
bouton5 = Radiobutton(fenetre, text="Greyscale", variable=value, value=5)
bouton6 = Radiobutton(fenetre, text="Green Effect", variable=value, value=6)
bouton7 = Radiobutton(fenetre, text="Blue Effect", variable=value, value=7)

bouton1.place(relx=0.5, rely=0.1, anchor=N)
bouton2.place(relx=0.5, rely=0.15, anchor=N)
bouton3.place(relx=0.5, rely=0.2, anchor=N)
bouton4.place(relx=0.5, rely=0.25, anchor=N)
bouton5.place(relx=0.5, rely=0.3, anchor=N)
bouton6.place(relx=0.5, rely=0.35, anchor=N)
bouton7.place(relx=0.5, rely=0.4, anchor=N)

def rouge(tab_mona,canva,output_name,taille):
    print(output_name)
    for x in range(0,taille[0],1):
        for y in range(0,taille[1],1):
            quotient = tab_mona.getpixel((x,y))
            canva.putpixel((x,y),((quotient[0]+50),quotient[1],quotient[2]))
    canva.save(output_name)
    messagebox.showinfo("Success !", "Your picture was successfully exported!")
    print("Fait, sauvegardé dans ",output_name)

def vert(tab_mona,canva,output_name,taille):
    print(output_name)
    for x in range(0,taille[0],1):
        for y in range(0,taille[1],1):
            quotient = tab_mona.getpixel((x,y))
            canva.putpixel((x,y),(quotient[0],(quotient[1]+50),quotient[2]))
    canva.save(output_name)
    messagebox.showinfo("Success !", "Your picture was successfully exported!")
    print("Fait, sauvegardé dans ",output_name)

def bleu(tab_mona,canva,output_name,taille):
    print(output_name)
    for x in range(0,taille[0],1):
        for y in range(0,taille[1],1):
            quotient = tab_mona.getpixel((x,y))
            canva.putpixel((x,y),(quotient[0],quotient[1],(quotient[2]+50)))
    canva.save(output_name)
    messagebox.showinfo("Success !", "Your picture was successfully exported!")
    print("Fait, sauvegardé dans ",output_name)

def invert(tab_mona,canva,output_name,taille): 
    for x in range(taille[0]):
        for y in range(taille[1]):
            quotient = tab_mona.getpixel((x,y))
            canva.putpixel((x,y),(quotient[2],quotient[1],quotient[0]))
    canva.save(output_name)
    messagebox.showinfo("Success !", "Your picture was successfully exported!")
    print("Fait, sauvegardé dans ",output_name)

def boost(tab_mona,canva,output_name,taille): 
    for x in range(taille[0]):
        for y in range(taille[1]):
            quotient = tab_mona.getpixel((x,y))
            if ((quotient[0] + quotient[1] + quotient[2]) / 3 ) < 50:
                canva.putpixel((x,y),(0,0,0))
            else:
                canva.putpixel((x,y),(quotient[0],quotient[1],quotient[2]))
    canva.save(output_name)
    messagebox.showinfo("Success !", "Your picture was successfully exported!")
    print("Fait, sauvegardé dans ",output_name)

def point(tab_mona,canva,output_name,taille): 
    for x in range(0,taille[0],2):
        for y in range(0,taille[1],2):
            quotient = tab_mona.getpixel((x,y))
            if ((quotient[0] + quotient[1] + quotient[2]) / 3 ) < 127:
                canva.putpixel((x,y),(0,0,0))
    canva.save(output_name)
    messagebox.showinfo("Success !", "Your picture was successfully exported!")
    print("Fait, sauvegardé dans ",output_name)

def grey(tab_mona,canva,output_name,taille): 
    for x in range(0,taille[0],1):
        for y in range(0,taille[1],1):
            quotient = tab_mona.getpixel((x,y))
            canva.putpixel((x,y),(int(((quotient[0] + quotient[1] + quotient[2]) / 3 )),int(((quotient[0] + quotient[1] + quotient[2]) / 3 )),int(((quotient[0] + quotient[1] + quotient[2]) / 3 ))))
    canva.save(output_name)
    messagebox.showinfo("Success !", "Your picture was successfully exported!")
    print("Fait, sauvegardé dans ",output_name)

def choisi(elfichier,tab_mona,canva,output_name,taille):
    if int(elfichier) == 1:
        rouge(tab_mona,canva,output_name,taille)
    elif int(elfichier) == 2:
        invert(tab_mona,canva,output_name,taille)
    elif int(elfichier) == 3:
        boost(tab_mona,canva,output_name,taille)
    elif int(elfichier) == 4:
        point(tab_mona,canva,output_name,taille)
    elif int(elfichier) == 5:
        grey(tab_mona,canva,output_name,taille)
    elif int(elfichier) == 6:
        vert(tab_mona,canva,output_name,taille)
    elif int(elfichier) == 7:
        bleu(tab_mona,canva,output_name,taille)

fenetre.mainloop()