#!/usr/bin/python3

import sys
import tempfile
import subprocess
from PyQt5 import QtWidgets
from PyQt5.QtCore import QThread, pyqtSignal

from mainwindow import Ui_MainWindow


class CloneThread(QThread):
    signal = pyqtSignal('PyQt_PyObject')

    def __init__(self):
        QThread.__init__(self)
        self.output = ""
        self.git_url = ""

    def run(self):
        tmpdir = tempfile.mkdtemp()
        cmd = "git clone {0} {1}".format(self.git_url, tmpdir)
        subprocess.check_output(cmd.split())
        self.signal.emit(tmpdir)


class ExampleApp(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(ExampleApp, self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.git_clone)
        self.git_thread = CloneThread()
        self.git_thread.signal.connect(self.finished)

    def git_clone(self):
        self.git_thread.git_url = self.lineEdit.text()
        self.pushButton.setEnabled(False)
        self.lineEdit.setText("Started git clone operation.")
        self.git_thread.start()

    def finished(self, result):
        self.textEdit.setText("Cloned at {0}".format(result))
        self.pushButton.setEnabled(True)


def main():
    app = QtWidgets.QApplication(sys.argv)
    form = ExampleApp()
    form.show()
    app.exec_()


if __name__ == '__main__':
    main()
