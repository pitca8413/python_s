# 자동 번호 생성기
import tkinter as tk
import random


# 번호 출력 함수 생성
def disp_num():
    nums = list(range(1, 45))
    random.shuffle(nums)
    lotto_num = nums[:6]
    lbl_num.configure(text=lotto_num)

# 창 생성
root = tk.Tk()
root.geometry("200x100")

# 레이블, 버튼 생성
lbl_num = tk.Label(text="")
btn_create = tk.Button(text="생성하기", command=disp_num)

# 화면에 배치
lbl_num.pack()
btn_create.pack()

tk.mainloop()
