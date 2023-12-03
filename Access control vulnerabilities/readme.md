# Access control vulnerabilities

## Lab 1: Unprotected admin functionality

![image.png](https://hackmd.io/_uploads/Byxlfe-c7T.png)

- Lab này có một trang quản trị admin không được bảo vệ chắc chắn, chúng ta cần truy cập và thực hiện xóa tài khoản `carlos`.
- Một trong những việc làm đầu tiên khi thực hiện Pentest một trang web là tìm kiếm các thông tin hữu ích liên quan tới mục tiêu. Và một trong những tệp tin thường được đọc đầu tiên là `robots.txt` (Khi thực hiện quét các đường dẫn cũng có tệp tin này). Tệp `robots.txt` chủ yếu dùng để quản lý lưu lượng truy cập của trình thu thập dữ liệu vào trang web và thường dùng để ẩn một tệp khỏi Google. Đôi khi nó cũng chứa một số thông tin hữu ích.

![image.png](https://hackmd.io/_uploads/HJt3lW5QT.png)

- Truy cập tới `/administrator-panel`:
![image.png](https://hackmd.io/_uploads/SkIlbb5X6.png)
![image.png](https://hackmd.io/_uploads/B1OlZZc7a.png)

## Lab 2: Unprotected admin functionality with unpredictable URL

![image.png](https://hackmd.io/_uploads/HJz4W-q7p.png)
- Lab này có một trang quản trị admin không được bảo vệ chắc chắn. Tuy đường dẫn được đặt tên để không thể bị quét ra nhưng nó bị lộ ở một nơi nào đó xung quanh trang web, chúng ta cần truy cập và thực hiện xóa tài khoản `carlos`.
- Mình thử truy cập tới file robots.txt như bài trước nhưng có không truy cập được, vì vậy cùng xem source code nào:

![image.png](https://hackmd.io/_uploads/BymNf-5Qp.png)

- Sau khi đọc source code thì mình thấy ở đây trang wed có sử dụng 1 đoạn mã script để xác định có phải là admin hay không thông qua biến isAdmin. Nếu nó đúng nó sẽ được chuyển đến `/admin-9b25rg`. Mình sẽ bỏ qua việc kiểm tra này bằng cách truy cập trực tiếp vào nó: 

![image.png](https://hackmd.io/_uploads/Sy7f7b9Qa.png)
![image.png](https://hackmd.io/_uploads/BJSGXb976.png)

## Lab 3: User role controlled by request parameter

![image.png](https://hackmd.io/_uploads/HkZCmWqQ6.png)
- Miêu tả đề bài cho biết trang quản trị tại `/admin` và hệ thống xác định vai trò quản trị thông qua tham số trong cookie. Chúng ta cần nâng quyền người dùng `wiener:peter` lên quyền admin và thực hiện xóa tài khoản `carlos`.
- Đầu tiên thì ta cứ đăng nhập vào với tài khoản `wiener:peter`
- Đề bài đã cho chúng mình đường dẫn `/admin`, vì vậy mình đã truy cập thử:

![image.png](https://hackmd.io/_uploads/SJHN4WqXT.png)

- Ồ vậy là trang web chỉ hiển thị ra giao diện của admin khi chúng ta đăng nhập với tư cách là administrator. Điều này có vẻ liên quan đến cookie và đề bài cũng có đề cập đến nó, vì thế mình đã kiểm tra cookie:

![image.png](https://hackmd.io/_uploads/B1F2H-9Xa.png)

- Thử đổi admin thành true và load lại trang:
![image.png](https://hackmd.io/_uploads/ryWxUb9mT.png)
![image.png](https://hackmd.io/_uploads/B1WZUb97T.png)

## Lab 4: User role can be modified in user profile

![image.png](https://hackmd.io/_uploads/ryfdLW9QT.png)

- Miêu tả đề bài cho biết trang quản trị tại `/admin` và nó chỉ cho phép các người dùng có giá trị `roleid` bằng 2 truy cập. Chúng ta cần nâng quyền người dùng `wiener:peter` lên quyền admin và thực hiện xóa tài khoản `carlos`.

- Làm gì thì làm, mình cứ đăng nhập vào trước xem có gì đã. 
![image.png](https://hackmd.io/_uploads/SyDCtW9X6.png)
- Tại request get mình đã thử thay đổi id thành admin nhưng nó lại quay về đăng nhập và không có điều gì xảy ra. Thôi thì cứ đăng nhập như bình thường vậy.Đăng nhập xong thì mình thử thêm `/admin` xem có gì không

![image.png](https://hackmd.io/_uploads/Sk10dZcXT.png)

- Khác với lab trước, request không chứa các tham số cụ thể xác định vai trò quản trị viên.
- Do đề bài cho biết hệ thống sử dụng tham số `roleid` để xác định vai trò người dùng, nên ta cần tìm cách "gửi kèm" giá trị này tới hệ thống với tài khoản `wiener`.
- Quay lại `my account` thì mình thấy ở đây có chức năng update, thử đi update xem nó có gì đặc biệt:

![image.png](https://hackmd.io/_uploads/Sys05b576.png)

- Tại request post, email được post lên hệ thống dưới dạng json, và nó trả về các thông tin trong đó mình có chú ý đến `roleid:1` tài vì đề bài có đề cập tới `roleid:2`. Bây giờ hãy thử thay đổi nó bằng việc gửi đính kèm nó bằng đoạn mã json post kèm với email thử:
![image.png](https://hackmd.io/_uploads/S1jT3bcmT.png)
![image.png](https://hackmd.io/_uploads/Hyygpb5mp.png)
- Ok vậy là mình đã đăng nhập với quyền admin, giờ thì làm nốt việc còn lại thôi

![image.png](https://hackmd.io/_uploads/SyoMpb5mT.png)

## Lab 5: User ID controlled by request parameter

![image.png](https://hackmd.io/_uploads/HyAy1zcQa.png)

- Miêu tả đề bài cho biết lab này chứa lỗ hổng trong dạng kiểm soát truy cập theo chiều ngang. Mỗi người dùng có một giá trị API duy nhất, nhiệm vụ của chúng ta sẽ dựa vào lỗ hổng này để thu thập giá trị API của `carlos` và submit. Chúng ta được cung cấp một tài khoản hợp lệ `wiener:peter`.
- Đăng nhập với tài khoản `wiener:peter`, thì tại phương thức get mình có thấy para `id=wiener`

![image.png](https://hackmd.io/_uploads/HJhggfqmp.png)

- Thử đổi nó bằng carlos thì mình có api key:

![image.png](https://hackmd.io/_uploads/SyJdxzc7T.png)
- API KEY: `3QytrJCncxhWhyaONQaSSsdFX8BBJ17w`

![image.png](https://hackmd.io/_uploads/SJuoeMcm6.png)

## Lab 6: User ID controlled by request parameter, with unpredictable user IDs

![image.png](https://hackmd.io/_uploads/BkUhDfqQa.png)
- Miêu tả đề bài cho biết lab này tồn tại lỗ hổng trong dạng kiểm soát truy cập theo chiều ngang. Mã định danh người dùng GUIDs là một giá trị không thể đoán được, tuy nhiên chúng có thể được tìm thấy đâu đó xung quanh trang web. Chúng ta cần truy cập vào hồ sơ `carlos` là lấy được giá trị API key của anh ấy. Chúng ta được cung cấp một tài khoản hợp lệ `wiener:peter`.
- Đăng nhập vào bằng tại khoản đã cho thì mình thấy trên url có 1 para là `id=a2923fff-9929-45d2-b542-c2fababbbfb9`tương ứng với người dùng `wiener` . Đây là một giá trị sinh ngẫu nhiên hoặc được định nghĩa để người dùng không thể dự đoán được giá trị id của người dùng khác.
- Truy cập vào blog, xem 1 bài bất kì. Mình có thấy trong bài viết có kèm theo cả tên tác giả

![image.png](https://hackmd.io/_uploads/S1Mg5zcmT.png)
- Ấn vào tên tác giả thì mình đến một trang mà tại đây trên url có thêm tham số là userID

![image.png](https://hackmd.io/_uploads/HJHN5GcQT.png)
- Mình để ý cái userid của wiener nó trùng với id của wiener, vậy nên mình sẽ đi tìm bài viết của tác giả carlos để đi lấy userid

![image.png](https://hackmd.io/_uploads/r10h5M57a.png)

- CÓ userid: 3698c1c5-6488-479a-a0cc-d2b0e6cb3ca0

![image.png](https://hackmd.io/_uploads/Bkf7oGcXa.png)

- API key:`0lnCJ4EyNxuaa0PJE5TSg84d5Y2OvjbN` 

![image.png](https://hackmd.io/_uploads/HyPcoz9mp.png)

## Lab 7: User ID controlled by request parameter with data leakage in redirect
![image](https://hackmd.io/_uploads/S1eoC_cmT.png)
- Miêu tả đề bài cho biết lab chứa lỗ hổng kiểm soát truy cập, trong đó một số thông tin nhạy cảm bị lộ trong phần thân của phản hồi chuyển hướng (redirect response). Chúng ta được cung cấp một tài khoản hợp lệ `wiener:peter` và cần tìm ra giá trị API key của người dùng `carlos`.
- Đăng nhập thành công với user: wiener mình thấy trên thành địa chỉ có para id=wiener:
![image](https://hackmd.io/_uploads/SkXieY5Xp.png)
- Đổi nó thành carlos thì mình bị chuyển về giao diện login Quan sát **HTTP history** trong Burp Suite, request `/my-account?id=carlos` vẫn được hệ thống thực hiện và trả về response thành công.
![image](https://hackmd.io/_uploads/S1zezF5X6.png)
- API key carlos: `DO1nalmFggYkLZZWuVavwekbVdUPKWnb`

![image](https://hackmd.io/_uploads/ry_7ftq7p.png)

## Lab 8: User ID controlled by request parameter with password disclosure

![image](https://hackmd.io/_uploads/Sy_PMKqXT.png)

- Miêu tả đề bài cho biết trang cá nhân của người dùng trực tiếp chứa mật khẩu hiện tại ở dạng ẩn. Chúng ta cần khai thác lỗ hổng kiếm soát truy cập, thu thập mật khẩu tài khoản administrator và thực hiện xóa tài khoản người dùng `carlos`. Lab cung cấp một tài khoản hợp lệ là `wiener:peter`.

- Đăng nhập vào với user: wiener mình vẫn thấy bài này có parameters là id:

![image](https://hackmd.io/_uploads/By7fVY9mT.png)

thay đổi nó thành administrator: 
![image](https://hackmd.io/_uploads/SkKr4Y9ma.png)
thì mình đã đăng nhập được vào được my account với username là administrator. Sau khi xem qua source code thì mình đã xem được mật khẩu của username này khi nó bị ẩn:
![image](https://hackmd.io/_uploads/SyR6VYqQp.png)
- password:`xriyw4zpr3sn9kdamms8`. Nhiệm vụ bây giờ là đăng nhập vào và đi xóa tài khoản carlos thôi.

![image](https://hackmd.io/_uploads/B1sNBKqm6.png)

## Lab 9: Insecure direct object references

![image](https://hackmd.io/_uploads/SyBXk59Xa.png)

- Miêu tả đề bài cho biết trang web lưu trữ các lịch sử trò chuyện của người dùng và có thể truy cập thông qua các đường dẫn tĩnh. Chúng ta cần thu thập thông tin nhạy cảm từ các tệp dữ liệu này, tìm kiếm mật khẩu và truy cập vào tài khoản của người dùng `carlos`.
- Đăng nhập và thay đổi parameters thành carlos thì nó cũng quay về trang login như bài trước nhưng bài này khi check history thì nó không thành công. Mở thử live chat thì có 2 chức năng là gửi tin nhắn và xem lại lịch sử trò chuyện
![image](https://hackmd.io/_uploads/SkhmXcq7p.png)
- Khi ấn vào View transcript thì nó cho mình tải về 1 file là 6.txt

![image](https://hackmd.io/_uploads/SkUq7c5XT.png)

- Đổi tên file 6.txt thành từ 1 đến 5 thì tại file 1.txt được thông tin như sau:

![image](https://hackmd.io/_uploads/BJ1eVc5XT.png)
- Nó cho mình 1 password:`9myi3vdyqpynf2mfia7n`. Nhưng mình không biết đây là mật khẩu của cái gì. Nhưng mà đề bài đang bắt mình đi tìm password của carlos nên mình nghĩ nó là của carlos dùng mật khẩu này đăng nhập thì vào được thật

![image](https://hackmd.io/_uploads/HJBDE997p.png)

## Lab 10: URL-based access control can be circumvented
![image](https://hackmd.io/_uploads/HkbEH597p.png)

- Miêu tả tình huống cho phép trang web có trang quản trị administrator với đường dẫn /admin. Hệ thống front-end đã thực hiện ngăn chặn các hành vi truy cập trái phép tới đường dẫn này, tuy nhiên, back-end server sử dụng framework cho phép tiêu đề **X-Original-URL** hoạt động. Nhiệm vụ của chúng ta là khai thác lỗ hổng này, truy cập tới trang quản trị hệ thống và xóa đi tài khoản của người dùng `carlos`.

- Mình thử thêm `/admin` vào url thì nhận được `"Access denied"`. Đề có đề cập tới việc sử dụng `X-Original-URL` nên mình đã chèn thêm nó vào request:

![image](https://hackmd.io/_uploads/r14StqqXT.png)
- Tương tự với khi xóa: 

![image](https://hackmd.io/_uploads/Hkh095976.png)
![image](https://hackmd.io/_uploads/r1Vkj95Qp.png)

## Lab 11: Method-based access control can be circumvented

![image](https://hackmd.io/_uploads/Byn5KBoXT.png)

- Mình được cung cập một tài khoản có vai trò administrator là `administrator:admin` giúp thu thập các thông tin hữu ích liên quan tới upgrade một tài khoản lên quyền quản trị viên. Chúng ta cần khai thác lỗ hổng trong HTTP reuqest method để upgrade tài khoản `wiener:peter` lên quyền admin.
- Đăng nhập với tài khoản `administrator:admin` và quan sát trang quản trị Admin panel:
![image](https://hackmd.io/_uploads/Byd5Rrjma.png)
- Tính năng cho phép chúng ta có thể upgrade hoặc downgrade vai trò của bất kì người dùng nào. Thử upgrade vai trò của của người dùng `carlos` và quan sát request trong Burp Suite:
 ![image](https://hackmd.io/_uploads/BJJA0BsXa.png)
- Hệ thống gọi tới path `/admin-roles` và truyền lên hai tham số `username=carlos&action=upgrade` bằng phương thức **POST**. Lưu ý giá trị tại header Cookie `session=gyIyALKqa3VgPiAYZobuGlCHj3SUt1yN` được sử dụng để xác thực người dùng.

- Đăng xuất ra rồi đăng nhập trở lại với tư cách là wiener, lấy seasion của tài khoản này
- Xong mình sẽ lấy seasion này thay vào request post upgrade mà mình đã lưu lại trong repeater trước đó:

![image](https://hackmd.io/_uploads/SyLkZ8j76.png)
- Chúng ta thu được thông báo "Unauthorized". Do hệ thống không thực hiện kiểm tra các HTTP request method từ người dùng, nên chúng ta có thể vượt qua lớp bảo vệ này bằng cách sử dụng HTTP request method. Click chuột phải và thay click vào change request method, đổi username thành wiener:

![image](https://hackmd.io/_uploads/BkZxMUiQp.png)

## Lab 12: Multi-step process with no access control on one step
![image](https://hackmd.io/_uploads/S10hQUiXp.png)
- Miêu tả lab đặt ra giả thuyết chúng ta đã có tài khoản với quyền quản trị là `administrator:admin`. Trang quản trị chứa một quá trình nhiều bước thực hiện thay đổi vai trò người dùng. Chúng ta có thể thu thập cách trang quản trị hoạt động bằng tài khoản `administrator`. Chúng ta còn được cung cấp một tài khoản hợp lệ `wiener:peter`, nhiệm vụ cần khai thác lỗ hổng kiểm soát truy cập để leo quyền tài khoản `wiener` lên quyền quản trị.
- Đăng nhập với tài khoản `administrator:admin`, tại trang **Admin panel** chứa chức năng upgrade vai trò người dùng. Mình thực hiện bắt 2 request là upgrade và xác thực upgrade và lưu trữ tại repeater.
![image](https://hackmd.io/_uploads/By4aBUiQa.png)
![image](https://hackmd.io/_uploads/B1X0SLo7a.png)
- Sau đó mình thoát ra và đăng nhập vào wiener lấy seasion như bài lab trước và quay trở lại thay nó vào request upgrade. Tuy nhiên, nhận được thông báo **"Unauthorized"**, mình biết rằng chức năng thay đổi vai trò người dùng hoạt động trong hai bước. Bởi vậy, thử bỏ qua bước thứ nhất (hệ thống khả năng thực hiện xác thực người dùng tại bước này), trực tiếp gửi các tham số `action=upgrade&confirmed=true&username=wiener` bằng phương thức **POST** tới `/admin-roles`:

![image](https://hackmd.io/_uploads/HJUEDUs7T.png)
![image](https://hackmd.io/_uploads/Sy6EvLimp.png)

## Lab 13: Referer-based access control
![image](https://hackmd.io/_uploads/HJJdvUi7a.png)
- Miêu tả lab cho biết trang web kiểm tra thông tin tiêu đề **Referer** để xác thực người dùng. Chúng ta được cung cấp một tài khoản vai trò quản trị viên `administrator:admin` để thu thập các đường dẫn cũng như thông tin liên quan tới chức năng upgrade vai trò người dùng. Chúng ta còn được cung cấp một tài khoản hợp lệ thông thường `wiener:peter`, nhiệm vụ cần khai thác lỗ hổng trên thực hiện leo quyền tài khoản `wiener` lên quyền quản trị viên.
- Đăng nhập với tài khoản quản trị viên `administrator:admin`, truy cập vào tùy chọn **Admin panel**, trong đó chứa chức năng upgrade tài khoản người dùng.
![image](https://hackmd.io/_uploads/r1V5hLs76.png)
- Thực hiện upgrade tài khoản `carlos` lên quyền quản trị và quan sát request:
![image](https://hackmd.io/_uploads/H1qp2Usma.png)
Request gửi tới đường dẫn `/admin-roles` các tham số `username=carlos&action=upgrade` bằng phương thức **GET**. Ngoài ra chú ý tiêu đề **Referer**.
- Thay đổi URL nguồn trong tiêu đề **Referer** thành một đường dẫn bất kì và quan sát response:
![image](https://hackmd.io/_uploads/SJ0XT8sX6.png)
- Nhận được thông báo **"Unauthorized"**. Điều này chứng tỏ hệ thống tồn tại cơ chế xác thực danh tính người dùng qua tiêu đề **Referer**, trong đó người dùng phải gửi yêu cầu upgrade tài khoản từ đường dẫn `/admin`.
- Đăng nhập với tài khoản `wiener:peter`, thực hiện gửi tới đường dẫn `/admin-roles` các tham số `username=wiener&action=upgrade` bằng phương thức **GET**, thêm tiêu đề **Referer** với giá trị `https://0aed00f6031ed0b7c0c86a80009c008c.web-security-academy.net/admin`:
![image](https://hackmd.io/_uploads/SyvsCUom6.png)
![image](https://hackmd.io/_uploads/ry22CUi76.png)










