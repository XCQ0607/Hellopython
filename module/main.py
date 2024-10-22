# main.py
"""
主脚本文件，演示如何导入和使用音频处理包
"""

# 导入音频处理包和模块
from audio.formats.wav import read_wav, write_wav
from audio.effects.echo import add_echo
from audio.filters.equalizer import apply_equalizer


def main():
    # 读取音频文件
    wav_data = read_wav("sample.wav")

    # 输出读取的音频信息
    print(f"读取的音频数据：{wav_data['data']}, 采样率：{wav_data['sample_rate']}Hz")

    # 添加回声效果
    echo_data = add_echo(wav_data['data'], delay=0.3, attenuate=0.7)
    print(f"添加回声后的音频数据: {echo_data}")

    # 应用均衡器
    equalizer_levels = {"bass": 5, "mid": 2, "treble": 3}
    equalized_data = apply_equalizer(echo_data, equalizer_levels)
    print(f"经过均衡处理的音频数据: {equalized_data}")

    # 写入处理后的音频数据到新文件
    write_wav("output.wav", equalized_data)


if __name__ == "__main__":
    main()


# audio/                          # 顶层包
#     __init__.py                 # 初始化audio包
#     formats/                     # 文件格式处理子包
#         __init__.py
#         wav.py                  # WAV文件处理模��
#     effects/                     # 音频效果子包
#         __init__.py
#         echo.py                 # 添加回声效果的模块
#     filters/                     # 滤波子包
#         __init__.py
#         equalizer.py            # 均衡器模块
# main.py                         # 主脚本文件

# 在本例中，我们将创建一个名为 audio 的包，内部包含三个子模块：
#
# formats/ - 用于处理不同音频文件格式的模块。
# effects/ - 用于添加音频效果的模块。
# filters/ - 用于应用音频滤波的模块。

# 重要的函数参数
# read_wav(file_path):
#
# 必选参数:
# file_path: 压缩文件路径，字符串类型。
# 返回: 包含音频数据和采样率的字典。
# add_echo(audio_data, delay=0.5, attenuate=0.5):
#
# 必选参数:
# audio_data: 输入的音频数据，字符串类型。
# 可选参数:
# delay: 回声的延迟时间，默认为 0.5 秒。
# attenuate: 回声的衰减比率，默认为 0.5。
# 返回: 处理后的音频数据，添加回声效果的字符串。
# apply_equalizer(audio_data, levels):
#
# 必选参数:
# audio_data: 输入的音频数据，字符串类型。
# levels: 均衡器设置，字典类型，包含各频段的增益值。
# 返回: 经均衡处理的音频数据的字符串。
# write_wav(file_path, data):
#
# 必选参数:
# file_path: 输出文件路径，字符串类型。
# data: 需要写入的音频数据，字符串类型。