# -*- coding:utf-8 -*-
import tkinter

def change_fill():

    # 現在選択されている項目のインデックスを取得
    indices = listbox.curselection()

    if len(indices) != 1:
        # ２つ以上選択されているor１つも選択されていない
        return

    # 項目を取得
    index = indices[0]
    color = listbox.get(index)

    # 取得した項目で長方形の色を変更
    canvas.itemconfig(rect, fill=color)


app = tkinter.Tk()

# キャンバスの作成と配置
canvas = tkinter.Canvas(
    app,
    width=300,
    height=200,
    highlightthickness=0
)
canvas.grid(row=0, column=0, padx=10, pady=10)

# キャンバスに長方形描画
rect = canvas.create_rectangle(
    10, 10, 290, 190,
    fill="white",
    width=1,
)

# リストボックスの作成と配置
listbox = tkinter.Listbox(
    app
)
listbox.grid(row=0, column=1, padx=10, pady=10)


# リストボックスに項目追加
colors = [
    "red", "blue", "green"
]
for color in colors:
    listbox.insert(tkinter.END, color)

# ボタンの作成と配置
button = tkinter.Button(
    app,
    text="色変更",
    command=change_fill
)
button.grid(row=1, column=1, padx=10, pady=10)

app.mainloop()