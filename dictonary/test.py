namuna = """
Photocopiable © Oxford University Press 2016
1
Name 
A1  Wordlist Unit 5
Here is a list of useful or new words from Unit 5 of Navigate A1 Coursebook. You can insert your own translation.
Words marked with a key (
) all appear in the Oxford 3000.
adj = adjective	
conj = conjunction	
phr v = phrasal verb	
phr = phrase	
pron = pronoun	
v = verb
adv = adverb	
det = determiner	
n = noun	
pl = plural	
prep = preposition
"""
import os

folder_path = r'C:\Users\SULTON\DangasaBot\navigate_books\navigate-a1-unit-wordlist'

# Papka mavjudligini tekshirish
if os.path.exists(folder_path):
    print(f"Papka mavjud: {folder_path}")
else:
    print(f"Papka topilmadi: {folder_path}")
