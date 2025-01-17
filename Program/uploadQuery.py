from SupabaseClient import initialize_supabase
from astropy.io import fits
from Image import FITStoImages
'''
FileName: upload

Devoloper: Austin Z

Description: 

Functions:
    * FITStoDatabase()
        input: File (FITS)
        output: Image ()

'''

#Init supabase
supabase = initialize_supabase()

def uploadFiles(user, file, fileName):
    # Upload the file directly to Supabase
    response = supabase.storage.from_("user_storage").upload(
        f"uploads/{user}/files/{fileName}", file.read()
    )

    return response




'''
FIX ME -- for generate image feature

def uploadFileImages(file):
    dataList = FITStoImages(file)
    print(f"List: {dataList}")

uploadFileImages("j9am01010_drz.fits")
'''
