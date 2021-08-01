import tkinter
import pafy
from tkinter import messagebox

def empty_url_entry():
	URL_entry.delete(0, "end")
	return

def download_audio():
	url = URL_entry.get()
	try:
		audio = pafy.new(url=url)
	except ValueError:
		messagebox.showerror(title="Error", message="Bad URL!")
		return

	audio_title = url.title

	get_audio = audio.getbestaudio()
	get_audio.download()
	print("Song name: %s" % audio_title)


window = tkinter.Tk()
window.title("Youtube music downloader")
window.geometry("500x150")
window.resizable(False, False)
window.config(bg="#6cc6d3")

logo = tkinter.PhotoImage(file='icon.png')
window.call('wm', 'iconphoto', window._w, logo)

URL_entry = tkinter.Entry(bd=0, bg="#F6F7F9", highlightthickness=0, font=("Arial-BoldMT",int(12.0)))
URL_entry.place(x=50, y=20, width=400, height=35)

trash_icon = tkinter.PhotoImage(file="trash.png", height=30, width=30)

trash_button = tkinter.Button(image=trash_icon, borderwidth=0, highlightthickness=0, command=empty_url_entry, relief="flat")
trash_button.place(x=460, y=20, width=30, height=30)

button1 = tkinter.Button(text="Download", command=download_audio)
button1.place(x=20, y=70, width=80, height=50)

window.mainloop()