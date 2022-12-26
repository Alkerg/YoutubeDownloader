from pytube import YouTube
import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.title("YoutubeDownloader")
root.geometry("700x350")

foldervar = str
linkvar = customtkinter.StringVar()
path = customtkinter.StringVar()

def download():
    link = linkvar.get()
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download(foldervar)
    except:
        print("There has been an error downloading this video")
    print("Download completed")

def select_folder():
    global foldervar
    folder = customtkinter.filedialog.askdirectory()
    foldervar = folder
    root.focus()

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20,padx=60,fill="both",expand=True)

label = customtkinter.CTkLabel(master=frame,text="YoutubeDownloader")
label.pack(pady=6,padx=12,fill="both")

entry = customtkinter.CTkEntry(master=frame,placeholder_text="Link",width=800,textvariable=linkvar)
entry.pack(pady=12,padx=10)

open_folder = customtkinter.CTkButton(frame,text="Open folder",command=select_folder)
open_folder.pack()

download_button = customtkinter.CTkButton(frame,text="Download",command=download,fg_color="#27AE60",hover_color="#229954")
download_button.pack(pady=12)

root.mainloop()