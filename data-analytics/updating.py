import pandas as pd
from data import students

# bring in the data
data = pd.DataFrame(students.students)

# renaming columns using the .loc construct

data.rename(columns={ "ages in years" :  "ages_in_years"}, inplace=True)


print(data)

