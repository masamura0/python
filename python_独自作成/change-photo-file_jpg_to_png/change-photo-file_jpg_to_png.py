from PIL import Image

# JPEG画像のパス
input_image_path = '<pngのファイルに変更したい対象のファイル>.jpg'

# PNG画像の保存先パス
output_image_path = '＜変更名にしたいファイル名＞.png'

# 画像を開く
image = Image.open(input_image_path)

# PNG形式で保存
image.save(output_image_path, format='PNG')

print('変換が完了しました。')
