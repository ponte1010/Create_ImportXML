# -*- coding: utf8 -*-
import sys  # sys関数のインポート(例外処理のため)
import myFunction, purseXML, makeList, makeJSON  # 自作関数のインポート
import xml.etree.ElementTree as ET  # xmlモジュールのインポート
import numpy as np  # numpyパッケージのインポート
import os, tkinter, tkinter.filedialog, tkinter.messagebox  # ファイル選択用モジュールのインポート

# xmlファイルの読み込み
FileName = myFunction.GetFileName()  # ファイル名を取得
tree = ET.parse(FileName)  # XMLを取得
root = tree.getroot()

# xml記述のパース（別モジュールをコール）
a = purseXML.PurseXML(root)
TeamData_list = a[0]
Actor_list = a[1];
Actor_array = np.array(Actor_list)
AC_list = a[2]
LO_list = a[3]
LOid_array = a[4]
Line_list = a[5]
Arrow_list = a[6]

# excel出力用リストの生成（別モジュールをコール）
b = makeList.MakeList(Actor_list, AC_list, LO_list, LOid_array, Line_list, Arrow_list)
ex_list = b[0]
ST2Num_list = b[1]
AT2Num_list = b[2]

# csv出力
c = myFunction.csvexport_list('TeamData_list', TeamData_list)  # actorsのチームデータ
c = myFunction.csvexport_list('Actor_list', Actor_list)  # actorsのアクタ
c = myFunction.csvexport_list('sample_writer_row', ex_list)  # senario
c = myFunction.csvexport_list('ST2Num', ST2Num_list)  # ID確認用
c = myFunction.csvexport_list('AT2Num', AT2Num_list)  # ID確認用

# json出力
d = makeJSON.SettingJson(TeamData_list)  # setting.json
d = makeJSON.ContactsJson(TeamData_list, Actor_list)  # contacts.json
d = makeJSON.ActionsJson(ex_list, Actor_list)  # actions.json
d = makeJSON.StatesJson(ex_list)  # states.json
d = makeJSON.RepliesJson(ex_list)  # replies.json
d = makeJSON.PointsJson(ex_list)  # points.json
