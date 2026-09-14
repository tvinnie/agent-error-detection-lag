from pathlib import Path
import json

DATA_DIR = Path("data")

print("=" * 60)
print("DATASET INVENTORY")
print("=" * 60)

files = [f for f in DATA_DIR.rglob("*") if f.is_file()]

print(f"\nTotal files: {len(files)}")

for file in files:
    print("\n" + "-" * 60)
    print(f"File: {file}")
    print(f"Size: {file.stat().st_size:,} bytes")

    if file.suffix.lower() == ".json":
        try:
            with open(file, "r", encoding="utf-8") as f:
                data = json.load(f)

            if isinstance(data, list):
                print(f"Records: {len(data)}")

                if data:
                    print(f"Fields: {list(data[0].keys())}")

            elif isinstance(data, dict):
                print(f"Top-level fields: {list(data.keys())}")

        except Exception as e:
            print(f"Could not parse: {e}")