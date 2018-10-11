#coding: utf-8

import numpy as np
import hashlib
import cv2
import yaml
import sys

size = 420 #画像のサイズ
pixel = 70 #1ピクセルのサイズ
frame = 35 #余白のサイズ

def create_image(canvas, palette, background):
    image = np.full([size,size,3],background)

    for i in range(5):
        for j in range(5):
                for k in range(pixel):
                    for l in range(pixel):
                        if canvas[i][j] == '0':
                            colors = background
                        else:
                            colors = palette[canvas[i][j]]
                        image[frame+i*pixel+k][frame+j*pixel+l][0] = colors[2]
                        image[frame+i*pixel+k][frame+j*pixel+l][1] = colors[1]
                        image[frame+i*pixel+k][frame+j*pixel+l][2] = colors[0]

    return image

if __name__ == '__main__':
    #変換するymlファイル名を取得
    yaml_file = sys.argv[1]
    
    #ymlファイルを開く
    try:
        with open(yaml_file, 'rt') as fp:
            text = fp.read()
    except IOError as err:
        print(err)
        exit()
        
    # YAML文字列の読み込み
    data = yaml.safe_load(text)
    
    #キャンバスを取得
    canvas = []
    for i in range(5):
        row = data['canvas'][i].split(',')
        canvas.append(row)
    
    #画像の生成
    image = create_image(canvas, data['palette'], data['background-color'])
    cv2.imwrite('identicon.png', image)
    print('Identicon generate succeeded: identicon.png')