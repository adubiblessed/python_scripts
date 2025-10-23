import os
import shutil

audio = (
    ".3ga", ".aac", ".ac3", ".aif", ".aiff",
    ".alac", ".amr", ".ape", ".au", ".dss",
    ".flac", ".flv", ".m4a", ".m4b", ".m4p",
    ".mp3", ".mpga", ".ogg", ".oga", ".mogg",
    ".opus", ".qcp", ".tta", ".voc", ".wav",
    ".wma", ".wv"
)

video = (
    ".webm", ".MTS", ".M2TS", ".TS", ".mov",
    ".mp4", ".m4p", ".m4v", ".mxf"
)

img = (
    ".jpg", ".jpeg", ".jfif", ".pjpeg", ".pjp", ".png",
    ".gif", ".webp", ".svg", ".apng", ".avif"
)


def is_audio(file):
    return os.path.splitext(file)[1].lower() in audio


def is_video(file):
    return os.path.splitext(file)[1].lower() in video


def is_image(file):
    return os.path.splitext(file)[1].lower() in img


def organise_file(folderpath):
    try:
        folder = ''
        for each in ['audio', 'video', 'images']:
            folder = os.path.join(folderpath, each)
            if os.path.exists(folder) == False:
                os.makedirs(folder)
            else:
                continue
        print('file moving starts')
        for file in os.listdir(folderpath):
            if os.path.isdir(os.path.join(folderpath, file)):
                continue
                
            if is_audio(file):
                destination_folder = os.path.join(folderpath, 'audio')
            elif is_video(file):
                destination_folder = os.path.join(folderpath, 'video')
            elif is_image(file):
                destination_folder = os.path.join(folderpath, 'images')
            else:
                continue
    
            destination_file = os.path.join(destination_folder, file)
            source = os.path.join(folderpath, file)
            
            if os.path.exists(destination_file):
                print(f'file exist skipping {file}')
                continue
            else:
                try:
                    print(f"Moving {file} → {destination_folder}")
                    shutil.move(source, destination_folder)
                except Exception as e:
                    print(f"Error while moving {file}: {e}")
                    continue
    
        print('done')
    except:
        print('error')
    
print('Python file organiser')
print('select or input file folder you wish to organise')
print('1: Current folder')
print('2: Another folder')

folder = input()

if folder == '1':
    folderpath = os.getcwd()
    organise_file(folderpath)
elif folder == '2':
    folderpath1 = input('Enter file directory: ')
    organise_file(folderpath1)