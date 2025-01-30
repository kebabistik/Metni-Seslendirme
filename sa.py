from gtts import gTTS
import os

def metni_sese_cevir(metin, dosya_adi="ses.mp3"):
    """Girilen metni MP3 ses dosyasına çevirir ve oynatır."""
    tts = gTTS(text=metin, lang="tr")
    tts.save(dosya_adi)
    os.system(f"start {dosya_adi}")  # Windows için

    print(f"✅ Ses dosyan hazır: {dosya_adi}")

# Kullanıcıdan metin al
metin = input("Seslendirilmesini istediğin metni gir: ")
metni_sese_cevir(metin)
