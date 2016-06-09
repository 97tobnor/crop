# -*- coding: utf-8 -*-
"""

@author: 97tobnor
"""

from PyQt4.QtGui import *

class ManualGrowDialog(QDialog):
    """This class provides a dialog window that take in water and light"""
    
    def __init__(self):
        super().__init__()
        
        self.water_spinbox = QSpinBox()
        self.light_spinbox = QSpinBox()
        
        self.water_spinbox.setRange(0,10)
        self.light_spinbox.setRange(0,10)
        
        self.water_spinbox.setSuffix(" Water ")
        self.light_spinbox.setSuffix(" Light ")
        
        self.water_spinbox.setValue(1)
        self.light_spinbox.setValue(1)
        
        self.submit_button = QPushButton("Enter Values")
        
        self.dialog_layout = QVBoxLayout()
        self.dialog_layout.addWidget(self.light_spinbox)
        self.dialog_layout.addWidget(self.water_spinbox)
        self.dialog_layout.addWidget(self.submit_button)
        
        self.setLayout(self.dialog_layout)
        
        self.submit_button.clicked.connect(self.close)
        
    def values(self):
        return int(self.light_spinbox.value()), int(self.water_spinbox.value())