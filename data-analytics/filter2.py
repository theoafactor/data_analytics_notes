import pandas as pd
from data import students
students_data = pd.DataFrame(students.students)


print(students_data)

## Get the firstname that starts with J

## write the filter
whatever = students_data["firstnames"].str.contains("Ja", na=False)

print(whatever)