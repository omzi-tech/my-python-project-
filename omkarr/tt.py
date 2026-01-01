def calculate_cgpa(gpa_list):
    total = sum(gpa_list)
    return round(total / len(gpa_list), 2)

def main():
    with open("C:/Users/user/Desktop/student.txt", "r") as file:
        lines = file.readlines()

    for line in lines:
        data = line.strip().split("//")
        student_id, student_name, *gpa_values = data

        gpa_values = [float(gpa) for gpa in gpa_values]
        cgpa = calculate_cgpa(gpa_values)

        print(f"{student_name} (Student ID: {student_id}) have a {cgpa} CGPA")

if __name__ == "__main__":
    main()
