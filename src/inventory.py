from pathlib import Path
import json
import pandas as pd

DATA_DIR = Path("data")

print("=" * 60)
print("DATASET INVENTORY")
print("=" * 60)

files = sorted(
    f for f in DATA_DIR.rglob("*") if f.is_file()
)

print(f"\nTotal files: {len(files)}")

# Store results for verification
inventory_records = []
field_records = []
parse_errors = []

for file in files:
    print("\n" + "-" * 60)
    print(f"File: {file}")
    print(f"Size: {file.stat().st_size:,} bytes")

    file_info = {
        "File": str(file.relative_to(DATA_DIR)),
        "Size (KB)": round(file.stat().st_size / 1024, 2),
        "Records": 0
    }

    if file.suffix.lower() == ".json":
        try:
            with open(file, "r", encoding="utf-8") as f:
                data = json.load(f)

            if isinstance(data, list):
                print(f"Records: {len(data)}")
                file_info["Records"] = len(data)

                if data and isinstance(data[0], dict):
                    print(f"Fields: {list(data[0].keys())}")

                rows = data

            elif isinstance(data, dict):
                print(f"Top-level fields: {list(data.keys())}")

                # Treat a top-level dictionary as one record
                rows = [data]
                file_info["Records"] = 1

            else:
                rows = []

            # Collect dictionary records for field analysis
            for row in rows:
                if isinstance(row, dict):
                    field_records.append(row)

        except Exception as e:
            print(f"Could not parse: {e}")
            parse_errors.append(str(file))
            file_info["Records"] = None

    inventory_records.append(file_info)

# Generating the file inventory table.
print("\n" + "=" * 60)
print("FILE INVENTORY SUMMARY")
print("=" * 60)

inventory_df = pd.DataFrame(inventory_records)

display(inventory_df)

total_json_files = sum(
    file.suffix.lower() == ".json" for file in files
)

total_records = inventory_df["Records"].sum()

print(f"\nTotal files: {len(files)}")
print(f"Total JSON files: {total_json_files}")
print(f"Total top-level records: {int(total_records)}")
print(f"JSON parsing errors: {len(parse_errors)}")


#The Field Types & Missing Value Rates
print("\n" + "=" * 60)
print("STEP 4B: FIELD SUMMARY")
print("=" * 60)

if field_records:

    df = pd.DataFrame(field_records)

    # Treat None, NaN, empty strings, and empty containers
    # as missing values
    def is_missing(value):
        if value is None:
            return True
        if isinstance(value, str):
            return value.strip() == ""
        if isinstance(value, (list, dict)):
            return len(value) == 0
        try:
            return bool(pd.isna(value))
        except (TypeError, ValueError):
            return False

    field_summary = []

    for column in df.columns:

        missing_count = sum(
            is_missing(value) for value in df[column]
        )

        missing_rate = (
            missing_count / len(df) * 100
            if len(df) > 0 else 0
        )

        # Show actual Python types found in the field
        data_types = sorted({
            type(value).__name__
            for value in df[column]
            if not is_missing(value)
        })

        field_summary.append({
            "Field": column,
            "Data Type": ", ".join(data_types) or "Unknown",
            "Missing Count": missing_count,
            "Missing Rate (%)": round(missing_rate, 2)
        })

    field_summary_df = pd.DataFrame(field_summary)

    display(field_summary_df)

else:
    field_summary_df = pd.DataFrame()
    print("No dictionary records found.")