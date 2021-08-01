import mritopng
# =============================================================================
# import os
# =============================================================================

folder_path = r"E:\Thesis\Images\DICOM"
destinate_path = 'E:\Thesis\Images\PNG'

# =============================================================================
# def convertImg(dicomImage):
#     print("Image: " + dicomImage)
#     outputImg = dicomImage.split('.')
#     mritopng.convert_file(os.path.join(folder_path, dicomImage), os.path.join(folder_path, outputImg[0] + '.jpg'), auto_contrast=True)
# 
#     convertedImg = os.path.join(folder_path, outputImg[0] + '.jpg')
#     return convertedImg
# =============================================================================

mritopng.convert_folder(folder_path, destinate_path)

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
