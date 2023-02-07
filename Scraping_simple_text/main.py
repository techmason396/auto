from selenium import webdriver

# khởi tạo lớp chrome mặc định ko tham số
options = webdriver.ChromeOptions()

# tạo tham số đầu vào
options.add_argument("disable-infobars")  # vộ hiệu hóa dấu gạch ngang
options.add_argument("start-maximized")  # độ lớn trình duyệt được mở tối đa
# tắt các hạn chế chức năng trình duyệt khi sử dụng
options.add_argument("no-sandbox")
# khởi tạo webdriver
driver = webdriver.Chrome()
