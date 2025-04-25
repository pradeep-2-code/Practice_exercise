def analysis_grades(grades):
    valid_grades = []
    error_count = 0

    for name, grade in grades.items():
        if not isinstance(grade, (int, float)):
            print(f"Warning: Invalid grade format for {name}: {grade}")
            error_count += 1

        elif grade < 0 or grade > 100:
            print(f"Warning: Invalid grade range for {name}: {grade}")
            error_count += 1
        else:
            valid_grades.append(grade)

    if valid_grades:
        average = sum(valid_grades) / len(valid_grades)
        highest = max(valid_grades)
        lowest = min(valid_grades)
        count = len(valid_grades)

        return {
            "errors": error_count,
            "average": round(average, 2),
            "highest": highest,
            "lowest": lowest,
            "count": count,
        }
    else:
        return {
            "errors": error_count,
            "average": None,
            "highest": None,
            "lowest": None,
            "count": 0,
        }


analysis_grades(
    Grades1={"Eve": "Not graded", "Frank": 88, "Grace": -5, "Henry": 105, "Ivy": 91}
)
