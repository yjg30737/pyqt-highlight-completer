# pyqt-highlight-text-completer
PyQt highlight text completer

## Requirements
*  PyQt5 >= 5.8

## Setup
``` pip3 install git+https://github.com/yjg30737/pyqt-highlight-text-completer.git --upgrade```

## Note
This package is not good to use. I made this because i want to add highlight feature to completer. 
At least highlight feature works.
QCompleter is not even used. This package mainly consist of QLineEdit and QTableWidget.

## Example
As always, I'm not good at explaining something (Moreover i'm not even native English speaker) so i will give you this.
```python
from PyQt5.QtWidgets import QApplication
from pyqt_highlight_text_completer import HighlightTextCompleter

if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    mainWindow = HighlightTextCompleter()
    mainWindow.show()
    mainWindow.addTexts('Alberic Litte,Angalmo,Antus Odiil,Ariela Doran,Arriana Valga,Athragar,Bittneld the Curse-Bringer,Carmen Litte,Casta Scribonia,Chanel,Chorrol Jailor,Chorrol Soldier,City Watch,Dar-Ma,Earana,Emfrid,Estelle Renoit,Eugal Belette,Fighters Guild Porter,Francois Motierre,Gaturn gro-Gonk,Glistel,Gureryne Selvilo,Honditar,Jirolin Doran,Kurz gro-Baroth,Laythe Wavrick,Lazy Kaslowyn,Lum gro-Baroth,Malintus Ancrus,Modryn Oreyn,Nardhil,Nermus the Mooch,Orag gra-Bargol,Orgnolf Hairy-Legs,Orok gro-Ghoth,Otius Loran,Rallus Odiil,Rasheda,Rena Bruiant,Reynald Jemane,Rimalus Bruiant,Seed-Neeus,Talasma,Teekeeus,Valus Odiil,Vilena Donton,Wallace'.split(
        ','))
    app.exec_()
```

Result

![image](https://user-images.githubusercontent.com/55078043/146474104-44a42dc3-0b80-49d5-9571-dec2f83e3b47.png)





