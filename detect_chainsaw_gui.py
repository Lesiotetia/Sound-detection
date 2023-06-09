# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
import sys, os, glob
sys.path.append("./functions")
sys.path.append("./gui_icons")
from main import main
import icons_rc


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(580, 700)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 580, 700))
        self.stackedWidget.setLineWidth(1)
        self.stackedWidget.setObjectName("stackedWidget")
        self.SettingsPage = QtWidgets.QWidget()
        self.SettingsPage.setObjectName("SettingsPage")
        self.frame = QtWidgets.QFrame(self.SettingsPage)
        self.frame.setGeometry(QtCore.QRect(0, 0, 580, 700))
        self.frame.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(221, 231, 199, 255), stop:1 rgba(238, 248, 214, 255));\n"
"border-radius: 10px\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(30, 90, 511, 441))
        self.frame_2.setStyleSheet("background-color: rgb(227, 227, 227);border-radius:10px;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.toolBox = QtWidgets.QToolBox(self.frame_2)
        self.toolBox.setGeometry(QtCore.QRect(0, 0, 511, 441))
        self.toolBox.setStyleSheet("background-color: rgb(227, 227, 227);border-radius:10px;")
        self.toolBox.setObjectName("toolBox")
        self.Dir = QtWidgets.QWidget()
        self.Dir.setGeometry(QtCore.QRect(0, 0, 511, 379))
        self.Dir.setStyleSheet("")
        self.Dir.setObjectName("Dir")
        self.del_temp = QtWidgets.QCheckBox(self.Dir)
        self.del_temp.setGeometry(QtCore.QRect(85, 340, 181, 16))
        self.del_temp.setObjectName("del_temp")
        self.btn_dir = QtWidgets.QPushButton(self.Dir)
        self.btn_dir.setGeometry(QtCore.QRect(80, 10, 151, 61))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.btn_dir.setFont(font)
        self.btn_dir.setStyleSheet("QPushButton{ \n"
"border:0.5px solid grey; \n"
"border-radius: 7px; \n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(60, 137, 109, 255), stop:1 rgba(60, 137, 109, 100));\n"
"}\n"
"QPushButton:hover{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(172, 194, 170, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}")
        self.btn_dir.setObjectName("btn_dir")
        self.include_sub = QtWidgets.QCheckBox(self.Dir)
        self.include_sub.setGeometry(QtCore.QRect(330, 23, 91, 32))
        self.include_sub.setObjectName("include_sub")
        self.pathIN = QtWidgets.QTextBrowser(self.Dir)
        self.pathIN.setGeometry(QtCore.QRect(80, 100, 351, 51))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pathIN.setFont(font)
        self.pathIN.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.pathIN.setObjectName("pathIN")
        self.dir_label = QtWidgets.QLabel(self.Dir)
        self.dir_label.setGeometry(QtCore.QRect(84, 80, 161, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.dir_label.setFont(font)
        self.dir_label.setStyleSheet("")
        self.dir_label.setObjectName("dir_label")
        self.files_label = QtWidgets.QLabel(self.Dir)
        self.files_label.setGeometry(QtCore.QRect(80, 160, 151, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setUnderline(True)
        self.files_label.setFont(font)
        self.files_label.setObjectName("files_label")
        self.wavs = QtWidgets.QTextBrowser(self.Dir)
        self.wavs.setGeometry(QtCore.QRect(80, 180, 351, 141))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.wavs.setFont(font)
        self.wavs.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.wavs.setObjectName("wavs")
        self.toolBox.addItem(self.Dir, "")
        self.Params = QtWidgets.QWidget()
        self.Params.setGeometry(QtCore.QRect(0, 0, 511, 379))
        self.Params.setStyleSheet("")
        self.Params.setObjectName("Params")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.Params)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(30, 20, 461, 321))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.model_frame = QtWidgets.QFrame(self.verticalLayoutWidget_2)
        self.model_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.model_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.model_frame.setObjectName("model_frame")
        self.model_label = QtWidgets.QLabel(self.model_frame)
        self.model_label.setGeometry(QtCore.QRect(20, 10, 111, 58))
        self.model_label.setObjectName("model_label")
        self.model_sel = QtWidgets.QComboBox(self.model_frame)
        self.model_sel.setGeometry(QtCore.QRect(220, 20, 221, 31))
        self.model_sel.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.model_sel.setObjectName("model_sel")
        self.verticalLayout.addWidget(self.model_frame)
        self.vad_frame = QtWidgets.QFrame(self.verticalLayoutWidget_2)
        self.vad_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.vad_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.vad_frame.setObjectName("vad_frame")
        self.vad_label = QtWidgets.QLabel(self.vad_frame)
        self.vad_label.setGeometry(QtCore.QRect(20, 10, 141, 59))
        self.vad_label.setObjectName("vad_label")
        self.vad_spin = QtWidgets.QDoubleSpinBox(self.vad_frame)
        self.vad_spin.setGeometry(QtCore.QRect(340, 20, 101, 31))
        self.vad_spin.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.vad_spin.setDecimals(3)
        self.vad_spin.setMinimum(0.078)
        self.vad_spin.setMaximum(0.15)
        self.vad_spin.setSingleStep(0.001)
        self.vad_spin.setProperty("value", 0.08)
        self.vad_spin.setObjectName("vad_spin")
        self.verticalLayout.addWidget(self.vad_frame)
        self.prob_frame = QtWidgets.QFrame(self.verticalLayoutWidget_2)
        self.prob_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.prob_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.prob_frame.setObjectName("prob_frame")
        self.prob_label = QtWidgets.QLabel(self.prob_frame)
        self.prob_label.setGeometry(QtCore.QRect(20, 10, 171, 58))
        self.prob_label.setObjectName("prob_label")
        self.prob_spin = QtWidgets.QDoubleSpinBox(self.prob_frame)
        self.prob_spin.setGeometry(QtCore.QRect(340, 20, 101, 31))
        self.prob_spin.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.prob_spin.setMaximum(1.0)
        self.prob_spin.setSingleStep(0.01)
        self.prob_spin.setProperty("value", 0.4)
        self.prob_spin.setObjectName("prob_spin")
        self.verticalLayout.addWidget(self.prob_frame)
        self.cpu_frame = QtWidgets.QFrame(self.verticalLayoutWidget_2)
        self.cpu_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.cpu_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.cpu_frame.setObjectName("cpu_frame")
        self.label_2 = QtWidgets.QLabel(self.cpu_frame)
        self.label_2.setGeometry(QtCore.QRect(20, 10, 91, 58))
        self.label_2.setObjectName("label_2")
        self.gridLayoutWidget = QtWidgets.QWidget(self.cpu_frame)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(150, 20, 291, 31))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.radio_low = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.radio_low.setObjectName("radio_low")
        self.gridLayout.addWidget(self.radio_low, 0, 1, 1, 1)
        self.radio_mid = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.radio_mid.setObjectName("radio_mid")
        self.radio_mid.setChecked(True)
        self.gridLayout.addWidget(self.radio_mid, 0, 2, 1, 1)
        self.radio_no = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.radio_no.setObjectName("radio_no")
        self.gridLayout.addWidget(self.radio_no, 0, 0, 1, 1)
        self.radio_high = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.radio_high.setObjectName("radio_high")
        self.gridLayout.addWidget(self.radio_high, 0, 3, 1, 1)
        self.verticalLayout.addWidget(self.cpu_frame)
        self.toolBox.addItem(self.Params, "")
        self.frame_title = QtWidgets.QFrame(self.frame)
        self.frame_title.setGeometry(QtCore.QRect(0, 0, 581, 31))
        self.frame_title.setStyleSheet("background-color: rgba(1, 32, 15, 100)")
        self.frame_title.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_title.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_title.setObjectName("frame_title")
        self.btn_min = QtWidgets.QPushButton(self.frame_title)
        self.btn_min.setGeometry(QtCore.QRect(520, 5, 20, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_min.setFont(font)
        self.btn_min.setStyleSheet("QPushButton{ \n"
"border:none; \n"
"border-radius: 7px; \n"
"background-color:rgb(240, 135, 0);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(240, 135, 0, 150);\n"
"}")
        self.btn_min.setObjectName("btn_min")
        self.btn_exit = QtWidgets.QPushButton(self.frame_title)
        self.btn_exit.setGeometry(QtCore.QRect(550, 5, 20, 20))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_exit.setFont(font)
        self.btn_exit.setStyleSheet("QPushButton{ \n"
"border:none; \n"
"border-radius: 7px; \n"
"background-color: rgb(235, 0, 0);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(235,0,0, 150);\n"
"}")
        self.btn_exit.setObjectName("btn_exit")
        self.title = QtWidgets.QLabel(self.frame_title)
        self.title.setGeometry(QtCore.QRect(11, -3, 381, 41))
        font = QtGui.QFont()
        font.setFamily("Caladea")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.title.setFont(font)
        self.title.setAutoFillBackground(False)
        self.title.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.title.setObjectName("title")
        self.btn_run = QtWidgets.QPushButton(self.frame)
        self.btn_run.setGeometry(QtCore.QRect(170, 600, 221, 60))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_run.setFont(font)
        self.btn_run.setStyleSheet("QPushButton{ \n"
"border:0.5px solid grey; \n"
"border-radius: 7px; \n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(60, 137, 109, 255), stop:1 rgba(60, 137, 109, 100));\n"
"}\n"
"QPushButton:hover{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(172, 194, 170, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(172, 194, 170, 10), stop:1 rgba(255, 255, 255, 10));\n"
"}\n"
"\n"
"")
        self.btn_run.setObjectName("btn_run")
        self.stackedWidget.addWidget(self.SettingsPage)
        self.ResultsPage = QtWidgets.QWidget()
        self.ResultsPage.setObjectName("ResultsPage")
        self.results_frame = QtWidgets.QFrame(self.ResultsPage)
        self.results_frame.setGeometry(QtCore.QRect(0, 0, 600, 671))
        self.results_frame.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(221, 231, 199, 255), stop:1 rgba(238, 248, 214, 255));\n"
"border-radius: 10px\n"
"")
        self.results_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.results_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.results_frame.setObjectName("results_frame")
        self.frame_3 = QtWidgets.QFrame(self.results_frame)
        self.frame_3.setGeometry(QtCore.QRect(30, 90, 520, 460))
        self.frame_3.setStyleSheet("background-color: rgb(227, 227, 227);border-radius:10px;")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.results = QtWidgets.QPlainTextEdit(self.frame_3)
        self.results.setGeometry(QtCore.QRect(20, 140, 481, 281))
        self.results.setWordWrapMode(QtGui.QTextOption.NoWrap) 
        font = QtGui.QFont()
        font.setPointSize(10)
        self.results.setFont(font)
        self.results.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.results.setReadOnly(True)
        self.results.setObjectName("results")
        self.dir_label_2 = QtWidgets.QLabel(self.frame_3)
        self.dir_label_2.setGeometry(QtCore.QRect(20, 10, 221, 42))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.dir_label_2.setFont(font)
        self.dir_label_2.setStyleSheet("")
        self.dir_label_2.setObjectName("dir_label_2")
        # self.filelist = QtWidgets.QComboBox(self.frame_3)
        # self.filelist.setGeometry(QtCore.QRect(170, 90, 331, 22))
        # self.filelist.setStyleSheet("background-color: rgb(255, 255, 255);")
        # self.filelist.setObjectName("filelist")
        # self.label = QtWidgets.QLabel(self.frame_3)
        # self.label.setGeometry(QtCore.QRect(20, 90, 151, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setUnderline(True)
        # self.label.setFont(font)
        # self.label.setObjectName("label")
        self.pathIN_2 = QtWidgets.QTextBrowser(self.frame_3)
        self.pathIN_2.setGeometry(QtCore.QRect(250, 10, 251, 61))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pathIN_2.setFont(font)
        self.pathIN_2.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.pathIN_2.setObjectName("pathIN_2")
        self.btn_listen = QtWidgets.QPushButton(self.frame_3)
        self.btn_listen.setGeometry(QtCore.QRect(350, 360, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_listen.setFont(font)
        self.btn_listen.setStyleSheet("QPushButton{ \n"
"border:0.5px solid grey; \n"
"border-radius: 7px; \n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(9, 144, 0, 255), stop:1 rgba(16, 255, 0, 255));\n"
"}\n"
"QPushButton:hover{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(16, 254, 0, 255), stop:1 rgba(171, 255, 166, 255))\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(172, 194, 170, 10), stop:1 rgba(255, 255, 255, 10));\n"
"}\n"
"\n"
"")
        self.btn_listen.setObjectName("btn_listen")
        self.textEdit = QtWidgets.QTextEdit(self.frame_3)
        self.textEdit.setGeometry(QtCore.QRect(470, 141, 31, 31))
        self.textEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.btn_xlsx = QtWidgets.QPushButton(self.results_frame)
        self.btn_xlsx.setGeometry(QtCore.QRect(350, 590, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_xlsx.setFont(font)
        self.btn_xlsx.setStyleSheet("QPushButton{ \n"
"border:0.5px solid grey; \n"
"border-radius: 7px; \n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(60, 137, 109, 255), stop:1 rgba(60, 137, 109, 100));\n"
"}\n"
"QPushButton:hover{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(172, 194, 170, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(172, 194, 170, 10), stop:1 rgba(255, 255, 255, 10));\n"
"}\n"
"\n"
"")
        self.btn_xlsx.setObjectName("btn_xlsx")
        self.title_res = QtWidgets.QLabel(self.results_frame)
        self.title_res.setGeometry(QtCore.QRect(30, 50, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Caladea")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.title_res.setFont(font)
        self.title_res.setAutoFillBackground(False)
        self.title_res.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.title_res.setObjectName("title_res")
        self.btn_txt = QtWidgets.QPushButton(self.results_frame)
        self.btn_txt.setGeometry(QtCore.QRect(100, 590, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_txt.setFont(font)
        self.btn_txt.setStyleSheet("QPushButton{ \n"
"border:0.5px solid grey; \n"
"border-radius: 7px; \n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(60, 137, 109, 255), stop:1 rgba(60, 137, 109, 100));\n"
"}\n"
"QPushButton:hover{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(172, 194, 170, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(172, 194, 170, 10), stop:1 rgba(255, 255, 255, 10));\n"
"}\n"
"\n"
"")
        self.btn_txt.setObjectName("btn_txt")
        self.frame_title_2 = QtWidgets.QFrame(self.results_frame)
        self.frame_title_2.setGeometry(QtCore.QRect(0, 0, 581, 31))
        self.frame_title_2.setStyleSheet("background-color: rgba(1, 32, 15, 100)")
        self.frame_title_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_title_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_title_2.setObjectName("frame_title_2")
        self.btn_min_5 = QtWidgets.QPushButton(self.frame_title_2)
        self.btn_min_5.setGeometry(QtCore.QRect(520, 5, 20, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_min_5.setFont(font)
        self.btn_min_5.setStyleSheet("QPushButton{ \n"
"border:none; \n"
"border-radius: 7px; \n"
"background-color:rgb(240, 135, 0);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(240, 135, 0, 150);\n"
"}")
        self.btn_min_5.setObjectName("btn_min_5")
        self.btn_exit_5 = QtWidgets.QPushButton(self.frame_title_2)
        self.btn_exit_5.setGeometry(QtCore.QRect(550, 5, 20, 20))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_exit_5.setFont(font)
        self.btn_exit_5.setStyleSheet("QPushButton{ \n"
"border:none; \n"
"border-radius: 7px; \n"
"background-color: rgb(235, 0, 0);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(235,0,0, 150);\n"
"}")
        self.btn_exit_5.setObjectName("btn_exit_5")
        self.title_5 = QtWidgets.QLabel(self.frame_title_2)
        self.title_5.setGeometry(QtCore.QRect(11, -3, 381, 41))
        font = QtGui.QFont()
        font.setFamily("Caladea")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.title_5.setFont(font)
        self.title_5.setAutoFillBackground(False)
        self.title_5.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.title_5.setObjectName("title_5")
        self.stackedWidget.addWidget(self.ResultsPage)

        self.btn_dir.clicked.connect(self.select_dir)                
        self.include_sub.stateChanged.connect(self.update_files)
        self.btn_min.clicked.connect(self.minimize)       
        self.btn_exit.clicked.connect(self.on_closing)        
        self.btn_min_5.clicked.connect(self.minimize)       
        self.btn_exit_5.clicked.connect(self.on_closing)        
        self.btn_run.setEnabled(False)  
        self.btn_run.clicked.connect(self.run_main)        
        modelslist = [model.replace("pcen_rnn4_cl2_RMED_allARUs_run0.hdf5", "pcen_rnn4_cl2_RMED_allARUs_run0.hdf5 (default)") for model in os.listdir("./models/") if model.endswith('.hdf5')]
        self.model_sel.addItems(modelslist)
        # [self.model_sel.addItem(mdl) for mdl in modelslist]
        self.model_sel.currentIndexChanged.connect(self.selectionchange)
        self.model_sel.setCurrentIndex(modelslist.index('pcen_rnn4_cl2_RMED_allARUs_run0.hdf5 (default)'))

        max_cpus = self.count_processors()
        # print(f"parchoice {self.parchoice.get()}, cpus = {self.cpus.get()}")
        self.cpu_choice_list = [1, max_cpus//4, max_cpus//2, max_cpus-1]
        self.cpus = 1
        self.radio_low.clicked.connect(self.parse_cpu_radio)
        self.radio_mid.clicked.connect(self.parse_cpu_radio)
        self.radio_no.clicked.connect(self.parse_cpu_radio)
        self.radio_high.clicked.connect(self.parse_cpu_radio)
        self.btn_xlsx.clicked.connect(self.export_xlsx)
        self.btn_txt.clicked.connect(self.export_txt)

        MainWindow.setCentralWidget(self.centralwidget)


        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        self.toolBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.del_temp.setText(_translate("MainWindow", "Delete intermediate files"))
        self.btn_dir.setText(_translate("MainWindow", "Select\n"
"Directory"))
        self.include_sub.setText(_translate("MainWindow", "Include\n"
"Subfolders"))
        self.pathIN.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:7.8pt;\">[Please select a directory]</span></p></body></html>"))
        self.dir_label.setText(_translate("MainWindow", "Directory with wav files:"))
        self.files_label.setText(_translate("MainWindow", "Files to be processed:"))
        self.wavs.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:7.8pt;\">[No directory selected]</span></p></body></html>"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.Dir), _translate("MainWindow", ">> Directory selection"))
        self.model_label.setText(_translate("MainWindow", "Select model (for \n"
"classification):"))
        self.vad_label.setText(_translate("MainWindow", "VAD threshold chosen: \n"
"[Can take any value \n"
"between 0.078-0.15]"))
        self.prob_label.setText(_translate("MainWindow", "Probability threshold chosen: \n"
"[Can take any value \n"
"between 0-1]"))
        self.label_2.setText(_translate("MainWindow", "Parallelization:"))
        self.radio_low.setText(_translate("MainWindow", "Low"))
        self.radio_mid.setText(_translate("MainWindow", "Mid"))
        self.radio_no.setText(_translate("MainWindow", "No"))
        self.radio_high.setText(_translate("MainWindow", "Full"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.Params), _translate("MainWindow", ">> Advanced Parameters"))
        self.btn_min.setText(_translate("MainWindow", "_"))
        self.btn_exit.setText(_translate("MainWindow", "X"))
        self.title.setText(_translate("MainWindow", "CHA.D. - Chainsaw Detection (v 1.1)"))
        self.btn_run.setText(_translate("MainWindow", "Run"))
        self.dir_label_2.setText(_translate("MainWindow", "Directory with wav files scanned:\n(Subfolders NOT included)"))
        # self.label.setText(_translate("MainWindow", "Results per file:"))
        self.pathIN_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:7.8pt;\">[Please select a directory]</span></p></body></html>"))
        self.btn_listen.setText(_translate("MainWindow", "Click to listen\n"
"detections"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/navigation/pop-out3.png\" width=\"18\" /></p></body></html>"))
        self.btn_xlsx.setText(_translate("MainWindow", "Save as .xlsx"))
        self.title_res.setText(_translate("MainWindow", "Results"))
        self.btn_txt.setText(_translate("MainWindow", "Save as .txt"))
        self.btn_min_5.setText(_translate("MainWindow", "_"))
        self.btn_exit_5.setText(_translate("MainWindow", "X"))
        self.title_5.setText(_translate("MainWindow", "CHA.D. - Chainsaw Detection (v 1.1)"))







    def minimize(self):
        self.showMinimized()

    def update_files(self):
        folder = self.pathIN.toPlainText()
        if self.include_sub.isChecked():
            files = glob.glob(f"{folder}/**/*.wav", recursive=True)
        else:
            files = glob.glob(f"{folder}/*.wav", recursive=False)

        if len(files)>0:
            files = "\n".join(files).replace("\\", "/").replace(folder, "./")
            self.btn_run.setEnabled(True)
            self.btn_run.setText("Run")
        else:
            files = "No .wav files found in selected directory."
            self.btn_run.setText("Run\n(Select a valid directory)")
            self.btn_run.setEnabled(False)
        self.wavs.setText(files)


    def selectionchange(self,i):
        self.model = self.model_sel.currentText()
        self.modelidx = i

        print(self.model, self.modelidx)


    def count_processors(self):
        import multiprocessing
        import numpy as np
        nop=multiprocessing.cpu_count()
        print(str(int(nop)) + ' cpus found')
        return nop
# grid_button.clicked.connect(lambda _, r=row, c=col: self.tell_me(r, c))

    def parse_cpu_radio(self):
        # max_cpus = self.max_cpus
        # print(f"parchoice {self.parchoice.get()}, cpus = {self.cpus.get()}")
        # print("low:", self.radio_low.isChecked())
        # print("mid:", self.radio_mid.isChecked())
        # print("high:", self.radio_high.isChecked())
        # print("no:", self.radio_no.isChecked())
        if self.radio_no.isChecked():     i=0
        elif self.radio_low.isChecked():  i=1
        elif self.radio_mid.isChecked():  i=2
        elif self.radio_high.isChecked(): i=3

        cpu_temp = self.cpu_choice_list[i]
        self.cpus = max([1, cpu_temp])

        

    # def parse_cpu_radio(self):
    #     max_cpus = self.max_cpus
    #     choice_list = [1, max_cpus//4, max_cpus//2, max_cpus]
    #     # print(f"parchoice {self.parchoice.get()}, cpus = {self.cpus.get()}")
    #     cpu_temp = choice_list[self.parchoice.get()]
    #     self.cpus.set(max([1, cpu_temp]))
    #     # print(f"parchoice {self.parchoice.get()}, cpus = {self.cpus.get()}")

    def select_dir(self):
        import glob
        folder = str(QtWidgets.QFileDialog.getExistingDirectory(self, "Select Directory"))
        if folder:
            self.pathIN.setText(folder)
            self.update_files()
            self.btn_dir.setText("Change\nDirectory")
        #window.label_2.setText(file)


    def on_closing(self):
        import gc

        reply = QtWidgets.QMessageBox.question(self, 'Quit',
            "Are you sure to quit?", QtWidgets.QMessageBox.Yes | 
            QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)

        if reply == QtWidgets.QMessageBox.Yes:
            print('Thank you for using our tool!')
            QtCore.QCoreApplication.instance().quit()
            gc.collect()
            exit()


    def copy_citation_(self):
        clipboard = QtWidgets.QApplication.clipboard()
        clipboard.setText(citation)
        # self.parent.update() # the text will stay there after the window is closed
        # self.copied_lbl_txt.set("(Copied!)")

    def export_xlsx(self):
        import os
        fname = f'{self.pathIN.toPlainText()}/results_chainsaw.xlsx'
        i=1
        if os.path.exists(fname):
            fname = fname.replace(".xlsx", f"_{i}.xlsx")
            while os.path.exists(fname):
                i+=1
                fname = fname.replace(f"_{i-1}.xlsx", f"_{i}.xlsx")
        self.df.to_excel(fname, index=False)
        QtWidgets.QMessageBox.information(self, 'Save succesful!',
            f"File saved as\n{fname}", QtWidgets.QMessageBox.Ok)
        
    def export_txt(self):
        import os
        fname = f'{self.pathIN.toPlainText()}/results_chainsaw.txt'
        i=1
        if os.path.exists(fname):
            fname = fname.replace(".txt", f"_{i}.txt")
            while os.path.exists(fname):
                i+=1
                fname = fname.replace(f"_{i-1}.txt", f"_{i}.txt")
        # with open(fname, 'w+') as file:
            # file.write(self.df.to_string(index=False, na_rep = '-', sep='\t'))
        self.df.to_csv((fname), index=False, header=True, sep='\t') #, mode='a')                

        QtWidgets.QMessageBox.information(self, 'Save succesful!',
            f"File saved as\n{fname}", QtWidgets.QMessageBox.Ok)

    def initialize_files(self):
        import glob, os, pandas as pd, numpy as np
        pathIN = self.pathIN.toPlainText()
        self.pathIN_2.setText(pathIN)
        cwd = os.getcwd().replace("\\", "/")
        if not os.path.exists(pathIN + '/' + 'results_chainsaw.txt'):
            self.results.setPlainText("No chainsaw instances found.")
            self.results.show()
            self.results.setReadOnly(True)
            self.btn_listen.hide()
            self.btn_xlsx.hide()
            self.btn_txt.hide()
        else:
            self.df = pd.read_csv((pathIN + '/' + 'results_chainsaw.txt'), sep='\t') #, mode='a')                
            self.results.setPlainText(self.df.to_markdown(index=False))#, tablefmt="grid"))
            model = pandasModel(self.df)
            self.view = QtWidgets.QTableView(parent = self.frame_3)
            # self.view.setGeometry(QtCore.QRect(20, 140, 481, 281))
            self.view.setGeometry(QtCore.QRect(20, 90, 481, 331))
            self.view.setModel(model)
            self.results.hide()
            self.btn_listen.hide()

#        self.view.show()

        # found = glob.glob(f"{cwd}/CoughResults/*.txt")
        # files = glob.glob(f"{self.pathIN.toPlainText()}/**/*.wav", recursive=True)
        # self.df = pd.DataFrame()
        # self.results.setPlainText("Please select a file to view chainsaw detectections.")
        # self.btn_xlsx.hide()
        # self.btn_txt.hide()

        # if len(found)==0:
        #     self.filelist.addItem("-")
        #     self.results.setPlainText("No chainsaw instances found.")
        #     self.filelist.setEnabled(False)
        # else:
        #     self.res_text = dict()
        #     self.extracted_wavs = dict()
        #     self.filelist.addItem("Select file")
        #     self.res_text["Select file"]="Please select a file to view chainsaw segments detected."
            # for f in found:
            #     cc = f.replace("\\", "/").split("/")[-1].split("_chainsaw.txt")[0]
            #     self.filelist.addItem(cc)
            #     self.df = pd.DataFrame(np.loadtxt(f)[:,1:], columns=["Time (s)", "Confidence"], index=np.loadtxt(f)[:,0].astype(int)) 
            #     self.res_text[cc] = self.df.to_string()
            #     self.extracted_wavs[cc] = f.replace(".txt", ".wav") #[fn for fn in files if cc in fn][0]

    # def change_results(self):
    #     self.results.setPlainText(self.res_text[self.filelist.currentText()])
    #     check=self.filelist.currentText()!="Select file"
    #     if check:
    #         self.btn_listen.show()
    #         self.btn_xlsx.show()
    #         self.btn_txt.show()
    #     else:
    #         self.btn_listen.hide()
    #         self.btn_xlsx.hide()
    #         self.btn_txt.hide()
        # self.btn_listen.setEnabled(check)
        # self.btn_xlsx.setEnabled(check)
        # self.btn_txt.setEnabled(check)


    def listen_active_wav(self):
        if self.filelist.currentText()=="Select file":
            return
        from playsound import playsound
        playsound(self.extracted_wavs[self.filelist.currentText()])

    def run_main(self):
        global vpathIN, vvad_th,vprob_th, vcpus , model, del_temp
        vpathIN = self.pathIN.toPlainText()
        vcpus = int(self.cpus)
        vvad_th = self.vad_spin.value()
        vprob_th = self.prob_spin.value()
        model = self.model_sel.currentText().replace("pcen_rnn4_cl2_RMED_allARUs_run0.hdf5 (default)", "pcen_rnn4_cl2_RMED_allARUs_run0.hdf5")
        del_temp = self.del_temp.isChecked()
        recursive = self.include_sub.isChecked()
        print("Starting execution. Please wait...")
        self.hide()
        main(vpathIN, vvad_th, \
         vprob_th, vcpus, del_temp = del_temp, model=model, recursive = recursive)
        
        self.stackedWidget.setCurrentIndex(1)
        self.initialize_files()
        self.show()
        med = (1-recursive)*"NOT "
        suffix = f"(Subfolders {med}included)"
        self.dir_label_2.setText("Directory with wav files scanned:\n"+suffix)

        #QtCore.QCoreApplication.instance().quit()



class MyWin(QtWidgets.QMainWindow, Ui_MainWindow):
    #Stack over flow - draggable window
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.dragPos = QtCore.QPoint()
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground, True)
        try:
            self.setWindowIcon(QtGui.QIcon('/lib/resources/forth_disk.png'))
        except:
            pass
    def mousePressEvent(self, event):                                 # +
        self.dragPos = event.globalPos()
        
    def mouseMoveEvent(self, event):                                  # !!!
        if event.buttons() == QtCore.Qt.LeftButton:
            self.move(self.pos() + event.globalPos() - self.dragPos)
            self.dragPos = event.globalPos()
            event.accept()     


from PyQt5.QtWidgets import QApplication, QTableView
from PyQt5.QtCore import QAbstractTableModel, Qt


class pandasModel(QAbstractTableModel):

    def __init__(self, data):
        QAbstractTableModel.__init__(self)
        self._data = data

    def rowCount(self, parent=None):
        return self._data.shape[0]

    def columnCount(self, parnet=None):
        return self._data.shape[1]

    def data(self, index, role=Qt.DisplayRole):
        if index.isValid():
            if role == Qt.DisplayRole:
                return str(self._data.iloc[index.row(), index.column()])
        return None

    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self._data.columns[col]
        return None


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = MyWin()
    w.show()
    sys.exit(app.exec())
