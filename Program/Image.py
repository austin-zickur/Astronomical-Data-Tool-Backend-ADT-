from astropy.io import fits
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from io import BytesIO
from uploadQuery import uploadImages
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

#default = "Program/j9am01010_drz.fits"

# For 'generate images' feature
def FITStoImages(file, userId, fileName):
    #file = input()
    #print("file:", file)
    file = BytesIO(file)
    with fits.open(file, mode="update") as hdul:
        header = hdul
        #print(header)
        '''
        dataList = []
        for i, hdu in enumerate(hdul):
            if isinstance(hdu, fits.ImageHDU):
                data = hdu.data
                title = hdu.name
                dataList.append(data)
        '''
        dataList = []
            
        #print(hdul)
        for i, hdu in enumerate(hdul):
            if isinstance(hdu, fits.TableHDU):
                #print(hdu.data)
                data = hdu.data
                title = f"tab_image_{i}"
                print("yes")
                dataList.append(title, data)
            if isinstance(hdu, (fits.ImageHDU, fits.PrimaryHDU)):
                # don't mess with .tab -- for now
                #print(hdu)
                #print(hdul[i].data) 
                data = hdul[i].data
                if data is not None:
                    
                    title = hdul[i].name
                    plt.imshow(data)
                    plt.title(f"{title} Image")
                    plt.colorbar()
                    #plt.savefig(f"debug_{title}.png",format="png" )
                    buffer = BytesIO()
                    buffer.seek(0)
                    plt.savefig(buffer, format="png")
                    print(title)
                    imgBytes = buffer.getvalue()
                    print(f"Image buffer length: {(imgBytes[:10])} bytes")
                
                    #buffer.seek(0)
                    #print(f"Buffer content for {title[:10]}...: {buffer.read(10)}")  # Print the first 10 bytes
                
                    dataList.append((title, imgBytes))
                    
                    buffer.close()
                    plt.close()
                    #print("hi")
        print(dataList)
        response = uploadImages(dataList, userId, fileName)  
    #print(dataList)
    return(response)

       

#if __name__ == "__main__":
    #data = FITStoImages(default)
    #userId = "fakeID000"
    #FITStoImages(default, userId, default)