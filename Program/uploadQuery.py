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
        input: ID (User)
        output: List (Dictionaries)
    * nameGet()
        input: ID (User)
        output: List (file names)
    

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

# For getting list of file names

def nameGet(user):
    names = []
    for dict in getFiles(user):
        names.append(dict["name"])
    print(names)
    return names

# TEST 
dummy_var = "982hehg9oijw98sij"
getFiles(dummy_var)
nameGet(dummy_var)
'''
FIX ME -- for generate image feature

def uploadFileImages(file):
    dataList = FITStoImages(file)
    print(f"List: {dataList}")

uploadFileImages("j9am01010_drz.fits")
'''
