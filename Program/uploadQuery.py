from SupabaseClient import initialize_supabase
from astropy.io import fits
from io import BytesIO
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

# For accepting 

def uploadImages(dataList, userId, fileName):
    responseList = []
    for title, buffer in dataList:
    #title = "test_img"
        print((buffer[:10]))
        
        response = supabase.storage.from_("user-storage").upload(
            file= buffer,
            path= f"uploads/{userId}/{fileName}/{title}.png", 
            file_options = {"Content-Type": "image/png", "upsert": "true", "cacheControl":"3600"}
        )
        
        responseList.append(response)
    print(responseList)
    return responseList
# For getting files

def getFiles(user):
    response = supabase.storage.from_("user-storage").list(f"uploads/{user}/files")
    print(response)
    return response

# For downloading files into database
def getFileData(name, user):
    
    response = supabase.storage.from_("user-storage").download(f"uploads/{user}/files/{name}")
    
    #print(response)
    return response
    
# For getting list of file names

def nameGet(user):
    names = []
    for dict in getFiles(user):
        names.append(dict["name"])
    print(names)
    return names

#name = "j9am01010_drz.fits"
# TEST 
if __name__ == "__main__":
    #name = "j9am01010_drz.fits"
    #data = "icons8-person-64.png"
    #user = "AustinZickur"
    #name = "iconTestFile"
    #getFileData(name, user)
    #uploadImages(data, userId, name)
    #FITStoImages(default)
    '''
    FIX ME -- for generate image feature

    def uploadFileImages(file):
        dataList = FITStoImages(file)
        print(f"List: {dataList}")

    uploadFileImages("j9am01010_drz.fits")
    '''
