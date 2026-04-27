import os
from pathlib import Path
from dotenv import load_dotenv
from PIL import Image

load_dotenv()
TARGET_DIR = Path(os.getenv("TARGET_DIR"))

IMAGE_EXTENSIONS = {'.webp', '.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff'}


def main():
    if not TARGET_DIR.exists():
        print(f"❌ Папка {TARGET_DIR} не найдена")
        return

    # Ищем все изображения в указанной папке (без подпапок)
    files = [f for f in TARGET_DIR.iterdir() if f.is_file() and f.suffix.lower() in IMAGE_EXTENSIONS]
    total = len(files)

    if total == 0:
        print("Нет изображений для конвертации")
        return

    converted = 0
    for file_path in files:
        if file_path.suffix.lower() == '.png':
            print(f"⏭️ Пропуск (уже PNG): {file_path.name}")
            continue

        try:
            img = Image.open(file_path)
            new_path = file_path.with_suffix('.png')
            img.save(new_path, 'PNG')
            file_path.unlink()  # удаляем оригинал
            converted += 1
            print(f"✅ {file_path.name} → {new_path.name} [{converted}/{total}]")
        except Exception as e:
            print(f"❌ Ошибка {file_path.name}: {e}")

    print(f"\nГотово! Конвертировано {converted} из {total} файлов.")


if __name__ == "__main__":
    main()