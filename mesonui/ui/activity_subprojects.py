# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'data/mesonui-layout/activity_subprojects.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Activity_Wrap_Dialog:
    def setupUi(self, Activity_Wrap_Dialog):
        Activity_Wrap_Dialog.setObjectName("Activity_Wrap_Dialog")
        Activity_Wrap_Dialog.resize(741, 422)
        Activity_Wrap_Dialog.setStyleSheet("")
        self.control_push_ok = QtWidgets.QPushButton(Activity_Wrap_Dialog)
        self.control_push_ok.setGeometry(QtCore.QRect(20, 370, 167, 24))
        self.control_push_ok.setStyleSheet("")
        self.control_push_ok.setObjectName("control_push_ok")
        self.groupBox = QtWidgets.QGroupBox(Activity_Wrap_Dialog)
        self.groupBox.setGeometry(QtCore.QRect(0, 0, 741, 361))
        self.groupBox.setStyleSheet("")
        self.groupBox.setObjectName("groupBox")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(20, 30, 81, 71))
        self.label_5.setAutoFillBackground(False)
        self.label_5.setStyleSheet("")
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap(":/icon/mesonui-icon/meson_modern.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.layoutWidget = QtWidgets.QWidget(self.groupBox)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 130, 701, 32))
        self.layoutWidget.setStyleSheet("")
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.control_push_download = QtWidgets.QPushButton(self.layoutWidget)
        self.control_push_download.setStyleSheet("")
        self.control_push_download.setObjectName("control_push_download")
        self.horizontalLayout.addWidget(self.control_push_download)
        self.control_push_update = QtWidgets.QPushButton(self.layoutWidget)
        self.control_push_update.setStyleSheet("")
        self.control_push_update.setObjectName("control_push_update")
        self.horizontalLayout.addWidget(self.control_push_update)
        self.control_push_checkout = QtWidgets.QPushButton(self.layoutWidget)
        self.control_push_checkout.setStyleSheet("")
        self.control_push_checkout.setObjectName("control_push_checkout")
        self.horizontalLayout.addWidget(self.control_push_checkout)
        self.entry_subproject_item = QtWidgets.QLineEdit(self.groupBox)
        self.entry_subproject_item.setGeometry(QtCore.QRect(120, 100, 601, 21))
        self.entry_subproject_item.setObjectName("entry_subproject_item")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(20, 100, 101, 21))
        self.label.setObjectName("label")
        self.info = QtWidgets.QPlainTextEdit(self.groupBox)
        self.info.setGeometry(QtCore.QRect(120, 30, 601, 61))
        self.info.setStyleSheet("")
        self.info.setObjectName("info")
        self.output_console_dashboard = QtWidgets.QGroupBox(self.groupBox)
        self.output_console_dashboard.setGeometry(QtCore.QRect(0, 170, 741, 191))
        self.output_console_dashboard.setFocusPolicy(QtCore.Qt.NoFocus)
        self.output_console_dashboard.setStyleSheet("")
        self.output_console_dashboard.setObjectName("output_console_dashboard")
        self.output_console = QtWidgets.QPlainTextEdit(self.output_console_dashboard)
        self.output_console.setGeometry(QtCore.QRect(20, 30, 701, 151))
        self.output_console.setStyleSheet("")
        self.output_console.setReadOnly(True)
        self.output_console.setPlainText("")
        self.output_console.setObjectName("output_console")

        self.retranslateUi(Activity_Wrap_Dialog)
        QtCore.QMetaObject.connectSlotsByName(Activity_Wrap_Dialog)

    def retranslateUi(self, Activity_Wrap_Dialog):
        _translate = QtCore.QCoreApplication.translate
        Activity_Wrap_Dialog.setWindowTitle(_translate("Activity_Wrap_Dialog", "Subprojects Manager"))
        self.control_push_ok.setText(_translate("Activity_Wrap_Dialog", "OK"))
        self.groupBox.setTitle(_translate("Activity_Wrap_Dialog", "Subprojects view:"))
        self.control_push_download.setText(_translate("Activity_Wrap_Dialog", "Download"))
        self.control_push_update.setText(_translate("Activity_Wrap_Dialog", "Update"))
        self.control_push_checkout.setText(_translate("Activity_Wrap_Dialog", "Checkout"))
        self.entry_subproject_item.setPlaceholderText(_translate("Activity_Wrap_Dialog", "   subproject name here"))
        self.label.setText(_translate("Activity_Wrap_Dialog", "subproject:"))
        self.info.setPlainText(_translate("Activity_Wrap_Dialog", "Subprojects is a subcommand of Meson that allows you to manage your source dependencies."))
        self.output_console_dashboard.setTitle(_translate("Activity_Wrap_Dialog", "Output Console:"))

from . import resource_rc