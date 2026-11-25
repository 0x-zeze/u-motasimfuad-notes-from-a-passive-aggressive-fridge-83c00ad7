"""Write the passive-aggressive fridge entry to /output/entry.txt."""

from pathlib import Path

ENTRY = (
    "My sensors found the leftovers behind the pickles in 0.4 seconds. "
    "Your keys have been missing for three days. I know exactly where they are."
)


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(f"{ENTRY}\n", encoding="utf-8")


if __name__ == "__main__":
    main()
