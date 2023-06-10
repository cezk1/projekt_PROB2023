from PyQt5.QtWidgets import QPushButton, QFileDialog
import os
import sys

class ChooseButton(QPushButton):
    def __init__(self, button_clicked_function):
        super().__init__()
        self.__btn_clicked = button_clicked_function
        self.__setup_button()

    def __setup_button(self):
        self.setText("Open file explorer")

        self.clicked.connect(self.__open_files_explorer)

    def __open_files_explorer(self):
        starting_dir = os.path.dirname(sys.argv[0])  # current dir
        options = QFileDialog.DontUseNativeDialog
        parent = None

        potential_file, _ = QFileDialog.getOpenFileName(parent, "Choose proper xlsx file",
                                                        starting_dir, "XLSX (*.xlsx);;All Files (*)", options=options)

        print(potential_file)

        if potential_file:
            self.__btn_clicked(potential_file)
        else:
            print("File chooser error")
