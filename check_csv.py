import os
folder = os.getcwd()
print("Current folder:", folder)
print()
print("CSV files found here:")
csvs = [f for f in os.listdir(folder) if f.lower().endswith(".csv")]
if csvs:
    for f in csvs:
        size_mb = os.path.getsize(f) / (1024*1024)
        print(f"   {f}   ({size_mb:.0f} MB)")
else:
    print("   NONE — no CSV file is in this folder.")