import os,sys,time
printfile = sys.argv[1]
os.system('lpr -P rawlaser %s'%printfile)
os.system('lpr -P rawlaser2 %s'%printfile)
time.sleep(8)
os.system('lprm -P rawlaser')
os.system('lprm -P rawlaser2')
