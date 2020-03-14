import tkinter as tk
import tkinter.filedialog as fd
import PIL.Image
import PIL.ImageTk

def dispPhoto(path):
    newImage = PIL.Image.open(path).resize((200, 200))
    gImage = PIL.Image.open(path).convert("L").resize( (32, 32) ).resize( (300, 300) )

    # 이미지 레이블에 출력하기
    imageData = PIL.ImageTk.PhotoImage(gImage)
    imageLabel.configure(image=imageData)
    imageLabel.image = imageData

    # 파일 레이블에 경로 출력하기
    fpathLabel.configure(text=path)

def openFile():
    fpath = fd.askopenfilename()

    if fpath:
        dispPhoto(fpath)

root = tk.Tk()
root.geometry("400x350")

btn = tk.Button(text="파일열기", command=openFile)
imageLabel = tk.Label()
fpathLabel = tk.Label()
btn.pack()
imageLabel.pack()
fpathLabel.pack()
tk.mainloop()
