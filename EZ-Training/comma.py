# Importing the math library to avoid recomputing values
import math

# Define the range
end_number = 12456789

# Function to count commas in a formatted number
def count_commas(number: int) -> int:
    formatted_number = f"{number:,}"  # Format the number with commas
    return formatted_number.count(',')

# Initialize a counter
comma_count = 0

# Loop through the range and count commas
for num in range(999, end_number + 1):
    comma_count += count_commas(num)

print(f"Total number of commas between 0 and {end_number}: {comma_count}")
