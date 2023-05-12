from PyQt5.QtWidgets import *
from project1_view import *

QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)


class Controller(QMainWindow, Ui_MainWindow):
    """
    Class representing the button controls for the calculator.
    """
    def __init__(self, *args, **kwargs):
        """
        Constructor to create initial state of the calculator.
        :param args:
        :param kwargs:
        """
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        self.pushButton_equal.clicked.connect(lambda: self.equal("="))
        self.pushButton_clear.clicked.connect(lambda: self.button_pressed("C"))

        self.pushButton_0.clicked.connect(lambda: self.button_pressed("0"))
        self.pushButton_1.clicked.connect(lambda: self.button_pressed("1"))
        self.pushButton_2.clicked.connect(lambda: self.button_pressed("2"))
        self.pushButton_3.clicked.connect(lambda: self.button_pressed("3"))
        self.pushButton_4.clicked.connect(lambda: self.button_pressed("4"))
        self.pushButton_5.clicked.connect(lambda: self.button_pressed("5"))
        self.pushButton_6.clicked.connect(lambda: self.button_pressed("6"))
        self.pushButton_7.clicked.connect(lambda: self.button_pressed("7"))
        self.pushButton_8.clicked.connect(lambda: self.button_pressed("8"))
        self.pushButton_9.clicked.connect(lambda: self.button_pressed("9"))

        self.pushButton_add.clicked.connect(lambda: self.button_pressed("+"))
        self.pushButton_subtract.clicked.connect(lambda: self.button_pressed("-"))
        self.pushButton_divide.clicked.connect(lambda: self.button_pressed("/"))
        self.pushButton_multiply.clicked.connect(lambda: self.button_pressed("*"))

    def button_pressed(self, pressed):
        """
        Method to update lineEdit_input with number and operator inputs from user.
        :param pressed: Value of button that user pressed.
        :return: None
        """
        if pressed == "C":
            self.lineEdit_input.setText("")
        else:
            self.lineEdit_input.setText(f'{self.lineEdit_input.text()}{pressed}')  # str of numbers and operators

    def equal(self, pressed):
        """
        Method to calculate input line and output correct answer.
        :param pressed:
        :return: None
        """
        screen = self.lineEdit_input.text()

        if pressed == "=":
            if self.lineEdit_input.text() == "":
                answer = 0
                self.lineEdit_input.setText(f'{answer}')  # 0
            elif "/0" in self.lineEdit_input.text():
                self.lineEdit_input.setText("DIVIDE BY ZERO ERROR")

            elif "++" in self.lineEdit_input.text():
                self.lineEdit_input.setText("SYNTAX ERROR")
            elif "+-" in self.lineEdit_input.text():
                self.lineEdit_input.setText("SYNTAX ERROR")
            elif "+*" in self.lineEdit_input.text():
                self.lineEdit_input.setText("SYNTAX ERROR")
            elif "+/" in self.lineEdit_input.text():
                self.lineEdit_input.setText("SYNTAX ERROR")

            elif "--" in self.lineEdit_input.text():
                self.lineEdit_input.setText("SYNTAX ERROR")
            elif "-+" in self.lineEdit_input.text():
                self.lineEdit_input.setText("SYNTAX ERROR")
            elif "-*" in self.lineEdit_input.text():
                self.lineEdit_input.setText("SYNTAX ERROR")
            elif "-/" in self.lineEdit_input.text():
                self.lineEdit_input.setText("SYNTAX ERROR")

            elif "**" in self.lineEdit_input.text():
                self.lineEdit_input.setText("SYNTAX ERROR")
            elif "*+" in self.lineEdit_input.text():
                self.lineEdit_input.setText("SYNTAX ERROR")
            elif "*-" in self.lineEdit_input.text():
                self.lineEdit_input.setText("SYNTAX ERROR")
            elif "*/" in self.lineEdit_input.text():
                self.lineEdit_input.setText("SYNTAX ERROR")

            elif "//" in self.lineEdit_input.text():
                self.lineEdit_input.setText("SYNTAX ERROR")
            elif "/+" in self.lineEdit_input.text():
                self.lineEdit_input.setText("SYNTAX ERROR")
            elif "/-" in self.lineEdit_input.text():
                self.lineEdit_input.setText("SYNTAX ERROR")
            elif "/*" in self.lineEdit_input.text():
                self.lineEdit_input.setText("SYNTAX ERROR")
            else:
                answer = eval(screen)
                self.lineEdit_input.setText(f'{answer}')  # float or integer

