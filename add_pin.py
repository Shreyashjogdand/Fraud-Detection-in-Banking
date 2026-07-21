import sqlite3

conn = sqlite3.connect('BankNH.db')
cur = conn.cursor()

# Add the PIN column if it isn't there yet
cols = [r[1] for r in cur.execute("PRAGMA table_info(NEWBANK)").fetchall()]
if "PIN" not in cols:
    cur.execute("ALTER TABLE NEWBANK ADD COLUMN PIN TEXT")
    print("PIN column added.")
else:
    print("PIN column already exists.")

# Existing users (registered before PIN existed) get a default PIN of 1234
# so they can still authorise large transfers during the demo.
cur.execute("UPDATE NEWBANK SET PIN = '1234' WHERE PIN IS NULL OR PIN = ''")
conn.commit()

print("\nUsers now:")
for r in cur.execute("SELECT USERNAME, BAL, PIN FROM NEWBANK"):
    print("  ", r)

conn.close()
print("\nDone")