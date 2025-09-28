STUDENT_RECORDS = [
    {"roll_no": 101, "name": "John ", "subject": "Mathematics", "marks": 85},
    {"roll_no": 102, "name": "kedhar", "subject": "Science", "marks": 92},
    {"roll_no": 103, "name": "keshav", "subject": "History", "marks": 78},
    {"roll_no": 104, "name": "charan", "subject": "Mathematics", "marks": 95},
    {"roll_no": 105, "name": "terance", "subject": "Science", "marks": 89},
    {"roll_no": 106, "name": "krithik", "subject": "English", "marks": 82},
]


def display_all_student_records(records):
    print("\n" + "=" * 50)
    print("ALL STUDENT RECORDS")
    print("=" * 50)
    print(f"{'Roll No':<10}{'Name':<20}{'Subject':<15}{'Marks':<5}")
    print("-" * 50)
    for student in records:
        print(
            f"{student['roll_no']:<10}"
            f"{student['name']:<20}"
            f"{student['subject']:<15}"
            f"{student['marks']:<5}"
        )
    print("=" * 50)


def find_highest_scorer(records):
    if not records:
        return None
    
    highest_scorer = max(records, key=lambda student: student['marks'])
    return highest_scorer

def calculate_class_average(records):
    if not records:
        return 0.0

    total_marks = sum(student['marks'] for student in records)
    total_students = len(records)
     
    average = total_marks / total_students
    return round(average, 2)


# Main execution block
def main():

    records = STUDENT_RECORDS
    print("--- Student Marks Management System Initialized ---")

    display_all_student_records(records)

    highest_scorer = find_highest_scorer(records)
    print("\n" + "*" * 50)
    print("CLASS PERFORMANCE ANALYSIS")
    print("*" * 50)
    if highest_scorer:
        print(f"🥇 Highest Scorer:")
        print(f"   Name: {highest_scorer['name']}")
        print(f"   Roll No: {highest_scorer['roll_no']}")
        print(f"   Subject: {highest_scorer['subject']}")
        print(f"   Marks: {highest_scorer['marks']}")
    else:
        print("No records found to determine the highest scorer.")

    class_average = calculate_class_average(records)
    print("-" * 50)
    print(f"📊 Class Average Marks: {class_average}")
    print("-" * 50)
    print("\n--- Program finished successfully. ---")

if __name__ == "__main__":
    main()
