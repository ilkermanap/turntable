# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'config.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFormLayout,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QSpinBox, QVBoxLayout,
    QWidget)

class Ui_dlgConfig(object):
    def setupUi(self, dlgConfig):
        if not dlgConfig.objectName():
            dlgConfig.setObjectName(u"dlgConfig")
        dlgConfig.resize(331, 176)
        self.verticalLayout = QVBoxLayout(dlgConfig)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label_3 = QLabel(dlgConfig)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_3)

        self.cmbUSB = QComboBox(dlgConfig)
        self.cmbUSB.setObjectName(u"cmbUSB")
        self.cmbUSB.setMinimumSize(QSize(150, 0))

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.cmbUSB)

        self.label_2 = QLabel(dlgConfig)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.editFilename = QLineEdit(dlgConfig)
        self.editFilename.setObjectName(u"editFilename")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.editFilename)

        self.label = QLabel(dlgConfig)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label)

        self.spinFrames = QSpinBox(dlgConfig)
        self.spinFrames.setObjectName(u"spinFrames")
        self.spinFrames.setMinimum(30)
        self.spinFrames.setMaximum(500)
        self.spinFrames.setDisplayIntegerBase(10)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.spinFrames)


        self.verticalLayout.addLayout(self.formLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btnOk = QPushButton(dlgConfig)
        self.btnOk.setObjectName(u"btnOk")

        self.horizontalLayout.addWidget(self.btnOk)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(dlgConfig)
        self.cmbUSB.currentIndexChanged.connect(dlgConfig.portChanged)
        self.btnOk.clicked.connect(dlgConfig.close)

        QMetaObject.connectSlotsByName(dlgConfig)
    # setupUi

    def retranslateUi(self, dlgConfig):
        dlgConfig.setWindowTitle(QCoreApplication.translate("dlgConfig", u"Dialog", None))
        self.label_3.setText(QCoreApplication.translate("dlgConfig", u"Arduino serial port", None))
        self.label_2.setText(QCoreApplication.translate("dlgConfig", u"Video file name", None))
        self.editFilename.setText(QCoreApplication.translate("dlgConfig", u"video.avi", None))
        self.label.setText(QCoreApplication.translate("dlgConfig", u"Frames", None))
        self.btnOk.setText(QCoreApplication.translate("dlgConfig", u"Ok", None))
    # retranslateUi

