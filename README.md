# Astronomical Data Tool: BackEnd
**Language**: `Python`

**Authors**: Austin Zickur, Kylee Brown
***
# Libraries used:

* ## Data Imaging
  * astropy
  * numpy
  * matplotlib
* ## User Auth and Database Querying
  * flask
  * CORS
  * Supabase
  * os
  * dotenv
  * supabase

# Purpose:

This program was created as a tool for astronomers to generate images from [Fits](https://fits.gsfc.nasa.gov/fits_primer.html) files they upload. 

This project also allows for each user to create an account, which will hold the files they upload and images they generate for future use.

***

# Summary of Code:

This project was developed incrementally with modularity in mind. Our goal was to enable querying the database independently through Supabase's API, separate from creating the actual API endpoints. 

### The file flow looks like:

    Query --> Route --> server.py

With every query function being imported into each coordinating route, and each route being imported and registered to the server. We used this same flow for setting up each route in this project. 

For each route I implemented error handling as much as I could to enable a smooth debugging process. Since this program was designed modularly, I wrote any debugging script below the line

``` python
if __name__ == __main__:

```

to keep program testing/debugging organized and swift.

### Authorization/Security

For authorization, since this is our first full stack project, we opted to go with Supabase API to sign up and sign in users instead of creating our own auth system. (refer to `user.py` and `userQueries.py`)

**To solve an issue with refresh tokens and token handling, although not as secure, the signin was handled through the frontend using Supabase's API*

All secure variables were put in a `.env` folder to ensure security.

Lastly, `CORS` was utilized to allow communication to any API's used by my program.

### Astronomy and FITS file manipulation

The FITS module in astropy was primarily used for capturing, indexing, and opening the Flexible Image Transport System (.fits) files as well as the data categorized in them. FITS files are particular to astronomical telescope missions and have bountiful access to information under HDUs (Header Data Units). After retrieving the image data usually found under "ImageHDU," matplotlib's pyplot module can directly use that binary data of the telescope instrumentation and plot the image pixel-to-pixel. 

The usual means of photon data capture is through a CCD (Charge-Coupled Device) camera with telescope instrumentation capable of measuring intensity, wavelength, polarization, and of course position of that light on the camera. The resultant data can be used to detect extremely precise "wobbles," redshifts, temperatures, spectrums, and images. For further science, research astrometry, spectral analysis, and planetary detection.



