import sympy as sp
import matplotlib.pyplot as plt
import numpy as np

def nhap_ham_so():
    x = sp.symbols('x')
    expression_str = input("Nhập hàm số (sử dụng 'x' là biến): ")
    expression = sp.sympify(expression_str)
    return x, expression

def dao_ham_cap_cao(expression, x, n):
    derivate = sp.diff(expression, x, n)
    return derivate

def tich_pha_dao_ham(expression, x):
    integral = sp.integrate(expression, x)
    return integral

def giai_phuong_trinh(expression, x):
    solutions = sp.solve(expression, x)
    return solutions

def ve_do_thi(expression, x, range_start, range_end):
    x_vals = np.linspace(range_start, range_end, 1000)
    y_vals = [expression.subs(x, val) for val in x_vals]

    plt.plot(x_vals, y_vals)
    plt.title("Đồ thị hàm số")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.grid(True)
    plt.show()

def tinh_dien_tich(expression, x, range_start, range_end):
    area = sp.integrate(expression, (x, range_start, range_end))
    return area

def tim_diem_cuc_tri(expression, x):
    critical_points = sp.solve(sp.diff(expression, x), x)
    return critical_points

# Chương trình chính
def main():
    x, ham_so = nhap_ham_so()

    # Chức năng 2: Tính đạo hàm cấp cao
    n = int(input("Nhập bậc của đạo hàm cần tính: "))
    derivate = dao_ham_cap_cao(ham_so, x, n)
    print(f"Đạo hàm bậc {n}: {derivate}")

    # Chức năng 3: Tính tích phân và đạo hàm
    integral = tich_pha_dao_ham(ham_so, x)
    print(f"Tích phân của hàm số: {integral}")

    # Chức năng 4: Giải phương trình f(x) = 0
    solutions = giai_phuong_trinh(ham_so, x)
    print(f"Nghiệm của phương trình: {solutions}")

    # Chức năng 5: Vẽ đồ thị hàm số
    range_start, range_end = map(float, input("Nhập khoảng giá trị x (bắt đầu và kết thúc, cách nhau bởi dấu cách): ").split())
    ve_do_thi(ham_so, x, range_start, range_end)

    # Chức năng 6: Tính diện tích hình phẳng giới hạn bởi hàm số và đường thẳng
    range_start, range_end = map(float, input("Nhập khoảng giá trị x để tính diện tích (bắt đầu và kết thúc, cách nhau bởi dấu cách): ").split())
    area = tinh_dien_tich(ham_so, x, range_start, range_end)
    print(f"Diện tích hình phẳng giới hạn bởi hàm số và đường thẳng: {area}")

    # Chức năng 7: Tìm điểm cực trị
    critical_points = tim_diem_cuc_tri(ham_so, x)
    print(f"Các điểm cực trị của hàm số: {critical_points}")

if __name__ == "__main__":
    main()
