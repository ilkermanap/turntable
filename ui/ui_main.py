# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QHBoxLayout,
    QLabel, QLayout, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_Turntable(object):
    def setupUi(self, Turntable):
        if not Turntable.objectName():
            Turntable.setObjectName(u"Turntable")
        Turntable.resize(816, 648)
        self.verticalLayout = QVBoxLayout(Turntable)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetMinimumSize)
        self.label_3 = QLabel(Turntable)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout.addWidget(self.label_3)

        self.cmbUSB = QComboBox(Turntable)
        self.cmbUSB.setObjectName(u"cmbUSB")
        self.cmbUSB.setMinimumSize(QSize(150, 0))

        self.horizontalLayout.addWidget(self.cmbUSB)

        self.label_2 = QLabel(Turntable)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.editFilename = QLineEdit(Turntable)
        self.editFilename.setObjectName(u"editFilename")

        self.horizontalLayout.addWidget(self.editFilename)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btnStart = QPushButton(Turntable)
        self.btnStart.setObjectName(u"btnStart")

        self.horizontalLayout.addWidget(self.btnStart)

        self.pushButton = QPushButton(Turntable)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout.addWidget(self.pushButton)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.lblCam = QLabel(Turntable)
        self.lblCam.setObjectName(u"lblCam")
        self.lblCam.setMinimumSize(QSize(800, 600))

        self.verticalLayout.addWidget(self.lblCam)


        self.retranslateUi(Turntable)
        self.btnStart.clicked.connect(Turntable.startCapture)
        self.pushButton.clicked.connect(Turntable.close)

        QMetaObject.connectSlotsByName(Turntable)
    # setupUi

    def retranslateUi(self, Turntable):
        Turntable.setWindowTitle(QCoreApplication.translate("Turntable", u"Dialog", None))
        self.label_3.setText(QCoreApplication.translate("Turntable", u"Arduino serial port", None))
        self.label_2.setText(QCoreApplication.translate("Turntable", u"Video file name", None))
        self.editFilename.setText(QCoreApplication.translate("Turntable", u"video.avi", None))
        self.btnStart.setText(QCoreApplication.translate("Turntable", u"Start", None))
        self.pushButton.setText(QCoreApplication.translate("Turntable", u"Exit", None))
        self.lblCam.setText("")
    # retranslateUi

