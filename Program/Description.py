from astropy.io import fits
import numpy as np
import requests

'''
*uses MAST database and API

FileName: Description.py

Developer: Austin Zickur

Description: showcases a description of the FITS file and images

Functions:
    * FITStoDescription()
        input: File (FITS)
        output: File (TXT)
    * extract_proposal_id()
        input: File (FITS)
        output: String
    * fetch_proposal_details()
        input: Proposal ID
        output: String

'''

# extract_proposal_id
'''For MAST API
def extract_proposal_id(file):
    with fits.open(file) as hdul:
        # Search the primary header for PROPOSID
        proposid = hdul[0].header.get('PROPOSID', None)
        if proposid is None:
            print("No PROPOSID found in the FITS file.")
        else:
            print(f"Proposal ID: {proposid}")
        return proposid
'''

# FITStoDescription()

default = "j9am01010_drz.fits"
# For 'generate description' feature
def FITStoDescription(file):
    with fits.open(file) as hdul:
        header = hdul[0].header
        tsc = header.get('TELESCOP') # For info on Telescope
        ins = header.get('INSTRUME') # For info on Instrument
        det = header.get('DETECTOR')
        obj = header.get('TARGNAME')


        
    return tsc

FITStoDescription(default)
