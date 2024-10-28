import time
import cv2
import os
def mp4_to_png(name,name2, output_folder='frames'):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    cap = cv2.VideoCapture(name2)
    frame_count = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame_filename = os.path.join(output_folder, f"{name}_frame_{frame_count}.png")
        cv2.imwrite(frame_filename, frame)

        frame_count += 1

    cap.release()
    print(f"Сохранено {frame_count} кадров в папку '{output_folder}'.")

def png_to_txt(name):
    if not os.path.exists(f'{name}_txt'):
        os.makedirs(f'{name}_txt')
    a = 1
    i = 0
    while a == 1:
        try:
            string = " `.,-':<>;+!*/?%&98#"
            coef = 255 / (len(string) - 1)
            image = cv2.imread(f'{name}_output_frames/{name}_frame_{i}.png')
            height, width, channels = image.shape
            gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            with open(f"{name}_txt/{name}_{i}.txt", "w") as file:
                for x in range(0, width - 1, 8):
                    s = ""
                    for y in range(0, height - 1, 4):
                        try:
                            s += string[len(string) - int(gray_image[x, y] / coef) - 1]
                            continue
                        except IndexError:
                            pass
                    if len(s) != 0:
                        file.write(s + "\n")
            i += 1
        except AttributeError:
            a = 0
    print('Все txt файлы созданы.')
def txt_to_print(name):
    try:
        i = 0
        while True:
            with open(f'{name}_txt/{name}_{i}.txt', 'r+') as file:
                print(file.read())
                time.sleep(0.0295)
                i += 1
    except FileNotFoundError:
        return 0

name_video = input('Название видио: ')
name = input('Просто название: ')
mp4_to_png(name,name_video, name + '_output_frames')
png_to_txt(name)
txt_to_print(name)
while True:
    y_or_n = input('Ещё раз: ')
    if y_or_n == 'y':
        txt_to_print(name)
    else:
        break
