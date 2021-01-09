import os
import shutil

sourcepath='C:/Users/HP/Downloads'
sourcefiles = os.listdir(sourcepath)
destinationpath_image = 'C:/Users/HP/Pictures'
destinationpath_icon = 'C:/Users/HP/Pictures/icons'
destinationpath_pdf = 'C:/Users/HP/Desktop/pdf'
destinationpath_ttf = 'C:/Users/HP/Documents/fontss'
destinationpath_doc = 'C:/Users/HP/Desktop/word'
destinationpath_music = 'C:/Users/HP/Music'
destinationpath_ppt = 'C:/Users/HP/Desktop/power point'
destinationpath_exl = 'C:/Users/HP/Desktop/excel'
destinationpath_zip = 'C:/Users/HP/Desktop/zip'
destinationpath_app = 'C:/Users/HP/Desktop/apps'

for file in sourcefiles:
    if file.endswith('.png'):
        shutil.move(os.path.join(sourcepath,file), os.path.join(destinationpath_image,file))
    elif file.endswith('.jpg'):
        shutil.move(os.path.join(sourcepath,file), os.path.join(destinationpath_image,file))
    elif file.endswith('.svg'):
        shutil.move(os.path.join(sourcepath, file), os.path.join(destinationpath_icon, file))
    elif file.endswith('.pdf'):
        shutil.move(os.path.join(sourcepath, file), os.path.join(destinationpath_pdf, file))
    elif file.endswith('.ttf'):
        shutil.move(os.path.join(sourcepath, file), os.path.join(destinationpath_ttf, file))
    elif file.endswith('.otf'):
        shutil.move(os.path.join(sourcepath, file), os.path.join(destinationpath_ttf, file))
    elif file.endswith('.docx'):
        shutil.move(os.path.join(sourcepath, file), os.path.join(destinationpath_doc, file))
    elif file.endswith('.doc'):
        shutil.move(os.path.join(sourcepath, file), os.path.join(destinationpath_doc, file))
    elif file.endswith('.mp3'):
        shutil.move(os.path.join(sourcepath, file), os.path.join(destinationpath_music, file))
    elif file.endswith('.xlsx'):
        shutil.move(os.path.join(sourcepath, file), os.path.join(destinationpath_exl, file))
    elif file.endswith('.xlsm'):
        shutil.move(os.path.join(sourcepath, file), os.path.join(destinationpath_exl, file))
    elif file.endswith('.pptx'):
        shutil.move(os.path.join(sourcepath, file), os.path.join(destinationpath_ppt, file))
    elif file.endswith('.ppt'):
        shutil.move(os.path.join(sourcepath, file), os.path.join(destinationpath_ppt, file))
    elif file.endswith('.zip'):
        shutil.move(os.path.join(sourcepath, file), os.path.join(destinationpath_zip, file))
    elif file.endswith('.exe'):
        shutil.move(os.path.join(sourcepath, file), os.path.join(destinationpath_app, file))
