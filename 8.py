import requests

url = "https://cbu.uz/uz/arkhiv-kursov-valyut/json/"

try:
    
    kod = input("Valyuta kodini kiriting (USD, EUR, RUB): ").upper()

    miqdor = float(input("Miqdorni kiriting: "))

    if miqdor <= 0:
        print("Miqdor musbat son bo'lishi kerak!")

    else:
        
        javob = requests.get(url, timeout=10)

        
        valyutalar = javob.json()

        
        topildi = False

        for valyuta in valyutalar:
            if valyuta["Ccy"] == kod:

                nomi = valyuta["CcyNm_UZ"]
                nominal = float(valyuta["Nominal"])
                kurs = float(valyuta["Rate"])

                
                bir_birlik_kurs = kurs / nominal

                jami = miqdor * bir_birlik_kurs

                print("\n--- VALYUTA MA'LUMOTLARI ---")
                print("Valyuta:", nomi)
                print("Miqdor:", miqdor, kod)
                print("Nominal:", nominal)
                print("Bir birlik kursi:", bir_birlik_kurs, "so'm")
                print("Kurs sanasi:", valyuta["Date"])
                print("Jami:", round(jami, 2), "so'm")

                topildi = True
                break

        if not topildi:
            print("Bunday valyuta kodi topilmadi!")

except ValueError:
    print("Miqdorni son ko'rinishida kiriting!")

except requests.exceptions.RequestException:
    print("Internet yoki API bilan bog'lanishda xatolik!")

except (KeyError, TypeError):
    print("API ma'lumotlarini o'qishda xatolik!")
