import pandas as pd
from data import students 

data = pd.DataFrame(students.students)




# data_filter = data["hobbies"].str.contains("Speaking", na='No data') | data["hobbies"].str.contains("Sleeping", na='No data')

# print(data[data_filter])


data.columns = [x.upper() for x in data.columns]

print(data)