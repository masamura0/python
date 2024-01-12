from tkinter import *
from tkinter import ttk

############################################################ ウインドウ

#ウィンドウを作成
root = Tk()

#ウィンドウサイズを指定
root.geometry("550x170")

#ウィンドウタイトルを指定
root.title('echo 生成コマンド')

frame1 = ttk.Frame(root, padding=(32))
frame1.grid()

############################################################ 枠

#day
label1 = ttk.Label(frame1, text='day', padding=(5, 2))
label1.grid(row=0, column=0, sticky=E)

#machinename
label2 = ttk.Label(frame1, text='machinename', padding=(5, 2))
label2.grid(row=1, column=0, sticky=E)

#operationfile
label3 = ttk.Label(frame1, text='operationfile', padding=(5, 2))
label3.grid(row=2, column=0, sticky=E)

############################################################ 入力フォーム
#day
day = StringVar()
day_txt = ttk.Entry(
    frame1,
    textvariable=day,
    width=35)
day_txt.grid(row=0, column=1)

#machinename
machinename = StringVar()
machinename_txt = ttk.Entry(
    frame1,
    textvariable=machinename,
    width=35)
machinename_txt.grid(row=1, column=1)

#machinename
operationfile = StringVar()
operationfile_txt = ttk.Entry(
    frame1,
    textvariable=operationfile,
    width=35)
operationfile_txt.grid(row=2, column=1)


############################################################ ok(show echo)
# Button
button1 = ttk.Button(
    frame1, text='OK', 
    command=lambda: print("ansible-playbook -i /home/max/22%s/i%s.yml -i /home/max/22%s/%s/operation_today/%s -i /home/max/%s/v%s.yml ececute.yml" % (day.get(), machinename.get(), day.get(), machinename.get(), operationfile.get(), day.get(), machinename.get())))
button1.grid(row=3, column=1)

#ウィンドウ表示継続
root.mainloop()