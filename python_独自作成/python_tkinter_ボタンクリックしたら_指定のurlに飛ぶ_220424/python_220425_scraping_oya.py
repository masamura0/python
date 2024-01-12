# tkinterのインポート
import tkinter as tk
import tkinter.ttk as ttk
import webbrowser

from setuptools import Command
from tkinter import Label, messagebox

def btn_click_1():
    messagebox.showinfo("メッセージ", "ボタンがクリックされました")
    webbrowser.open('https://www.amazon.co.jp/?&tag=hydraamazonav-22&ref=pd_sl_7ibq2d37on_e&adgrpid=56100363354&hvpone=&hvptwo=&hvadid=592007363477&hvpos=&hvnetw=g&hvrand=5796029085449256506&hvqmt=e&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=1009329&hvtargid=kwd-10573980&hydadcr=27922_14541005&gclid=Cj0KCQjwpImTBhCmARIsAKr58cy0mdayQAJaBhC2oLYmP5OfmB70TjV6LMidZEpFyvxPZdLBARbnLxgaAsCvEALw_wcB')

def btn_click_2():
    messagebox.showinfo("メッセージ", "ボタンがクリックされました")
    webbrowser.open('https://bellard.org/jslinux/')

def btn_click_3():
    messagebox.showinfo("メッセージ", "ボタンがクリックされました")
    webbrowser.open('https://translate.google.co.jp/')
    

# rootメインウィンドウの設定
root = tk.Tk()
root.title("Frame widget:relief")
root.geometry("500x100")

frame = tk.Frame(root,height=400, width=400, pady=10, padx=10)
frame.pack()

#################################

frame_raised = tk.Frame(frame, relief=tk.RAISED, bg='blue', bd=2)

btn = tk.Button(root, text='Amazonショッピング',  command = btn_click_1)
btn.place(x=300, y=50)


frame_raised.pack(side=tk.LEFT)

#################################

frame_groove = tk.Frame(frame, relief=tk.GROOVE, bg='white', bd=2)

btn = tk.Button(root, text='linux学習',  command = btn_click_2)

btn.place(x=200, y=50)

#################################

frame_sunken = tk.Frame(frame,  relief=tk.SUNKEN, bg='white', bd=2)

btn = tk.Button(root, text='google翻訳',  command = btn_click_3)

btn.place(x=100, y=50)

#################################

root.mainloop()