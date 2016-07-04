#-*- coding:utf-8 -*-
import sys
from PyQt4 import QtGui, QtCore
import random 
from train import *
class chat(QtGui.QWidget):

    def __init__(self):
        super(chat, self).__init__()

        self.initUI()

    def initUI(self):
        global talk,edit,s,s2
        s,s2= [],[]
        talk = QtGui.QTextBrowser()
        talk.setText('')        
        edit = QtGui.QLineEdit(self)

        send = QtGui.QPushButton("发送",self)
        grid = QtGui.QGridLayout()
        grid.setSpacing(10)


        grid.addWidget(talk, 1, 1)

 
        grid.addWidget(edit, 2, 1)
        grid.addWidget(send, 2, 2)

        self.setLayout(grid)

        self.connect(send,QtCore.SIGNAL('clicked()'),self.sendClicked)

        
        self.connect(edit, QtCore.SIGNAL('textChanged(QString)'),
            self.onChanged)


        self.setWindowTitle('chat')
        self.resize(400, 350)
    def onChanged(self, text):
        global t
        t = text
        edit.setText(t)
        edit.adjustSize()
        return t
    def sendClicked(self):
        
        b = self.onChanged(t)
        #m = ["你好","谢谢","再见","晚安"]
        mm = response(b)
        #mm = random.choice(m)
        s.append(b)
        s2.append(mm)
        te = ''
        for j,i in enumerate(s):
            te = te+"me:\t"+i+'\n'+"robot:\t"+s2[j]+'\n'
        talk.setText(te)
        edit.setText('')
        
		
        

app = QtGui.QApplication(sys.argv)
ex = chat()
ex.show()
sys.exit(app.exec_())