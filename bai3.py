patients = [
	["BN001", "Nguyen Van A", "Nam", "Viem Phoi"],
	["BN002", "Tran Thi B", "Nu", "Sot Xuat Huyet"]
]

def find_patient_index():
    while True:
        new_id = input("Hãy nhập mã bênh nhân: ").strip().upper()
        if not new_id:
            print("Mã bệnh nhân không được để trống")
            continue
        break
    for index, item in enumerate(patients):
        if item[0] == new_id:
            return index, item
    return -1, new_id

def validate_gender(gender_input):
    if gender_input == "nam" or gender_input == "nu":
        return True
    return False

def add_patient():
    new_patient = []
    index_patient, id_patient = find_patient_index()
    if index_patient != -1:
        print("Mã bệnh nhân đã tồn tại")
        return
    new_patient.append(id_patient)
    while True:
        name_patient = input("Hãy nhập tên bệnh nhân: ").strip().title()
        if not name_patient:
            print("Tên bệnh nhân không được để trống")
            continue
        new_patient.append(name_patient)
        break
    while True:
        gender_patient = input("Hãy nhập giới tính bệnh nhân: ").strip().lower()
        if validate_gender(gender_patient) is False:
            print("Dữ liệu không hợp lệ. Vui lòng nhập (nam/nu)")
            continue
        new_patient.append(gender_patient)
        break
    while True:
        illness = input("Hãy nhập tên bệnh: ").strip().title()
        if illness == "":
            print("Tên bệnh không được để trống")
            continue
        new_patient.append(illness)
        break
    patients.append(new_patient)
    print("Tiếp nhận bệnh nhân thành công")

def  display_patients(patients):
    for index, item in enumerate(patients, start=1):
        print(f"{index}. Mã: {item[0]} | Tên: {item[1]} | Giới tính: {item[2]} | Bệnh: {item[3]}")

def update_diagnosis():
    index_patient, patient = find_patient_index()
    if index_patient == -1:
        print(f"Không tìm thấy hồ sơ mang mã {patient}!")
        return
    print(f"Tìm thấy bệnh nhân: {patient[1]}")
    print(f"Chẩn đoán hiện tại: {patient[3]}")
    while True:
        patient[3] = input("Nhập chẩn đoán mới: ").strip().title()
        if patient[3] == "":
            print("Chẩn đoán bệnh không được để trống")
            continue
        break
    print("Cập nhật chẩn đoán bệnh thành công!") 

def search_by_disease():
    count = 0
    print("----- TÌM KIẾM BỆNH NHÂN THEO TÊN BỆNH -----")
    while True:
        key_search = input("Hãy nhập từ khóa tên bệnh: ").strip().lower()
        if key_search == "":
            print("Từ khóa tìm kiếm không được để trống!")
            continue
        break
    for patient in patients:
        if key_search in patient[3].lower():
            display_patients([patient])
            count += 1
    if count == 0:
        print("Không tìm thấy bệnh nhân nào phù hợp.")
        
    print(f"Có tổng cộng {count} bệnh nhân mắc bệnh liên quan đến '{key_search}'")


def menu():
    return input('''
            ===== HỆ THỐNG QUẢN LÝ BỆNH NHÂN RIKKEI =====
            1. Hiển thị danh sách bệnh nhân
            2. Tiếp nhận bệnh nhân mới
            3. Cập nhật chẩn đoán bệnh theo mã BN
            4. Tìm kiếm và thống kê theo tên bệnh
            5. Thoát chương trình
            =============================================
            Nhập lựa chọn của bạn: ''')

def main():
    while True:
        choice = menu()
        if choice.isdigit():
            choice = int(choice)
            match choice:
                case 1:
                    print("--- DANH SÁCH BỆNH NHÂN ĐANG ĐIỀU TRỊ ---")
                    display_patients(patients)
                case 2:
                    add_patient()
                case 3:
                    update_diagnosis()
                case 4:
                    search_by_disease()
                case 5:
                    print("Cảm ơn bác sĩ đã sử dụng hệ thống!")
                    break
                case _:
                    print("Dữ liệu không hợp lệ")
        else:
            print("Lựa chọn không hợp lệ")

main()