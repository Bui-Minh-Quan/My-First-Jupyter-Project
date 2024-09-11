from docx import Document

# Tạo một tài liệu Word mới
doc = Document()

# Dữ liệu lớp học
classes = [
    {"Thứ": "Thứ 2", "Tiết": "3-4", "Học phần": "Giáo dục thể chất cơ bản (PES 1003)", "Giảng viên": "TT GDTC&TT", "Giảng đường": "SVĐ ĐHNN", "Nhóm": "CL"},
    {"Thứ": "Thứ 2", "Tiết": "7-9", "Học phần": "Tín hiệu và hệ thống (ELT2035)", "Giảng viên": "TS. Lê Vũ Hà", "Giảng đường": "303-GĐ2", "Nhóm": "CL"},
    {"Thứ": "Thứ 3", "Tiết": "5-6", "Học phần": "Lập trình xử lý dữ liệu (AIT2006)", "Giảng viên": "TS. Trần Quốc Long, ThS. Nguyễn Thị Thuỳ Linh", "Giảng đường": "103-G2", "Nhóm": "CL"},
    {"Thứ": "Thứ 4", "Tiết": "1-2", "Học phần": "Lập trình xử lý dữ liệu (AIT2006)", "Giảng viên": "CN. Đỗ Thu Uyên", "Giảng đường": "PM402-E5", "Nhóm": "1"},
    {"Thứ": "Thứ 4", "Tiết": "3-4", "Học phần": "Bóng chuyền (PES 1015)", "Giảng viên": "TT GDTC&TT", "Giảng đường": "SVĐ ĐHNN", "Nhóm": "CL"},
    {"Thứ": "Thứ 4", "Tiết": "7-8", "Học phần": "Cơ sở hệ thống máy tính (AIT2002)", "Giảng viên": "ThS. Vũ Quang Dũng", "Giảng đường": "3-G3", "Nhóm": "CL"},
    {"Thứ": "Thứ 5", "Tiết": "1-2", "Học phần": "Cơ sở dữ liệu (INT2211)", "Giảng viên": "TS. Trần Hồng Việt", "Giảng đường": "301-G2", "Nhóm": "CL"},
    {"Thứ": "Thứ 5", "Tiết": "3-4", "Học phần": "Cơ sở dữ liệu (INT2211)", "Giảng viên": "TS. Trần Hồng Việt", "Giảng đường": "Online", "Nhóm": "CL"},
    {"Thứ": "Thứ 6", "Tiết": "1-2", "Học phần": "Cơ sở hệ thống máy tính (AIT2002)", "Giảng viên": "CN. Nguyễn Tiến Đạt", "Giảng đường": "PM402-E5", "Nhóm": "N2"},
    {"Thứ": "Thứ 6", "Tiết": "7-9", "Học phần": "Xác suất thống kê (MAT1101)", "Giảng viên": "TS. Trần Quốc Long, ThS. Nguyễn Thị Thuỳ Linh, TS. Lê Trung Thành", "Giảng đường": "103-G2", "Nhóm": "CL"},
]

# Thêm tiêu đề bảng
table = doc.add_table(rows=1, cols=5)
hdr_cells = table.rows[0].cells
hdr_cells[0].text = 'Thứ'
hdr_cells[1].text = 'Tiết'
hdr_cells[2].text = 'Học phần'
hdr_cells[3].text = 'Giảng viên'
hdr_cells[4].text = 'Giảng đường'

# Thêm dữ liệu vào bảng
for cls in classes:
    row_cells = table.add_row().cells
    row_cells[0].text = cls["Thứ"]
    row_cells[1].text = cls["Tiết"]
    row_cells[2].text = cls["Học phần"]
    row_cells[3].text = cls["Giảng viên"]
    row_cells[4].text = cls["Giảng đường"]

# Lưu tài liệu
file_path = "LichHoc_DuocSapXep.docx"
doc.save(file_path)

file_path
