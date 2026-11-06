from pathlib import Path


folder = Path(
    "new_folder"
)

folder.mkdir(
    exist_ok=True
)

print("Folder Created")