from PIL import Image, ImageDraw, ImageOps

def add_zodiac_sign(profile_image, birth_day, birth_month):
    # Laden des Profilbilds
    try:
        img = Image.open(profile_image)
    except IOError:
        print("Fehler: Das angegebene Profilbild konnte nicht geladen werden.")
        return

    # Unicode-Zeichen für die Sternzeichen
    zodiac_symbols = [
        "\u2648", "\u2649", "\u264A", "\u264B",
        "\u264C", "\u264D", "\u264E", "\u264F",
        "\u2650", "\u2651", "\u2652", "\u2653"
    ]

    # Zeichen für das entsprechende Sternzeichen
    zodiac_symbol = zodiac_symbols[birth_month - 1]

    # Erstelle ein neues Bild für das Sternzeichen
    zodiac_img = Image.new("RGBA", (100, 100), (0, 0, 0, 0))
    draw = ImageDraw.Draw(zodiac_img)
    draw.text((40, 40), zodiac_symbol, fill=(0, 0, 0, 128))

    # Füge das Sternzeichenbild in die obere rechte Ecke des Profilbilds ein
    img.paste(zodiac_img, (img.width - 100, 0), zodiac_img)

    # Speichere das bearbeitete Bild ab
    output_path = "output_image.png"
    img.save(output_path)
    print(f"Das bearbeitete Bild wurde unter {output_path} gespeichert.")

# Hauptprogramm
if __name__ == "__main__":
    try:
        profile_image_path = input("Pfad zum Profilbild: ")
        birth_day = int(input("Geburtstag (Tag): "))
        birth_month = int(input("Geburtsmonat (Zahl): "))
        
        if birth_month < 1 or birth_month > 12:
            print("Fehler: Ungültiger Geburtsmonat.")
        else:
            add_zodiac_sign(profile_image_path, birth_day, birth_month)
    except ValueError:
        print("Fehler: Ungültige Eingabe. Bitte stellen Sie sicher, dass Sie korrekte Werte eingeben.")
