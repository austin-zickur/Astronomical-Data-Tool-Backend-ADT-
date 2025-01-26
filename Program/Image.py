from astropy.io import fits
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from io import BytesIO
matplotlib.use("Agg") # Macbook is weird :( -- needed because GUI was trying to render on Backend (not needed)
# from uploadQuery import uploadImages

'''
FileName: Image.py

Devoloper: Austin Zickur

Description: saves all images in FITS file

Functions:
    * FITStoImages()
        input: File (FITS)
        output: Image (LIST)

'''

# FITStoImages()

#default = "j9am01010_drz.fits"

# For 'generate images' feature
def FITStoImages(file):
    #file = input()
    #print(file)
    
    with fits.open(file, mode="update") as hdul:
        header = hdul[0].header
        '''
        dataList = []
        for i, hdu in enumerate(hdul):
            if isinstance(hdu, fits.ImageHDU):
                data = hdu.data
                title = hdu.name
                dataList.append(data)
        '''
        dataList = []
        for i, hdu in enumerate(hdul):
            if isinstance(hdu, fits.ImageHDU):  # don't mess with .tab
                data = hdul[i].data
                title = hdul[i].name
                plt.imshow(data)
                plt.title(f"{title} Image")
                plt.colorbar()

                buffer = BytesIO()
                plt.savefig(buffer, format="png")
                
                buffer.seek(0)

                imgBytes = buffer.read()
                
                #buffer.seek(0)
                #print(f"Buffer content for {title[:10]}...: {buffer.read(10)}")  # Print the first 10 bytes
                
                plt.close()
                dataList.append((title, imgBytes))
                buffer.close()
                #plt.savefig(f"{title}.png")
                #plt.show()
                #plt.close()
            else:
                title = hdul[i].name
                #print(title)
                
    #print(dataList)
    return(dataList)

       

if __name__ == "__main__":
    #data = FITStoImages(default)
    userId = "fakeID000"
    #FITStoImages(default)