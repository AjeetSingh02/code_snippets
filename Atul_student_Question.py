import pandas as pd
import numpy as np


with open("student.txt", "r") as f:
    lines = f.readlines()

temp = []
for line in lines:
    sp = line.split(",")
    sp1 = []
    # To remove \n
    for part in sp:
        sp1.append(part.strip())
    temp.append(sp)

df = pd.DataFrame(temp, columns=["ID", "Name", "Subject", "Marks"])

for stu_id in df.ID.unique():

    indx = np.where(df.ID == stu_id)
    stu_list, total_marks = [], 0
    stu_name = df.Name[indx[0][0]].strip()

    for i in indx[0]:
        marks = df.Marks[i].strip()
        stu_dict = {"Id": stu_id, "Name": stu_name, "Subject": df.Subject[i], "Marks": marks}
        stu_list.append(stu_dict)
        total_marks += int(marks)

    with open(f"{stu_name}.{stu_id}.txt", "w") as fw:
        for stu_dict in stu_list:
            fw.write(str(stu_dict))
            fw.write("\n")
        fw.write(f"Total: {total_marks}")
