from collections import Counter


def kelimeBul(harfler):
    harfSayisi = Counter(harfler)
    try:
        with open("sozluk.txt", "r", encoding="utf-8") as dosya:
            kelimeler = dosya.read().splitlines()
            uygunKelimeler = [kelime for kelime in kelimeler if len(kelime)==len(harfler)] # harf sayısına göre kelime filtreleme
            bulunanKelimeler = [kelime for kelime in uygunKelimeler if Counter(kelime) == harfSayisi]
            return bulunanKelimeler    
    except FileNotFoundError:
        print("Sözlük dosyası yolu HATALI.")    
        exit()
        

print("NOT : Bir harfi virgülle ayırarak birden fazla girebilirsiniz. Bu o harfin kelimede ne kadar sayıda bulunacağını gösterir.")
harfler = input("Harfleri virgüllü şekilde giriniz (Örnek a,b,c,c,c,d) : ")

# kullanıcı tarafından hatalı girilebilecek ifadeleri düzenle
harfler = harfler.strip().lower().replace(" ","").split(",")


sonuc = kelimeBul(harfler)
print("\n".join(sonuc))


