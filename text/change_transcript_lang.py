"""
requires..

pip install deep-translator
pip install pysrt

"""

import pysrt
from deep_translator import GoogleTranslator


def translate_subtitle(subtitle, target_language='spanish'):
    translated_subtitles = []
    for sub in subtitle:
        translated_text = GoogleTranslator(source='en', target=target_language).translate(sub.text)
        sub.text = translated_text
        translated_subtitles.append(sub)
    # Return a SubRipFile object
    return pysrt.SubRipFile(translated_subtitles)

def save_translated_subtitle(subtitle, output_filename):
    subtitle.save(output_filename, encoding='utf-8')

def translate_srt(input_filename, output_filename):
    subtitle = pysrt.open(input_filename)
    translated_subtitle = translate_subtitle(subtitle)
    save_translated_subtitle(translated_subtitle, output_filename)

input_filename = "audio.srt"
output_filename = "translated_subtitle.srt"
translate_srt(input_filename, output_filename)
