#!/usr/bin/python

import os
import sys
import tarfile
import datetime
import shutil


print "creating backup folder"
print "\n"

def folder_creation(backup):
  os.mkdir( backup , 0755 )

  print "coping app1 folder to backup"
  print "\n"  

  src = "/location/of/source/app1/folder"
  dst = backup
  shutil.move(src, dst)

today = datetime.datetime.now() 
folder = "/location/of/backup/folder/to/be/created-"+str(today)
folder_creation( folder )

print "creating tar file"
print "\n"

with tarfile.open( folder + ".tar.gz" , 'w:gz') as tar:
 tar.add( folder )
 tar.close()  

print "Backup Process copleted successfully"
