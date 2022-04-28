import sys
# f_in  = '5096864-_-_128-_-_8f79dc33f4ca00f7c61a9761e3dd3249.uc!.mp3'
# f_out = 'demo.mp3'

f_in  = sys.argv[1]
f_out = f_in.split('.')[0] + '.mp3'

fp_in = open(f_in, 'rb')
fp_out= open(f_out, 'wb')

out_b = []
while True:
    strb = fp_in.read(1)
    if strb == b"":
        break
    out_b.append( ord(strb) ^ ord(b'\xa3')) 

import array
charArray = array.array('B')
charArray.fromlist(out_b)
fp_out.write(charArray)

fp_in.close()
fp_out.close()