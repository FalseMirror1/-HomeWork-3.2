import csv
import re


with open("phonebook_raw.csv", encoding="utf-8") as file:
    rows = csv.reader(file, delimiter=",")
    contacts_list = list(rows)


# 1 - поместить Фамилию, Имя и Отчество человека в поля lastname, firstname и surname соответственно.
def names_editor(contact_list):
    updated_list = []
    for data in contact_list:
        updated_list.append(" ".join(data[:3]).split(" ")[:3] + data[3:])
    return updated_list


# 2 - привести все телефоны в формат +7(999)999-99-99. Если есть добавочный номер - +7(999)999-99-99 доб.9999;
def phone_num_editor(contact_list):
    updated_list = []
    pattern = r"(\+7|8)?(\s)?(\()?(\d{3})(\))?(\s|-)?(\d{3})(\s|-)?(\d{2})(\s|-)?(\d{2})" \
              r"((\s)?(\()?(доб)*(\.)\s(\d+)(\))?)?"
    pattern_updated = r"+7(\4)\7-\9-\11 \15\16\17"
    for data in contact_list:
        new_str = ','.join(data)
        regex = re.sub(pattern, pattern_updated, new_str)
        new_list = regex.split(',')
        updated_list.append(new_list)
    return updated_list


# 3 - объединить все дублирующиеся записи о человеке в одну.
def duplicates_editor(contact_list):
    rows_new = []
    for i in range(len(contact_list)):
        for j in range(len(rows_new)):
            if phones_edited[i][:2] == rows_new[j][:2]:
                rows_new[j] = [x or y for x, y in zip(contact_list[i], rows_new[j])]
                break
        else:
            rows_new.append(contact_list[i])
    return rows_new


if __name__ == '__main__':

    names_edited = names_editor(contacts_list)
    phones_edited = phone_num_editor(names_edited)
    final_list = duplicates_editor(phones_edited)

    with open("phonebook.csv", "w") as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(final_list)

    for a in final_list:
        print(a)
