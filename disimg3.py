import tkinter as tk
import tkinter.filedialog as fd
import PIL.Image
import PIL.ImageTk

def disp_photo(path):
    # 이미지 불러오기
    newImage = PIL.Image.open(path)

    # 이미지 크기 계산하기
    mywidth = 300
    sizefac = mywidth / newImage.size[0]
    myheight = int(newImage.size[1] * sizefac)
    print(newImage.size)
    print(mywidth, myheight)
    newImage = newImage.resize((mywidth, myheight))

    # 이미지 라벨에 표시하기
    imageData = PIL.ImageTk.PhotoImage(newImage)
    imageLabel.configure(image=imageData)
    imageLabel.image = imageData

    imageData = PIL.ImageTk.PhotoImage(newImage.convert("L"))
    gimgLabel.configure(image=imageData)
    gimgLabel.image = imageData

def open_file():
    fpath = fd.askopenfilename()

    if fpath:
        disp_photo(fpath)

# 윈도우 창 만들기 (400x600)
root = tk.Tk()
root.geometry("400x600")

# 버튼과 이미지레이블, 흑백이미지레이블 만들기
btn = tk.Button(text="open", command=open_file)
imageLabel = tk.Label()
gimgLabel = tk.Label()

# 버튼과 이미지 화면에 출력하기
btn.pack()
imageLabel.pack()
gimgLabel.pack()

tk.mainloop()