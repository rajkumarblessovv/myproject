# Calculate the total number of people who have a Ph.D.degreefrom the SalaryGender CSV file.
d=pd.read_csv("F:\Python_Edureka\SalaryGender.csv")
count=d.query("PhD==1")
print("Total number of people with PhD degree", len(count))

