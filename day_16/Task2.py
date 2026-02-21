# Playing with prettytable
from prettytable import PrettyTable

# Creating a table
table = PrettyTable()

# Creating table column headings
table.field_names = ["Pokemon Name", "Type"]

# Adding rows
table.add_row(["Pikachu", "Electric"])
table.add_row(["Squirtle", "Water"])
table.add_row(["Charmander", "Fire"])

# Modifying the table alignment
table.align = "l"

# Print table
print(table)