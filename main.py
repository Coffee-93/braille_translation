from PyQt5.QtWidgets import *
from PyQt5 import QtGui
from PyQt5 import QtCore
import pyqtgraph as pg

import sys

class test_extractor(QWidget):
    def __init__(self, parent = None):
        super(test_extractor, self).__init__(parent)
		
        layout = QGridLayout()
    
        #File select
        self.fileSelect = QPushButton("Select Image")
        self.fileSelect.clicked.connect(self.getfile)
    
        #Image show
        self.image = QLabel()
        #self.image = pg.ImageView()
    
        #Text Outputs
        self.tesserect_label = QLabel()
        self.tesserect_label.setText("Tesserect:")
        self.tesserect_text = QLabel()
        self.tesserect_text.setText("Tesserect")
    
        self.spellcheck_label = QLabel()
        self.spellcheck_label.setText("Spell Check:")
        self.spellcheck_text = QLabel()
        self.spellcheck_text.setText("Spell Check")
    
        self.cv_label = QLabel()
        self.cv_label.setText("CV:")
        self.cv_text = QLabel()
        self.cv_text.setText("CV")
    
        self.cv_spell_label = QLabel()
        self.cv_spell_label.setText("CV Spell:")
        self.cv_spell_text = QLabel()
        self.cv_spell_text.setText("CV Spell")
    
        #Grid setup
    
        layout.addWidget(self.fileSelect, 0, 0, 1, 2)
        layout.addWidget(self.image, 1, 0, 1, 2)
        
        layout.addWidget(self.tesserect_label, 2, 0)
        layout.addWidget(self.tesserect_text, 2, 1)
        
        layout.addWidget(self.spellcheck_label, 3, 0)
        layout.addWidget(self.spellcheck_text, 3, 1)
        
        layout.addWidget(self.cv_label, 4, 0)
        layout.addWidget(self.cv_text, 4, 1)
        
        layout.addWidget(self.cv_spell_label, 5, 0)
        layout.addWidget(self.cv_spell_text, 5, 1)
        
        self.setLayout(layout)
        self.setWindowTitle("Text Extraction")
    
    def getfile(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', 'c:\\', "Image files (*.jpg *.png)")

        pixmap = QtGui.QPixmap(fname[0])
        self.image.resize(400, 400)
        self.image.setPixmap(pixmap.scaled(self.image.size(), QtCore.Qt.IgnoreAspectRatio))
    
    

def main():
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    ex = test_extractor()
    ex.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()