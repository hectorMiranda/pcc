from datascience import *
import numpy as np
import matplotlib.pyplot as plots
plots.style.use('classic')

# Create a table with some sample data
data = Table().with_columns(
    'X', np.arange(1, 6),
    'Y', np.array([2, 3, 5, 7, 11])
)

# Add a new column that is the square of the 'X' column
data = data.with_column('X Squared', data.column('X') ** 2)

# Display the table
print("Table with data:")
data.show()

# Plot the data
plots.figure(figsize=(8, 6))
plots.plot(data.column('X'), data.column('Y'), 'ro-', label='Y values')
plots.plot(data.column('X'), data.column('X Squared'), 'bs-', label='X squared')
plots.xlabel('X')
plots.ylabel('Values')
plots.title('Sample Plot')
plots.legend()
plots.grid(True)
plots.show()
plots.savefig('plot.png')

