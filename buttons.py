from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

def main_menu() -> ReplyKeyboardMarkup:
    """
    Asosiy menyu tugmalari
    """
    builder = ReplyKeyboardBuilder()
    
    builder.button(text="📊 Testlar")
    builder.button(text="Tarjimon")
    builder.button(text="Mening lug'atlarim")
    builder.button(text="Mening testlarim")
    builder.button(text="Yuklab olish")
    builder.button(text="Profil")
    
    builder.adjust(2, 2, 2)  # 2 ta tugma har bir qatorda
    return builder.as_markup(resize_keyboard=True, input_field_placeholder="Tugmalardan birini tanlang")

def tests_menu() -> ReplyKeyboardMarkup:
    """
    Testlar menyusi
    """
    buttons = [
        [KeyboardButton(text="Ingliz tili testlari")],
        [KeyboardButton(text="Rus tili testlari")],
        [KeyboardButton(text="Matematika testlari")],
        [KeyboardButton(text="← Orqaga")]
    ]
    return ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)

def translation_options() -> InlineKeyboardMarkup:
    """
    Tarjima variantlari uchun inline tugmalar
    """
    builder = InlineKeyboardBuilder()
    
    builder.button(text="O'zbek", callback_data="uz_1")
    builder.button(text="O'zbek", callback_data="uz_2")

    builder.button(text="English", callback_data="en_1")
    builder.button(text="English", callback_data="en_2")

    # tayor tugma
    builder.button(text="Tayyor",callback_data="tayor")
    
    builder.adjust(2)  # 2 ta tugma har bir qatorda
    return builder.as_markup()

def download_options() -> InlineKeyboardMarkup:
    """
    Yuklab olish variantlari
    """
    buttons = [
        [InlineKeyboardButton(text="PDF formatda", callback_data="download_pdf")],
        [InlineKeyboardButton(text="TXT formatda", callback_data="download_txt")],
        [InlineKeyboardButton(text="Excel formatda", callback_data="download_excel")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)

def profile_actions() -> InlineKeyboardMarkup:
    """
    Profil uchun amallar
    """
    builder = InlineKeyboardBuilder()
    
    builder.button(text="📊 Statistika", callback_data="profile_stats")
    builder.button(text="✏️ Ismni o'zgartirish", callback_data="profile_change_name")
    builder.button(text="🔄 Qayta yuklash", callback_data="profile_refresh")
    
    builder.adjust(1)  # Har bir tugma alohida qatorda
    return builder.as_markup()