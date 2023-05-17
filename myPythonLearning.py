# Tao 1 Dict tu File CSV voi cac Key la Cac cot; Values la trong file
""" import csv
import json
PATH = "iris.csv"
with open(PATH, "r", encoding = "utf8", newline="") as myFile:
    myData = csv.DictReader(myFile)
    for row in myData:
        print(json.dumps(row, indent = 4)) """

# Sử dụng chế độ chắp thêm để viết "How are you?"trên dòng thứ hai của hello_world.txt tệp trên.
""" with open("hello_world.txt", "a") as f:
    f.write("\n")
    f.write("How are you?")
     """

# Lấy danh sách từ điển mà chúng tôi đã tạo từ bộ dữ liệu hoa Iris và ghi nó vào một tệp mới ở định dạng CSV.
irises = [
    {'sepal_length': '5.1', 'sepal_width': '3.5', 'petal_length': '1.4',
        'petal_width': '0.2', 'species': 'Iris-setosa'},
    {'sepal_length': '4.9', 'sepal_width': '3',   'petal_length': '1.4',
        'petal_width': '0.2', 'species': 'Iris-setosa'},
    {'sepal_length': '4.7', 'sepal_width': '3.2', 'petal_length': '1.3',
        'petal_width': '0.2', 'species': 'Iris-setosa'},
    {'sepal_length': '4.6', 'sepal_width': '3.1', 'petal_length': '1.5',
        'petal_width': '0.2', 'species': 'Iris-setosa'},
    {'sepal_length': '5',   'sepal_width': '3.6', 'petal_length': '1.4',
        'petal_width': '0.2', 'species': 'Iris-setosa'},
    {'sepal_length': '7',   'sepal_width': '3.2', 'petal_length': '4.7',
        'petal_width': '1.4', 'species': 'Iris-versicolor'},
    {'sepal_length': '6.4', 'sepal_width': '3.2', 'petal_length': '4.5',
        'petal_width': '1.5', 'species': 'Iris-versicolor'},
    {'sepal_length': '6.9', 'sepal_width': '3.1', 'petal_length': '4.9',
        'petal_width': '1.5', 'species': 'Iris-versicolor'},
    {'sepal_length': '5.5', 'sepal_width': '2.3', 'petal_length': '4',
        'petal_width': '1.3', 'species': 'Iris-versicolor'},
    {'sepal_length': '6.5', 'sepal_width': '2.8', 'petal_length': '4.6',
        'petal_width': '1.5', 'species': 'Iris-versicolor'},
    {'sepal_length': '6.3', 'sepal_width': '3.3', 'petal_length': '6',
        'petal_width': '2.5', 'species': 'Iris-virginica'},
    {'sepal_length': '5.8', 'sepal_width': '2.7', 'petal_length': '5.1',
        'petal_width': '1.9', 'species': 'Iris-virginica'},
    {'sepal_length': '7.1', 'sepal_width': '3',   'petal_length': '5.9',
        'petal_width': '2.1', 'species': 'Iris-virginica'},
    {'sepal_length': '6.3', 'sepal_width': '2.9', 'petal_length': '5.6',
        'petal_width': '1.8', 'species': 'Iris-virginica'},
    {'sepal_length': '6.5', 'sepal_width': '3',   'petal_length': '5.8',
        'petal_width': '2.2', 'species': 'Iris-virginica'}
]
import csv
header = list(irises[0].keys())
data = []
with open("my_new_file.csv", "w", encoding="utf8", newline="") as f:
    Data = csv.writer(f)
    Data.writerow(list(irises[0].keys()))
    for dict in irises:
        Data.writerow(list(dict.values()))
