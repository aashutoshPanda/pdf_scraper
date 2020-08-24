from pathlib import Path
import textract


for path in Path("profile_pdfs").iterdir():
    if path.is_file():
        if path.suffix != ".pdf":
            continue
        text = textract.process(path)
        print(text)
