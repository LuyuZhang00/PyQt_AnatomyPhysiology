# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'windows_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(620, 700)
        MainWindow.setMinimumSize(QtCore.QSize(620, 700))
        MainWindow.setMaximumSize(QtCore.QSize(620, 700))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(620, 675))
        self.centralwidget.setMaximumSize(QtCore.QSize(620, 675))
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(60, 30, 500, 600))
        self.frame.setMinimumSize(QtCore.QSize(400, 600))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_3 = QtWidgets.QFrame(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.frame_2 = QtWidgets.QFrame(self.frame_3)
        self.frame_2.setGeometry(QtCore.QRect(0, 0, 480, 491))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(5)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.pushButton_A = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_A.setGeometry(QtCore.QRect(20, 110, 51, 31))
        self.pushButton_A.setObjectName("pushButton_A")
        self.pushButton_B = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_B.setGeometry(QtCore.QRect(20, 180, 51, 31))
        self.pushButton_B.setObjectName("pushButton_B")
        self.pushButton_C = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_C.setGeometry(QtCore.QRect(20, 250, 51, 31))
        self.pushButton_C.setObjectName("pushButton_C")
        self.pushButton_D = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_D.setGeometry(QtCore.QRect(20, 330, 51, 31))
        self.pushButton_D.setObjectName("pushButton_D")
        self.label_ques = QtWidgets.QLabel(self.frame_2)
        self.label_ques.setGeometry(QtCore.QRect(80, 0, 391, 81))
        self.label_ques.setStyleSheet("font: 13pt \"楷体\";")
        self.label_ques.setWordWrap(True)
        self.label_ques.setOpenExternalLinks(True)
        self.label_ques.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByKeyboard|QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextBrowserInteraction|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.label_ques.setObjectName("label_ques")
        self.label_A = QtWidgets.QLabel(self.frame_2)
        self.label_A.setGeometry(QtCore.QRect(80, 100, 381, 51))
        self.label_A.setStyleSheet("font:12pt \"楷体\";")
        self.label_A.setText("")
        self.label_A.setWordWrap(True)
        self.label_A.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByKeyboard|QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextBrowserInteraction|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.label_A.setObjectName("label_A")
        self.label_B = QtWidgets.QLabel(self.frame_2)
        self.label_B.setGeometry(QtCore.QRect(80, 170, 381, 51))
        self.label_B.setStyleSheet("font: 12pt \"楷体\";")
        self.label_B.setText("")
        self.label_B.setWordWrap(True)
        self.label_B.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByKeyboard|QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextBrowserInteraction|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.label_B.setObjectName("label_B")
        self.label_C = QtWidgets.QLabel(self.frame_2)
        self.label_C.setGeometry(QtCore.QRect(80, 240, 391, 51))
        self.label_C.setStyleSheet("font: 12pt \"楷体\";")
        self.label_C.setText("")
        self.label_C.setWordWrap(True)
        self.label_C.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByKeyboard|QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextBrowserInteraction|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.label_C.setObjectName("label_C")
        self.label_D = QtWidgets.QLabel(self.frame_2)
        self.label_D.setGeometry(QtCore.QRect(80, 320, 401, 51))
        self.label_D.setStyleSheet("font: 12pt \"楷体\";")
        self.label_D.setInputMethodHints(QtCore.Qt.ImhNone)
        self.label_D.setText("")
        self.label_D.setWordWrap(True)
        self.label_D.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByKeyboard|QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextBrowserInteraction|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.label_D.setObjectName("label_D")
        self.pushButton_question = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_question.setGeometry(QtCore.QRect(30, 390, 181, 51))
        self.pushButton_question.setObjectName("pushButton_question")
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setGeometry(QtCore.QRect(10, 0, 51, 91))
        self.label_3.setStyleSheet("font: 13pt \"楷体\";")
        self.label_3.setObjectName("label_3")
        self.pushButton_Bing = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_Bing.setGeometry(QtCore.QRect(250, 390, 181, 51))
        self.pushButton_Bing.setObjectName("pushButton_Bing")
        self.label_count = QtWidgets.QLabel(self.frame_2)
        self.label_count.setGeometry(QtCore.QRect(280, 460, 141, 20))
        self.label_count.setStyleSheet("font: 9pt \"楷体\";")
        self.label_count.setText("")
        self.label_count.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByKeyboard|QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextBrowserInteraction|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.label_count.setObjectName("label_count")
        self.stackedWidget = QtWidgets.QStackedWidget(self.frame_3)
        self.stackedWidget.setGeometry(QtCore.QRect(30, 500, 441, 80))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.stackedWidget.addWidget(self.page)
        self.page_true = QtWidgets.QWidget()
        self.page_true.setObjectName("page_true")
        self.label = QtWidgets.QLabel(self.page_true)
        self.label.setGeometry(QtCore.QRect(40, 10, 331, 51))
        self.label.setStyleSheet("color: rgb(0, 170, 0);\n"
"font: 12pt \"楷体\";")
        self.label.setObjectName("label")
        self.stackedWidget.addWidget(self.page_true)
        self.page_false = QtWidgets.QWidget()
        self.page_false.setObjectName("page_false")
        self.label_2 = QtWidgets.QLabel(self.page_false)
        self.label_2.setGeometry(QtCore.QRect(80, 10, 241, 51))
        self.label_2.setStyleSheet("color: rgb(255, 0, 0);\n"
"font: 12pt \"楷体\";")
        self.label_2.setObjectName("label_2")
        self.stackedWidget.addWidget(self.page_false)
        self.verticalLayout.addWidget(self.frame_3)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(70, 650, 481, 21))
        self.label_4.setObjectName("label_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_A.setText(_translate("MainWindow", "A"))
        self.pushButton_B.setText(_translate("MainWindow", "B"))
        self.pushButton_C.setText(_translate("MainWindow", "C"))
        self.pushButton_D.setText(_translate("MainWindow", "D"))
        self.label_ques.setText(_translate("MainWindow", "点击【随机出题】则可显示题目"))
        self.pushButton_question.setText(_translate("MainWindow", "随机出题"))
        self.label_3.setText(_translate("MainWindow", "题目："))
        self.pushButton_Bing.setText(_translate("MainWindow", "一键问Bing"))
        self.label.setText(_translate("MainWindow", "恭喜你回答正确！你真是个小天才"))
        self.label_2.setText(_translate("MainWindow", "回答错误！请仔细思考哦！"))
        self.label_4.setText(_translate("MainWindow", "@题目来源蔡宗远老师2023Spring课前课后测验  from Barry 2023.5"))
