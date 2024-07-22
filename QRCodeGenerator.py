"""
import qrcode

# Data to be encoded
data = 'https://spn-sta.spinny.com/blog/20221004191046/Hyundai-Venue-2022.jpg?compress=true&quality=80&w=1200&dpr=2.6'

# Encoding data using make() function
img = qrcode.make(data)

# Saving as an image file
img.save('image1.png')

print("QR code generated and saved as image1.png")
"""

# ==============================================================================

import qrcode

# Data to be encoded
data = 'KJDSGIJGRNRGRLOJTH,. ERHJO,ETHDJOJPERH ,G KSJKPMHS HKNL NGR''D KJFDOJORGEPOKNLNEGE GIJOOPGKG DSK,MOJOR RIPEKPEG GIJOOJPGR GN VKNLJPOEGGN GNIIOPOWEG GIJOJPOEGGMLKMXD  ENNFKDFM, F FLEJOEGPOGRML GNIIOOEG WENNEGPOMMLKW SENOPEGEGL GEKJNIOIEJPGE EWIJJFA,M DVM AFKJIEGE EGIOJOEG MFSM DVKNKFPKOQQW;WDQMAF HEJNKJE 3IOJONT FHK GFMKMFD DIOGKMGR GRJIIOGEN GJOIFEM INEGKGE  '


# Encoding data using make() function
img = qrcode.make(data)

# Saving as an image file
img.save('image2.png')

print("QR code generated and saved as image1.png")