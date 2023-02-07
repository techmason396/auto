import tkinter
from tkinter import *
from selenium import webdriver
import os

PATH = "./urls.csv"


def read_file():
    try:
        with open(PATH) as file_data:
            urls = file_data.readlines()
        return urls
    except FileNotFoundError:
        with open(PATH, "r") as file_data:
            file_data.write("")
        with open(PATH, "r") as file_data:
            urls = file_data.readlines()
            return urls


def write_file(urls):
    with open(PATH, mode="w") as file_data:
        urls = "\n".join(urls)
        file_data.write(urls)


data_file = read_file()
urls = [url.strip() for url in data_file]


window = Tk()
window.config(padx=30, pady=30)
window.title("Tự động tìm việc")

input_url = Entry(width=60)
input_url.grid(row=0, column=0)


def add_url():
    # lấy dữ liệu input và thêm vào mảng
    url = input_url.get()
    urls.append(url)

    # lưu file
    write_file(urls)

    # reset hiển thị list và input
    update_listbox()
    input_url.delete(0, END)


btn_add_url = Button(text="Thêm URL", command=add_url)
btn_add_url.grid(row=0, column=2)

label_list_url = Label(text="Danh sách URL", font=("bold"))
# sticky = "w" căn trái màn hình
label_list_url.grid(row=1, column=0, sticky="w")

list_url = Listbox(width=60)
list_url.grid(row=2, column=0)


def update_listbox():
    # xóa list trước khi render ra list mới (xóa từ hàng 0)
    list_url.delete(0, END)
    for i, url in enumerate(urls):
        list_url.insert(END, f"{i+1}. {url}")


update_listbox()


def delete_url():
    selected_item = list_url.curselection()
    # chuyển dang tuple sang kiểu int để xóa theo index phần tử trong list
    index_item = list(map(int, selected_item))
    list_url.delete(selected_item)

    # xóa url trong urls
    urls.pop(index_item[0])

    # lưu file
    write_file(urls)


delete_button = Button(text="Xóa url", command=delete_url)
delete_button.grid(row=2, column=2)


def find_job():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(options=options)

    for url in urls:
        driver.execute_script(f"window.open('{url}', '_blank');")


btn_find_job = Button(text="Tìm việc", font=("red"), command=find_job)
btn_find_job.grid(row=3, column=0)


window.mainloop()
