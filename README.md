# 📊 CSV Data Processor

A Python tool to read CSV files, calculate Price × Quantity = Total, and save the result to a new CSV file. Supports multiple file processing with auto-naming output.

## ✨ Features

- ✅ Read CSV files with Price and Quantity columns
- ✅ Auto-detect columns – Shows available columns in your CSV file
- ✅ Custom column selection – Choose which columns are Price and Quantity
- ✅ Calculate Total = Price × Quantity automatically
- ✅ Auto-generate output filenames (outfail_1.csv, outfail_2.csv, ...)
- ✅ Process multiple files in one session
- ✅ Error handling for missing files and invalid data
- ✅ User-friendly command-line interface

## 🛠️ Technologies

- Python 3
- CSV module (standard library)
- OS module (standard library)

## 📦 Installation

```bash
# No external packages needed - just Python 3
git clone https://github.com/Been-07/csv-data-processor.git
cd csv-data-processor
```

:rocket: Usage

Step 1: Run the program

```bash
python csv_processor.py
```

Step 2: Enter the file path

```bash
Enter the address of the desired file, otherwise enter 0 to use 
the default file (products.csv) or type exit to exit the program

Please enter (exit=exit, 0=default file): 0
```

Step 3: Select columns

After loading the file, the program shows all available columns:
```bash
📋 Available columns: ['Product', 'Price', 'Quantity']
Enter the name of the price column: Price
Enter the name of the quantity column: Quantity
```
Step 4: View results

```bash
--- Processing Session_1 ---
File saved with name outfail_1.csv
Seve to outfail_1.csv
```

Step 5: Process another file (optional)
```bash
Do you want to process another file? (Yes/No): Yes
```

:file_folder: Sample Input (products.csv)

| Price | Quantity |
| :--- | :--- |
| 100 | 5 |
| 200 | 3 |
| 150 | 2 |

:file_folder: Sample Output (outfail_1.csv)

| Price | Quantity | Total|
| :--- | :--- | :--- |
| 100 | 5 | 500 |
| 200 | 3 | 600 |
| 150 | 2 | 300 |

:dart: Example Session

```bash
==================================================================
                        CSV-Data-Processor
               Calculates Price × Quantity = Total
==================================================================
                   --- Processing Session_1 ---
==================================================================
Enter the address of the desired file, otherwise enter 0 to use 
the default file (products.csv) or type exit to exit the program
==================================================================
Please enter (exit=quit, 0=default): 0

File saved with name outfail_1.csv
Enter the name of the price column (e.g. price or unit_price): Price
Enter the name of the number column (e.g. quantity or count): Quantity
Seve to outfail_1.csv

Do you want to process another file? (Yes/No): No
bye bye
```

:file_folder: Project Structure

```
CSV-Data-Processor/
├── csv_processor.py    # Main Python script
├── products.csv        # Sample input file
├── README.md           # Project documentation
├── .gitignore          # Git ignore file
└── LICENSE             # MIT License
```

:warning: Requirements

· The CSV file must contain columns with numeric values (you can choose any column names)

· Values in selected columns must be numbers (integers)

:bug: Error Handling

Error Program Response
File not found File not found, try again
Invalid Price or Quantity Error processing row and continues
Empty or missing columns Skips the row with warning

👨‍💻 Author

Benjamin Shojaee | [GitHub](https://github.com/Been-07) | [ORCID](https://orcid.org/0009-0005-2756-7140)
