import re
import numpy as np
import pandas as pd

def process(student_file_path, template_path, output_folder_path):

    if not output_folder_path.endswith("/"):
        output_folder_path += "/"

    with open(student_file_path, "r") as f:
        lines = f.readlines()

    with open(template_path, "r") as f:
        template = f.readline()

    temp = []
    for line in lines:
        sp = line.split(",")
        temp.append(sp)

    df = pd.DataFrame(temp, columns=["ID", "Name", "Subject", "Marks"])

    for stu_id in df.ID.unique():
        indx = np.where(df.ID == stu_id)
        stu_list, total_marks = [], 0
        stu_name = df.Name[indx[0][0]].strip()

        for i in indx[0]:
            marks = df.Marks[i].strip()
            stu_dict = {"rollno": stu_id, "StudName": stu_name, "subject": df.Subject[i], "marks": marks}
            flag = 0

            for key in stu_dict:
                if flag == 0:
                    stu_string = re.sub(f"<{key}>", stu_dict[f"{key}"], template, count=1, flags=re.IGNORECASE)
                    flag = 1
                else:
                    stu_string = re.sub(f"<{key}>", stu_dict[f"{key}"], stu_string, count=1, flags=re.IGNORECASE)
                    
            stu_list.append(stu_string)
            total_marks += int(marks)

        with open(f"{output_folder_path}{stu_name}.{stu_id}.txt", "w") as fw:
            for stu_dict in stu_list:
                fw.write(str(stu_dict))
                fw.write("\n")
            fw.write(f"Total: {total_marks}")
            
            
            
student_file_path = "student.txt"
template_path = "template2.txt"
output_folder_path = "out/"

process(student_file_path, template_path, output_folder_path)
