#from supabase import create_client, Client


from astropy.io import fits
from ImageAPI import FITStoImages
'''
FileName: upload

Devoloper: Austin Z

Description: 

Functions:
    * FITStoDatabase()
        input: File (FITS)
        output: Image ()

'''

def uploadFile(file):
    dataList = FITStoImages(file)
    print(f"List: {dataList}")

uploadFile("j9am01010_drz.fits")