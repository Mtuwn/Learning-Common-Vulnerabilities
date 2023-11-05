## Simple Blind SQL Injection

![image.png](https://hackmd.io/_uploads/rkoGGLmXp.png)
![image.png](https://hackmd.io/_uploads/Hy9mG8Q76.png)
- Sau khi check response của request: 

![image.png](https://hackmd.io/_uploads/Sk1H7UXXT.png)

và mình đã có được câu truy vấn sql `SELECT * FROM users WHERE uid='admin'`. Mình đã thử chèn ký tự `'` sau admin và nhận được thông báo lỗi nhưng khi chèn `''` thì lỗi lại biến mất. Và khi mình thử chèn thêm 1 điều kiện luôn đúng phía sau thì mình cũng bị thông báo lỗi:

![image.png](https://hackmd.io/_uploads/rJ0uVUQQT.png)

- Nhưng ở đây mình để ý là câu truy vấn sql luôn tự động chèn thêm kí tự `'` và cuối câu nên mình đã sửa lại thành

![image.png](https://hackmd.io/_uploads/SyU7r8X7T.png)

Vậy là mình đã bỏ qua được lỗi cú pháp. Bây giờ mình sẽ đi tiến hành kiểm tra độ dài mật khẩu của `admin` thì sau 1 thời gian thử thì mình tìm được độ dài của nó là 13

![image.png](https://hackmd.io/_uploads/By5iHUmm6.png)

- Bây giờ việc còn lại của mình là đi brute force mật khẩu của admin bằng việc sử dụng câu lệnh `substring` để đi tìm từng kí tự của mật khẩu 

![image.png](https://hackmd.io/_uploads/r1DdFUQXT.png)
![image.png](https://hackmd.io/_uploads/HyrqFLmma.png)

- Vậy mình đã tìm được password admin là y0u_4r3_4dm1n. Dùng password: y0u_4r3_4dm1n và user:admin đăng nhập vào ta tìm được flag:`CHH{SImPle_B1IND_SQLi_c2e307a3c3fddd93eaeababaf929bbe2}`