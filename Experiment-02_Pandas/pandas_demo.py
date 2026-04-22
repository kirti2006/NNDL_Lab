# Experiment 2: Pandas
# Aim: Perform data manipulation using Pandas

import pandas as pd  # Import Pandas

# Create dataset
data = {
    "Name": ["A", "B", "C"],
    "Marks": [80, 90, 85]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Display data
print("DataFrame:\n", df)

# Calculate average marks
print("Average Marks:", df["Marks"].mean())