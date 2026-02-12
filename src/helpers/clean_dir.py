from pathlib import Path

path  = Path("assets/ME135Lecture").resolve()
for p in path.iterdir():
    if p.is_dir() and p.name.endswith(".pdf"):
        new_path = p.with_name(p.name.removesuffix(".pdf"))
        p.rename(new_path)