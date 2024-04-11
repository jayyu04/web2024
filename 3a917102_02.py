import json
import os

def read_student_data(file_path: str) -> list:

    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"File {file_path} does not exist.")

    with open(file_path, encoding='utf-8') as file:
        return json.load(file)

def get_student_info(student_id: str, student_data: list) -> dict:

    for student in student_data:
        if student["student_id"] == student_id:
            return student
    raise ValueError(f"學號 {student_id} 找不到.")

def add_course(student_id: str, course_name: str, course_score: float, student_data: list) -> None:

    if not course_name or not course_score:
        raise ValueError("課程名稱或分數不可空白.")

    for student in student_data:
        if student["student_id"] == student_id:
            student["courses"].append({"name": course_name, "score": course_score})
            print("課程已成功新增。")
            return
    raise ValueError(f"學號 {student_id} 找不到.")

def calculate_average_score(student_data: dict) -> float:

    total_score = sum(course["score"] for course in student_data["courses"])
    return total_score / len(student_data["courses"]) if student_data["courses"] else 0.0

def main():
    file_path = "students.json"
    try:
        students = read_student_data(file_path)
    except FileNotFoundError as e:
        print(f"File not found: {e}")
        return

    menu = """
***************選單***************
1. 查詢指定學號成績
2. 新增指定學號的課程名稱與分數
3. 顯示指定學號的各科平均分數
4. 離開
**********************************
"""
    while True:
        print(menu)
        choice = input("請選擇操作項目：")

        if choice == "1":
            student_id = input("請輸入學號: ")
            try:
                student_info = get_student_info(student_id, students)
                print(json.dumps(student_info, indent=2, ensure_ascii=False))
            except ValueError as e:
                print(f"=>發生錯誤: {e}")
        elif choice == "2":
            student_id = input("請輸入學號: ")
            course_name = input("請輸入要新增課程的名稱: ")
            course_score = input("請輸入要新增課程的分數: ")
            try:
                add_course(student_id, course_name, float(course_score), students)
            except ValueError as e:
                print(f"=>其它例外: {e}")
        elif choice == "3":
            student_id = input("請輸入學號: ")
            try:
                student_info = get_student_info(student_id, students)
                avg_score = calculate_average_score(student_info)
                print(f"=>各科平均分數: {avg_score}")
            except ValueError as e:
                print(f"=>發生錯誤: {e}")
        elif choice == "4":
            print("=>程式結束。")
            break
        else:
            print("=>請輸入有效的選項。")

if __name__ == "__main__":
    main()
