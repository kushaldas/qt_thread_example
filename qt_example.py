#!/usr/bin/python3

import sys
import tempfile
import subprocess
from PyQt5 import QtWidgets

from mainwindow import Ui_MainWindow


class ExampleApp(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(ExampleApp, self).__init__(parent)
        self.setupUi(self)
        # Here we are telling to call git_clone method when
        # someone clicks on the pushButton.
        self.pushButton.clicked.connect(self.git_clone)

    # Here is the actual method which does git clone
    def git_clone(self):
        git_url = self.lineEdit.text()  # Get the git URL
        tmpdir = tempfile.mkdtemp()  # Creates a temporary directory
        cmd = "git clone {0} {1}".format(git_url, tmpdir)
        subprocess.check_output(cmd.split())  # Execute the command
        self.textEdit.setText(tmpdir)  # Show the output to the user


def main():
    app = QtWidgets.QApplication(sys.argv)
    form = ExampleApp()
    form.show()
    app.exec_()


if __name__ == '__main__':
    main()
