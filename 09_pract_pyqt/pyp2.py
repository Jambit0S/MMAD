import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtWidgets import QApplication, QWidget,QFileDialog


class Canvas(FigureCanvas):

    def __init__(self, parent):
        fig, self.ax = plt.subplots(figsize=(5, 4), dpi=200)
        super().__init__(fig)
        self.setParent(parent)
        
        filename= QFileDialog.getOpenFileName(None, "Выберите текст...",
                                        'C:/', filter="All files (*)")[0]
        self.show()
        print(filename)
        with open(filename,'r',encoding = 'utf-8') as txt_file:
            data=txt_file.read().replace('\n','')
            data =data.lower()
            print(data)
            
            letters=list('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')
            hist=[]
            for letter in letters:
                hist.append((data.count(letter)))
            
            print(hist)
            
                        
        
                
        plt.bar(np.arange(len(hist)),hist)
    

        plt.plot()
        print(len(hist))
    
class AppDemo(QWidget)      :
    def __init__(self):
        super().__init__()
        self.resize(1600, 800)

        chart = Canvas(self)

app = QApplication(sys.argv)        
demo = AppDemo()
demo.show()
sys.exit(app.exec_())
            
