""" Người dùng có thể thêm một cuốn sách vào danh sách đọc của họ bằng cách cung cấp
tên sách,
tên tác giả và năm xuất bản.
Chương trình sẽ lưu trữ thông tin về tất cả những cuốn sách này trong một tệp có tên
books.csv
và dữ liệu này sẽ được lưu trữ ở định dạng CSV.
Người dùng sẽ có thể truy xuất những cuốn sách trong danh sách đọc của họ và những cuốn sách này 
sẽ được in ra ở định dạng thân thiện với người dùng.
Người dùng có thể tìm kiếm một cuốn sách cụ thể bằng cách cung cấp tên sách.
Người dùng có thể chọn các tùy chọn này từ menu văn bản và họ có thể thực hiện nhiều thao tác mà
không cần khởi động lại chương trình. Bạn có thể xem một ví dụ về một menu đang hoạt động trong bài viết
về vòng lặp while (ngày 8). """

import csv
import json
import re
BOOK_PATH = "books.csv"
""" header = ["Name", "Author", "Published Year"]
with open(BOOK_PATH, "w", encoding = "utf8", newline ="") as fH:
    writeHeader = csv.DictWriter(fH,fieldnames = header)
    writeHeader.writeheader() """
print("""
      Select follow the instruction bellow:
      a: Add new book
      f: Find a book
      q: Quit the App
      """)
n = input("Select your option: ")
while True and n != "q":
    if n == "a":
        bookName = input("What's your book name: ")
        bookAuthor = input("What's author name: ")
        bookPublishTime = input("When was it published: ")
        bookInfo = [bookName, bookAuthor, bookPublishTime]
        with open(BOOK_PATH, "a", encoding="utf8", newline="") as f:
            addData = csv.writer(f)
            addData.writerow(bookInfo)
    elif n == "f":
        x = int()
        q = input("Search your book: ")
        def searchYourBook(keyword):
            keyword = keyword
            with open(BOOK_PATH, "r", encoding="utf8", newline="") as fr:
                fReader = csv.DictReader(fr)
                myDictLib = []
                for line in fReader:
                    myDictLib.append(line)
                resultSearch = []
                for i in range(len(myDictLib)):
                    if keyword in dict(myDictLib[i]).values():
                        resultSearch.append(myDictLib[i])
                if resultSearch == []:
                    print("Sorry, no information...")
                else:
                    print("Your Results: ", json.dumps(resultSearch, indent= 4))
                    x = 5
        searchYourBook(q)
        while x != 5:
            m = str(input("1 to search again or any to quit "))
            if m == "1":
                q = input("Keyword Again: ")
                searchYourBook(q)
            else:
                break
    else:
        print("No option, select again")
    n = input("Select your option: ")