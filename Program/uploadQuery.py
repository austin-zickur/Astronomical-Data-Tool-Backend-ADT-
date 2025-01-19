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
    * getFiles()
        input: Name (User)
        output: List
    

'''

#Init supabase
supabase = initialize_supabase()

# For uploading files

def uploadFiles(userId, file, fileName):
    # Upload the file directly to Supabase
    response = supabase.storage.from_("user-storage").upload(
        f"uploads/{userId}/files/{fileName}", file.read()
    )

    return response

# For getting files

def getFiles(user):
    response = supabase.storage.from_("user-storage").list(f"uploads/{user}/files")
    print(response)
    return response
# TEST 
dummy_var = "Austin Zickur"
getFiles(dummy_var)

'''
FIX ME -- for generate image feature

def uploadFileImages(file):
    dataList = FITStoImages(file)
    print(f"List: {dataList}")

uploadFileImages("j9am01010_drz.fits")
'''
