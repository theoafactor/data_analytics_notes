import pandas as pd
from data import students

data = pd.DataFrame(students.students)

# Update the years by adding years at the back of each value

data.rename(columns= { "ages in years" : "ages_in_years"}, inplace=True)

print(data)

data.ages_in_years = [ str(x) + " years old" for x in data.ages_in_years ] 


print(data)
