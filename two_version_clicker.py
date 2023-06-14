import sys

from PyQt5 import QtCore, QtGui, QtWidgets

from FilClick.click import Clicker


class Ui_click(object):
    def setupUi(self, click):
        click.setObjectName("click")
        click.setEnabled(True)
        click.setFixedSize(650, 446)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed,
            QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(click.sizePolicy().hasHeightForWidth())
        click.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        click.setFont(font)
        click.setWindowOpacity(1.0)
        click.setAutoFillBackground(False)
        click.setStyleSheet(
            "background: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:1,\n"
            "stop:0 #5F149A,\n"
            "stop:0.5604 rgba(34, 72, 133, 0.64),\n"
            "stop:0.625 rgba(29, 53, 92, 0.86),\n"
            "stop:0.9999 #000003,\n"
            "stop:1 #27295E);\n"
            "\n"
        )
        click.setWindowFilePath("")

        self.NameApp = QtWidgets.QFrame(click)
        self.NameApp.setEnabled(True)
        self.NameApp.setGeometry(QtCore.QRect(335, 72, 300, 60))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed,
            QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.NameApp.sizePolicy().hasHeightForWidth()
        )
        self.NameApp.setSizePolicy(sizePolicy)
        self.NameApp.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.NameApp.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.NameApp.setAutoFillBackground(False)
        self.NameApp.setStyleSheet(
            "background-color: qlineargradient(spread:repeat,\n"
            "x1:0.505273, y1:0, x2:0.506, y2:1,\n"
            "stop:0.259887 rgba(166, 47, 208, 0.2),\n"
            "stop:1 rgba(60, 12, 255, 0));\n")
        self.NameApp.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.NameApp.setFrameShadow(QtWidgets.QFrame.Plain)
        self.NameApp.setLineWidth(1)
        self.NameApp.setMidLineWidth(11)
        self.NameApp.setObjectName("NameApp")

        self.Action = QtWidgets.QFrame(click)
        self.Action.setEnabled(True)
        self.Action.setGeometry(QtCore.QRect(335, 148, 300, 60))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed,
            QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Action.sizePolicy().hasHeightForWidth()
        )
        self.Action.setSizePolicy(sizePolicy)
        self.Action.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.Action.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.Action.setAutoFillBackground(False)
        self.Action.setStyleSheet(
            "background-color: qlineargradient(spread:repeat, x1:0.505273,\n"
            "y1:0, x2:0.506, y2:1,\n"
            "stop:0.259887 rgba(166, 47, 208, 0.2),\n"
            "stop:1 rgba(60, 12, 255, 0));\n"  # кастомный бекграунд
            "border: 2px solid qlineargradient(spread:repeat,\n"
            "x1:0.505273, y1:0, x2:0.506, y2:1,\n"
            "stop:0.259887 rgba(94, 33, 122, 1),\n"
            "stop:1 rgba(55, 34, 81, 0));\n")
        self.Action.setFrameShape(QtWidgets.QFrame.HLine)
        self.Action.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Action.setLineWidth(5)
        self.Action.setMidLineWidth(10)
        self.Action.setObjectName("Action")

        self.TitleAction = QtWidgets.QLabel(self.Action)
        self.TitleAction.setGeometry(QtCore.QRect(10, 10, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.TitleAction.setFont(font)
        self.TitleAction.setObjectName("TitleAction")

        self.SelectionAction = QtWidgets.QComboBox(self.Action)
        self.SelectionAction.setGeometry(QtCore.QRect(200, 10, 81, 31))
        self.SelectionAction.setFocusPolicy(QtCore.Qt.NoFocus)
        self.SelectionAction.setObjectName("SelectionAction")
        self.SelectionAction.addItem("")
        self.SelectionAction.addItem("")

        self.Interval = QtWidgets.QFrame(click)
        self.Interval.setEnabled(True)
        self.Interval.setGeometry(QtCore.QRect(335, 208, 300, 60))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed,
            QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Interval.sizePolicy().hasHeightForWidth()
        )
        self.Interval.setSizePolicy(sizePolicy)
        self.Interval.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.Interval.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.Interval.setAutoFillBackground(False)
        self.Interval.setStyleSheet(
            "background-color: qlineargradient(spread:repeat,\n"
            "x1:0.505273, y1:0, x2:0.506, y2:1,\n"
            "stop:0.259887 rgba(166, 47, 208, 0.2),\n"
            "stop:1 rgba(60, 12, 255, 0));\n"
            "border: 2px solid qlineargradient(spread:repeat,\n"
            "x1:0.505273, y1:0, x2:0.506, y2:1,\n"
            "stop:0.259887 rgba(94, 33, 122, 1),\n"
            "stop:1 rgba(55, 34, 81, 0));\n")
        self.Interval.setFrameShape(QtWidgets.QFrame.HLine)
        self.Interval.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Interval.setLineWidth(5)
        self.Interval.setMidLineWidth(10)
        self.Interval.setObjectName("Interval")

        self.TitleInterval = QtWidgets.QLabel(self.Interval)
        self.TitleInterval.setGeometry(QtCore.QRect(10, 10, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.TitleInterval.setFont(font)
        self.TitleInterval.setObjectName("TitleInterval")

        self.SelectionInterval = QtWidgets.QSlider(self.Interval)
        self.SelectionInterval.setGeometry(QtCore.QRect(180, 20, 91, 21))
        self.SelectionInterval.setMinimum(5)
        self.SelectionInterval.setMaximum(21)
        self.SelectionInterval.setPageStep(1)
        self.SelectionInterval.setProperty("value", 13)
        self.SelectionInterval.setSliderPosition(13)
        self.SelectionInterval.setOrientation(QtCore.Qt.Horizontal)
        self.SelectionInterval.setInvertedAppearance(True)
        self.SelectionInterval.setTickPosition(
            QtWidgets.QSlider.TicksBothSides
        )
        self.SelectionInterval.setTickInterval(4)
        self.SelectionInterval.setObjectName("SelectionInterval")

        self.HotKey = QtWidgets.QFrame(click)
        self.HotKey.setEnabled(True)
        self.HotKey.setGeometry(QtCore.QRect(335, 268, 300, 60))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed,
            QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.HotKey.sizePolicy().hasHeightForWidth()
        )
        self.HotKey.setSizePolicy(sizePolicy)
        self.HotKey.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.HotKey.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.HotKey.setAutoFillBackground(False)
        self.HotKey.setStyleSheet(
            "background-color: qlineargradient(spread:repeat,\n"
            "x1:0.505273, y1:0, x2:0.506, y2:1,\n"
            "stop:0.259887 rgba(166, 47, 208, 0.2),\n"
            "stop:1 rgba(60, 12, 255, 0));\n"
            "border: 2px solid qlineargradient(spread:repeat,\n"
            "x1:0.505273, y1:0, x2:0.506, y2:1,\n"
            "stop:0.259887 rgba(94, 33, 122, 1),\n"
            "stop:1 rgba(55, 34, 81, 0));\n")
        self.HotKey.setFrameShape(QtWidgets.QFrame.HLine)
        self.HotKey.setFrameShadow(QtWidgets.QFrame.Raised)
        self.HotKey.setLineWidth(5)
        self.HotKey.setMidLineWidth(10)
        self.HotKey.setObjectName("HotKey")

        self.TitleHotKey = QtWidgets.QLabel(self.HotKey)
        self.TitleHotKey.setGeometry(QtCore.QRect(20, 10, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.TitleHotKey.setFont(font)
        self.TitleHotKey.setLineWidth(0)
        self.TitleHotKey.setAlignment(QtCore.Qt.AlignCenter)
        self.TitleHotKey.setWordWrap(False)
        self.TitleHotKey.setIndent(15)
        self.TitleHotKey.setOpenExternalLinks(False)
        self.TitleHotKey.setTextInteractionFlags(
            QtCore.Qt.LinksAccessibleByMouse
        )
        self.TitleHotKey.setObjectName("TitleHotKey")

        self.SelectionHotKey = QtWidgets.QComboBox(self.HotKey)
        self.SelectionHotKey.setGeometry(QtCore.QRect(200, 10, 69, 31))
        self.SelectionHotKey.setFocusPolicy(QtCore.Qt.NoFocus)
        self.SelectionHotKey.setObjectName("SelectionHotKey")
        self.SelectionHotKey.addItem("")
        self.SelectionHotKey.addItem("")

        self.Stop = QtWidgets.QPushButton(click)
        self.Stop.setGeometry(QtCore.QRect(335, 328, 140, 46))
        self.Stop.setFocusPolicy(QtCore.Qt.NoFocus)
        self.Stop.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Stop.setStyleSheet(
            "background-color: qlineargradient(spread:pad,\n"
            "x1:0, y1:0, x2:0, y2:1,\n"
            "stop:0 rgba(229, 213, 189, 0.85),\n"
            "stop:0.5 rgba(94, 33, 122, 0.8),\n"
            "stop:1 rgba(60, 12, 255, 0));\n"
            "border: 2px solid qlineargradient(spread:repeat,\n"
            "x1:0.505273, y1:0, x2:0.506, y2:1,\n"
            "stop:0.259887 rgba(94, 33, 122, 1),\n"
            "stop:1 rgba(55, 34, 81, 0));\n")
        self.Stop.setIconSize(QtCore.QSize(16, 16))
        self.Stop.setAutoRepeat(False)
        self.Stop.setAutoRepeatDelay(300)
        self.Stop.setAutoDefault(False)
        self.Stop.setDefault(False)
        self.Stop.setObjectName("Stop")

        self.Start = QtWidgets.QPushButton(click)
        self.Start.setGeometry(QtCore.QRect(495, 328, 140, 46))
        self.Start.setFocusPolicy(QtCore.Qt.NoFocus)
        self.Start.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Start.setStyleSheet(
            "background-color: qlineargradient(spread:pad,\n"
            "x1:0, y1:0, x2:0, y2:1,\n"
            "stop:0 rgba(229, 213, 189, 0.85),\n"
            "stop:0.5 rgba(94, 33, 122, 0.8),\n"
            "stop:1 rgba(60, 12, 255, 0));\n"
            "border: 2px solid qlineargradient(spread:repeat,\n"
            "x1:0.505273, y1:0, x2:0.506, y2:1,\n"
            "stop:0.259887 rgba(94, 33, 122, 1),\n"
            "stop:1 rgba(55, 34, 81, 0));\n")
        self.Start.setIconSize(QtCore.QSize(16, 16))
        self.Start.setAutoRepeat(False)
        self.Start.setAutoRepeatDelay(300)
        self.Start.setAutoDefault(False)
        self.Start.setDefault(False)
        self.Start.setObjectName("Start")

        self.retranslateUi(click)
        QtCore.QMetaObject.connectSlotsByName(click)
        click.setTabOrder(self.SelectionAction, self.Stop)
        click.setTabOrder(self.Stop, self.Start)
        click.setTabOrder(self.Start, self.SelectionInterval)

        self.clicker = None
        self.start_and_stop_cliecker()

    def retranslateUi(self, click):
        _translate = QtCore.QCoreApplication.translate
        click.setWindowTitle(_translate("click", "click"))
        self.TitleAction.setText(_translate("click", "Mouse Action"))
        self.SelectionAction.setItemText(0, _translate("click", "left click"))
        self.SelectionAction.setItemText(1, _translate("click", "right click"))
        self.TitleInterval.setText(_translate("click", "Interval"))
        self.TitleHotKey.setText(_translate("click", "Hot Key"))
        self.SelectionHotKey.setItemText(0, _translate("click", "space"))
        self.SelectionHotKey.setItemText(1, _translate("click", "ctrl"))
        self.Stop.setText(_translate("click", "Stop"))
        self.Start.setText(_translate("click", "Start"))

    def start_and_stop_cliecker(self):
        self.Start.clicked.connect(lambda: self.performing_a_click())
        self.Stop.clicked.connect(lambda: self.stop_clicker())

    def performing_a_click(self):
        print(self.SelectionAction.currentText())
        print(self.SelectionInterval.value()/10)
        print(self.SelectionHotKey.currentText())

        buttom = self.SelectionAction.currentText()
        time_sleep = self.SelectionInterval.value()/10
        hot_key = self.SelectionHotKey.currentText()

        self.clicker = Clicker(
            buttom,
            time_sleep,
            hot_key
        )
        self.clicker.start()

    def stop_clicker(self):
        print('зашли в остановку кликера')
        if self.clicker is not None:
            print('stop')
            self.clicker.stop()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_click()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
