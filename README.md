# pyqt-highlight-completer
PyQt highlight completer

## Requirements
*  PyQt5 >= 5.8

## Setup
`python -m pip install pyqt-highlight-completer`

## Note
This package mainly consist of QLineEdit and QTableWidget. QCompleter is not even used.

This is case-insensitive, searching for text anywhere. 

## Example
Code Sample
```python
from PyQt5.QtWidgets import QApplication
from pyqt_highlight_completer import HighlightCompleter

if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    mainWindow = HighlightCompleter()
    mainWindow.show()
    mainWindow.addTexts('Alberic Litte,Angalmo,Antus Odiil,Ariela Doran,Arriana Valga,Athragar,Bittneld the Curse-Bringer,Carmen Litte,Casta Scribonia,Chanel,Chorrol Jailor,Chorrol Soldier,City Watch,Dar-Ma,Earana,Emfrid,Estelle Renoit,Eugal Belette,Fighters Guild Porter,Francois Motierre,Gaturn gro-Gonk,Glistel,Gureryne Selvilo,Honditar,Jirolin Doran,Kurz gro-Baroth,Laythe Wavrick,Lazy Kaslowyn,Lum gro-Baroth,Malintus Ancrus,Modryn Oreyn,Nardhil,Nermus the Mooch,Orag gra-Bargol,Orgnolf Hairy-Legs,Orok gro-Ghoth,Otius Loran,Rallus Odiil,Rasheda,Rena Bruiant,Reynald Jemane,Rimalus Bruiant,Seed-Neeus,Talasma,Teekeeus,Valus Odiil,Vilena Donton,Wallace'.split(
        ','))
    app.exec_()
```

Result

![image](https://user-images.githubusercontent.com/55078043/146474104-44a42dc3-0b80-49d5-9571-dec2f83e3b47.png)





