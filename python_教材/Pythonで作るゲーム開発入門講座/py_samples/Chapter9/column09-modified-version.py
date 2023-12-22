import sounddevice as sd
import numpy as np

def play_sound(frequency, duration):
    fs = 44100  # サンプリングレート

    # サウンドのデータを生成（ここでは単純な正弦波を使用）
    t = (1 / fs) * np.arange(fs * duration)
    data = 0.5 * np.sin(2 * np.pi * frequency * t)

    sd.play(data, fs)
    sd.wait()

print("サウンド開始")
play_sound(261, 1)  # ドの音（261Hz）を1秒間再生
play_sound(293, 1)  # レの音（293Hz）を1秒間再生
play_sound(329, 1)  # ミの音（329Hz）を1秒間再生
play_sound(349, 1)  # ファの音（349Hz）を1秒間再生
play_sound(440, 1)  # ラの音（440Hz）を1秒間再生
play_sound(493, 1)  # シの音（493Hz）を1秒間再生
play_sound(523, 1)  # ドの音（523Hz）を1秒間再生
play_sound(493, 1)  # シの音（493Hz）を1秒間再生
play_sound(440, 1)  # ラの音（440Hz）を1秒間再生
play_sound(349, 1)  # ファの音（349Hz）を1秒間再生
play_sound(329, 1)  # ミの音（329Hz）を1秒間再生
play_sound(293, 1)  # レの音（293Hz）を1秒間再生
play_sound(261, 1)  # ドの音（261Hz）を1秒間再生
print("サウンド終わり")
