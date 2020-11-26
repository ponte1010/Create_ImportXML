# -*- coding: utf8 -*-
import tkinter.messagebox
import tkinter.filedialog

# メッセージダイアログの表示
tkinter.messagebox.showinfo('xmlファイルの選択','処理するxmlファイルを選択してください！')

# ファイル選択ダイアログの表示
file_path = tkinter.filedialog.asksaveasfilename()