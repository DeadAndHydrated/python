# mengimport 4 hal:
# a. os (operation system)
# b. pygame (untuk menjalankan audio)
# c. gtts (untuk mengekstrak file menjadi bentuk audio)
# d. pypdf2 (untuk membaca dan mengekstrak file dari PDF)
import os
import pygame
from gtts import gTTS
from PyPDF2 import PdfReader

#memberikan lokasi file yang akan digunakan 
pdf_path = r'C:/Users/LENOVO/.vscode/python/UUD45 ASLI.pdf'

#teks yang ditampilkan sebelum teks pdf bisa ditampilkan
print(f"Attempting to open file: {pdf_path}")

#if command
#jika path (lokasi file ditemukan) maka jalankan program berikut
if os.path.exists(pdf_path):
    #mencoba menjalankan mixer (salah satu modul pada pygame) supaya bisa menjalankan suara
    try:
        pygame.init()
        pygame.mixer.init()

        #membuka file pdf dan membacanya dengan mode read binary (rb)
        with open(pdf_path, 'rb') as file:
            pdfreader = PdfReader(file)

            #menngekstrak file pdf dan mengubah enter menjadi spasi
            for page in range(len(pdfreader.pages)):
                text = pdfreader.pages[page].extract_text()
                legible_text = text.strip().replace('\n', ' ')

                #print text yang sudah diekstrak
                print(legible_text)

                #mengatur bahasa dan menyimpan hasil ekstrak ke audio file
                tts = gTTS(legible_text, lang='id')
                tts.save('file.mp3')

                #memuat dan memutar file audio yang sudah bisa diubah
                pygame.mixer.music.load('file.mp3')
                pygame.mixer.music.play()

                #mengontrol frame rate pada loop dengan menyalakan tick pada pygame selama 10 detik
                while pygame.mixer.music.get_busy():
                    pygame.time.Clock().tick(10)

        #mengakhiri progres
        pygame.quit()

    #pemberitahuan error apabila gagal
    except Exception as e:
        print(f"An error occurred: {e}")

#pemberitahuan error apabila file tidak dapat ditemukan
else:
    print(f"File not found: {pdf_path}")
