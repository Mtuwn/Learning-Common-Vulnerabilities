# File upload vulnerabilities

## Lab 1: Remote code execution via web shell upload
![image](https://hackmd.io/_uploads/SkDNlw1NT.png)
- Trang web chứa lỗ hổng Upload File trong chức năng upload ảnh, nó không thực hiện bất kì bước kiểm tra nào đối với file do người dùng tải lên. Để giải quyết bài lab, chúng ta cần upload một Webshell PHP, từ đó đọc nội dung tệp `/home/carlos/secret`. Tài khoản hợp lệ được cung cấp: `wiener:peter`.
- Đăng nhập vào với username là wiener thì xuất hiện trang cá nhân upload hình đại diện, upload 1 ảnh bất kỳ lên thì avt sẽ được thay đổi: ![image](https://hackmd.io/_uploads/HJNEGwkNp.png)
- Click chuột vào xem ảnh:

![image](https://hackmd.io/_uploads/rkc_zvkEp.png)
thì mình thấy ảnh sau khi upload sẽ được lưu vào `/file/avatars/`. Vì vật mình sẽ thực hiện upload một file shell.php để đọc nội dung file `/home/carlos/secret` với nội dung:
```
<?php
echo file\_get\_contents('/home/carlos/secret'); 
?>
```
- Hàm `file_get_contents()` sẽ lấy nội dung file `/home/carlos/secret` và được lệnh `echo` in ra.
![image](https://hackmd.io/_uploads/rkllBP1N6.png)
- Sau khi upload thành công mình truy cập tới đường dẫn `https://0a8c007304d906c5809fdf0400dd0067.web-security-academy.net/files/avatars/shell.php` để xem nội dung
![image](https://hackmd.io/_uploads/ryODBPyE6.png)
![image](https://hackmd.io/_uploads/rJSKBwy4p.png)
## Lab 2: Web shell upload via Content-Type restriction bypass
![image](https://hackmd.io/_uploads/HJXr8PJVp.png)
- Trang web chứa lỗ hổng file upload. Để giải quyết bài lab, chúng ta cần upload một web shell PHP nhằm đọc nội dung file `/home/carlos/secret`. Tài khoản hợp lệ được cung cấp `wiener:peter`.
- Đăng nhập với tài khoản wiener, nó vẫn cho mình trang upload ảnh đại diện, mình thử upload 1 file php shell.php như bài trước:

![image](https://hackmd.io/_uploads/BkBMwPyEa.png)
- Trang web báo lỗi do chỉ cho phép upload các file dạng `image/jpeg` hoặc `image/png`. Vậy nên mình đã đổi content-type thành `image/jpeg` để đúng yêu cầu của header **Content-Type** 

![image](https://hackmd.io/_uploads/By0-uvJ4T.png)

- Ok vậy là đã thành công, đi xem nội dung `/home/carlos/secret` nào:
![image](https://hackmd.io/_uploads/H1Wc_P1ET.png)
![image](https://hackmd.io/_uploads/SksjuDyNp.png)

## Lab 3: Web shell upload via path traversal

![image](https://hackmd.io/_uploads/HkIjVakEa.png)
- Trang web chứa lỗ hổng upload file, trong đó cơ chế ngăn chặn không cho phép người dùng thực thi file. Để giải quyết bài lab, chúng ta cần vượt qua cơ chế này, khai thác lỗ hổng nhằm đọc nội dung tệp `/home/carlos/secret`. Tài khoản hợp lệ được cung cấp `wiener:peter`.
- Đăng nhập với tài khoản `wiener:peter`. Upload một file **php** với nội dung như sau:

```php=
<?php
    echo file_get_contents('/home/carlos/secret');
?>

```
File được upload thành công:
![image](https://hackmd.io/_uploads/HyTKIp1E6.png)

- Tuy nhiên, khi truy cập vào đường dẫn như các bài trước thì lại không thu được kết quả gì
![image](https://hackmd.io/_uploads/rJsgDpJ4p.png)
-Có vẻ như ở folder `avatar` không có quyền thực thi file php nên mình chuyển qua folder trước đó là `files` bằng cách đổi tên file là `../shell.php`

![image](https://hackmd.io/_uploads/r1-fday4a.png)
- Bằng một cách thần kỳ nào đó mà `../` đã biến mất sau khi upload nên mình decode URl nó
![image](https://hackmd.io/_uploads/BJG8OayN6.png)
- Truy cập vào xem nội dung thôi

![image](https://hackmd.io/_uploads/HkxcxY6JVT.png)
![image](https://hackmd.io/_uploads/rJOfF61E6.png)

## Lab 4: Web shell upload via extension blacklist bypass
![image](https://hackmd.io/_uploads/HJtcXR1V6.png)
- Trang web chứa lỗ hổng upload file, trong đó có một black list các extension file. Để giải quyết bài lab, chúng ta cần vượt qua cơ chế này, khai thác lỗ hổng nhằm đọc nội dung tệp `/home/carlos/secret`. Tài khoản hợp lệ được cung cấp `wiener:peter`.
- Đăng nhập với tài khoản `wiener:peter`, với chức năng upload avatar, thử tải lên một file `shell.php` với nội dung như các bài trước

![image](https://hackmd.io/_uploads/BJBRN0kV6.png)
- Có lẽ phần mở rộng php đã bị cho vào danh sách blacklist. Vì vậy mình đã thêm `%00.png` vào cuối file để thành`shell.php%00.png` để bypass blacklist:

![image](https://hackmd.io/_uploads/B1PG_01N6.png)

- bypass qua nó thành công nhưng khi truy cập thì lại không vào được. Mình có tìm hiểu và biết được file `.htaccess` có thể cấu hình để chặn tải file php lên. **.htaccess** \- là một file có ở thư mục gốc của các hostting và do apache quản lý, cấp quyền. File **.htaccess** có thể điều khiển, cấu hình được nhiều yếu tố với đa dạng các thông số, nó có khả năng thay đổi các giá trị được set mặc định của **Apache**. Upload một file với tên `.htaccess`, thay đổi header **Content-Type** thành giá trị **text/plain**, nội dung file như sau: `AddType application/x-httpd-php .tuan`

![image](https://hackmd.io/_uploads/BJCg9AyE6.png)

- Như vậy, hiện tại chúng ta có thể upload các file với phần mở rộng `.tuan` và có thể thực thi các đoạn code tương đương với một file **php**.
![image](https://hackmd.io/_uploads/r1FnsRk4a.png)
- Truy cập tới `/avatars/shell.viblo`:
![image](https://hackmd.io/_uploads/By8RjC1E6.png)
![image](https://hackmd.io/_uploads/S1Ze2AJ4T.png)

## Lab 5: Web shell upload via obfuscated file extension
![image](https://hackmd.io/_uploads/B1xFBUlNa.png)
- Trang web chứa lỗ hổng upload file, trong đó có một black list các extension file. Để giải quyết bài lab, chúng ta cần vượt qua cơ chế này, khai thác lỗ hổng nhằm đọc nội dung tệp `/home/carlos/secret`. Tài khoản hợp lệ được cung cấp `wiener:peter`.
- Đăng nhập với tư cách là wiener và mình vẫn tải lên file shell như các bài trước, dĩ nhiên nó cũng sẽ thông báo lỗi khi mà file tải lên nó chỉ chấp nhập jpg hoặc png:

![image](https://hackmd.io/_uploads/Sy-BLLxEa.png)

- Mình thử thêm %00 để thử bypass qua cơ chế này và file tải lên sẽ trở thành `shell.php%00.png`, phần mở rộng trang web nhận được là `.png` không nằm trong black list, sau khi xử lý thì các ký tự bắt đầu từ ký tự Null byte được loại bỏ, tên file chỉ còn `shell.php` có thể thực thi.

![image](https://hackmd.io/_uploads/Sk91v8l4a.png)

- Truy cập thử vào đường dẫn để xem nội dung: 
![image](https://hackmd.io/_uploads/SkiBv8gN6.png)
![image](https://hackmd.io/_uploads/r1wtDIgVa.png)
## Lab 6: Remote code execution via polyglot web shell upload
![image](https://hackmd.io/_uploads/HkFE38xVT.png)

- Trang web chứa lỗ hổng trong chức năng upload avatar, với nhiều cơ chế bảo vệ nhưng vẫn có thể bị bypass. Để giải quyết bài lab, chúng ta cần khai thác lỗ hổng nhằm đọc nội dung file `/home/carlos/secret`. Tài khoản hợp lệ được cung cấp: `wiener:peter`.
- Vẫn là một quy trình đăng nhập tải file shell lên như các bài, nhưng ở đây thông báo sẽ là:

![image](https://hackmd.io/_uploads/SJBvT8gNp.png)

- Nó không đề cập đến phần mở rộng của file nữa, có thể ở đây nó kiểm tra nội dung của file chứ không phải là đuôi file. Để kiểm chứng điều này, mình thử tải 1 file ảnh và thêm đuôi php:

![image](https://hackmd.io/_uploads/rJtZAIe46.png)

- Nó vẫn có thông báo upload thành công. Vào đường dẫn `https://0afe00610333a6e0801ef3c600ea00a9.web-security-academy.net/files/avatars/Screenshot%202023-11-03%20225728.png.php` thì ở đây nó là nội dung bên trong ảnh chứ không phải là hình ảnh:
![image](https://hackmd.io/_uploads/HyUsAUeNa.png)
- Vì thế mình thử chèn 1 đoạn mã php vào trong nội dung ảnh:
![image](https://hackmd.io/_uploads/HkIz1DeN6.png)
- Giờ đi xem nội dung cần tìm thôi
![image](https://hackmd.io/_uploads/rJx4kDx46.png)
`6fU5X0bYMuXENnRBUCom6z1VG8v5wSUf`
![image](https://hackmd.io/_uploads/HkIUkDe46.png)




