#A 1. Input data: quantity of milk collection in liters from farmers of AGRICOOP MILK COLLECTION
milk_collection = (250, 320, 280, 380, 420, 700, 500, 100)

print(f"initial data: {milk_collection}")

# 2.calculation
total_milk = sum(milk_collection)
num_farmers= len(milk_collection)
average_milk= total_milk/num_farmers
max_collection= max(milk_collection)
min_collection= min(milk_collection)

# display result
print(f" total milk collected : {total_milk} liters")
print(f" average milk collected : {average_milk:.2f} liters") # formatted to 2 decimal place
print(f" maximum milk collected : {max_collection} liters")
print(f" minimum milk collected : {min_collection} liters")

# B  1. create 2 separate f-string for the summary 
total_summary= f"Total milk collected summary: total of {total_milk} liters were collected over {num_farmers} farmers"
average_summary=f"Average milk collected summary: the average milk collected from farmers was {average_milk:.2f} liters"

# 2.combine to make final to make final report
report_header= "-- Agricoop milk collections from farmers report --"
final_report= (f""" 
{report_header}

{total_summary}
{average_summary}
Hightest quantity of milk collected : {max_collection} liters
lowest quantity of milk collected: {min_collection} liters
-----------------------------------------------
""")
print(final_report)

# C 1. Set performance threshold
average_threshold= 300
min_milk_collected_threshold= 200
print(f"Checking against standards: Average > {average_threshold} AND Minimum > {min_milk_collected_threshold}")

# 2. Apply boolean condition
if (average_milk > average_threshold) and (min_collection > min_milk_collected_threshold):
  # 3.this block run if both condition are true 
  status = "✅ Above Standard: Performance targets were met."
else:    
     # 4. This block runs if one or both conditions are False
    status = "❌ Below Standard: Performance targets were not met."

print(status)

# D # 1. Start with the initial list of collections
collection_records = [250, 320, 280, 380, 420, 700, 500, 100]
print(f"Original list of records: \n{collection_records}")

# 2. Add a new element (new farmer)
new_collection = 570
collection_records.append(new_collection)
print(f"\nList after adding {new_collection}: \n{collection_records}")

# 3. Remove an element based on a condition (remove the lowest value) 
lowest_value = min(collection_records)
collection_records.remove(lowest_value)
print(f"\nList after removing {lowest_value}: \n{collection_records}")

print("---------------------------------------------")

import array

# Original milk collection data (list)
milk_collection_list = [250, 320, 280, 380, 420, 700, 500, 100]

# 1. Create a numeric subset for the array
numeric_subset = milk_collection_list[:4] # Using the first four values: [250, 320, 280, 380]
print(f"Subset of data: {numeric_subset}")

# 2. Store the subset in an array
# 'i' is a type code for a signed integer
milk_array = array.array('i', numeric_subset)
print(f"Array version: {milk_array}")

# 3. Compute the sum for both the array and the list subset
sum_from_array = sum(milk_array)
sum_from_list_subset = sum(numeric_subset)

print(f"\nSum from array: {sum_from_array}")
print(f"Sum from list subset: {sum_from_list_subset}")

# 4. Compare the sums
if sum_from_array == sum_from_list_subset:
    print("\n✅ The sum from the array and the list subset are identical.")
else:
    print("\n❌ The sums are different.")

# 1. Build a list of dictionaries for Agricoop Milk Collection
milk_records = [
    {'id': 1, 'name': 'Farmer A', 'value': 250},
    {'id': 2, 'name': 'Farmer B', 'value': 320},
    {'id': 3, 'name': 'Farmer C', 'value': 280},
    {'id': 4, 'name': 'Farmer D', 'value': 380},
    {'id': 5, 'name': 'Farmer E', 'value': 420},
    {'id': 6, 'name': 'Farmer F', 'value': 700},
    {'id': 7, 'name': 'Farmer G', 'value': 500},
    {'id': 8, 'name': 'Farmer H', 'value': 100},
]
print(f"--- Initial Records ---\n{milk_records}\n")

# 2. Update one record (e.g., change the value for Farmer C, id=3)
# Find the record and update its 'value'
for record in milk_records:
    if record['id'] == 3:
        record['value'] = 300 # Update from 280 to 300
        break # Exit loop once updated
print(f"--- Records after updating ID 3 ---\n{milk_records}\n")

# 3. Delete another record (e.g., remove Farmer F, id=6)
# Use a list comprehension to create a new list without the target record
milk_records = [record for record in milk_records if record['id'] != 6]
print(f"--- Records after deleting ID 6 ---\n{milk_records}\n")


# 4. Compute the total of the 'value' field across all remaining records
total_value = sum(record['value'] for record in milk_records)
print(f"✅ Final total milk collected from the remaining records: {total_value} liters")