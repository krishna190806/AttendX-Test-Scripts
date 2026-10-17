def test_mark_attendance():
    student_id = "STU101"
    attendance_status = "Present"

    if student_id and attendance_status in ["Present", "Absent"]:
        print("PASS: Attendance data is valid")
    else:
        print("FAIL: Invalid attendance data")


test_mark_attendance()
