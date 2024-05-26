# Manipulação de Dados com o Pandas - Select and Sort

import pandas as pd

# Leitura do arquivo em txt
print("Leitura do arquivo em csv")
homelessness = pd.read_csv("homelessness.csv")
print(homelessness.head(10))


# Print the head of the homelessness data
print(homelessness.head())
print("\n")

# Print information about homelessness
print(homelessness.info())
print("\n")

# Print the shape of homelessness
print(homelessness.shape)
print("\n")

# Print a description of homelessness
print(homelessness.describe())
print("\n")

# Print the values of homelessness
print(homelessness.values)
print("\n")

# Print the column index of homelessness
print(homelessness.columns)
print("\n")

# Print the row index of homelessness
print(homelessness.index)
print("\n")


# SORTING AND SELECT

# Sort homelessness by individuals
homelessness_ind = homelessness.sort_values("individuals")

# Print the top few rows
print(homelessness_ind.head())
print("\n")

# Sort homelessness by descending family members
homelessness_fam = homelessness.sort_values("family_members", ascending = [False])

# Print the top few rows
print(homelessness_fam.head())
print("\n")

# Sort homelessness by region, then descending family members
homelessness_reg_fam = homelessness.sort_values(["region","family_members"], ascending = [True,False])

# Print the top few rows
print(homelessness_reg_fam.head())
print("\n")

# Select the individuals column
individuals = homelessness["individuals"]

# Print the head of the result
print(individuals.head())
print("\n")

# Select the state and family_members columns
state_fam = homelessness[["state","family_members"]]

# Print the head of the result
print(state_fam.head())
print("\n")