import os
import re


keraksiz_words = [
    "Name", 
    "You can insert your own translation.",
    "Photocopiable © Oxford University Press 2016",
    "(",")",
    "Here is a list of useful or new words from",
    "of Navigate A1 Coursebook.",
    "Words marked with a key", 
    "all appear in the Oxford 3000",
    "You can insert your own translation.",
    "adj = adjective",
    "conj = conjunction",
    "phr v = phrasal verb",
    "phr = phrase",
    "pron = pronoun",
    "v = verb",
    "adv = adverb",
    "det = determiner",
    "n = noun",
    "pl = plural",
    "prep = preposition",
    "Unit 1",
    "Unit 2",
    "Unit 3",
    "Unit 4",
    "Unit 5",
    "Unit 6",
    "Unit 7",
    "Unit 8",
    "Unit 9",
    "Unit 10",
    "Unit 11",
    "Unit 12",
    "A1  Wordlist Unit 1",
    "A1  Wordlist Unit 2",
    "A1  Wordlist Unit 3",
    "A1  Wordlist Unit 4",
    "A1  Wordlist Unit 5",
    "A1  Wordlist Unit 6",
    "A1  Wordlist Unit 7",
    "A1  Wordlist Unit 8",
    "A1  Wordlist Unit 9",
    "A1  Wordlist Unit 10",
    "A2  Wordlist Unit 1",
    "A2  Wordlist Unit 2",
    "A2  Wordlist Unit 3",
    "A2  Wordlist Unit 4",
    "A2  Wordlist Unit 5",
    "A2  Wordlist Unit 6",
    "A2  Wordlist Unit 7",
    "A2  Wordlist Unit 8",
    "A2  Wordlist Unit 9",
    "A2  Wordlist Unit 10",
    "A2  Wordlist Unit 11",
    "A2  Wordlist Unit 12",
    "B1  Wordlist Unit 1",
    "B1  Wordlist Unit 2",
    "B1  Wordlist Unit 3",
    "B1  Wordlist Unit 4",
    "B1  Wordlist Unit 5",
    "B1  Wordlist Unit 6",
    "B1  Wordlist Unit 7",
    "B1  Wordlist Unit 8",
    "B1  Wordlist Unit 9",
    "B1  Wordlist Unit 10",
    "B1  Wordlist Unit 11",
    "B1  Wordlist Unit 12",
    "B1+  Wordlist Unit 1",
    "B1+  Wordlist Unit 2",
    "B1+  Wordlist Unit 3",
    "B1+  Wordlist Unit 4",
    "B1+  Wordlist Unit 5",
    "B1+  Wordlist Unit 6",
    "B1+  Wordlist Unit 7",
    "B1+  Wordlist Unit 8",
    "B1+  Wordlist Unit 9",
    "B1+  Wordlist Unit 10",
    "B1+  Wordlist Unit 11",
    "B1+  Wordlist Unit 12",
]
testcha = ["1","2","3","4","5"," .","  ​n  ​","  adj  ","  ​adv  ​","  ​v  ​","  det  ","Numbers –0","  ​pron  ​","A  Wordlist ","  ​conj  ​","  ​prep  ​"
           "  ​phr  ​","  ​exclamation  ​","  ​adj  ​","  ​prep  ","  ​phr  ​"]


# Faylni o'qish va tozalash funksiyasi
def clean_text(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    for word in keraksiz_words:
        content = content.replace(word, '')
    # Unit va boshqa muhim ma'lumotlarni olib tashlash
    content = re.sub(r'A\d\sWordlist\sUnit\s\d+', '', content)  # Unit nomini olib tashlash
    content = re.sub(r'Name\s*', '', content)  # 'Name' so'zini olib tashlash
    content = re.sub(r'You\scan\sinsert\syour\sown\stranslation\.', '', content)  # 'Insert translation' matnini olib tashlash
    content = re.sub(r'Words\smarked\swith\sa\skey\([^\)]+\)', '', content)  # "Words marked with a key" qismi
    content = re.sub(r'(\s*verb\s*)+', '', content)  # 'verb' kabi so'zlarni olib tashlash
    content = re.sub(r'\n+', '\n', content)  # Bo'sh qatorlarni olib tashlash
    content = re.sub(r'\s+$', '', content)  # O'ngdan bo'shliqni olib tashlash
    content = re.sub(r'^\s+', '', content)  # Chapdan bo'shliqni olib tashlash

    # So'zlarning fonetik va qisqartmalarini olib tashlash
    content = re.sub(r'\/[^\n]*', '', content)  # "phr  ​/ə ˈpiːs əv/" kabi qismni olib tashlash
    content = re.sub(r' [\w\s]+', '', content)  # Tushunarsiz bo'laklarni olib tashlash

    # Bo'sh joylar va begona belgilarni tozalash
    content = content.strip()
    for word in testcha:
        content = content.replace(word, '')

    return content

# Faylni tozalab yangi faylga yozish
def save_cleaned_file(file_name, cleaned_content):
    with open(file_name, 'w', encoding='utf-8') as file:
        file.write(cleaned_content)

# Fayllarni tozalash
def clean_all_files(folder_path):
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.txt'):
            file_path = os.path.join(folder_path, file_name)
            cleaned_content = clean_text(file_path)
            save_cleaned_file(file_path, cleaned_content)
            print(f"Fayl tozalandi: {file_name}")

# Folderdagi barcha fayllarni tozalash
folder_path = r'C:\Users\SULTON\DangasaBot\navigate_books\navigate-a1-unit-wordlist'  # Bu yerga o'z papkangizning yo'lini qo'ying
clean_all_files(folder_path)
