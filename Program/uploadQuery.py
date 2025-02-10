from SupabaseClient import initialize_supabase
from astropy.io import fits
from io import BytesIO
'''
FileName: uploadQuery.py

Devoloper: Austin Zickur, Kylee Brown

Description: queries used to upload and get data to and from the database

Functions:
    * uploadFiles()
        input:
            params: 
                userId (String)
                file (FITS)
                fileName (String)
        output: 
            response (From databsae)
    * uploadImages()
        input:
            params:
                dataList (Array)
                userId (String)
                fileName (String)
        output:
            ResponseList (Array)
    * getPublicUrlsOfPlotImages() -- for preview right after upload
        input:
            params:
                plot_Response (Array)
        output:
            publicUrls (Array)

    * GetPublicUrlsOfImages() -- for thumbnail and individual photo
        input:
            params:
                imageResponse (Array) -- (an array of all image paths per one user)
        ouput:
            publicUrls (Array)
    * getPlotImages()
        input:
            params:
                userId (String)
        output:
            pathResponse (Array)
            folderNames (Array)
            imageNames (Array)
    * getFiles()
        input: 
            params:
                user (String)
        ouput:
            response (From database)
    * getFileData()
        input:
            params:
                name (String)
                user (String)
        output:
            response (From database)
'''

#Init supabase
supabase = initialize_supabase()

# For uploading files (based on unique userId)
def uploadFiles(userId, file, fileName):
    # Upload the file directly to Supabase
    response = supabase.storage.from_("user-storage").upload(
        f"uploads/{userId}/files/{fileName}", file.read()
    )

    return response

# For uploading images (based on uniques userId) 
def uploadImages(dataList, userId, fileName):
    responseList = []
    for title, buffer in dataList:
        path = f"uploads/{userId}/images/{fileName}/{title}.png"
        #options = {"Content-Type": "image/png", "upsert": "true", "cacheControl":"3600"}
        response = supabase.storage.from_("user-storage").upload(path, buffer,{"upsert":"true"})
        
        responseList.append(response)
    print(responseList)
    return responseList

# GET public URLS of PLOT images to preview on frontend
def getPublicUrlsOfPlotImages(plot_Response):
    paths = [response.path for response in plot_Response]
    publicUrls = []
    for path in paths:
        file_url = supabase.storage.from_("user-storage").get_public_url(path)
        publicUrls.append(file_url)
    #print(paths)
    return(publicUrls)

# Get public URLS of ALL user images to store in "my images:" on the frontend
def GetPublicUrlsOfImages(imageResponse):
    paths = imageResponse
    publicUrls = []
    for path in paths:
        file_url = supabase.storage.from_("user-storage").get_public_url(path)
        publicUrls.append(file_url)
    #print(publicUrls)
    return(publicUrls)

# GET ALL images a user has generated
def getPlotImages(userId):
    folders = supabase.storage.from_("user-storage").list(f"uploads/{userId}/images")
    foldersList =[]
    #print(folders)
    imageResponseList = []
    pathResposne = []
    folderNames = []
    imageNames = []
    # iterate through ALL user folders and grab the group of images per folder
    for folder in folders:
        folderName = folder['name']
        #print(folder['name'])
        imageResponse = supabase.storage.from_("user-storage").list(f"uploads/{userId}/images/{folderName}")
        imageResponseList.append(imageResponse)
        foldersList.append(folder)
    #print(len(imageResponseList))
        
    # iterate through imageResponse and folders to grab ALL pictures with corresponding image names and file names
    for imageGroup, folder in zip(imageResponseList, folders):
        for image in imageGroup:
            if image is not None:
                folderNames.append(folder['name'])
                imageNames.append(image['name'])

                path =f"uploads/{userId}/images/{folder['name']}/{image['name']}"
                pathResposne.append(path)

    return pathResposne, folderNames, imageNames

# For getting files based on userId
def getFiles(user):
    response = supabase.storage.from_("user-storage").list(f"uploads/{user}/files")
    print(response)
    
    return response

# For downloading files into database
def getFileData(name, user):
    
    response = supabase.storage.from_("user-storage").download(f"uploads/{user}/files/{name}")
    
    #print(response)
    return response
    
# UNUSED -- For getting list of file names -- UNUSED
'''
def nameGet(user):
    names = []
    for dict in getFiles(user):
        names.append(dict["name"])
    print(names)
    return names
'''


# DEBUG BELOW 
#name = "j9am01010_drz.fits"

if __name__ == "__main__":
    #name = "j9am01010_drz.fits"
    #data = "icons8-person-64.png"
    #user = "AustinZickur"
    #name = "iconTestFile"
    #getFileData(name, user)
    #uploadImages(data, userId, name)
    #FITStoImages(default)
    user = "fc1031d0-80c4-4b30-94c5-bb49c41ff2d2"
    respo, foldN, imgN = getPlotImages(user)
    print( foldN, imgN)
    #GetPublicUrlsOfImages(respo)
    '''
    FIX ME -- for generate image feature

    def uploadFileImages(file):
        dataList = FITStoImages(file)
        print(f"List: {dataList}")

    uploadFileImages("j9am01010_drz.fits")
    '''
