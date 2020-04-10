from PIL import Image

im = Image.open("capture.JPG")
width, height = im.size

workbook = xlsxwriter.Workbook('demo.xlsx')
worksheet = workbook.add_worksheet()

numberOfImages = 4
worksheet.set_column('B:B', width/2)
worksheet.set_row(2, height/2)

worksheet.insert_image('B3', 'capture.JPG', {"x_offset": 0, "y_offset":0, "x_scale":0.5, "y_scale":0.5})
worksheet.insert_image('B3', 'capture.JPG', {"x_offset": width, "y_offset":0, "x_scale":0.5, "y_scale":0.5})
worksheet.insert_image('B3', 'capture.JPG', {"x_offset": width*2, "y_offset":0, "x_scale":0.5, "y_scale":0.5})
worksheet.insert_image('B3', 'capture.JPG', {"x_offset": width*3, "y_offset":0, "x_scale":0.5, "y_scale":0.5})

workbook.close()
