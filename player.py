
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QFileDialog, QMainWindow, QSlider, QStyle, QToolTip
from PyQt5.QtWinExtras import QWinThumbnailToolBar, QWinThumbnailToolButton
from PyQt5.QtGui import QIcon

from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer, QMediaPlaylist

import sys

import ctypes



class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.resize(800, 600)
        self.setMinimumSize(QtCore.QSize(800, 600))
        self.setMaximumSize(QtCore.QSize(800, 600))
        self.setWindowIcon(QIcon('icon.png'))

        # Thumbnail toolbar
        self.toolbar = QWinThumbnailToolBar(self)
        myappid = 'akash.groove.music.player.1'
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

        self.initUI()

    def initUI(self):
        self.mediaPlayer = QMediaPlayer()
        self.mediaPlayer.setVolume(50)

        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")

        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1.setGeometry(QtCore.QRect(300, 210, 181, 71))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.label1.setFont(font)
        self.label1.setAlignment(QtCore.Qt.AlignCenter)
        self.label1.setObjectName("label1")

        self.label2 = QtWidgets.QLabel(self.centralwidget)
        self.label2.setGeometry(QtCore.QRect(300, 210, 181, 71))
        self.label2.setFont(font)
        self.label2.setAlignment(QtCore.Qt.AlignCenter)
        self.label2.setObjectName("label2")

        self.label3 = QtWidgets.QLabel(self.centralwidget)
        self.label3.setGeometry(QtCore.QRect(300, 210, 181, 71))
        self.label3.setFont(font)
        self.label3.setAlignment(QtCore.Qt.AlignCenter)
        self.label3.setObjectName("label3")

        self.Middle = QtWidgets.QToolButton(self.centralwidget)
        self.Middle.setGeometry(QtCore.QRect(380, 450, 31, 31))
        self.Middle.setObjectName("Middle")
        self.Middle.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
        self.Middle.setEnabled(False)

        self.Previous = QtWidgets.QToolButton(self.centralwidget)
        self.Previous.setGeometry(QtCore.QRect(330, 450, 31, 31))
        self.Previous.setObjectName("Previous")
        self.Previous.setIcon(self.style().standardIcon(
            QStyle.SP_MediaSkipBackward))
        self.Previous.clicked.connect(lambda: self.control_playlist(-1))

        self.next = QtWidgets.QToolButton(self.centralwidget)
        self.next.setGeometry(QtCore.QRect(430, 450, 31, 31))
        self.next.setObjectName("next")
        self.next.setIcon(self.style().standardIcon(
            QStyle.SP_MediaSkipForward))
        self.next.clicked.connect(lambda: self.control_playlist(1))

        self.hSlider = QtWidgets.QSlider(self.centralwidget)
        self.hSlider.setGeometry(QtCore.QRect(110, 530, 581, 20))
        self.hSlider.setOrientation(QtCore.Qt.Horizontal)
        self.hSlider.setObjectName("hSlider")
        self.hSlider.setRange(0, 0)
        self.hSlider.sliderMoved.connect(self.set_position)
        # self.hSlider.setTickPosition(QSlider.TicksBothSides)
        self.hSlider.setTickPosition(QSlider.TicksAbove)

        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")

        self.menuMedia = QtWidgets.QMenu(self.menubar)
        self.menuMedia.setObjectName("menuMedia")

        self.menuPlayback = QtWidgets.QMenu(self.menubar)
        self.menuPlayback.setObjectName("menuPlayback")

        self.menuAudio = QtWidgets.QMenu(self.menubar)
        self.menuAudio.setObjectName("menuAudio")

        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.actionOpen_File = QtWidgets.QAction(self)
        self.actionOpen_File.setObjectName("actionOpen_File")
        self.actionOpen_File.setIcon(
            self.style().standardIcon(QStyle.SP_FileIcon))

        self.actionOpen_Files = QtWidgets.QAction(self)
        self.actionOpen_Files.setObjectName("actionOpen_Files")
        self.actionOpen_Files.setIcon(
            self.style().standardIcon(QStyle.SP_FileDialogNewFolder))
        self.actionOpen_Files.triggered.connect(self.open_files)

        self.actionQuit = QtWidgets.QAction(self)
        self.actionQuit.setObjectName("actionQuit")
        self.actionQuit.setIcon(
            self.style().standardIcon(QStyle.SP_DialogCancelButton))

        self.actionPlay = QtWidgets.QAction(self)
        self.actionPlay.setObjectName("actionPlay")
        self.actionPlay.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
        self.actionPlay.setEnabled(False)

        self.actionPause = QtWidgets.QAction(self)
        self.actionPause.setObjectName("actionPause")
        self.actionPause.setIcon(
            self.style().standardIcon(QStyle.SP_MediaPause))

        self.actionStop = QtWidgets.QAction(self)
        self.actionStop.setObjectName("actionStop")
        self.actionStop.setIcon(self.style().standardIcon(QStyle.SP_MediaStop))
        self.actionStop.triggered.connect(self.stop_music)
        self.actionStop.setEnabled(False)

        self.actionPrevious = QtWidgets.QAction(self)
        self.actionPrevious.setObjectName("actionPrevious")
        self.actionPrevious.setIcon(
            self.style().standardIcon(QStyle.SP_MediaSkipBackward))

        self.actionNext = QtWidgets.QAction(self)
        self.actionNext.setObjectName("actionNext")
        self.actionNext.setIcon(
            self.style().standardIcon(QStyle.SP_MediaSkipForward))

        self.actionIncrease_Volume = QtWidgets.QAction(self)
        self.actionIncrease_Volume.setObjectName("actionIncrease_Volume")
        self.actionIncrease_Volume.setIcon(QIcon('vup.svg'))
        self.actionIncrease_Volume.setShortcut("Ctrl++")
        self.actionIncrease_Volume.triggered.connect(
            lambda: self.control_volume(1))

        self.actionDecrease_Volume = QtWidgets.QAction(self)
        self.actionDecrease_Volume.setObjectName("actionDecrease_Volume")
        self.actionDecrease_Volume.triggered.connect(
            lambda: self.control_volume(-1))
        self.actionDecrease_Volume.setIcon(QIcon('vdown.svg'))
        self.actionDecrease_Volume.setShortcut("Ctrl+-")

        self.actionMute = QtWidgets.QAction(self)
        self.actionMute.setObjectName("actionMute")
        self.actionMute.triggered.connect(lambda: self.control_volume(0))
        self.actionMute.setIcon(QIcon('vmute.svg'))
        self.actionMute.setShortcut("Ctrl+0")

        self.actionAbout = QtWidgets.QAction(self)
        self.actionAbout.setObjectName("actionAbout")
        self.actionAbout.setIcon(QIcon('info.svg'))

        self.menuMedia.addAction(self.actionOpen_File)
        self.menuMedia.addAction(self.actionOpen_Files)
        self.menuMedia.addAction(self.actionQuit)

        self.menuPlayback.addAction(self.actionPlay)
        self.menuPlayback.addAction(self.actionPause)
        self.menuPlayback.addAction(self.actionStop)
        self.menuPlayback.addAction(self.actionPrevious)
        self.menuPlayback.addAction(self.actionNext)

        self.menuAudio.addAction(self.actionIncrease_Volume)
        self.menuAudio.addAction(self.actionDecrease_Volume)
        self.menuAudio.addAction(self.actionMute)

        self.menuHelp.addAction(self.actionAbout)

        self.menubar.addAction(self.menuMedia.menuAction())
        self.menubar.addAction(self.menuPlayback.menuAction())
        self.menubar.addAction(self.menuAudio.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

        self.actionPlay.triggered.connect(self.control_music)
        self.actionPause.triggered.connect(self.control_music)
        self.actionPause.setEnabled(False)
        self.actionQuit.triggered.connect(self.quit)

        self.Middle.clicked.connect(self.control_music)

        #Pause, Next, Previous @Taskbar
        self.toolPrev = QWinThumbnailToolButton(self.toolbar)
        self.toolPrev.setToolTip("Previous Song")
        self.toolPrev.setIcon(self.style().standardIcon(
            QStyle.SP_MediaSkipBackward))
        self.toolbar.addButton(self.toolPrev)

        self.toolMiddle = QWinThumbnailToolButton(self.toolbar)
        self.toolMiddle.setToolTip("Play")
        self.toolMiddle.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
        self.toolMiddle.setEnabled(False)
        self.toolbar.addButton(self.toolMiddle)
        self.toolMiddle.clicked.connect(self.control_music)

        self.toolNext = QWinThumbnailToolButton(self.toolbar)
        self.toolNext.setToolTip("Next Song")
        self.toolNext.setIcon(
            self.style().standardIcon(QStyle.SP_MediaSkipForward))
        self.toolbar.addButton(self.toolNext)

        # music signals
        self.mediaPlayer.positionChanged.connect(self.position_changed)
        self.mediaPlayer.durationChanged.connect(self.duration_changed)
        self.mediaPlayer.stateChanged.connect(self.state_changed)
        # self.mediaPlayer.mediaChanged.connect(self.media_changed)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Music Player | Developed by @Rohan"))

        self.label1.setStyleSheet(
            "background-image : url(bg.png); border : 2px ")
        self.label1.resize(800, 600)
        self.label1.move(0, 0)
        self.label1.setScaledContents(True)

        self.label2.setStyleSheet(
            "background-color: rgba(255, 255, 255, 100);")
        self.label2.resize(800, 160)
        self.label2.move(0, 440)

        #self.label3.setStyleSheet("background-image : url(bg.png); border : 2px ")
        #self.label3.setStyleSheet("background-color: rgba(255, 255, 255, 100);")
        #self.label3.resize(200, 133)
        #self.label3.move(300, 233)
        #movie = QtGui.QMovie("paying.gif")
        # self.label3.setMovie(movie)
        # movie.start()
        # self.label3.setScaledContents(True)

        self.menuMedia.setTitle(_translate("MainWindow", "Media"))
        self.menuPlayback.setTitle(_translate("MainWindow", "Playback"))
        self.menuAudio.setTitle(_translate("MainWindow", "Audio"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))

        self.actionOpen_File.setText(_translate("MainWindow", "Open File"))
        self.actionOpen_File.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionOpen_File.triggered.connect(self.open_file)

        self.actionOpen_Files.setText(_translate("MainWindow", "Open Files"))
        self.actionOpen_Files.setShortcut(
            _translate("MainWindow", "Ctrl+Shift+O"))

        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        self.actionQuit.setShortcut(_translate("MainWindow", "Ctrl+Q"))

        self.actionPlay.setText(_translate("MainWindow", "Play"))
        self.actionPlay.setShortcut(_translate("MainWindow", "Ctrl+P"))

        self.actionPause.setText(_translate("MainWindow", "Pause"))
        self.actionPause.setShortcut(_translate("Mainwindow", "Ctrl+Shift+P"))

        self.actionStop.setText(_translate("MainWindow", "Stop"))

        self.actionPrevious.setText(_translate("MainWindow", "Previous"))

        self.actionNext.setText(_translate("MainWindow", "Next"))

        self.actionIncrease_Volume.setText(
            _translate("MainWindow", "Increase Volume"))

        self.actionDecrease_Volume.setText(
            _translate("MainWindow", "Decrease Volume"))

        self.actionMute.setText(_translate("MainWindow", "Mute"))

        self.actionAbout.setText(_translate("MainWindow", "About"))

    def stop_music(self):
        self.mediaPlayer.stop()

    def control_music(self):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.mediaPlayer.pause()
        else:
            self.mediaPlayer.play()

    '''def media_changed(self):
        print(self.playlist.mediaCount())
        if(self.playlist.currentIndex()+1>self.playlist.mediaCount()):
            self.next.setEnabled(False)
        elif(self.next.isEnabled() == False):
            self.next.setEnabled(True)
        if(self.playlist.currentIndex()-1<0):
            self.Previous.setEnabled(False)
        elif(self.Previous.isEnabled()==False):
            self.Previous.setEnabled(True)'''

    def state_changed(self):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.toolMiddle.setIcon(
                self.style().standardIcon(QStyle.SP_MediaPause))
            self.Middle.setIcon(
                self.style().standardIcon(QStyle.SP_MediaPause))
            self.actionPlay.setEnabled(False)
            self.actionPause.setEnabled(True)
            self.toolMiddle.setEnabled(True)
            self.actionStop.setEnabled(True)
        elif self.mediaPlayer.state() == QMediaPlayer.PausedState:
            self.toolMiddle.setIcon(
                self.style().standardIcon(QStyle.SP_MediaPlay))
            self.Middle.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
            self.actionPlay.setEnabled(True)
            self.actionPause.setEnabled(False)
        else:
            self.Middle.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
            self.toolMiddle.setIcon(
                self.style().standardIcon(QStyle.SP_MediaPlay))
            self.toolMiddle.setEnabled(False)
            self.actionPause.setEnabled(False)
            self.actionPlay.setEnabled(True)
            self.actionStop.setEnabled(False)
            self.hSlider.setValue(0)

    def control_volume(self, task):
        curr_volume = self.mediaPlayer.volume()
        if(task == 1):
            if(curr_volume != 100):
                self.mediaPlayer.setVolume(curr_volume + 5)
            else:
                self.x, self.y = self.pos().x(), self.pos().y()
                QToolTip.showText(QtCore.QPoint(self.x+330, self.y+445), "Max Volume Reached",
                                  QtWidgets.QWidget(self), QtCore.QRect(300, 210, 181, 71), 1200)

        elif(task == -1):
            if(curr_volume != 0):
                self.mediaPlayer.setVolume(curr_volume - 5)
            else:
                if(QToolTip.isVisible() == False):
                    self.x, self.y = self.pos().x(), self.pos().y()
                    QToolTip.showText(QtCore.QPoint(self.x+330, self.y+445), "Min Volume Reached",
                                      QtWidgets.QWidget(self), QtCore.QRect(300, 210, 181, 71), 1200)
        else:
            self.mediaPlayer.setMuted(not self.mediaPlayer.isMuted())

    def control_playlist(self, task):
        if(task == 1):
            if(self.playlist.currentIndex()+1 != self.playlist.mediaCount()):
                self.playlist.setCurrentIndex(self.playlist.nextIndex())
        if(task == -1):
            if(self.playlist.currentIndex()-1 >= 0):
                self.playlist.setCurrentIndex(self.playlist.previousIndex())

    def open_file(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Open File")

        if filename != '':
            self.stop_music()
            self.mediaPlayer.setMedia(QMediaContent(
                QtCore.QUrl.fromLocalFile(filename)))
            self.actionPlay.setEnabled(True)
            self.Middle.setEnabled(True)

    def open_files(self):
        filenames, _ = QFileDialog.getOpenFileNames(self, "Open File")
        self.playlist = QMediaPlaylist(self.mediaPlayer)
        filee = list(map(QMediaContent, list(
            map(QtCore.QUrl.fromLocalFile, filenames))))

        if len(filenames) != 0:
            # self.stop_music()
            self.actionPlay.setEnabled(True)
            self.Middle.setEnabled(True)
            self.playlist.addMedia(filee)
            self.mediaPlayer.setPlaylist(self.playlist)
            self.playlist.setCurrentIndex(0)

    def position_changed(self, position):
        self.hSlider.setValue(position)
        # print(position)

    def duration_changed(self, duration):
        self.hSlider.setRange(0, duration)
        # print(duration)

    def set_position(self, position):
        self.mediaPlayer.setPosition(position)

    def update(self):
        self.label1.adjustSize()

    def quit(self):
        sys.exit(0)

    def showEvent(self, event):
        super(MyWindow, self).showEvent(event)
        if not self.toolbar.window():
            self.toolbar.setWindow(self.windowHandle())


def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())


window()
