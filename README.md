# github風identiconジェネレーター

## 使い方
sample_canvas.ymlにならって、paletteとcanvasを設定してください。  
paletteに色を定義。canvasにpaletteで定義した色で好きなアイコンを書きましょう。  
背景色はbackground-colorで定義できます。  
当然ymlなのでバージョン管理ができます。（だからどうした）  

コマンドラインで下記のように実行してください。  
python identicongen.py canvas.yml

## 必要pythonモジュール
- opencv-python
- PyYAML
- numpy