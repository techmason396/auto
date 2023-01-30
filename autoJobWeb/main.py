from selenium import webdriver
urls = [
    "https://www.careerlink.vn/tim-viec-lam-tai/binh-thuan/BT?posted_within=1",
    "https://www.careerlink.vn/viec-lam/huyen-bac-binh?posted_within=1",
    "https://www.careerlink.vn/viec-lam/huyen-tuy-phong?posted_within=1",
    "https://www.topcv.vn/tim-viec-lam-tai-phan-thiet-l18d1801?sort=up_top",
    "https://123job.vn/tuyen-dung?q=&l=B%E1%BA%AFc+B%C3%ACnh%2CB%C3%ACnh+Thu%E1%BA%ADn+&date=1",
    "https://123job.vn/tuyen-dung?q=&l=Phan+Thi%E1%BA%BFt%2CB%C3%ACnh+Thu%E1%BA%ADn+&date=1",
    "https://123job.vn/tuyen-dung?q=&l=Tuy+Phong+B%C3%ACnh+Thu%E1%BA%ADn&date=1"
]

# khắc phục auto close trình duyệt khi tải xong
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
# end

driver = webdriver.Chrome(options=options)


for url in urls:
    driver.execute_script(f"window.open('{url}', '_blank');")
