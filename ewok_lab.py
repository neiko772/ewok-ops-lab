# Description: Demonstrates list operations and loops with a roster of Ewoks.
#! Part 1 
print("=== Ewok Ops: List & Loops ===\n")

# A starting roster of Ewoks (a python list)
ewoks = ["Wicket", "Paploo", "Teebo", "Nippet"]

# Indexing: 0 = first, -1 = last
print("first ewok:", ewoks[0])
print("last ewok:", ewoks[-1])

# Slicing: ewoks[start:stop] (stop is exclusive)
print("Middle pair:", ewoks[1:3]) # Paploo and Teebo 

# Length of list 
print("Roster size:", len(ewoks))

#! Part 2 
print("\n-- Updating the roster --") 
ewoks.append("Chief Chirpa") #add to end
print("After append:", ewoks)

ewoks.insert(0, "Logray") #add at a specific position (index 0)
print("After insert at front:", ewoks)

ewoks.extend(["Kneesaa", "Latara"]) #add multiple at once
print("After extend:", ewoks)

ewoks.remove("Paploo") #remove the FRIST match by value
print("After removr Paploo:", ewoks)

ewoks.append("Walda")
print("After adding Walda:", ewoks)

ewoks.insert(2, "Tazia")
print("After inserting Tazia at index 2:", ewoks)

if "Teebo" in ewoks:
    ewoks.remove("Teebo")
print("After removing Teebo if present:", ewoks)

on_scout = ewoks.pop()
print("On scout:", on_scout)

# Sorting: alphabetical A-Z, then reverse
ewoks.sort()
print("Sorted A-Z:", ewoks)
ewoks.reverse()
print("Final roster (Z-A):", ewoks)

#! Part 3 
print("\n-- Roll call --")
for ewok in ewoks:
    print("Present:", ewok)

print("\n-- Numbered roll call (enumerate) --") 
for i, ewok in enumerate(ewoks, start=1):
    print(f"{i}. {ewok}")

ewoks.append("Walda")
print("After adding Walda:", ewoks)

ewoks.insert(2, "Tazia")
print("After inserting Tazia at index 2:", ewoks)

if "Teebo" in ewoks:
    ewoks.remove("Teebo")
print("After removing Teebo if present:", ewoks)

on_scout = ewoks.pop()
print("On scout:", on_scout)

ewoks.sort()
print("Sorted A-Z:", ewoks)
ewoks.reverse()
print("Final roster (Z-A):", ewoks)

#! Task B
print("\n-- L-only squad --")
for ewok in ewoks:
    if ewok.startswith("L"):
        print("L-only squad member:", ewok)

#! Task C
print("\n-- Uppercase call signs --")
call_signs =[]
for ewok in ewoks:
    call_signs.append(ewok.upper())
print(call_signs)

#! Part 5 
print("\n=== Supply drop ===")
items = ["Berries", "Spears", "Bandages", "Glider Parts"]
counts = [30, 12, 8, 6]

# Sanity check: lengths should match 
if len(items) != len(counts):
    print("Data error: items and counts are different lengths!")
else:
    total = 0
    for i in range(len(items)): #index-based loop pairs up lists
        line = f"{items[i]} x {counts[i]}"
        print(line)
        total += counts[i]
    print("Total items:", total)