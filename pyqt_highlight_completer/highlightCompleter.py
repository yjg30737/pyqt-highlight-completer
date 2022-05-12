from PyQt5.QtCore import Qt, pyqtSignal, QPoint
from PyQt5.QtGui import QTextCharFormat, QTextCursor
from PyQt5.QtWidgets import QWidget, QTableWidget, QApplication, QHeaderView, QTextBrowser, QMainWindow, \
    QVBoxLayout, QLineEdit, QListWidget


class HighlightCompleterTableWidget(QTableWidget):
    showText = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.__initUi()

    def __initUi(self):
        self.setWindowFlags(Qt.ToolTip)
        self.setColumnCount(1)

        self.horizontalHeader().setVisible(False)
        self.verticalHeader().setVisible(False)
        self.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.clicked.connect(self.__showText)

    def searchTexts(self, text):
        matched_texts_lst = []
        for i in range(self.rowCount()):
            widget = self.cellWidget(i, 0)
            if widget:
                widget_text = widget.toPlainText()
                if text.strip() != '':
                    if widget_text.startswith(text):
                        matched_texts_lst.append(text)
                        cursor = QTextCursor(widget.document())
                        self.__hightlightText(cursor, Qt.red, 0, len(text))
                        self.__hightlightText(cursor, Qt.black, len(text), len(widget_text))
                        self.showRow(i)
                    else:
                        self.hideRow(i)
                else:
                    cursor = QTextCursor(widget.document())
                    self.__hightlightText(cursor, Qt.black, 0, len(widget_text))
                    self.hideRow(i)
        return len(matched_texts_lst) > 0

    def __hightlightText(self, cursor, color, start, end):
        fmt = QTextCharFormat()
        fmt.setForeground(color)

        cursor.setPosition(start, QTextCursor.MoveAnchor)
        cursor.setPosition(end, QTextCursor.KeepAnchor)
        cursor.setCharFormat(fmt)

    def addText(self, text):
        tb = QTextBrowser()
        tb.setText(text)
        tb.setFrameStyle(0)
        tb.setTextInteractionFlags(Qt.NoTextInteraction)
        row_idx = self.rowCount()
        self.setRowCount(row_idx+1)
        self.setCellWidget(row_idx, 0, tb)
        self.hideRow(row_idx)

    def addTexts(self, texts: list):
        for i in range(len(texts)):
            self.addText(texts[i])

    def __showText(self, idx):
        widget = self.indexWidget(idx)
        if widget:
            self.showText.emit(widget.toPlainText())


class HighlightCompleterLineEdit(QLineEdit):
    def __init__(self):
        super().__init__()
        self.__initUi()

    def __initUi(self):
        self.__initHightlightTextCompleter()
        self.textChanged.connect(self.__textChanged)

    def __initHightlightTextCompleter(self):
        self.__completer = HighlightCompleterTableWidget()
        self.__completer.showText.connect(self.setText)

    def __textChanged(self, text):
        f = self.__completer.searchTexts(text)
        if f:
            self.__completer.move(self.mapToGlobal(QPoint(self.geometry().bottomLeft().x(),
                                                          self.geometry().bottomLeft().y())))
            self.__completer.setMinimumWidth(self.width())
            self.__completer.show()
        else:
            self.__completer.hide()

    def resizeEvent(self, e):
        if e.oldSize().width() > e.size().width():
            self.__completer.setFixedWidth(self.width())
        else:
            self.__completer.setMinimumWidth(self.width())
        return super().resizeEvent(e)

    def closeCompleter(self):
        self.__completer.hide()

    def addTexts(self, texts):
        self.__completer.addTexts(texts)


class HighlightCompleter(QWidget):
    def __init__(self):
        super().__init__()
        self.__initUi()

    def __initUi(self):
        self.__lineEdit = HighlightCompleterLineEdit()

        resultListWidget = QListWidget()

        lay = QVBoxLayout()
        lay.addWidget(self.__lineEdit)
        lay.addWidget(resultListWidget)
        lay.setContentsMargins(0, 0, 0, 0)

        widget = QWidget()
        widget.setLayout(lay)

        lay = QVBoxLayout()
        lay.addWidget(widget)

        self.setLayout(lay)

    def addTexts(self, texts: list):
        self.__lineEdit.addTexts(texts)

    def moveEvent(self, e):
        self.__lineEdit.closeCompleter()
        return super().moveEvent(e)

    def changeEvent(self, e):
        if e.type() == 99:
            self.__lineEdit.closeCompleter()
        return super().changeEvent(e)