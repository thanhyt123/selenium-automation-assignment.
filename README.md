# BÁO CÁO BÀI TẬP THỰC HÀNH: KIỂM THỬ TỰ ĐỘNG VỚI SELENIUM

## 1. Thông tin sinh viên
- **Họ và tên:** [Nguyễn Văn Thành]
- **Mã số sinh viên:** [23010764]
- **Lớp:** [Kiểm định và chất lượng]

## 2. Công cụ và Môi trường kiểm thử
- **Website kiểm thử:** [SauceDemo](https://www.saucedemo.com/) (Trang thương mại điện tử demo).
- **Ngôn ngữ lập trình:** Python 3.14.6
- **Thư viện sử dụng:** Selenium WebDriver v4.45.0

## 3. Danh sách các Kịch bản Kiểm thử (Test Cases)

Hệ thống được xây dựng tối thiểu 03 kịch bản kiểm thử tự động bao gồm:

| STT | Tên Test Case | Các bước thực hiện | Kết quả mong đợi | Trạng thái |
|---|---|---|---|---|
| 1 | Đăng nhập thành công | 1. Truy cập trang chủ Saucedemo<br>2. Nhập username & password hợp lệ<br>3. Nhấn nút Login | Chuyển hướng thành công vào trang quản lý sản phẩm (`inventory.html`) | **PASSED** |
| 2 | Thêm sản phẩm vào giỏ | 1. Tại trang sản phẩm, nhấn nút "Add to cart" của sản phẩm đầu tiên<br>2. Kiểm tra icon giỏ hàng | Biểu tượng giỏ hàng cập nhật số lượng là '1' | **PASSED** |
| 3 | Đăng xuất hệ thống | 1. Nhấn vào menu bên góc trái<br>2. Chọn nút "Logout" | Quay trở lại màn hình đăng nhập ban đầu | **PASSED** |

## 4. Hướng dẫn chạy Code (Setup & Run)
1. Cài đặt thư viện Selenium bằng lệnh: `pip install selenium`
2. Di chuyển vào thư mục dự án và chạy file test bằng lệnh: `python test_saucedemo.py`<img width="727" height="755" alt="image" src="https://github.com/user-attachments/assets/cf90c839-6626-471c-954d-f97779e6382e" />
