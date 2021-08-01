import dicom2jpg
import numpy
import os


origin = r"E:\Thesis\Images\DICOM"
target_root = 'E:\Thesis\Images\PNG'

dicom2jpg.dicom2png(dicom_dir)  

dicom2jpg.dicom2jpg(origin, target_root=None, anonymous=False, multiprocessing=True)

dicom2jpg.dicom2img(origin)

dicom2jpg.io2img(dicomIO)

# =============================================================================
# def convertImg(dicomImage):
#     print("Image: " + dicomImage)
#     outputImg = dicomImage.split('.')
# dicom2jpg.dicom2png(origin, target_root=None, anonymous=False, multiprocessing=True)    
# 
#     convertedImg = os.path.join(folder_path, outputImg[0] + '.jpg')
#     return convertedImg
# =============================================================================

dicom2jpg.dicom2png(dicom_dir) 

# =============================================================================
# def rename(): 
#     i = 0
# 
#     for filename in os.listdir(folder_path): 
#         dst =str(i) + ".png"
#         src =destinate_path + filename + ".png"
#         dst =destinate_path + dst 
#           
#         # rename() function will 
#         # rename all the files 
#         os.rename(src, dst) 
#         i += 1
# =============================================================================

# rename()
