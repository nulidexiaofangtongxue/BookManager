# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'book_borrow_info_window.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(827, 452)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setStyleSheet("font: 12pt \"宋体\";")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout.addWidget(self.comboBox)
        self.borrow_user_search_lineEdit = QtWidgets.QLineEdit(Form)
        self.borrow_user_search_lineEdit.setStyleSheet("font: 12pt \"宋体\";")
        self.borrow_user_search_lineEdit.setObjectName("borrow_user_search_lineEdit")
        self.horizontalLayout.addWidget(self.borrow_user_search_lineEdit)
        self.search_borrow_user_pushButton = QtWidgets.QPushButton(Form)
        self.search_borrow_user_pushButton.setStyleSheet("font: 12pt \"宋体\";")
        self.search_borrow_user_pushButton.setObjectName("search_borrow_user_pushButton")
        self.horizontalLayout.addWidget(self.search_borrow_user_pushButton)
        self.refresh_pushButton = QtWidgets.QPushButton(Form)
        self.refresh_pushButton.setStyleSheet("font: 12pt \"宋体\";")
        self.refresh_pushButton.setObjectName("refresh_pushButton")
        self.horizontalLayout.addWidget(self.refresh_pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setStyleSheet("font: 12pt \"宋体\";")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(8)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        self.verticalLayout.addWidget(self.tableWidget)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.comboBox.setItemText(0, _translate("Form", "用户"))
        self.comboBox.setItemText(1, _translate("Form", "书名"))
        self.comboBox.setItemText(2, _translate("Form", "出版社"))
        self.search_borrow_user_pushButton.setText(_translate("Form", "搜索"))
        self.refresh_pushButton.setText(_translate("Form", "刷新"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "借阅人"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "书名"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "出版社"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "出版日期"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "借出数量"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Form", "借出日期"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Form", "应还日期"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("Form", "借还状态"))

