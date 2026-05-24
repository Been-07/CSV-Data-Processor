# ======================================|
# Author: Benjamin Shojaee              |
# GitHub: https://github.com/Been-07    |
# ORCID: 0009-0005-2756-7140            |
# ======================================|
import csv
import os

# Function to generate a new output filename that does not already exist
def get_next_outfail(base = "outfail"):
     # Start counter from 1
     counter = 1
     # Keep trying until we find an unused filename
     while True:
          # Create filename like outfail_1.csv, outfail_2.csv, etc
          fail_name = f"{base}_{counter}.csv"
          # If no file with this name exists, return it
          if not os.path.exists(fail_name):
               return fail_name
          # Otherwise increment counter and try again
          counter +=1

# Main processing function: reads CSV, multiplies price by quantity, writes new CSV
def formol(data,outfail):
     # List to store all successfully processed rows (as dictionaries)
     all_fild = []
     # Create a DictReader object to read CSV with headers
     rieder = csv.DictReader(data)
     # Print available column names to help user decide
     print(rieder.fieldnames)
     # Ask user which column contains the price
     value_price = input("Enter the name of the price column (e.g. price or unit_price): ")
     # Ask user which column contains the quantity
     value_quantity = input("Enter the name of the number column (e.g. quantity or count): ")
     # Iterate over each row in the CSV file
     for lines in rieder:
          try:
               # Convert price value to integer
               Price = int(lines[value_price])
               # Convert quantity value to integer
               Quantity = int(lines[value_quantity])
               # Add a new key 'Total' with the product of price and quantity
               lines['Total'] = Price * Quantity
               # Append this enriched row to the list
               all_fild.append(lines)
          # Catch errors: missing column (KeyError) or non-integer value (ValueError)
          except(ValueError,KeyError) as Error:
               # Print error and skip this row
               print(f"Error processing row: {Error}")
               continue

     # After processing all rows, check if we have any valid data
     if all_fild:
          # Store the output filename for later message (because outfail will be overwritten)
          name_outfail = outfail
          # Open output file in write mode (text mode, newline='' to avoid extra blank lines)
          with open(outfail, mode='w', newline='') as outfail:
               # Create a DictWriter using field names from the first row (keys of first dict)
               write = csv.DictWriter(outfail, fieldnames=all_fild[0].keys())
               # Write the header row
               write.writeheader()
               # Write all processed rows
               write.writerows(all_fild)
          # Inform user where the file was saved
          print(f"Save to {name_outfail}")
          return True
     else:
          # No valid rows to write
          print("No data available")
          return False

# Function to get a valid input file path from the user
def get_failname():
    # Keep asking until valid input or exit
    while True:
        # Print decorative banner
        print("=" * 130)
        print("Enter the address of the desired file, otherwise enter 0 to use the default file (products.csv) or type exit to exit the program".center(130))
        print("=" * 130)
        # Get user input, strip spaces, capitalize first letter (so 'exit' becomes 'Exit')
        address_user = input("\nPlease enter the address (for exit: exit, for default address: 0): ").strip().capitalize()
        # If user typed 'Exit', return None to signal program termination
        if address_user == "Exit":
            return None
        # If user typed '0', use default filename 'products.csv'
        if address_user == "0":
            file_name = "products.csv"
        else:
            # Otherwise treat input as a custom file path
            file_name = address_user
        # Check if the file exists on disk
        if os.path.exists(file_name):
            return file_name
        else:
            # File not found, show error and repeat loop
            print(f"File {file_name} not found, try again")
             
# Main program entry point                        
def main():
    # Print welcome banner
    print("=" * 130)
    print("CSV-Data-Processor".center(130))
    print("Calculates Price × Quantity = Total".center(130))
    print("=" * 130)
    # Counter to show processing session number (1,2,3...)
    counter = 1
    # Main loop: allow user to process multiple files until they choose to exit
    while True:
        print(f"--- Processing Session_{counter} ---".center(130))
        # Get input file path (or None if exit)
        deta = get_failname()
        if deta is None:
            print("bye bye")
            break
        # Generate a unique output filename (e.g., outfail_1.csv)
        outfail = get_next_outfail()
        print(f"File saved with name {outfail}")
        try:
            # Open input file in read mode
            with open(deta,mode="r") as file:
                # Call processing function
                formol(file,outfail)
        except Exception as error:
            # Catch any unexpected errors (e.g., file access issues)
            print(f"Error File: {error}")
        # Increment session counter
        counter += 1
        print("\n" + "-" * 100)
        # Ask user if they want to process another file
        again = input("Do you want to process another file? (Yes/No): ").strip().lower()
        if again != "yes":
            print("bye bye")
            break


# Standard Python idiom: run main() only when script is executed directly
if __name__ == "__main__":
    main()
