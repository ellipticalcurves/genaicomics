import os
from krita import Krita
from PyQt5.Qt import *

width = 1600
height = 2560

   
def draw_panels(width, height, n, padding=20, m=0, rh=1000):
    svgstring = ""
    width= width
    panel_width = (width - padding*(n+1))/n
    for i in range(n):
        rect = f"<rect x='{i*(panel_width+padding)+padding}' y='{m+padding}' width ='{panel_width}px' height='{rh}px' fill ='none' stroke='black' stroke-width='2'  />\n"
        print(rect)
        svgstring += rect
    return svgstring

positions = []


def draw_text(x,y, string="test"):
    svgstring = f"<text x='{x}' y ='{y}' font-size='36px' font-family='Arial' fill='blue'>{string}</text> "
    return svgstring

svgContent = f"""\
<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<svg
   width="{width}"
   height="{height}"
   viewBox="0 0 {width} {height}">
"""

svgstring = ""

svgContent+=svgstring
x = draw_text(20,20,"texst")
heightlist = [2, 3, 1,2]

for j in range(len(heightlist)):
    svgstring = draw_panels(width, height, heightlist[j],20, j*630,600)
    svgContent+=svgstring
    
    
    
svgContent+=x

svgContent +="</svg>"


print(svgContent)
#svgContent = oth

def sleep(value): 
    loop = QEventLoop()
    QTimer.singleShot(value, loop.quit)
    loop.exec()

def importSvg(svgContent, layer):
#    if not layer is None:    
#        doc.setActiveNode(vLayer)
#        #doc.waitForDone()  # ==> waitForDone() doesn't work, need to apply a sleep :-(
#        sleep(450)
        
    mimeContent=QMimeData()
    mimeContent.setData('image/svg+xml', svgContent.encode())
    QGuiApplication.clipboard().setMimeData(mimeContent)
    #Krita.instance().action('edit_paste').trigger()

doc = Krita.instance().createDocument(1600, 2560, "Test", "RGBA", "U8", "", 100.0)
Krita.instance().activeWindow().addView(doc)

#vLayer=doc.createVectorLayer('test-v')
#doc.rootNode().addChildNode(vLayer, None)

importSvg(svgContent, 0)

doc.refreshProjection()
