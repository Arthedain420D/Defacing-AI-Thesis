import med2image
# =============================================================================
# import os
# =============================================================================

inputFile = r"E:\Thesis\Images\DICOM"
outputDir = 'E:\Thesis\Images\PNG'

med2image -inputFile -outputDir

# =============================================================================
# # Convert a DICOM file 'file.dcm' to JPEG and store
# # the results in a dirctory called 'out'.
# # The 'out' dir will contain a set of JPEG
# # images of form 'output-sliceXXX.jpg'.
# 
# # NOTE! If the directory containing 'file.dcm' contains
# # multiple DICOM files, *ALL* of these will be converted
# # to JPEG. See later for only converting a *single*
# # DICOM file.
# 
# med2image -i file.dcm -d out
# =============================================================================
