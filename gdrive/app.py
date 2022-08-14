# import gzip
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

import tarfile

tar = tarfile.open("./downloaded_files.gz", "w:gz")
tar.add("/downloads/complete",)
tar.close()

gauth = GoogleAuth()
drive = GoogleDrive(gauth)

file2 = drive.CreateFile({'title':'downloaded_files.gz'})
file2.SetContentFile('./downloaded_files.gz')
file2.Upload()