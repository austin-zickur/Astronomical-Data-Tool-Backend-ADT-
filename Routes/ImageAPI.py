from astropy.io import fits
import numpy as np
import matplotlib.pyplot as plt

'''
FileName: 

Devoloper: 

Description:

Functions:
    * FITStoImages()
        input: File (FITS)
        output: Image ()

'''

# FITStoImages()

default = "j9am01010_drz.fits"

def FITStoImages(file):
    #file = input()
    print(file)
    with fits.open(file) as hdul:
        #header = hdul[0].header
        #data = hdul[2].data
        #title = hdul[2].name

        for i, hdu in enumerate(hdul):
            #if type(hdu) == "ImageHDU":
            data = hdu.data
            title = hdu.name
            print(data)
            plt.imshow(data)
            plt.title(f"{title} Image")
            plt.colorbar()
            plt.show()
            #print(f"index here -->: {i}")
            #print(f"object here -->: {hdu}")

        for col in hdul.data.columns:
            print(col)

            '''
            plt.imshow(data)
            plt.title(f"{title} Image")
            plt.colorbar()
            plt.show()
            '''
       



FITStoImages(default)