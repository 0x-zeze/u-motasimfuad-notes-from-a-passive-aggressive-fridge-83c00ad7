from pathlib import Path

NOTE = "My sensors found the leftovers behind the pickles in 0.4 seconds. Your keys have been missing for three days. I know exactly where they are."

if __name__ == "__main__":
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(NOTE, encoding="utf-8")
