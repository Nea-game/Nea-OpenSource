# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Clicker.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QDoubleSpinBox, QGridLayout,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)
import file_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(300, 150)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(300, 150))
        MainWindow.setMaximumSize(QSize(300, 150))
        icon = QIcon()
        icon.addFile(u":/Icons/left_click_24dp_FILL0_wght400_GRAD0_opsz24.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"QWidget {\n"
"    color:white;\n"
"    background-color: #151719;\n"
"    font-family: 'Times New Roman', Times, serif;\n"
"    font-size: 20pt;\n"
"    font-weight: 600;\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #161a1e;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #1b1116;\n"
"}\n"
"\n"
"QDoubleSpinBox {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.Grid = QGridLayout()
        self.Grid.setObjectName(u"Grid")
        self.Start = QPushButton(self.centralwidget)
        self.Start.setObjectName(u"Start")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.Start.sizePolicy().hasHeightForWidth())
        self.Start.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setFamilies([u"Times New Roman"])
        font.setPointSize(20)
        font.setWeight(QFont.DemiBold)
        self.Start.setFont(font)
        self.Start.setCursor(QCursor(Qt.PointingHandCursor))

        self.Grid.addWidget(self.Start, 1, 0, 1, 1)

        self.Speed_info = QLabel(self.centralwidget)
        self.Speed_info.setObjectName(u"Speed_info")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.Speed_info.sizePolicy().hasHeightForWidth())
        self.Speed_info.setSizePolicy(sizePolicy2)
        self.Speed_info.setFont(font)
        self.Speed_info.setStyleSheet(u"color: #E6E6E6")

        self.Grid.addWidget(self.Speed_info, 3, 1, 1, 1)

        self.Speed_box = QDoubleSpinBox(self.centralwidget)
        self.Speed_box.setObjectName(u"Speed_box")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.Speed_box.sizePolicy().hasHeightForWidth())
        self.Speed_box.setSizePolicy(sizePolicy3)
        self.Speed_box.setFont(font)
        self.Speed_box.setCursor(QCursor(Qt.PointingHandCursor))
        self.Speed_box.setSingleStep(0.000001000000000)
        self.Speed_box.setDecimals(6)
        self.Speed_box.setStepType(QAbstractSpinBox.StepType.DefaultStepType)

        self.Grid.addWidget(self.Speed_box, 3, 0, 1, 1)

        self.Main_info = QLabel(self.centralwidget)
        self.Main_info.setObjectName(u"Main_info")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.Main_info.sizePolicy().hasHeightForWidth())
        self.Main_info.setSizePolicy(sizePolicy4)
        font1 = QFont()
        font1.setFamilies([u"Times New Roman"])
        font1.setPointSize(14)
        font1.setWeight(QFont.DemiBold)
        font1.setStyleStrategy(QFont.PreferAntialias)
        self.Main_info.setFont(font1)
        self.Main_info.setStyleSheet(u"color: #E6E6E6")
        self.Main_info.setWordWrap(True)

        self.Grid.addWidget(self.Main_info, 1, 1, 1, 1)


        self.verticalLayout.addLayout(self.Grid)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Clicker", None))
        self.Start.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.Speed_info.setText(QCoreApplication.translate("MainWindow", u"Speed", None))
        self.Main_info.setText(QCoreApplication.translate("MainWindow", u"Press start", None))
    # retranslateUi

