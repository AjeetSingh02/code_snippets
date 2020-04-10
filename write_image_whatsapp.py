from PIL import Image

# im = Image.open("capture.JPG")
# width, height = im.size

def save_images(list_of_images, heights, widths, path_of_excel, column, row):
    workbook = xlsxwriter.Workbook(path_of_excel)
    worksheet = workbook.add_worksheet()
    
    max_height = max(heights)
    max_width = max(widths)
    
    worksheet.set_column(f"{column}:{column}", max_width/2)
    worksheet.set_row(row-1, max_height)
    
    numberOfImages = len(list_of_images)
    
    margin = 30
    last_width = 0 
    offset = 0
    
    for i in range(numberOfImages):
        offset = offset + last_width + margin
        last_width = widths[i]
        worksheet.insert_image(column + str(row), list_of_images[i], {"x_offset": offset, "y_offset":0})
    
    workbook.close()
    
    
images_data = ["capture1.JPG", "capture2.JPG","capture3.JPG", "capture4.JPG"]
heights = [155, 363, 345, 257]
widths = [253, 253, 431, 171]

save_images(images_data, heights, widths, "demo.xlsx", "B", 3)
