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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLabel,
    QLayout, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

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
        self.btnStart = QPushButton(Turntable)
        self.btnStart.setObjectName(u"btnStart")

        self.horizontalLayout.addWidget(self.btnStart)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.lblStatus = QLabel(Turntable)
        self.lblStatus.setObjectName(u"lblStatus")

        self.horizontalLayout.addWidget(self.lblStatus)

        self.btnConfig = QPushButton(Turntable)
        self.btnConfig.setObjectName(u"btnConfig")

        self.horizontalLayout.addWidget(self.btnConfig)

        self.btnClose = QPushButton(Turntable)
        self.btnClose.setObjectName(u"btnClose")

        self.horizontalLayout.addWidget(self.btnClose)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.lblCam = QLabel(Turntable)
        self.lblCam.setObjectName(u"lblCam")
        self.lblCam.setMinimumSize(QSize(800, 600))

        self.verticalLayout.addWidget(self.lblCam)


        self.retranslateUi(Turntable)
        self.btnStart.clicked.connect(Turntable.startCapture)
        self.btnClose.clicked.connect(Turntable.close)
        self.btnConfig.clicked.connect(Turntable.configure)

        QMetaObject.connectSlotsByName(Turntable)
    # setupUi

    def retranslateUi(self, Turntable):
        Turntable.setWindowTitle(QCoreApplication.translate("Turntable", u"Dialog", None))
        self.btnStart.setText(QCoreApplication.translate("Turntable", u"Start", None))
        self.lblStatus.setText(QCoreApplication.translate("Turntable", u"TextLabel", None))
        self.btnConfig.setText(QCoreApplication.translate("Turntable", u"Configure", None))
        self.btnClose.setText(QCoreApplication.translate("Turntable", u"Exit", None))
        self.lblCam.setText("")
    # retranslateUi

