__doc__ = """
this script takes a url & saves YouTube or other streaming video to the Download folder on your Android device
instructions from YouTube app: select share --> copy link to clipboard, run this script (or switch back to it)  & put in the url when prompted
only for use where permitted; I take no responsibility for whether you comply with copyright law or anybody else's terms of service
written for Android, on Android, summer 2017
""" 

__author__ = 'Nate Smith nrsmith012@gmail.com (ytdl.py top level script) but the real work gets done by youtube-dl https://rg3.github.io/youtube-dl/ and Android sl4a code'
__license__ = 'Apache License, Version 2.0'

import sl4a
import os
import pip
from subprocess import call as C
from time import sleep as zz

def dload(url):
  if (len(url.split(".")) < 2) and (len(url.split(":")) < 3):
    raise ValueError("input error : %s can't be a valid
  C(["youtube-dl", 
    	"--no-check-certificate", 
    	url])
  droid.makeToast("downloaded to Downloads folder /sdcard/Download") 
    	 

if __name__ == "__main__":
  for li in __doc__.split("\n"):
    print(li)
    zz(3.5) # you can lower this number to make the text faster
  droid = sl4a.Android()
  print("\ndroid ready+'\n'*2")
  zz(2)
  url = droid.dialogGetInput('Paste video link here').result
  zz(.77)
  print("got URL"+'\n'*2)  
  zz(. 77)
  print("preparing youtube-dl") 
  zz(6)
  print("[ give it up to a minute - after that, it's best to check your network connection ] ") 
  os.chdir("/sdcard/Download")
  pip.main(["install", "youtube-dl", "--upgrade"])
  print("pipped") 
  dload(url) 
  
