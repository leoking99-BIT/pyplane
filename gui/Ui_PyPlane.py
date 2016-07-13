# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_PyPlane.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_pyplane(object):
    def setupUi(self, pyplane):
        pyplane.setObjectName(_fromUtf8("pyplane"))
        pyplane.resize(770, 757)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(pyplane.sizePolicy().hasHeightForWidth())
        pyplane.setSizePolicy(sizePolicy)
        pyplane.setMinimumSize(QtCore.QSize(770, 757))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/pyplane_logo.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        pyplane.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(pyplane)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.full = QtGui.QVBoxLayout()
        self.full.setSizeConstraint(QtGui.QLayout.SetNoConstraint)
        self.full.setSpacing(1)
        self.full.setObjectName(_fromUtf8("full"))
        self.inputBox = QtGui.QHBoxLayout()
        self.inputBox.setObjectName(_fromUtf8("inputBox"))
        self.syst = QtGui.QVBoxLayout()
        self.syst.setObjectName(_fromUtf8("syst"))
        self.title = QtGui.QLabel(self.centralwidget)
        self.title.setObjectName(_fromUtf8("title"))
        self.syst.addWidget(self.title)
        self.xDotBox = QtGui.QHBoxLayout()
        self.xDotBox.setObjectName(_fromUtf8("xDotBox"))
        self.xDotLabel = QtGui.QLabel(self.centralwidget)
        self.xDotLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.xDotLabel.setObjectName(_fromUtf8("xDotLabel"))
        self.xDotBox.addWidget(self.xDotLabel)
        self.xDotLineEdit = QtGui.QLineEdit(self.centralwidget)
        self.xDotLineEdit.setObjectName(_fromUtf8("xDotLineEdit"))
        self.xDotBox.addWidget(self.xDotLineEdit)
        self.submitButton = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.submitButton.sizePolicy().hasHeightForWidth())
        self.submitButton.setSizePolicy(sizePolicy)
        self.submitButton.setMinimumSize(QtCore.QSize(0, 0))
        self.submitButton.setMaximumSize(QtCore.QSize(100, 16777215))
        self.submitButton.setObjectName(_fromUtf8("submitButton"))
        self.xDotBox.addWidget(self.submitButton)
        self.syst.addLayout(self.xDotBox)
        self.yDotBox = QtGui.QHBoxLayout()
        self.yDotBox.setObjectName(_fromUtf8("yDotBox"))
        self.yDotLabel = QtGui.QLabel(self.centralwidget)
        self.yDotLabel.setObjectName(_fromUtf8("yDotLabel"))
        self.yDotBox.addWidget(self.yDotLabel)
        self.yDotLineEdit = QtGui.QLineEdit(self.centralwidget)
        self.yDotLineEdit.setObjectName(_fromUtf8("yDotLineEdit"))
        self.yDotBox.addWidget(self.yDotLineEdit)
        self.clearButton = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.clearButton.sizePolicy().hasHeightForWidth())
        self.clearButton.setSizePolicy(sizePolicy)
        self.clearButton.setMinimumSize(QtCore.QSize(0, 0))
        self.clearButton.setMaximumSize(QtCore.QSize(100, 16777215))
        self.clearButton.setObjectName(_fromUtf8("clearButton"))
        self.yDotBox.addWidget(self.clearButton)
        self.syst.addLayout(self.yDotBox)
        self.inputBox.addLayout(self.syst)
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.inputBox.addWidget(self.line)
        self.funcBox = QtGui.QVBoxLayout()
        self.funcBox.setObjectName(_fromUtf8("funcBox"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.funcBox.addWidget(self.label)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.yLabel = QtGui.QLabel(self.centralwidget)
        self.yLabel.setObjectName(_fromUtf8("yLabel"))
        self.horizontalLayout_6.addWidget(self.yLabel)
        self.yLineEdit = QtGui.QLineEdit(self.centralwidget)
        self.yLineEdit.setObjectName(_fromUtf8("yLineEdit"))
        self.horizontalLayout_6.addWidget(self.yLineEdit)
        self.FctPlotButton = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.FctPlotButton.sizePolicy().hasHeightForWidth())
        self.FctPlotButton.setSizePolicy(sizePolicy)
        self.FctPlotButton.setMinimumSize(QtCore.QSize(0, 0))
        self.FctPlotButton.setMaximumSize(QtCore.QSize(100, 16777215))
        self.FctPlotButton.setObjectName(_fromUtf8("FctPlotButton"))
        self.horizontalLayout_6.addWidget(self.FctPlotButton)
        self.funcBox.addLayout(self.horizontalLayout_6)
        self.verticalLayout_10 = QtGui.QVBoxLayout()
        self.verticalLayout_10.setObjectName(_fromUtf8("verticalLayout_10"))
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.slider = QtGui.QSlider(self.centralwidget)
        self.slider.setOrientation(QtCore.Qt.Horizontal)
        self.slider.setObjectName(_fromUtf8("slider"))
        self.horizontalLayout_8.addWidget(self.slider)
        self.FctClearButton = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.FctClearButton.sizePolicy().hasHeightForWidth())
        self.FctClearButton.setSizePolicy(sizePolicy)
        self.FctClearButton.setMinimumSize(QtCore.QSize(0, 0))
        self.FctClearButton.setMaximumSize(QtCore.QSize(100, 16777215))
        self.FctClearButton.setObjectName(_fromUtf8("FctClearButton"))
        self.horizontalLayout_8.addWidget(self.FctClearButton)
        self.verticalLayout_10.addLayout(self.horizontalLayout_8)
        self.funcBox.addLayout(self.verticalLayout_10)
        self.inputBox.addLayout(self.funcBox)
        self.full.addLayout(self.inputBox)
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tabWidget.setTabPosition(QtGui.QTabWidget.West)
        self.tabWidget.setDocumentMode(True)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setMaximumSize(QtCore.QSize(720, 16777215))
        self.tab.setObjectName(_fromUtf8("tab"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.tab)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.SettingsLayout = QtGui.QVBoxLayout()
        self.SettingsLayout.setObjectName(_fromUtf8("SettingsLayout"))
        self.SettingsWidgetPlaceholder = QtGui.QWidget(self.tab)
        self.SettingsWidgetPlaceholder.setObjectName(_fromUtf8("SettingsWidgetPlaceholder"))
        self.SettingsLayout.addWidget(self.SettingsWidgetPlaceholder)
        self.verticalLayout_3.addLayout(self.SettingsLayout)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.full.addWidget(self.tabWidget)
        self.logField = QtGui.QTextEdit(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logField.sizePolicy().hasHeightForWidth())
        self.logField.setSizePolicy(sizePolicy)
        self.logField.setMinimumSize(QtCore.QSize(0, 0))
        self.logField.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.logField.setFont(font)
        self.logField.setMouseTracking(False)
        self.logField.setAutoFillBackground(True)
        self.logField.setStyleSheet(_fromUtf8("QTextEdit { background-color: rgb(0, 0, 0) }"))
        self.logField.setFrameShape(QtGui.QFrame.NoFrame)
        self.logField.setFrameShadow(QtGui.QFrame.Plain)
        self.logField.setLineWidth(0)
        self.logField.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.logField.setTextInteractionFlags(QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.logField.setObjectName(_fromUtf8("logField"))
        self.full.addWidget(self.logField)
        self.gridLayout.addLayout(self.full, 0, 0, 1, 1)
        pyplane.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(pyplane)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 770, 24))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        pyplane.setMenuBar(self.menubar)
        self.actionNew = QtGui.QAction(pyplane)
        self.actionNew.setObjectName(_fromUtf8("actionNew"))
        self.actionOpen = QtGui.QAction(pyplane)
        self.actionOpen.setObjectName(_fromUtf8("actionOpen"))
        self.actionSave = QtGui.QAction(pyplane)
        self.actionSave.setObjectName(_fromUtf8("actionSave"))
        self.actionQuit = QtGui.QAction(pyplane)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.actionNullclines = QtGui.QAction(pyplane)
        self.actionNullclines.setObjectName(_fromUtf8("actionNullclines"))
        self.action = QtGui.QAction(pyplane)
        self.action.setObjectName(_fromUtf8("action"))
        self.action_2 = QtGui.QAction(pyplane)
        self.action_2.setObjectName(_fromUtf8("action_2"))
        self.actionPyPlane_Help = QtGui.QAction(pyplane)
        self.actionPyPlane_Help.setObjectName(_fromUtf8("actionPyPlane_Help"))
        self.actionAbout = QtGui.QAction(pyplane)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))

        self.retranslateUi(pyplane)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.actionQuit, QtCore.SIGNAL(_fromUtf8("activated()")), pyplane.close)
        QtCore.QMetaObject.connectSlotsByName(pyplane)

    def retranslateUi(self, pyplane):
        pyplane.setWindowTitle(_translate("pyplane", "MainWindow", None))
        self.title.setText(_translate("pyplane", "Dynamical System", None))
        self.xDotLabel.setText(_translate("pyplane", "x\' = ", None))
        self.xDotLineEdit.setPlaceholderText(_translate("pyplane", "y", None))
        self.submitButton.setText(_translate("pyplane", "Submit", None))
        self.yDotLabel.setText(_translate("pyplane", "y\' = ", None))
        self.yDotLineEdit.setPlaceholderText(_translate("pyplane", "x-x**3", None))
        self.clearButton.setText(_translate("pyplane", "Clear Trajectories", None))
        self.label.setText(_translate("pyplane", "Additional Function:", None))
        self.yLabel.setText(_translate("pyplane", "0 = f(x,y) =", None))
        self.yLineEdit.setPlaceholderText(_translate("pyplane", "x**2+y**2-4", None))
        self.FctPlotButton.setText(_translate("pyplane", "Plot", None))
        self.FctClearButton.setText(_translate("pyplane", "Clear Plots", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("pyplane", "Settings", None))
        self.actionNew.setText(_translate("pyplane", "New", None))
        self.actionOpen.setText(_translate("pyplane", "Open", None))
        self.actionSave.setText(_translate("pyplane", "Save", None))
        self.actionQuit.setText(_translate("pyplane", "Quit", None))
        self.actionNullclines.setText(_translate("pyplane", "Nullclines", None))
        self.action.setText(_translate("pyplane", "Vector Field", None))
        self.action_2.setText(_translate("pyplane", "...", None))
        self.actionPyPlane_Help.setText(_translate("pyplane", "PyPlane Help", None))
        self.actionAbout.setText(_translate("pyplane", "About", None))

import icons_rc
