import os, sys

style = sys.argv[1]
filename = 'giop.' + style

os.system("echo # Offline Gaussian IOps > %s" % filename)

overlays = [1,2,3,4,5,6,7,8,9,10,11,99]
for i in overlays:
    os.system("echo ## Overlay %d >> %s" % (i, filename))
    os.system("python get_iop.py %d all %s >> %s" %(i, style, filename))
    #os.system("echo  >> %s" % filename)
