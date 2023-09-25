import AveryLabels
from reportlab.lib.units import mm, cm
from reportlab_qrcode import QRCodeImage

startASN = 1

def render(c,x,y):
    global startASN
    barcode_value = f"ASN41{startASN:04d}" ## 11 Markus, 21 Silke, 31 Trici, 41 Allgemein
    barcode_text = f"Allg. 41{startASN:04d}"
    startASN = startASN + 1

    qr = QRCodeImage(barcode_value, size=y*0.9)
    qr.drawOn(c,1*mm,y*0.05)
    c.setFont("Helvetica", 2*mm)
    c.drawString(y, (y-2*mm)/2, barcode_text)
    print(x)
    print(y)


label = AveryLabels.AveryLabel(4731)
label.open( "labels4731.pdf" )
label.render(render, 189 )
label.close()
