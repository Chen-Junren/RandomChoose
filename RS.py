# -*- coding: utf-8 -*-
# Latest Update:2023-5-15-15:33 Line 391-395
import contextlib
import logging
import os
import sys
import time
from random import randint
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from win32api import MessageBox
from win32con import MB_OK, MB_ICONWARNING

date = (
    f"{time.localtime().tm_year}-{time.localtime().tm_mon}-{time.localtime().tm_mday} {time.localtime().tm_hour}_"
    f"{time.localtime().tm_min}_{time.localtime().tm_sec}"
)
if not os.path.exists("./log/"):
    os.mkdir("log")
# open("./log/"+date+".log","w")
logging.basicConfig(
    level=logging.DEBUG,  # 设置日志输出格式
    filename=f"./log/{date}.log",  # log日志输出的文件位置和文件名
    filemode="w",  # 文件的写入格式，w为重新写入文件，默认是追加
    format="%(asctime)s - %(name)s - %(levelname)-9s - %(filename)-8s : %(lineno)s line - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
big = False
running = False
name = True
a = """1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
"""

seed = False
choud = False


def name():
    with open("name.txt", "w") as f:
        print(f.truncate())
        print(f.write(a))


global name_list
try:
    wordlist3 = []
    with open("name.txt", encoding="utf8") as f:
        wordlist3.extend(line.strip("\n") for line in f)
    # print(wordlist3)
    name_list = wordlist3
    logging.info("Successfully loaded name.txt")
except Exception:
    name()
    name = False
    MessageBox(
        0,
        "请及时修改当前目录下name文件，默认将为1-43",
        "MessageBox",
        MB_OK | MB_ICONWARNING,
    )
    logging.warning("name.txt not found. Created name.txt")

    name_list = [
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "10",
        "11",
        "12",
        "13",
        "14",
        "15",
        "16",
        "17",
        "18",
        "19",
        "20",
        "21",
        "22",
        "23",
        "24",
        "25",
        "26",
        "27",
        "28",
        "29",
        "30",
        "31",
        "32",
        "33",
        "34",
        "35",
        "36",
        "37",
        "38",
        "39",
        "40",
        "41",
        "42",
        "43",
    ]


class Ui_MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.RowLength = 0
        with contextlib.suppress(Exception):
            from os import path as pathq

            icon_path = pathq.join(pathq.dirname(__file__), "./logo.ico")

            icon = QIcon()
            icon.addPixmap(QPixmap(icon_path))  # 这是对的
            MainWindow.setWindowIcon(icon)
        # self.setupUi(MainWindow())

    def setupUi(self, MainWindow):
        # 以下课直接粘贴生成的setupui代码
        MainWindow.setObjectName("点名器正式版V1.0.0 ")
        MainWindow.resize(420, 360)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)

        self.label.setGeometry(QtCore.QRect(55, 50, 331, 71))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(55, 190, 111, 61))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(20)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(253, 190, 111, 61))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(20)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(11, 570, 111, 41))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(0, 830, 111, 41))
        self.pushButton_4.setObjectName("pushButton_4")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(11, 370, 397, 191))
        self.listWidget.setObjectName("listWidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(11, 340, 210, 21))
        self.label_2.setObjectName("label_2")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(11, 303, 111, 20))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(319, 300, 75, 20))
        self.pushButton_6.setObjectName("pushButton_6")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(550, 260, 89, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setText("3")
        self.lineEdit.setStyleSheet(
            """
        QListView, QLineEdit { 
            color: #D2D2D2; 
            background-color:#29292C;
            selection-color: #29292C; 
            border: 2px groove #29292C; 
            border-radius: 10px; 
            padding: 2px 4px; 
        } 
        QLineEdit:focus { 
            color: #D2D2D2; 
            selection-color: #29292C; 
            border: 2px groove #29292C; 
            border-radius: 10px; 
            padding: 2px 4px; 
        } 
        
                """
        )
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(495, 260, 56, 21))
        self.label_3.setObjectName("label_3")
        self.label_3.setStyleSheet("color:white;background:#222225")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(649, 240, 111, 61))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(30)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setObjectName("pushButton_7")
        self.listWidget_2 = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_2.setGeometry(QtCore.QRect(473, 20, 353, 221))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.listWidget_2.setFont(font)
        self.listWidget_2.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.listWidget_2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.listWidget_2.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.listWidget_2.setSizeAdjustPolicy(
            QtWidgets.QAbstractScrollArea.AdjustToContents
        )
        self.listWidget_2.setObjectName("listWidget_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 874, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton.clicked.connect(self.start)

        self.pushButton_2.clicked.connect(self.stop)
        self.pushButton_5.clicked.connect(self.showHistory)

        self.pushButton_7.setStyleSheet(
            """QPushButton{background:#6DDF6D;border-radius:5px;}QPushButton:hover{background:green;}"""
        )
        self.pushButton_6.clicked.connect(self.showContinue)
        self.pushButton_7.clicked.connect(self.ten)
        self.pushButton_6.setStyleSheet(
            """QPushButton{background:#F7D674;border-radius:5px;}QPushButton:hover{background:yellow;}"""
        )
        self.pushButton.setStyleSheet(
            """QPushButton{background:#6DDF6D;border-radius:5px;}QPushButton:hover{background:green;}"""
        )
        self.pushButton_2.setStyleSheet(
            """QPushButton{background:#F76677;border-radius:5px;}QPushButton:hover{background:red;}"""
        )
        self.pushButton_3.setStyleSheet(
            """QPushButton{background:#6DDF6D;border-radius:5px;}QPushButton:hover{background:green;}"""
        )
        self.pushButton_5.setStyleSheet(
            """QPushButton{background:#F7D674;border-radius:5px;}QPushButton:hover{background:yellow;}"""
        )

        self.pushButton_4.setStyleSheet(
            """QPushButton{background:#F7D674;border-radius:5px;}QPushButton:hover{background:yellow;}"""
        )
        # 以上可以修改
        self.centralwidget.setStyleSheet(
            """
             QWidget#centralwidget{
             color:#222225;
             background:#222225;
             border-top:1px solid #222225;
             border-bottom:1px solid #222225;
             border-right:1px solid #222225;
             border-left:1px solid #444444;
             border-top-left-radius:10px;
             border-top-right-radius:10px;
             border-bottom-left-radius:10px;
             border-bottom-right-radius:10px;
             }

             """
        )
        self.close_widget = QtWidgets.QWidget(self.centralwidget)
        self.close_widget.setGeometry(QtCore.QRect(333, 0, 90, 30))
        self.close_widget.setObjectName("close_widget")
        self.close_layout = QGridLayout()  # 创建左侧部件的网格布局层
        self.close_widget.setLayout(self.close_layout)  # 设置左侧部件布局为网格

        self.left_close = QPushButton("")  # 关闭按钮
        self.left_close.clicked.connect(MainWindow.close)
        self.left_visit = QPushButton("")  # 空白按钮
        self.left_visit.clicked.connect(MainWindow.big)
        self.left_mini = QPushButton("")  # 最小化按钮
        self.left_mini.clicked.connect(MainWindow.mini)
        self.close_layout.addWidget(self.left_mini, 0, 0, 1, 1)
        self.close_layout.addWidget(self.left_close, 0, 2, 1, 1)
        self.close_layout.addWidget(self.left_visit, 0, 1, 1, 1)
        self.left_close.setFixedSize(15, 15)  # 设置关闭按钮的大小
        self.left_visit.setFixedSize(15, 15)  # 设置按钮大小
        self.left_mini.setFixedSize(15, 15)  # 设置最小化按钮大小
        self.left_close.setStyleSheet(
            """QPushButton{background:#F76677;border-radius:5px;}QPushButton:hover{background:red;}"""
        )
        self.left_visit.setStyleSheet(
            """QPushButton{background:#F7D674;border-radius:5px;}QPushButton:hover{background:yellow;}"""
        )
        self.left_mini.setStyleSheet(
            """QPushButton{background:#6DDF6D;border-radius:5px;}QPushButton:hover{background:green;}"""
        )
        self.pushButton_3.clicked.connect(self.ren)
        self.label_2.setStyleSheet("color:white")

        self.scc = """
         QListWidget{background-color:#2B2B2B;color:white}
         /*垂直滚动条*/
         QScrollBar:vertical{
             width:12px;
             border:1px solid #2B2B2B;
             margin:0px,0px,0px,0px;
             padding-top:0px;
             padding-bottom:0px;
         }
         QScrollBar::handle:vertical{
             width:3px;
             background:#4B4B4B;
             min-height:3;
         }
         QScrollBar::handle:vertical:hover{
             background:#3F3F3F;
             border:0px #3F3F3F;
         }
         QScrollBar::sub-line:vertical{
             width:0px;
             border-image:url(:/Res/scroll_left.png);
             subcontrol-position:left;
         }
         QScrollBar::sub-line:vertical:hover{
             height:0px;
             background:#222225;
             subcontrol-position:top;
         }
         QScrollBar::add-line:vertical{
             height:0px;
             border-image:url(:/Res/scroll_down.png);
             subcontrol-position:bottom;
         }
         QScrollBar::add-line:vertical:hover{
             height:0px;
             background:#3F3F3F;
             subcontrol-position:bottom;
         }
         QScrollBar::add-page:vertical{
             background:#2B2B2B;
         }
         QScrollBar::sub-page:vertical{
             background:#2B2B2B;
         }
         QScrollBar::up-arrow:vertical{
             border-style:outset;
             border-width:0px;
         }
         QScrollBar::down-arrow:vertical{
             border-style:outset;
             border-width:0px;
         }

         QScrollBar:horizontal{
             height:12px;
             border:1px #2B2B2B;
             margin:0px,0px,0px,0px;
             padding-left:0px;
             padding-right:0px;
         }
         QScrollBar::handle:horizontal{
             height:16px;
             background:#4B4B4B;
             min-width:20;
         }
         QScrollBar::handle:horizontal:hover{
             background:#3F3F3F;
             border:0px #3F3F3F;
         }
         QScrollBar::sub-line:horizontal{
             width:0px;
             border-image:url(:/Res/scroll_left.png);
             subcontrol-position:left;
         }
         QScrollBar::sub-line:horizontal:hover{
             width:0px;
             background:#2B2B2B;
             subcontrol-position:left;
         }
         QScrollBar::add-line:horizontal{
             width:0px;
             border-image:url(:/Res/scroll_right.png);
             subcontrol-position:right;
         }
         QScrollBar::add-line:horizontal:hover{
             width:0px;
             background::#2B2B2B;
             subcontrol-position:right;
         }
         QScrollBar::add-page:horizontal{
                    background:#2B2B2B;
         }
         QScrollBar::sub-page:horizontal{
                     background:#2B2B2B;
         }
        """
        self.listWidget.setStyleSheet(self.scc)
        self.listWidget_2.setStyleSheet(self.scc)

        MainWindow.setWindowOpacity(0.95)  # 设置窗口透明度
        MainWindow.setAttribute(Qt.WA_TranslucentBackground)
        MainWindow.setWindowFlag(Qt.FramelessWindowHint)  # 隐藏边框

        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(132, 570, 100, 41))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_8.setStyleSheet(
            """QPushButton{background:#F7D674;border-radius:5px;}QPushButton:hover{background:yellow;}"""
        )
        self.pushButton_8.clicked.connect(self.rename)
        self.pushButton_8.setText("重置名字文件")
        logging.info("Successfully generate the mainwindow")

    def ten(self):
        num = self.lineEdit.text()
        # print (num)
        try:
            num = int(num)
        except ValueError:
            logging.critical(f"Choose_ERR: Number must be an integer, but found {num}")
            self.listWidget_2.clear()
            self.listWidget_2.addItem("ERR")
            self.listWidget.addItem("ERR")
            return 0
        # name_list = name_list
        # print(name_list)
        if num != "" and 0 < num <= 1000 and num <= len(name_list):

            # if num > 20:
            #    reply = QtWidgets.QMessageBox.warning(self, u'警告', u'认真的吗，这么多', QtWidgets.QMessageBox.Yes)
            self.listWidget_2.clear()
            for _ in range(num):
                name = name_list[randint(0, len(name_list) - 1)]
                # name_list.remove(name)
                self.listWidget_2.addItem(name)
                self.listWidget.addItem(name)
            logging.info(f"Choose: Number:{num}")
        elif num > len(name_list):
            reply = QtWidgets.QMessageBox.warning(
                self, "警告", "输入大于剩余人数", QtWidgets.QMessageBox.Yes
            )
            self.listWidget_2.clear()
            logging.critical("Choose_ERR: Found 'number' > name_list")
        elif num == "":
            self._extracted_from_ten_30(
                "请输入数字", "Choose_WARN: Found 'number' = ''"
            )
        elif num < 0:
            self._extracted_from_ten_30(
                "人数负数，输入有误！", "Choose_WARN: Found 'number' < 0"
            )
        elif num == 0:
            self._extracted_from_ten_30(
                "人数为0，输入有误！", "Choose_WARN: Found 'number' = '0'"
            )
        elif num > 1000:
            self._extracted_from_ten_30(
                "人数超出限制，输入有误！", "Choose_WARN: Found 'number' > '1000'"
            )

    # TODO Rename this here and in `ten`
    def _extracted_from_ten_30(self, arg0, arg1):
        reply = QtWidgets.QMessageBox.warning(
            self, "警告", arg0, QtWidgets.QMessageBox.Yes
        )
        self.listWidget_2.clear()
        logging.warning(arg1)

    def ren(self):
        os.system("start ./name.txt")
        logging.info("Opened name.txt for user")

    def retranslateUi(self, MainWindow):
        self.wide = 420
        self.high = 360
        _translate = QtCore.QCoreApplication.translate
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "随机点名"))
        self.label.setStyleSheet("color:white")
        self.pushButton.setText(_translate("MainWindow", "开始"))
        self.pushButton_2.setText(_translate("MainWindow", "结束"))
        self.pushButton_3.setText(_translate("MainWindow", "打开名字文件"))
        self.label_2.setText(_translate("MainWindow", "点过的学号/姓名："))
        self.pushButton_5.setText(_translate("MainWindow", "查看点过的名字"))
        self.pushButton_6.setText(_translate("MainWindow", "连抽模式"))
        self.label_3.setText(_translate("MainWindow", "连抽人数"))
        self.pushButton_7.setText(_translate("MainWindow", "开始"))

    def showHistory(self):
        global seed
        if not seed:
            self._extracted_from_showHistory_4(656, True, "Opened history")
        else:
            self._extracted_from_showHistory_4(360, False, "Closed history")

    # TODO Rename this here and in `showHistory`
    def _extracted_from_showHistory_4(self, arg0, arg1, arg2):
        self.high = arg0
        MainWindow.resize(self.wide, self.high)
        seed = arg1
        logging.info(arg2)

    def showContinue(self):
        global choud
        if not choud:
            self._extracted_from_showContinue_4(874, True, "Opened Multiple extraction")
        else:
            self._extracted_from_showContinue_4(
                420, False, "Closed Multiple extraction"
            )

    # TODO Rename this here and in `showContinue`
    def _extracted_from_showContinue_4(self, arg0, arg1, arg2):
        self.wide = arg0
        MainWindow.resize(self.wide, self.high)
        choud = arg1
        logging.info(arg2)

    def setname(self):
        global running
        global name
        try:
            name = name_list[randint(0, len(name_list) - 1)]
            self.label.setText(f"恭喜{name}号")

        except Exception:
            self.name()
            reply = QtWidgets.QMessageBox.warning(
                self,
                "警告",
                "发生错误，请检查name文件的学号后再重新打开本软件",
                QtWidgets.QMessageBox.Yes,
            )
            logging.error("Choose_ERR: Please check name.txt and try again")
            sys.exit()

    def rename(self):
        reply = QtWidgets.QMessageBox.question(
            self,
            "警告",
            "确定重置name文件为1-43?",
            QtWidgets.QMessageBox.Yes,
            QtWidgets.QMessageBox.No,
        )
        if reply == QtWidgets.QMessageBox.Yes:
            a = """1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
"""

            with open("name.txt", "w") as f:
                print(f.truncate())
                print(f.write(a))
            logging.info("Reset name.txt")
            MessageBox(0, "重置完成,", "通知", MB_OK | MB_ICONWARNING)

    def name(self):
        with open("name.txt", "w") as f:
            print(f.truncate())
            print(f.write(a))
            logging.info("Reset name.txt")
        # win32api.MessageBox(0,"已将name文件重置为1-52，请及时修改","MessageBox",win32con.MB_OK | win32con.MB_ICONWARNING)

    def start(self):
        global running
        if running:
            print("running")
            logging.info("Begin choosing")
        else:
            self.timer = QTimer(self)
            self.timer.timeout.connect(self.setname)
            self.timer.start(50)
            running = "True"

    def stop(self):
        global running, a
        if running:
            self.timer.stop()
            running = False
            logging.info("End choosing")
            self.listWidget.addItem(name)
        else:

            reply = QtWidgets.QMessageBox.warning(
                self, "警告", "还没开始就想结束？", QtWidgets.QMessageBox.Yes
            )
            logging.warning("WARN: Stop before start")

    # 识别


