# -*- coding: utf8 -*-
import sys
import tkinter.messagebox, tkinter.filedialog

# メッセージダイアログの表示
tkinter.messagebox.showinfo('xmlファイルの選択','xmlファイルを選択してください。')

# ファイル選択ダイアログの表示
file_path = tkinter.filedialog.asksaveasfilename()

file_format=file_path[-4:]

# xmlファイルではないときにエラーメッセージを表示
if file_format != ".xml":
    tkinter.messagebox.showinfo('Error!!','xmlファイルを選択してください。')
    sys.exit()