from googletrans import Translator, LANGUAGES
from typing import Tuple, Optional

# Tarjimon obyektini yaratish
translator = Translator()

def translate_text(text: str, src: str = 'auto', dest: str = 'en') -> Tuple[Optional[str], Optional[str]]:
    """
    Matnni bir tildan ikkinchi tilga tarjima qilish
    :param text: Tarjima qilinadigan matn
    :param src: Manba til kodi (avto aniqlash uchun 'auto')
    :param dest: Belgilangan til kodi
    :return: (tarjima, manba_tili) yoki (None, None) xato yuz berganda
    """
    try:
        result = translator.translate(text, src=src, dest=dest)
        return result.text, result.src
    except Exception as e:
        print(f"Tarjima xatosi: {e}")
        return None, None


def uz_to_en(text: str) -> Optional[str]:
    """
    Uzbek tilidan Ingliz tiliga tarjima
    :param text: Uzbekcha matn
    :return: Inglizcha tarjima yoki None xato yuz berganda
    """
    translation, _ = translate_text(text, src='uz', dest='en')
    return translation

def en_to_uz(text: str) -> Optional[str]:
    """
    Ingliz tilidan Uzbek tiliga tarjima
    :param text: Inglizcha matn
    :return: Uzbekcha tarjima yoki None xato yuz berganda
    """
    translation, _ = translate_text(text, src='en', dest='uz')
    return translation

