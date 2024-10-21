import pandas as pd
import random

# Function to create sample data
def create_sample_data(num_rows):
    data = {
        'Item': [f'Item {i}' for i in range(1, num_rows + 1)],
        'Quantity': [random.randint(1, 100) for _ in range(num_rows)],
        'Price': [round(random.uniform(1.0, 100.0), 2) for _ in range(num_rows)]
    }
    return pd.DataFrame(data)

# Number of rows for the sample data
num_rows = 100  # You can adjust this number

# Create the sample DataFrame
sample_data = create_sample_data(num_rows)

# Save the DataFrame to an Excel file
output_file = 'sample_data.xlsx'
sample_data.to_excel(output_file, index=False)

print(f"Sample Excel file '{output_file}' created with {num_rows} rows of data.")
