import tkinter as tk
import youtube_dl as yd
from tkinter import *
from tkinter import messagebox, filedialog


def CreateWidgets():

    linkLabel= Label(root, text="ENTER THE VIDEO LINK: ", bg="#80BD9E")
    linkLabel.grid(row=1, column=0, pady=5, padx=5)

    root.linkText= Entry(root, width=60)
    root.linkText.grid(row=1, column=1, pady=5, padx=5, columnspan=2)

    destinationLabel= Label(root, text="SAVE AUDIO IN : ", bg= "#80BD9E")
    destinationLabel.grid(row=2, column=0, pady=5, padx=5)

    root.destinationText= Entry(root, width=38)
    root.destinationText.grid(row=2, column=1,pady=5, padx=5)

    browseButton= Button(root, text="BROWSE", command=Browse, width=15, bg='#F98866', fg='white')
    browseButton.grid(row=2, column=2, pady=5, padx=5)

    downloadButton = Button(root, text="DOWNLOAD AUDIO", command=Download, width=30, bg='#F98866',fg='white')
    downloadButton.grid(row=3, column=1, pady=5, padx=5)


def Browse():
    root.destinationText.delete(0,END)
    root.destinationDIR= filedialog.askdirectory(initialdir="C:/Users/300262/Desktop/")
    print(root.destinationDIR)
    root.destinationText.insert(END, root.destinationDIR)





def my_hook(d):
    if d['status'] == 'finished':
        print('Done downloading, now converting ...')
        messagebox.showinfo("Possessing","Done downloading, now converting ...")


def Download():
    try:
        videoLink = root.linkText.get()
        savePath = root.destinationText.get()
        audDWLDopt = {
            'format': 'bestaudio/best',
            'outtmpl': savePath + "/%(title)s.%(ext)s",
            'postprocessors': [{'key': 'FFmpegExtractAudio',
                                'preferredcodec': 'mp3',
                                'preferredquality': '320',
                                }],
            'progress_hooks': [my_hook],

        }
        with yd.YoutubeDL(audDWLDopt) as aud_dwld:
            aud_dwld.download([videoLink])
        messagebox.showinfo("SUCCESS", "VIDEO CONVERTED AND DOWNLOADED AS AUDIO...")
    except:
        messagebox.showwarning("Warning","Please insert a valid link")
        root.linkText.delete(0, END)
root=tk.Tk()
root.geometry('530x110')
root.title('PyYouTubeAudio')
root.resizable(False,False)
root.config(background='#80BD9E')

CreateWidgets()
root.mainloop()