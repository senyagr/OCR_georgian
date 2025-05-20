from PIL import Image, ImageDraw, ImageFont

# Указываем путь к шрифту
font_path = r"C:\Tesseract-OCR\fonts\NotoSansGeorgian-Regular.ttf"
font = ImageFont.truetype(font_path, 40)  # Устанавливаем размер шрифта

# Текст на грузинском
text = "გამარჯობა მსოფლიო"  # Пример текста: "Hello, World!" на грузинском

# Получаем размер текста с помощью getbbox()
bbox = font.getbbox(text)  # Получаем bounding box для текста
width, height = bbox[2] - bbox[0], bbox[3] - bbox[1]  # Вычисляем ширину и высоту

# Размер изображения
image = Image.new("RGB", (width + 20, height + 20), color=(255, 255, 255))  # Белое изображение

# Рисуем текст
draw = ImageDraw.Draw(image)
draw.text((10, 10), text, font=font, fill=(0, 0, 0))  # Черный текст

# Сохраняем изображение
image_path = "C:/Projects/OCR_georg/pictures/test_image.png"
image.save(image_path)

# Создание текстового файла с тем же текстом
text_file_path = "C:/Projects/OCR_georg/pictures/test_image.txt"
with open(text_file_path, "w", encoding="utf-8") as file:
    file.write(text)

# Печать результатов
print(f"Изображение и текстовый файл созданы: {image_path}, {text_file_path}")