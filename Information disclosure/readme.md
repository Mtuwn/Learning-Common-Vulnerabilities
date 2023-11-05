
# Information disclosure vulnerabilities
## Lab 1: Information disclosure in error messages

![](https://hackmd.io/_uploads/B1PNFnifa.png)

- Khi chọn **View detail** của sản phẩm bất kì, chúng ta được chuyển tới thư mục `/product`. Quan sát thanh URL nhận thấy trang web hiển thị tới giao diện người dùng chi tiết sản phẩm thông qua tham số `productId=1`. Mình đã thử thay `producId=-1` và nhận được kết quả

    ![](https://hackmd.io/_uploads/rk1Jg6oza.png)

- Như vậy tham số chỉ nhận giá chỉ là số nguyên dương và các trường hợp còn lại sẽ rơi vào các `exception`. Sau đó mình thử cho tham số `producId` bằng 1 chuỗi abc để xem `exception` khi khác kiểu dữ kiệu là gì

    ![](https://hackmd.io/_uploads/ByyxWaiGp.png)

- Kết quả hệ thống báo lỗi và in ra luôn phiên bản sử dụng của framework `Apache Struts 2 2.3.31`

![](https://hackmd.io/_uploads/BytLbpsGa.png)
## Lab 2: Information disclosure on debug page

![](https://hackmd.io/_uploads/B1ou8khGT.png)

- Trang web chứa một trang debug tiết lộ một số thông tin quan trọng. Chúng ta cần tìm kiếm giá trị biến môi trường **SECRET_KEY**

- Sau khi kiểm tra source code thì mình thấy đoạn comment cho biết một đường dẫn `/cgi-bin/phpinfo.php` tới một trang Debug.
    
    ![](https://hackmd.io/_uploads/rJesukhz6.png)
    ![](https://hackmd.io/_uploads/BJ_nd12MT.png)

## Lab 3: Source code disclosure via backup files

![](https://hackmd.io/_uploads/rklleghGp.png)

- Trang web bị lộ file backup trong một thư mục ẩn, chúng ta cần tìm kiếm database password chứa trong file backup đó.
- Sau khi truy cập vào roots.txt mình thấy có đường dẫn chứa file backup

    ![](https://hackmd.io/_uploads/BkfqXxnG6.png)
- Truy cập vào thì có thông tin như sau

    ![](https://hackmd.io/_uploads/BJonml2MT.png)
    ![](https://hackmd.io/_uploads/Hyu-Venfa.png)

- Ta thấy passwork database là `g7t4vrnx8ypbfakr2jdxs7nj9nybolb3`
    ![](https://hackmd.io/_uploads/HyLSVl2Mp.png)

## Lab 4: Authentication bypass via information disclosure

![](https://hackmd.io/_uploads/S1yHSghG6.png)

- Giao diện administrator của trang web chứa lỗ hỏng xác thực và có thể khai thác bằng các lỗ hổng qua phương thức HTTP. Chúng ta cần truy cập vào trang admin panel từ đó xóa tài khoản người dùng `carlos`. Chúng ta được cung cấp một tài khoản hợp lệ `wiener:peter` cho mục đích kiểm thử.
- Mình đã thử thêm `/admin` thì nhận được phản hồi như sau

    ![](https://hackmd.io/_uploads/H13TW-2fp.png)
- Đổi phương thức `GET` thành `TRACE` ta được

    ![](https://hackmd.io/_uploads/ByqhGbnza.png)
- Ở đây mình ý header **X-Custom-IP-Authorization: 183.81.120.97**. Đây là header xác định IP người dùng. Bởi vậy, để trở thành local user, có thể sử dụng header này với IP 127.0.0.1 giả mạo local user.

    ![](https://hackmd.io/_uploads/ryJ8UWhz6.png)
    ![](https://hackmd.io/_uploads/BJHc8ZnMa.png)
    ![](https://hackmd.io/_uploads/r1LaIZnfp.png)
## Lab 5: Information disclosure in version control history

![](https://hackmd.io/_uploads/HkgkIM3zT.png)

- Trang web tiết lộ một số thông tin nhạy cảm qua các công nghệ kiểm soát phiên bản lịch sử mã nguồn. Chúng ta cần khai thác, tìm kiếm mật khẩu người dùng `administrator`, từ đó xóa tài khoản người dùng `carlos`.
- Mình thử thêm `/.git` vào url thì nhận được kết quả:
    ![](https://hackmd.io/_uploads/H1-j3f2za.png)
- Đây là dấu hiệu cho thấy trang web sử dụng công nghệ git quản lý mã nguồn và đang bị lộ thông tin tại thư mục `/.git`.
- Ở đây, tôi sử dụng hệ điều hành Linux để khai thác lỗ hổng này. Sử dụng lệnh `wget -r https://example-website/.git` để crawl toàn bộ dữ liệu về:

    ![](https://hackmd.io/_uploads/SJjY_73M6.png)

- Bây giờ mình sẽ đi kiểm tra nhật ký của git xem đã có chuyện gì xảy ra

    ![](https://hackmd.io/_uploads/SJ3Ium2zT.png)
    ![](https://hackmd.io/_uploads/rkHhO73fa.png)


- Vậy là tại `commit 9d91833db7ade41ac68762a69c4f07c9fdc452ef` mật khẩu admin bị xóa khỏi file config. Vì vậy mình đã dùng lệnh `git checkout 9d91833db7ade41ac68762a69c4f07c9fdc452ef` để chuyển đến commit và nó đã xuất hiện thêm 1 file mới là `admin.conf` so với lúc ban đầu

    ![](https://hackmd.io/_uploads/B1tAOm3Mp.png)

- Sau khi đọc file `admin.conf` thì mình thu được

    ![](https://hackmd.io/_uploads/rJGltmhfa.png)

- Vậy mình có username và password là `administrator:jv77qpxazn8muomtep4c` 

    ![](https://hackmd.io/_uploads/BJ8EFXnfT.png)


Lab: Information disclosure in error messages.md
Đang hiển thị Lab: Information disclosure in error messages.md.