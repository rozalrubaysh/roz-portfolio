from pathlib import Path
import shutil

# Folder that will be organized
folder = Path.home() / "Downloads"

# Categories and their file extensions
categories = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt", ".pptx", ".xlsx"],
    "Videos": [".mp4", ".mov", ".avi"],
    "Audio": [".mp3", ".wav"],
    "Archives": [".zip", ".rar"]
}

for file in folder.iterdir():

    if not file.is_file():
        continue

    moved = False

    for category, extensions in categories.items():

        if file.suffix.lower() in extensions:

            destination = folder / category
            destination.mkdir(exist_ok=True)

            shutil.move(
                str(file),
                str(destination / file.name)
            )

            print(f"Moved {file.name} → {category}")
            moved = True
            break

    if not moved:
        destination = folder / "Other"
        destination.mkdir(exist_ok=True)

        shutil.move(
            str(file),
            str(destination / file.name)
        )

        print(f"Moved {file.name} → Other")

print("Done! Your files are organized.")
