import os
import pymupdf

# Kitoblar joylashgan papka
BOOKS_FOLDER = "navigate_books"

# Menda kitoblari ro'yxati
menda_books = [
    {
        "navigate-a1-unit-wordlist":{
            "file":"navigate-a1-unit-wordlist.pdf",
            "unit1":[1,2],
            "unit2":[3,4,5],
            "unit3":[6,7],
            "unit4":[8,9,10],
            "unit5":[11,12,13],
            "unit6":[14,15],
            "unit7":[16,17],
            "unit8":[18,19],
            "unit9":[20,21],
            "unit10":[22,23]
        }
    },
    {
        "navigate-a2-unit-wordlist":{
            "file":"navigate-a2-unit-wordlist.pdf",
            "unit1":[1,2],
            "unit2":[3,4],
            "unit3":[5,6],
            "unit4":[7,8],
            "unit5":[9,10],
            "unit6":[11,12],
            "unit7":[13,14],
            "unit8":[15,16],
            "unit9":[17,18],
            "unit10":[19,20],
            "unit11":[21,22],
            "unit12":[23,24]
            
        }
    },
    {
        "navigate-b1-unit-wordlist":{
            "file":"navigate-b1-unit-wordlist.pdf",
            "unit1":[1,2],
            "unit2":[3,4],
            "unit3":[5,6],
            "unit4":[7,8],
            "unit5":[9,10],
            "unit6":[11,12],
            "unit7":[13,14],
            "unit8":[15,16],
            "unit9":[17,18],
            "unit10":[19,20],
            "unit11":[21,22],
            "unit12":[23,24]
            
        }
    },
    {
        "navigate-b1plus-unit-wordlist":{
            "file":"navigate-b1plus-unit-wordlist.pdf",
            "unit1":[1,2],
            "unit2":[3,4,5],
            "unit3":[6,7,8],
            "unit4":[9,10],
            "unit5":[11,12,13],
            "unit6":[14,15,16],
            "unit7":[17,18,19,20],
            "unit8":[21,22,23],
            "unit9":[24,25],
            "unit10":[26,27,28],
            "unit11":[29,30],
            "unit12":[31,32]
            
        }
    },
    {
        "navigate-b2-unit-wordlist":{
            "file":"navigate-b2-unit-wordlist.pdf",
            "unit1":[1,2,3],
            "unit2":[4,5,6,7],
            "unit3":[8,9,10],
            "unit4":[11,12,13],
            "unit5":[14,15,16],
            "unit6":[17,18],
            "unit7":[19,20,21],
            "unit8":[22,23,24],
            "unit9":[25,26],
            "unit10":[27,28],
            "unit11":[29,30,31],
            "unit12":[32,33]
            
        }
    },
    {
        "navigate-c1-unit-wordlist":{
            "file":"navigate-c1-unit-wordlist.pdf",
            "unit1":[1,2,3],
            "unit2":[4,5,6,7],
            "unit3":[8,9,10],
            "unit4":[11,12,13],
            "unit5":[14,15,16],
            "unit6":[17,18,19],
            "unit7":[20,21,22],
            "unit8":[23,24,25],
            "unit9":[26,27,28],
            "unit10":[29,30,31],
            "unit11":[32,33,34],
            "unit12":[35,36,37]
            
        }
    },
]


def extract_units(book_data, books_folder="navigate_books"):
    """PDF fayldan unitlarni belgilangan sahifalar bo'yicha ajratib olish"""
    try:
        book_name = list(book_data.keys())[0]
        book_info = book_data[book_name]
        
        # PDF fayl yo'li
        pdf_path = os.path.join(books_folder, book_info["file"])
        
        if not os.path.exists(pdf_path):
            print(f"{book_info['file']} fayli topilmadi! O'tkazib yuborildi.")
            return False
        
        # Unitlar uchun papka yaratish
        output_folder = os.path.join(books_folder, book_name)
        os.makedirs(output_folder, exist_ok=True)
        
        # PDF faylni ochish
        doc = pymupdf.open(pdf_path)
        
        # Har bir unit uchun ishlash
        for unit_name, pages in book_info.items():
            if unit_name == "file":
                continue  # "file" kaliti ma'lumot uchun, uni o'tkazamiz
            
            unit_text = ""
            for page_num in pages:
                # PDF sahifalari 0-indeksli, shuning uchun 1 ni ayiramiz
                page = doc[page_num - 1]
                text = page.get_text()
                if text:
                    unit_text += f"{text}\n\n"
            
            if unit_text:
                # Unit faylini saqlash
                unit_filename = f"{unit_name}.txt"
                unit_path = os.path.join(output_folder, unit_filename)
                
                with open(unit_path, 'w', encoding='utf-8') as f:
                    f.write(unit_text)
                print(f"{book_name}: {unit_filename} saqlandi")
        
        doc.close()
        return True
    
    except Exception as e:
        print(f"Xato: {book_name} qayta ishlanmadi - {str(e)}")
        return False

def process_all_books():
    """Barcha kitoblarni qayta ishlash"""
    print("DangasaBot - PDF dan Unitlarni ajratish boshlandi...")
    
    # navigate_books papkasini tekshirish
    if not os.path.exists("navigate_books"):
        print("navigate_books papkasi topilmadi! Iltimos, loyiha ildizida papka yarating.")
        return
    
    for book_data in menda_books:
        extract_units(book_data)
    
    print("Barcha kitoblar qayta ishlandi!")

if __name__ == "__main__":
    process_all_books()