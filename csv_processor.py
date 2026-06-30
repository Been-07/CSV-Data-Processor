# ======================================|
# Author: Benjamin Shojaee              |
# GitHub: https://github.com/Been-07    |
# ORCID: 0009-0005-2756-7140            |
# ======================================|

import csv
import os

# Generate next output file name (like output_1.csv, output_2.csv, ...)
def next_output(base="output"):
    n = 1
    while True:
        fname = f"{base}_{n}.csv"
        if not os.path.exists(fname):
            return fname
        n += 1

# Process one CSV file
def process_file(input_path, output_path):
    with open(input_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        print("Columns:", reader.fieldnames)

        price_col = input("Price column name: ")
        qty_col = input("Quantity column name: ")

        rows = []
        for row in reader:
            try:
                price = float(row[price_col])   # allow decimal too
                qty = float(row[qty_col])
                row["Total"] = price * qty
                rows.append(row)
            except (ValueError, KeyError) as e:
                print(f"Skipping row: {e}")

        if rows:
            with open(output_path, "w", newline="", encoding="utf-8") as out:
                writer = csv.DictWriter(out, fieldnames=rows[0].keys())
                writer.writeheader()
                writer.writerows(rows)
            print(f"Saved to {output_path}")
            return True
        else:
            print("No valid data")
            return False

# Get input file from user
def get_input():
    while True:
        print("\n" + "=" * 60)
        print("Enter file path (0 = products.csv, exit = quit)")
        inp = input("> ").strip()

        if inp.lower() == "exit":
            return None
        if inp == "0":
            path = "products.csv"
        else:
            path = inp

        if os.path.exists(path):
            return path
        print("File not found, try again")

# Main loop
def main():
    print("=" * 60)
    print("CSV PROCESSOR".center(60))
    print("Price × Quantity = Total".center(60))
    print("=" * 60)

    session = 1
    while True:
        print(f"\n--- Session {session} ---")
        infile = get_input()
        if infile is None:
            print("Bye")
            break

        outfile = next_output()
        print("Output will be:", outfile)

        try:
            process_file(infile, outfile)
        except Exception as e:
            print("Error:", e)

        session += 1
        again = input("Process another file? (y/n): ").lower()
        if again != "y":
            print("Bye")
            break

if __name__ == "__main__":
    main()
