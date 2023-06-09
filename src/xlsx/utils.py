from datetime import datetime

import xlsxwriter

from defection.router import get_defection_no_card_all, get_defection_being_late_all, get_defection_appearance_all
from student.repository import RepositoryStudent, RepositoryGrade


async def get_table_no_card():
    name = f'students{datetime.now()}_no_card.xlsx'
    dict_grade = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0}
    # открываем новый файл на запись
    workbook = xlsxwriter.Workbook(name)
    # создаем там "лист"
    worksheet = workbook.add_worksheet()
    # Шапка, где классы
    for col in range(1, 12):
        worksheet.write(0, col - 1, f"{col} класс")

    student_id = await get_defection_no_card_all()
    student_id_all = {}
    for id in student_id:
        if student_id[id] != 0:
            student_id_all[id] = student_id[id]

    for student_id in student_id_all:
        quantity = student_id_all[student_id]
        info_about_student = await RepositoryStudent.get_student_info_by_id(student_id)
        grade_student = await RepositoryGrade.get_info_by_group_id(info_about_student.group_id)
        grade_student = grade_student[0].grade
        worksheet.write(dict_grade[grade_student] + 1,
                        grade_student - 1,
                        "%s %s %d" % (info_about_student.name, info_about_student.surname, quantity))
        dict_grade[grade_student] += 1
    # сохраняем и закрываем
    workbook.close()
    return name


async def get_table_being_late():
    name = f'students{datetime.now()}_being_late.xlsx'
    dict_grade = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0}
    # открываем новый файл на запись
    workbook = xlsxwriter.Workbook(name)
    # создаем там "лист"
    worksheet = workbook.add_worksheet()
    # Шапка, где классы
    for col in range(1, 12):
        worksheet.write(0, col - 1, f"{col} класс")

    student_id = await get_defection_being_late_all()
    student_id_all = {}

    for id in student_id:
        if student_id[id] != 0:
            student_id_all[id] = student_id[id]

    for student_id in student_id_all:
        quantity = student_id_all[student_id]
        info_about_student = await RepositoryStudent.get_student_info_by_id(student_id)
        grade_student = await RepositoryGrade.get_info_by_group_id(info_about_student.group_id)
        grade_student = grade_student[0].grade
        worksheet.write(dict_grade[grade_student] + 1,
                        grade_student - 1,
                        "%s %s %d" % (info_about_student.name, info_about_student.surname, quantity))
        dict_grade[grade_student] += 1
    # сохраняем и закрываем
    workbook.close()
    return name


async def get_table_appearance():
    name = f'students{datetime.now()}_appearance.xlsx'
    dict_grade = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0}
    # открываем новый файл на запись
    workbook = xlsxwriter.Workbook(name)
    # создаем там "лист"
    worksheet = workbook.add_worksheet()
    # Шапка, где классы
    for col in range(1, 12):
        worksheet.write(0, col - 1, f"{col} класс")

    student_id = await get_defection_appearance_all()

    student_id_all = {}

    for id in student_id:
        if student_id[id] != 0:
            student_id_all[id] = student_id[id]

    for student_id in student_id_all:
        quantity = student_id_all[student_id]
        info_about_student = await RepositoryStudent.get_student_info_by_id(student_id)
        grade_student = await RepositoryGrade.get_info_by_group_id(info_about_student.group_id)
        grade_student = grade_student[0].grade
        worksheet.write(dict_grade[grade_student] + 1,
                        grade_student - 1,
                        "%s %s %d" % (info_about_student.name, info_about_student.surname, quantity))
        dict_grade[grade_student] += 1
    # сохраняем и закрываем
    workbook.close()
    return name
