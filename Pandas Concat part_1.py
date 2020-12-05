import pandas as pd, random, numpy as np
import sys, os

# To go into the pandas tutorial.


list143 = [random.randint(3400, 5000) for x in range(5)]
list144 = [random.randint(3400, 5000) for x in range(5)]
list145 = [random.randint(3400, 5000) for x in range(5)]


list143.insert(0, "Hamza");
list144.insert(0, "Hamza");
list145.insert(0, "Hamza");


# Dataframe
df = pd.DataFrame(columns = ["Roll", "Name", "Email", "Gender", "Contact", "DOB"])

# Series with same columns and a list.
series1 = pd.Series(list143, ["Roll", "Name", "Email", "Gender", "Contact", "DOB"])
# list143 = [random.randint(3400, 5000) for x in range(5)]

# Add series to dataframe - convert series to frame and transpose.
df = pd.concat([df, series1.to_frame().T])

#repeat
series1 = pd.Series(list144, ["Roll", "Name", "Email", "Gender", "Contact", "DOB"])
df = pd.concat([df, series1.to_frame().T])

#repeat
series1 = pd.Series(list145, ["Roll", "Name", "Email", "Gender", "Contact", "DOB"])
df = pd.concat([df, series1.to_frame().T])

# Dataframe index reassigned
df.index = [x for x in range(1,len(df)+1)]

# elements from 3 to 10 with size 4x4
a = np.random.randint(3,10, size=(4,4)) 
# elements from 3 to 10 with size 4x4
b = np.random.randint(3,10, size=(5,4)) 

# Adding to Pandas DataFrame
df1 = pd.DataFrame(a, columns=["A","B","C","D"], index = [4,5,6,7])
c1 = [5,6,7,8]; # list
c1 = pd.Series(c1, df1.columns); # series with c1 as list and dataframe columns as the columns
c1 = c1.to_dict(); # series to dictionary


print("\nSeries added using append method.\n")
print(f"The df1 dataframe is:\n{df1}\n")
print(f"The c1 series is:\n{c1}\n")

# Lambda method tat has an index ranging from 4 to length of that dataframe.
resetIndex = lambda x: [a for a in range(4, 4+len(x))]

# Append series to dataframe and ignore index
df1 = df1.append(c1, ignore_index=1)

# The index will be assigned by what is returned by the method
df1.index = resetIndex(df1)

print(f"The df1 dataframe is now:\n{df1}\n")
print(df1, "\n\n")

# List called c2.
c2 = [6,6,9,9]

print(f"\n\nMore df1 dataframe expansion.\n")
# dataframe1 has c2 added as series but it is converted within the concat method.
df1 = pd.concat([df1, pd.Series(c2, df1.columns).to_frame().T], ignore_index = 1)
df1.index = resetIndex(df1)
print(df1)

# df1.loc[len(df1)] = c1
# df1.loc[len(df1)] = c2

curr_path = sys.path[0]
try:
    os.mkdir('data_folder')
except:
    print(FileExistsError.__class__)
    print("Folder already exists.")
curr_path = os.path.join(curr_path, 'data_folder')
curr_path = os.path.join(curr_path, "my_data.xlsx") # data_file\\

try:
    writer1 = pd.ExcelWriter(curr_path)
except:
    print("File could not be generated. Check path for bitwise errors.")
else:
    print("File generated.")


df1.to_excel(writer1)
writer1.save()