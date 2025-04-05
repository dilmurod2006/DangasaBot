import os
import json

# Foydalanuvchidan nechta unit borligini so'raymiz
unit_count = int(input("Nechta unitni o‘zgartirmoqchisiz? (Masalan: 10): "))

# Txt fayllar joylashgan folder yo'li
folder_path = r"C:\Users\SULTON\DangasaBot\navigate_books\tozalanganlar\navigate-c1-unit-wordlist"

# Yakuniy JSON struktura
result = {"navigate_c1": {}}

# Faqat berilgancha unitlarni ko'rib chiqamiz
for i in range(1, unit_count + 1):
    filename = f"unit{i}.txt"
    file_path = os.path.join(folder_path, filename)
    unit_name = f"unit{i}"
    unit_data = []

    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            lines = [line.strip() for line in f if line.strip()]
            for j in range(0, len(lines), 2):
                if j + 1 < len(lines):
                    word = lines[j]
                    sentence = lines[j + 1]
                    unit_data.append({
                        "en": word,
                        "gap": sentence
                    })
        result["navigate_c1"][unit_name] = unit_data
    else:
        print(f"{filename} topilmadi, o‘tkazib yuborildi.")

# JSON faylga yozish
output_path = os.path.join(folder_path, "navigate_c1.json")
with open(output_path, "w", encoding="utf-8") as json_file:
    json.dump(result, json_file, ensure_ascii=False, indent=4)

print(f"\n✅ {unit_count} ta unitdan JSON yaratildi: {output_path}")
