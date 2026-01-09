def inputs():
    array_points = []

    while True:
        temp_points = []
        points = input("Exam points exercises completed: ")
        if points == "":
            break
        int_point = points.split(" ")
        for item in int_point:
            temp_points.append(int(item))
        array_points.append(temp_points)

    return array_points


def average(inputs):
    total_sum = 0
    for item in inputs:
        total_sum += item[0] + item[1] // 10
    return total_sum / len(inputs)


def grade(inputs):
    array_grade = []
    for item in inputs:
        exercise_points = item[1] // 10
        exam_points = item[0]
        total_points = exercise_points + exam_points
        if exam_points < 10:
            array_grade.append(0)
        elif 0 <= total_points <= 14:
            array_grade.append(0)
        elif 15 <= total_points <= 17:
            array_grade.append(1)
        elif 18 <= total_points <= 20:
            array_grade.append(2)
        elif 21 <= total_points <= 23:
            array_grade.append(3)
        elif 24 <= total_points <= 27:
            array_grade.append(4)
        elif 28 <= total_points <= 30:
            array_grade.append(5)
    return sorted(array_grade)


def pass_percent(inputs, grade):
    fail = grade.count(0)
    passed = 100 - (fail / len(inputs) * 100)

    return passed


def prints(average, pass_percent, grades):
    print("Statistics:")
    print(f"Points average: {average:.1f}")
    print(f"Pass percentage: {pass_percent:.1f}")
    print("Grade distribution:")
    for item in range(5, -1, -1):
        if item in grades:
            print(f"{item}: {'*' * grades.count(item)}")
            continue
        print(f"{item}: {'*' * grades.count(item)}")


def main():
    to_input = inputs()
    points = average(to_input)
    grades = grade(to_input)
    passed = pass_percent(to_input, grades)
    prints(points, passed, grades)


main()
