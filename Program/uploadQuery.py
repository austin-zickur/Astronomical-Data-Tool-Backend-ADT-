from SupabaseClient import initialize_supabase
from astropy.io import fits
from Image import FITStoImages
'''
FileName: uploadQuery.py

Devoloper: Austin Zickur, Kylee Brown

Description: queries used to upload data to the database

Functions:
    * uploadFiles()
        input: File (FITS)
        output: Response
    

'''

#Init supabase
supabase = initialize_supabase()

def uploadFiles(user, file, fileName):
    # Upload the file directly to Supabase
    response = supabase.storage.from_("user_storage").upload(
        f"uploads/{user}/files/FITS/{fileName}", file.read()
    )

    return response

# TEST 


'''
FIX ME -- for generate image feature

def uploadFileImages(file):
    dataList = FITStoImages(file)
    print(f"List: {dataList}")

uploadFileImages("j9am01010_drz.fits")
'''
