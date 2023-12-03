# Lab 1: Basic SSRF against the local server
![image](https://hackmd.io/_uploads/B1FHaI74a.png)
- Chức năng stock check của trang web lấy dữ liệu từ trang mạng nội bộ trả về cho người dùng. Tại đây chứa lỗ hổng SSRF. Để giải quyết bài lab, chúng ta cần khai thác lỗ hổng SSRF truy cập vào trang quản trị viên có địa chỉ **`http://localhost/admin`** và thực hiện xóa tài khoản người dùng **carlos**.

- Kiểm tra request check stock:
![image](https://hackmd.io/_uploads/Hk3sH27NT.png)
- Mình thấy xuất hiện tham số **`stockApi`** truyền bằng phương thức **POST** cho hệ thống giá trị là một địa chỉ URL **`https://0aac00c503c786c181d3615800fb00cb.web-security-academy.net/product?productId=1`**. Do hệ thống nhận giá trị **`stockApi`** là một địa chỉ URL nên mình thử thay nó bằng địa chỉ của burp suite
- ![image](https://hackmd.io/_uploads/rJXJd274T.png)
- Kiểm tra tab collaborator thì nhận được request tương tác  DNS lookup thành công:

![image](https://hackmd.io/_uploads/S178OhX4a.png)
- Chứng tỏ chức năng stock check có thể tương tác với bất kỳ URL nào, khả năng lớn chứa lỗ hổng SSRF. Bởi vậy, chúng ta có thể khai thác lỗ hổng truy cập trang quản trị bằng một số cách như sau:
![image](https://hackmd.io/_uploads/r1vbF27Np.png)
- Đọc source mình thấy nó bảo xóa carlos thì đến `/admin/delete?username=carlos`

![image](https://hackmd.io/_uploads/Bkg0Q92QEa.png)
![image](https://hackmd.io/_uploads/BJ7oc2mNa.png)
![image](https://hackmd.io/_uploads/ryW2cnXEp.png)

## Lab 2: Basic SSRF against another back-end system

![image](https://hackmd.io/_uploads/HyRbo2QVa.png)

- Chức năng stock check của trang web truy xuất dữ liệu từ trang mạng nội bộ trả về cho người dùng. Tại đây chứa lỗ hổng SSRF. Biết rằng hệ thống mạng nội bộ có trang quản trị viên **`/admin`** trong dải **192.168.0.X** với cổng 8080. Để giải quyết bài lab, chúng ta cần khai thác lỗ hổng SSRF truy cập vào trang quản trị viên này và thực hiện xóa tài khoản người dùng **carlos**.
- Vẫn như bài trước mình vẫn sẽ đi kiểm tra SSRF bằng DNS lookup và thành công:
![image](https://hackmd.io/_uploads/SkhzphQNa.png)
![image](https://hackmd.io/_uploads/rkpfahX4p.png)

- Request ban đầu cho mình 1 địa chỉ ip là 192.168.0.1 port là 8080:
![image](https://hackmd.io/_uploads/r1l9TnmET.png)
- Mình có trang quản trị là `/admin` địa chỉ này nằm nội bộ trong dải **192.168.0.X** với cổng 8080. Vậy nên mình sẽ tiến hành đi brute force nó để tìm ra địa chỉ trang admin:

![image](https://hackmd.io/_uploads/B1VMyTmE6.png)

- Vậy là mình đã có url cụ thể và source nó cũng cho ta đường dẫn để xóa tài khoản carlos, vậy thì làm nốt việc còn lại thôi:
![image](https://hackmd.io/_uploads/B1vFyp7Va.png)
![image](https://hackmd.io/_uploads/BJoKJam46.png)
## Lab 3: Blind SSRF with out-of-band detection
![image](https://hackmd.io/_uploads/Syv1xT7Ep.png)
- Trang web sử dụng một phần mềm tìm nạp và phân tích URL được xác định trong header Referer khi người dùng truy cập vào trang hiển thị chi tiết sản phẩm. Để giải quyết bài lab, chúng ta cần sử dụng chức năng này thực hiện một kịch bản DNS lookup với server Burp Collaborator.
- Khi truy cập vào sản phẩn mình có kiểm tra request:

![image](https://hackmd.io/_uploads/Bkgy4pXNT.png)

- Nhìn đi nhìn lại thì chỉ có referer là đáng ngờ nhất nên mình đã thử kiểm tra nó như cách kiểm tra các bài trước bằng client collaborator và dns lookup thành công:
![image](https://hackmd.io/_uploads/By0Y46XNa.png)
![image](https://hackmd.io/_uploads/ryvc4pXE6.png)
## Lab 4: SSRF with blacklist-based input filter
![image](https://hackmd.io/_uploads/Hy3p4p7Va.png)
Chức năng stock check của trang web truy xuất dữ liệu từ trang mạng nội bộ trả về cho người dùng. Tại đây chứa lỗ hổng SSRF. Biết rằng trang web có một cơ chế ngăn chặn tấn công SSRF bao gồm hai lớp kiểm tra. Để giải quyết bài lab, chúng ta cần vượt qua cơ chế ngăn chặn này, truy cập vào trang quản trị viên tại **`http://localhost/admin`** và thực hiện xóa tài khoản người dùng **carlos**.
- Vẫn như bài trước mình vẫn sẽ đi kiểm tra SSRF bằng DNS lookup và thành công nhưng khi mình mình cho stockApi=localhost thì nó lại bị chặn ![image](https://hackmd.io/_uploads/HytmU6Q4a.png)

- Điều này tương tự với 127.0.0.1. Có vẻ nó là một trong những blacklist của trang web. Sau khi tìm hiểu thì mình tìm ra được cách bypass nó bằng rare address http://127.1 hoặc http://127.0.1
![image](https://hackmd.io/_uploads/SJLuv6XET.png)
- Và khi truy cập đến admin thì điều tương tự cũng xảy ra:
![image](https://hackmd.io/_uploads/S18Hta7VT.png)
- Thử encode url nó 2 lần vì khi post thì đã có 1 lần decode:

![image](https://hackmd.io/_uploads/ryIb31E4p.png)

- Vậy là đã bypass thành công, đi xóa carlos thôi
![image](https://hackmd.io/_uploads/rkPV3yVVa.png)
![image](https://hackmd.io/_uploads/H1kS2yEE6.png)

## Lab 5: SSRF with filter bypass via open redirection vulnerability

![image](https://hackmd.io/_uploads/HyLjI8VNT.png)
- Chức năng stock check của trang web truy xuất dữ liệu từ trang mạng nội bộ trả về cho người dùng. Tại đây chứa lỗ hổng SSRF. Để giải quyết bài lab, chúng ta cần khai thác lỗ hổng SSRF kết hợp chức năng open redirection nhằm truy cập vào trang quản trị viên nội bộ tại **`http://192.168.0.12:8080/admin`** và thực hiện xóa tài khoản người dùng **carlos**.
- Kiểm tra request của check stock:

![image](https://hackmd.io/_uploads/rkd5RdENp.png)
- Dễ thấy phần path của stockApi là url: `/product/stock/check?productId=1&storeId=1`, nên chúng ta có thể dự đoán trang web thực hiện ghép phần host, chẳng hạn **`http://localhost`** với giá trị **`stockApi`**. Thử thay giá trị của stockApi bằng url của cliet collaborator thì nhận được thông báo lỗi:
![image](https://hackmd.io/_uploads/Hk-JgKN4a.png)
- Bây giờ mình thử dùng kí tự đặc biệt `@` để bypass thử và thành công

![image](https://hackmd.io/_uploads/SkXLlYNEa.png)
- chúng ta hoàn toàn có thể bypass bằng ký tự **`@`**, có thể hình dung URL trang web truy xuất lúc này là **`http://localhost:80@jzmooswcf63gu0fch5oraifmedk48uwj.oastify.com`**.
- Tiếp theo, truy cập tới trang quản trị viên nội bộ, payload: **`stockApi=@192.168.0.12:8080/admin`**
![image](https://hackmd.io/_uploads/Bk-kZKV46.png)
![image](https://hackmd.io/_uploads/Sk4GWFNNp.png)
![image](https://hackmd.io/_uploads/Bk3fZK4E6.png)

