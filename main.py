import tkinter
import pafy
from tkinter import messagebox

def empty_url_entry():
	URL_entry.delete(0, "end")

def download_audio():
	url = URL_entry.get()
	try:
		window.title("Downloader: started downloading")
		audio = pafy.new(url=url)
	except ValueError:
		messagebox.showerror(title="Error", message="Bad URL!")
		window.title("Downloader: downloading cancelled")
		return
	except KeyError:
		messagebox.showerror(title="Error", message="KeyError! Read README.md!")
		window.title("Downloader: CRITICAL ERROR! READ README.md!!!!!")

	audio_title = audio.title
	print("\nSong name: %s" % audio_title)
	
	get_audio = audio.getbestaudio()

	get_audio.download()

	messagebox.showinfo(title="Completed", message="✅Your song was downloaded! Enjoy! <3")
	window.title("Downloader: ready for downloading")


window = tkinter.Tk()
window.title("Downloader: ready for downloading")
window.geometry("500x150")
window.resizable(False, False)
window.config(bg="#6cc6d3")

logo = tkinter.PhotoImage(file='images/icon.png')
window.call('wm', 'iconphoto', window._w, logo)

URL_entry = tkinter.Entry(bd=0, bg="#F6F7F9", highlightthickness=0, font=("Arial-BoldMT",int(12.0)))
URL_entry.place(x=50, y=20, width=400, height=35)

trash_icon = tkinter.PhotoImage(file="images/trash.png", height=30, width=30)

trash_button = tkinter.Button(image=trash_icon, borderwidth=0, highlightthickness=0, command=empty_url_entry, relief="flat")
trash_button.place(x=460, y=20, width=30, height=35)

button1 = tkinter.Button(text="Download", command=download_audio)
button1.place(x=200, y=90, width=80, height=50)

window.mainloop()