# 重写MainWindow类
class MainWindow(QtWidgets.QMainWindow):

    def closeEvent(self, event):
        reply = QtWidgets.QMessageBox.question(
            self,
            "提示",
            "是否要退出程序？",
            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
            QtWidgets.QMessageBox.No,
        )
        if reply == QtWidgets.QMessageBox.Yes:
            logging.info("Exit the program")
            event.accept()
        else:
            event.ignore()

    def mousePressEvent(self, event):
        global big
        big = False

        if event.button() == Qt.LeftButton:
            self.m_flag = True
            self.m_Position = event.globalPos() - self.pos()  # 获取鼠标相对窗口的位置
            event.accept()
            self.setCursor(QCursor(Qt.OpenHandCursor))  # 更改鼠标图标

    def mouseMoveEvent(self, QMouseEvent):
        global big
        big = False
        if Qt.LeftButton and self.m_flag:
            self.setWindowState(Qt.WindowNoState)
            self.move(QMouseEvent.globalPos() - self.m_Position)  # 更改窗口位置
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        global big
        big = False
        self.m_flag = False
        self.setCursor(QCursor(Qt.ArrowCursor))

    def big(self):
        global big
        # print(f"最大化：{big}")
        self.setWindowState(Qt.WindowNoState)
        big = False

    def close(self):
        reply = QtWidgets.QMessageBox.question(
            self,
            "提示",
            "是否要退出程序？",
            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
            QtWidgets.QMessageBox.No,
        )
        if reply == QtWidgets.QMessageBox.Yes:
            logging.info("Exit")
            sys.exit()

    def mini(self):

        self.showMinimized()


if __name__ == "__main__":
    logging.info("Start the program")
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = MainWindow()  # QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
