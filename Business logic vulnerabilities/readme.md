
# Business logic vulnerabilities

## Lab 1: Excessive trust in client-side controls

![](https://hackmd.io/_uploads/SklDGcaWT.png)

- Bài lab này có chứa lỗ hổng logic trong quy trình mua hàng của nó để mua các mặt hàng với mức giá ngoài ý muốn. Để solve bài lab này. Tài khoản hợp lệ được cung cấp: wiener:peter.

- Khi add to cart, mình có nhận được 1 request post khá bất thường

![](https://hackmd.io/_uploads/ryedKPcabp.png)

Request post chứa thông tin sản phẩm mình đã chọn. Nó sẽ gửi các thông tin đó đến giỏ hàng. Vậy nên ở đây mình thử chỉnh sửa giá của sản phẩm nhỏ hơn số tiền mình đang có còn 1000$ và nhận thấy sản phẩm tại giỏ hàng đã thay đổi giá thành 

![](https://hackmd.io/_uploads/rJw-Kq6Wa.png)

- Bây giờ ta ấn place order và bài lab đã được giải quyết

![](https://hackmd.io/_uploads/HJVIYcTZa.png)

## Lab 2: High-level logic vulnerability

![](https://hackmd.io/_uploads/ByapYcaW6.png)

- Bài lab này có chứa lỗ hổng logic trong quy trình mua hàng của nó để mua các mặt hàng với mức giá ngoài ý muốn. Để solve bài lab này. Tài khoản hợp lệ được cung cấp: wiener:peter.
- Bài lab này khá giống với bài lab đầu tiên. Nhưng ở đây khi ta chặn request khi add to cart thì không còn thấy giá thành sản phẩm mà thay bằng 3 thông tin khác như sau:

![](https://hackmd.io/_uploads/ByISscp-T.png)

- Chúng ta có thể khai thác thông tin này, mình để ý thấy ở đây có 1 cột là số lượng sản phẩm. Vậy sẽ ra sao nó ta mua số lượng sản phẩm là âm?

![](https://hackmd.io/_uploads/rJfH25pWp.png)

- Như vậy ta nhận được 1 thông báo là không thể mua với số tiền là âm. Như vậy, chúng ta phải đi mua sắm thêm để số tiền của mình là dương thì mới mua được Lightweight l33t leather jacket và tất nhiên là tổng nó phải ít hơn số tiền mình đang có. 

![](https://hackmd.io/_uploads/HkVxJjpWp.png)
![](https://hackmd.io/_uploads/rJiZksaZa.png)

## Lab 3: Inconsistent security controls

![](https://hackmd.io/_uploads/BJu0ospba.png)

- Bài lab này có lỗi logic có thể cho phép người khác truy cập vào trang quản trị. Để solve được thì đi vào trang quản trị vào xóa tài khoản `carlos`.
- Khi đăng kí tài koản ta có thấy 1 thông báo chưa đuôi email công việc `@dontwannacry.com`. Có vẻ như đây là email của admin. 

    ![](https://hackmd.io/_uploads/ByhfRopba.png)

- Tất nhiên mình là chỉ là guest nên sẽ đăng kí với đuôi email khác

    ![](https://hackmd.io/_uploads/SJmRRsaWa.png)

- Ở đây mình đã thử đôi email của thành `abc@dontwannacry.com`

![](https://hackmd.io/_uploads/Sy2X1haba.png)

- Như vậy là mình đã vào được tài khoản có chức năng tương tự như admin. Bây giờ chúng ta cùng đi xóa user carlos thôi

![](https://hackmd.io/_uploads/ry4tkhpb6.png)

## Lab 4: Flawed enforcement of business rules

![](https://hackmd.io/_uploads/H1gpJ2aZp.png)

- Phòng thí nghiệm này có một lỗ hổng logic trong quy trình mua hàng của nó. Để giải quyết bài lab, hãy khai thác lỗ hổng này để mua một chiếc “Lightweight l33t leather jacket”. Đăng nhập vào tài khoản của mình bằng thông tin đăng nhập sau: `wiener:peter`
- Đối với bài lab này mình đã thử các cách y như bài lab 1 và 2 nhưng không thành công, vì vậy buộc mình phải nghĩ theo hướng khác. Sau 1 lúc lượn lờ ở trang Home mình có để ý 2 mã giá
![](https://hackmd.io/_uploads/Sy9Wm2Tb6.png)

![](https://hackmd.io/_uploads/SJfb7h6ba.png)

- Sau khi áp 2 mã giảm giá này thì tiền được giảm đi kha khá nhưng mà vẫn chưa đủ để mua hàng 
![](https://hackmd.io/_uploads/ryQsQha-a.png)

- Mình đã thử nhập tiếp mã giảm giá `SIGNUP30` nhưng nó báo mã đã được sử dụng. Vì thế mình đã thử nhập lại mà `NEWCUST5` thì bất ngờ nó vẫn cho áp mã

    ![](https://hackmd.io/_uploads/HJP_E26Wp.png)
- Vậy là ta rút ra kết luận là cứ 2 mã giảm giá liên tiếp mà không trùng nhau thì sẽ được áp dụng. Như vậy là bây giờ mình đã có thể mua được `Lightweight l33t leather jacket` với giá rẻ rồi

    ![](https://hackmd.io/_uploads/BJq-r36Wp.png)

## Lab 5: Low-level logic flaw

![](https://hackmd.io/_uploads/HyySR8lMa.png)

- Trang web mua sắm trên có một quá trình kiểm tra không chặt chẽ đối với tham số từ người dùng, dẫn đến lỗ hổng có thể mua sắm sản phẩm với số lượng ngoài mong muốn. Để vượt qua bài lab, chúng ta cần mua thành công sản phẩm "Lightweight l33t leather jacket". Tài khoản hợp lệ được cung cấp: `wiener:peter`. 
- Trong trường hợp này, trang web không cho phép số lượng món hàng nhận giá trị âm. Và trang web chỉ cho tăng số lượng sản phẩm nhưng việc tăng này chỉ dừng lại ở con số 99 và khi tới 100 thì nó trả về thông báo

![](https://hackmd.io/_uploads/SkVRWPeGp.png)

- Như vậy tham số `quantity` có giới hạn, chúng ta có thể dự đoán giá trị **total price** cũng tồn tại giới hạn. Để kiểm chứng điều này, mình có dùng intruder của burp suite với Null payloads để thêm sản phẩm thì nhận thấy sau khi giá sản phẩm vượt qua giới hạn của kiểu dữ liệu `int` thì lập tức nó quay về giá trị âm 

![](https://hackmd.io/_uploads/SkszBPxf6.png)

- Như vậy mình chỉ cần tính toán sao cho mua các sản phẩm mà tổng của chúng là 1 số nguyên dương nhỏ hơn số tiền mình hiện có

![](https://hackmd.io/_uploads/SyqwqvxG6.png)

![](https://hackmd.io/_uploads/SkyK9weM6.png)

## Lab 6: Inconsistent handling of exceptional input

![](https://hackmd.io/_uploads/rJyi8StGT.png)

- Trang web có một quá trình kiểm tra không chặt chẽ đối với tham số từ người dùng. Chúng ta cần khai thác để có thể truy cập vào trang quản trị và xóa tài khoản người dùng Carlos
- Bài lab này tương tự với bài số 3. Điểm khác là không còn chức năng update email nữa. Thay vào đó, tận dụng các server xử lý email khi render để tấn công. Cụ thể, nếu ta đăng kí tài khoản với email dài như sau: 
    ![](https://hackmd.io/_uploads/S1DXmqqz6.png)
thì ứng dụng đã cắt và chỉ lấy 255 kí tự đầu.

    ![](https://hackmd.io/_uploads/BJWr759GT.png)

- Mặt khác vì email được cấp có thể nhận được tất cả các mail kể cả các subdomain nên ta sẽ nảy ra ý tưởng chèn `dontwannacry.com.` vào domain của email đăng kí và kết hợp với các kí tự khác sao cho khi server lấy 255 kí tự đầu thì kết quả sẽ là `<...>@dontwannacry.com`.

- Cụ thể mình sẽ tạo ra email bằng đoạn code sau: 

```
tmp = 'a'*238+'@dontwannacry.com.'+'exploit-0ae000ce041bfa5a811983a101050053.exploit-server.net'
print(tmp)
```

![](https://hackmd.io/_uploads/HJo-B9cGa.png)

![](https://hackmd.io/_uploads/BknmrqqM6.png)

![](https://hackmd.io/_uploads/Hkpid9qf6.png)

## Lab 7: Weak isolation on dual-use endpoint

![](https://hackmd.io/_uploads/SJH223qzT.png)

- Bài lab có lỗ hổng xác thực admin. Để solve được bài lab thì truy cập vào và xóa tải khoản `carlos`
- Sau khi đăng nhập thì trang web hiển thị 1 trang có chức năng thayt đổi mật khẩu. Mình có dùng burp suite để lấy request 

    ![](https://hackmd.io/_uploads/S1bfgTqfT.png)

Nó có hiển thi param username gửi đi nên mình đã thử đổi nó thành `administrator` nhưng không thành công

    ![](https://hackmd.io/_uploads/SJAOeT9Gp.png)

Nó có hiển thị mật khẩu hiện tại không đúng nhưng username thì vẫn được đẩy đi là `administrator`. Ở đây mình đã thử bỏ đi việc xác thực param `current-password` thì việc đổi mật khẩu đã thành công

    ![](https://hackmd.io/_uploads/rkF_ZTqMa.png)
    ![](https://hackmd.io/_uploads/Bk7ibaqMa.png)

## Lab 8: Insufficient workflow validation

![](https://hackmd.io/_uploads/H1lBU6qz6.png)


- Mình có test qua các lỗi lúc add vào giỏ hàng nhưng không khai thác gì. Nên mình đã thử mua 1 món đồ rẻ phù hợp với giá tiền. Sau khi kiểm tra HTTP history mình có nhận được request

![](https://hackmd.io/_uploads/S1OQFpczp.png)

-   POST `/cart/checkout`: request thanh toán
-   GET `/cart/order-confirmation?order-confirmed=true`: request confirm các sản phẩm đã mua.

Bây giờ mình sẽ add món đồ cần mua vào giỏ hàng, và thanh toán bằng cách gửi luôn request GET `/cart/order-confirmation?order-confirmed=true` và bỏ request `POST /cart/checkout`.

![](https://hackmd.io/_uploads/rkWE9TqMp.png)

## Lab 9: Authentication bypass via flawed state machine

![](https://hackmd.io/_uploads/rkWtursGp.png)

- Trang web chứa lỗ hổng logic trong các bước của quá trình xác thực. Để giải quyết bài lab, chúng ta cần khai thác lỗ hổng để truy cập tài khoản admin, từ đó xóa tài khoản người dùng Carlos. Tài khoản hợp lệ được cung cấp: `wiener:peter`.

- Mình đã thử truy cập trực tiếp vào trang admin bằng cách thêm `/admin` vào url nhưng không thành công.

- Đăng nhập với tài khoản `wiener:peter`, sau khi đăng nhập chúng ta được lựa chọn vai trò là **User** hoặc **Content author**:

![](https://hackmd.io/_uploads/ByMIsrjza.png)

- Vậy nếu mình đăng nhập vào mà không với 2 vai trò này thì không biết mình sẽ có quyền gì. Vì vậy mình đã dùng burp suite bắt lấy request và drop request yêu cầu này:

![](https://hackmd.io/_uploads/ry2nhHsM6.png)

![](https://hackmd.io/_uploads/BJBAhBiGT.png)
- Bây giờ mình sẽ truy cập đến my account bằng cách thêm `/my-account` vào thanh url 

![](https://hackmd.io/_uploads/r1ZHTSsGT.png)

- Vậy là chúng ta đã truy cập được vào với vai trò là `administrator` bây giờ mình sẽ đi xóa tài koản carlos nữa là solve bài lab

![](https://hackmd.io/_uploads/H1SiaBsfp.png)






Business logic vulnerabilities.md
Đang hiển thị Business logic vulnerabilities.md.