# audio/effects/echo.py
"""
添加回声效果的模块
"""


def add_echo(audio_data, delay=0.5, attenuate=0.5): #delay是延迟时间，attenuate是衰减比率
    """在音频数据上添加回声效果

    :param audio_data: 输入的音频数据
    :param delay: 回声延迟，单位秒
    :param attenuate: 回声衰减比率，0到1之间
    """
    print(f"在音频数据中添加回声: delay={delay}, attenuate={attenuate}")
    return f"{audio_data} (加了回声)"