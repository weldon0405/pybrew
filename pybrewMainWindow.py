# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pybrewMainWindow.ui'
#
# Created: Tue Feb  2 17:40:55 2010
#      by: PyQt4 UI code generator 4.6.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(801, 495)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.targetTempLineEdit = QtGui.QLineEdit(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.targetTempLineEdit.sizePolicy().hasHeightForWidth())
        self.targetTempLineEdit.setSizePolicy(sizePolicy)
        self.targetTempLineEdit.setMinimumSize(QtCore.QSize(0, 0))
        self.targetTempLineEdit.setMaximumSize(QtCore.QSize(40, 28))
        self.targetTempLineEdit.setMaxLength(2)
        self.targetTempLineEdit.setObjectName("targetTempLineEdit")
        self.horizontalLayout_2.addWidget(self.targetTempLineEdit)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.runTempProfileButton = QtGui.QPushButton(self.centralwidget)
        self.runTempProfileButton.setCheckable(True)
        self.runTempProfileButton.setObjectName("runTempProfileButton")
        self.horizontalLayout_2.addWidget(self.runTempProfileButton)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tempQwtPlot = Qwt5.QwtPlot(self.centralwidget)
        self.tempQwtPlot.setObjectName("tempQwtPlot")
        self.horizontalLayout.addWidget(self.tempQwtPlot)
        self.Thermo = Qwt5.QwtThermo(self.centralwidget)
        self.Thermo.setAlarmColor(QtGui.QColor(0, 170, 127))
        self.Thermo.setAlarmEnabled(True)
        self.Thermo.setScalePosition(Qwt5.QwtThermo.RightScale)
        self.Thermo.setFillColor(QtGui.QColor(0, 0, 127))
        self.Thermo.setMaxValue(80.0)
        self.Thermo.setMinValue(20.0)
        self.Thermo.setObjectName("Thermo")
        self.horizontalLayout.addWidget(self.Thermo)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.valveButtonLayout = QtGui.QHBoxLayout()
        self.valveButtonLayout.setObjectName("valveButtonLayout")
        self.verticalLayout.addLayout(self.valveButtonLayout)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMaximumSize(QtCore.QSize(220, 16777215))
        self.groupBox.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.newTempButton = QtGui.QPushButton(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.newTempButton.sizePolicy().hasHeightForWidth())
        self.newTempButton.setSizePolicy(sizePolicy)
        self.newTempButton.setObjectName("newTempButton")
        self.horizontalLayout_4.addWidget(self.newTempButton)
        self.removeTempButton = QtGui.QPushButton(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.removeTempButton.sizePolicy().hasHeightForWidth())
        self.removeTempButton.setSizePolicy(sizePolicy)
        self.removeTempButton.setObjectName("removeTempButton")
        self.horizontalLayout_4.addWidget(self.removeTempButton)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.tempProfileTableView = QtGui.QTableView(self.groupBox)
        self.tempProfileTableView.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tempProfileTableView.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tempProfileTableView.setEditTriggers(QtGui.QAbstractItemView.AnyKeyPressed|QtGui.QAbstractItemView.DoubleClicked|QtGui.QAbstractItemView.EditKeyPressed|QtGui.QAbstractItemView.SelectedClicked)
        self.tempProfileTableView.setObjectName("tempProfileTableView")
        self.tempProfileTableView.horizontalHeader().setDefaultSectionSize(80)
        self.tempProfileTableView.horizontalHeader().setHighlightSections(False)
        self.tempProfileTableView.horizontalHeader().setStretchLastSection(True)
        self.tempProfileTableView.verticalHeader().setDefaultSectionSize(0)
        self.tempProfileTableView.verticalHeader().setMinimumSectionSize(0)
        self.verticalLayout_2.addWidget(self.tempProfileTableView)
        self.horizontalLayout_3.addWidget(self.groupBox)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 801, 24))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionSave_temp_profile = QtGui.QAction(MainWindow)
        self.actionSave_temp_profile.setObjectName("actionSave_temp_profile")
        self.actionLoad_temp_profile = QtGui.QAction(MainWindow)
        self.actionLoad_temp_profile.setObjectName("actionLoad_temp_profile")
        self.actionSave_temp_data = QtGui.QAction(MainWindow)
        self.actionSave_temp_data.setObjectName("actionSave_temp_data")
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())
        self.toolBar.addAction(self.actionSave_temp_data)
        self.toolBar.addAction(self.actionSave_temp_profile)
        self.toolBar.addAction(self.actionLoad_temp_profile)
        self.label.setBuddy(self.targetTempLineEdit)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.targetTempLineEdit, QtCore.SIGNAL("editingFinished()"), MainWindow.setTargetTempEvent)
        QtCore.QObject.connect(self.newTempButton, QtCore.SIGNAL("clicked()"), MainWindow.newTargetTempEvent)
        QtCore.QObject.connect(self.removeTempButton, QtCore.SIGNAL("clicked()"), MainWindow.removeTargetTempEvent)
        QtCore.QObject.connect(self.runTempProfileButton, QtCore.SIGNAL("toggled(bool)"), self.targetTempLineEdit.setDisabled)
        QtCore.QObject.connect(self.runTempProfileButton, QtCore.SIGNAL("toggled(bool)"), MainWindow.runTempProfileToggledEvent)
        QtCore.QObject.connect(self.actionLoad_temp_profile, QtCore.SIGNAL("triggered()"), MainWindow.loadTempProfileEvent)
        QtCore.QObject.connect(self.actionSave_temp_profile, QtCore.SIGNAL("triggered()"), MainWindow.saveTempProfileEvent)
        QtCore.QObject.connect(self.actionSave_temp_data, QtCore.SIGNAL("triggered()"), MainWindow.saveTempDataEvent)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "pyBrew", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Target temp", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "°C", None, QtGui.QApplication.UnicodeUTF8))
        self.runTempProfileButton.setText(QtGui.QApplication.translate("MainWindow", "Run temp profile", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("MainWindow", "Temp profile", None, QtGui.QApplication.UnicodeUTF8))
        self.newTempButton.setText(QtGui.QApplication.translate("MainWindow", "New", None, QtGui.QApplication.UnicodeUTF8))
        self.removeTempButton.setText(QtGui.QApplication.translate("MainWindow", "Remove", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar.setWindowTitle(QtGui.QApplication.translate("MainWindow", "toolBar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setText(QtGui.QApplication.translate("MainWindow", "Exit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave_temp_profile.setText(QtGui.QApplication.translate("MainWindow", "Save temp profile", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLoad_temp_profile.setText(QtGui.QApplication.translate("MainWindow", "Load temp profile", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave_temp_data.setText(QtGui.QApplication.translate("MainWindow", "Save temp data", None, QtGui.QApplication.UnicodeUTF8))

from PyQt4 import Qwt5

class MainWindow(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None, f=QtCore.Qt.WindowFlags()):
        QtGui.QMainWindow.__init__(self, parent, f)

        self.setupUi(self)

