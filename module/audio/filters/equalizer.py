# audio/filters/equalizer.py
"""
均衡器模块
"""


def apply_equalizer(audio_data, levels):
    """应用均衡器设置

    :param audio_data: 输入的音频数据
    :param levels: 均衡器设置，字典形式
    """
    print(f"应用均衡器设置: {levels}")
    return f"{audio_data} (均衡处理)"