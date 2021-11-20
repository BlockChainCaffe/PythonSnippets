#!/usr/bin/python3

# https://pypi.org/project/segno/
# https://segno.readthedocs.io/en/latest/
import segno
import io

qr = segno.make_qr("This is a qrcode")
qr = segno.make_qr("This is a qrcode", error='Q')

## Export/Save
qr.save('myqr.svg')  # SVG document
qr.save('myqr.png')  # PNG image
qr.save('myqr.eps')  # EPS document
qr.save('myqr.txt')  # Text output

## Extra parameters
qr.save('myqr.svg', border=0)   # No border
qr.save('myqr.svg', border=10)  # 10px border
qr.save('myqr.png', scale=2)    # enlarge
qr.save('sgt-peppers.svg', dark='darkred', light='lightblue') #Use colors instead of B/W


## Save to Buffer
buff = io.BytesIO()
qr.save(buff, kind='svg', dark='darkblue', light='#eee')

# ## Examples
# # Email
# segno.helpers.make_email(to, cc=None, bcc=None, subject=None, body=None)
# segno.helpers.make_make_email_data(to, cc=None, bcc=None, subject=None, body=None)
# # Creates and returns an European Payments Council Quick Response Code (EPC QR Code) version 002.
# segno.helpers.make_epc_qr(name, iban, amount, text=None, reference=None, bic=None, purpose=None, encoding=None) 
# # Geographic Location
# segno.helpers.make_geo(lat, lng)
# # Returns a QR code which encodes a MeCard  https://en.wikipedia.org/wiki/MeCard_(QR_code)
# segno.helpers.make_mecard(name, reading=None, email=None, phone=None, videophone=None, memo=None, nickname=None, birthday=None, url=None, pobox=None, roomno=None, houseno=None, city=None, prefecture=None, zipcode=None, country=None)
# # Creates a QR code which encodes a vCard version 3.0.  https://en.wikipedia.org/wiki/VCard
# segno.helpers.make_vcard(name, displayname, email=None, phone=None, fax=None, videophone=None, memo=None, nickname=None, birthday=None, url=None, pobox=None, street=None, city=None, region=None, zipcode=None, country=None, org=None, lat=None, lng=None, source=None, rev=None, title=None, photo_uri=None)
# # WiFi connectiont 
# segno.helpers.make_wifi(ssid, password, security, hidden=False)
