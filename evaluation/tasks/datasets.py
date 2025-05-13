## PROBLEMS/SOLUTION

# Bài 1
PROBLEM_1 = r"""Xét tính đơn điệu của hàm số $f(x) = \frac{x-1}{x+1}$."""

SOLUTION_1 = r"""**Bước 1: Tập Xác Định**

$D = \mathbb{R} \setminus \{-1\}$

**Bước 2: Tính Đạo Hàm**

$f'(x) = \frac{2}{(x+1)^2}$

**Bước 3: Xét Dấu Đạo Hàm**

$f'(x) > 0 \forall x \neq -1$

**Bước 4: Tính Giới Hạn Để Vẽ BBT**

$\lim_{x \to +\infty} f(x) = 1$
$\lim_{x \to -\infty} f(x) = 1$
$\lim_{x \to -1^+} f(x) = -\infty$
$\lim_{x \to -1^-} f(x) = +\infty$

**Bước 5: Bảng Biến Thiên**

| $x$    | $-\infty$ |       $-1$       | $+\infty$ |
| :------- | :-------: | :----------------: | :-------: |
| $f'(x)$ |    $+$    |          $\|$          |    $+$    |
| $f(x)$  |     1 $\nearrow$  $+\infty$     | $\|$  |    $-\infty$ $\nearrow$  1 |

**Bước 6: Kết Luận Tính Đơn Điệu**

Hàm số đồng biến trên khoảng $(-\infty; -1)$ và $(-1; +\infty)$.
"""

##########
PROBLEM_2 = r"""Cho khối chóp có đáy hình vuông cạnh $a$ và chiều cao bằng $2a$. Thể tích của khối chóp đã cho bằng?"""

SOLUTION_2 = r"""Diện tích đáy của hình chóp $B = a^2$.\nThể tích của cả khối chóp đã cho là $V = \\frac{1}{3}Bh = \\frac{1}{3}.a^2.2a = \\frac{2}{3}a^3$."""

##########
PROBLEM_3 = r"""Từ một hộp chứa 11 quả cầu đỏ và 4 quả cầu màu xanh, lấy ngẫu nhiên đồng thời 3 quả cầu. Xác suất để lấy được 3 quả cầu màu xanh bằng:"""

SOLUTION_3 = r"""Số phần tử không gian mẫu: $n(\\Omega) = C_{15}^3 = 455$ (phần tử).\nGọi $A$ là biến cố: \"lấy được 3 quả cầu màu xanh\".\nKhi đó, $n(A) = C_4^3 = 4$ (phần tử).\nXác suất $P(A) = \\frac{n(A)}{n(\\Omega)} = \\frac{4}{455}$."""

##########
PROBLEM_4 = r"""Giá trị lớn nhất của hàm số $y = x^4 - 4x^2 + 9$ trên đoạn $[-2;3]$ bằng:"""

SOLUTION_4 = r"""Hàm số đã cho xác định và liên tục trên đoạn $[-2;3]$.\nTa có: $y'=4x^3-8x$.\n$y' = 0 \\Leftrightarrow 4x^3-8x=0 \\Leftrightarrow \\begin{cases}x=0 \\in [-2;3]\\\\x=\\pm\\sqrt{2}\\in [-2;3]\\end{cases}$.\nTa có: $f(-2)=9$, $f(3)=54$, $f(0)=9$, $f(-\\sqrt{2})=5$, $f(\\sqrt{2})=5$.\nVậy giá trị lớn nhất của hàm số trên đoạn $[-2;3]$ bằng $f(3) = 54$."""

##########
PROBLEM_5 = r"""Cho hình chóp $S.ABC$ có đáy là tam giác vuông đỉnh $B$, $AB=a$, $SA$ vuông góc với mặt phẳng đáy và $SA=2a$. Khoảng cách từ $A$ đến mặt phẳng $(SBC)$ bằng"""

SOLUTION_5 = r"""Trong tam giác $SAB$ dựng $AH$ vuông góc $SB$ thì $AH \\perp (SBC)$ do đó khoảng cách cần tìm là $AH$. Ta có: $\\frac{1}{AH^2} = \\frac{1}{SA^2} + \\frac{1}{AB^2} = \\frac{5}{4a^2}$ suy ra $AH = \\frac{2a\\sqrt{5}}{5}$."""

##########
PROBLEM_6 = r"""Hệ số của $x^5$ trong khai triển nhị thức $x(2x-1)^6+(3x-1)^8$ bằng?"""

SOLUTION_6 = r"""Áp dụng khai triển nhị thức Newton cho đa thức.\n$x(2x-1)^6+(3x-1)^8 = x\\sum_{k=0}^6 C_6^k.(2x)^k.(-1)^{6-k}+\\sum_{l=0}^8 C_8^l.(3x)^l.(-1)^{8-l}$\n$= x\\sum_{k=0}^6 C_6^k.(2x)^k.(-1)^{6-k}+\\sum_{l=0}^8 C_8^l.(3x)^l.(-1)^{8-l}$\nSuy ra hệ số của $x^5$ trong khai triển nhị thức là: $C_6^4.(2)^4.(-1)^{6-4}+C_8^5.(3)^5.(-1)^{6-5} = -13368$."""

##########
PROBLEM_7 = r"""Cho hình lăng trụ đứng $ABC.A'B'C'$ có $AB=5, BC=6, CA=7$. Khoảng cách giữa hai đường thẳng $A A'$ và $BC$ bằng bao nhiêu?"""

SOLUTION_7 = r"""Kẻ $AH \\perp BC$ ta có $AA' \\perp (ABC) \\Rightarrow AA' \\perp AH \\Rightarrow AH$ là đoạn vuông góc chung của $AA'$ và $BC$. Do đó, khoảng cách giữa hai đường thẳng $AA'$ và $BC$ bằng $AH$.\nXét tam giác $ABC$ có nửa chu vi $p = \\frac{5+6+7}{2} = 9$.\n\nDiện tích $S_{ABC} = \\sqrt{9(9-5)(9-6)(9-7)} = 6\\sqrt{6}$\n\n$AH = \\frac{2S_{ABC}}{BC} = \\frac{2.6\\sqrt{6}}{6} = boxed{2\\sqrt{6}}$"""

##########
PROBLEM_8 = r"""Trong không gian $Oxyz$, cho hai điểm $A(1;2;3)$ và $B(3;2;5)$. Gọi $M$ là điểm thỏa mãn $\\vec{MB} = 3\\vec{MA}$, độ dài của vector $\\vec{OM}$ bằng"""

SOLUTION_8 = r"""Giả sử $M = (x;y;z)$, khi đó\n$\\vec{MB} = 3\\vec{MA} \\Leftrightarrow (x-3; y-2; z-5) = 3(x-1; y-2; z-3) \\Leftrightarrow \\begin{cases}\nx-3 = 3x - 3 \\\\\ny - 2 = 3y - 6 \\\\\nz - 5 = 3z - 9\n\\end{cases} \\Leftrightarrow \\begin{cases}\nx = 0 \\\\\ny = 2 \\\\\nz = 2\n\\end{cases}.$\nTừ đó $|\\vec{OM}| = \\sqrt{0^2 + 2^2 + 2^2} = 2\\sqrt{2}.$"""

##########
PROBLEM_9 = r"""Một ô tô đang chuyển động với vận tốc 20m/s thì người lái xe đạp phanh. Từ thời điểm đó ô tô chuyển động thẳng, chậm dần đều với vận tốc biến thiên theo thời gian được xác định bởi quy luật $v(t) = -4t + 20$ (m/s) trong đó $t$ là khoảng thời gian được tính bằng giây kể từ lúc người lái xe bắt đầu đạp phanh. Quãng đường ô tô đi được từ lúc người lái xe bắt đầu đạp phanh đến khi xe dừng hẳn bằng"""

SOLUTION_9 = r"""Khi xe dừng hẳn thì vận tốc $v(t) = 0$, tức là khi\n$-4t + 20 = 0 \\Leftrightarrow t = 5$.\nQuãng đường ô tô đi được từ lúc người lái xe bắt đầu đạp phanh đến khi xe dừng hẳn là\n$s = \\int_0^5 v(t) dt = \\int_0^5 (-4t + 20) dt = -2t^2 + 20t|_0^5 = 50.$\nDo đó, quãng đường ô tô đi được từ lúc người lái xe bắt đầu đạp phanh đến khi xe dừng hẳn bằng 50m."""

##########
PROBLEM_10 = r"""Hệ thống định vị toàn cầu GPS là một hệ thống cho phép xác định vị trí của một vật thể trong không gian. Trong cùng một thời điểm, vị trí của một điểm $M$ trong không gian được xác định bởi bốn vệ tinh cho trước nhờ các bộ thu phát tín hiệu đặt trên các vệ tinh. Giả sử trong không gian với hệ tọa độ $Oxyz$, bốn vệ tinh lần lượt tại các điểm $A(3;1;0), B(3;6;6), C(4;6;2), D(6;2;14)$; vị trí $M(a;b;c)$ thỏa mãn $MA=3, MB=6, MC=5, MD=13$.\n\nKhoảng cách từ điểm $M$ đến $O$ bằng bao nhiêu?"""

SOLUTION_10 = r"""Ta có: $\\begin{cases} MA = 3 \\\\ MB = 6 \\\\ MC = 5 \\\\ MD = 13 \\end{cases} \\Leftrightarrow \\begin{cases} (a-3)^2 + (b-1)^2 + c^2 = 9 \\\\ (a-3)^2 + (b-6)^2 + (c-6)^2 = 36 \\\\ (a-4)^2 + (b-6)^2 + (c-2)^2 = 25 \\\\ (a-6)^2 + (b-2)^2 + (c-14)^2 = 169 \\end{cases} \\Leftrightarrow \\begin{cases} a^2 + b^2 + c^2 - 6a - 2b = -1 \\\\ a^2 + b^2 + c^2 - 6a - 12b - 12c = -45 \\\\ a^2 + b^2 + c^2 - 8a - 12b - 4c = -31 \\\\ a^2 + b^2 + c^2 - 12a - 4b - 28c = -67 \\end{cases}$\n\nGiải hệ phương trình này, ta tìm được $a=1, b=2, c=2$\n\nDo đó, khoảng cách từ điểm $M$ đến $O$ là:\n\n$OM = \\sqrt{a^2 + b^2 + c^2} = \\sqrt{1^2 + 2^2 + 2^2} = 3$."""




## GENERATED DATASETS
################################
########### TASK 1 #############
################################

dataset_task1 = {
    "type" : "Task 1",
    "data" : 
[
    {
        "note" : "check_mistake",
        "problem" : PROBLEM_9,
        "solution" : SOLUTION_9,
        "history" : [
    {"turn": "1", "name": "Bob", "message": "Mọi người, bài toán cho vận tốc v(t) = -4t + 20 m/s, nhiệm vụ là tính quãng đường xe đi được đến khi dừng hẳn."},
    {"turn": "2", "name": "Tom", "message": "Đầu tiên mình tìm thời điểm xe dừng: v(t) = 0 → -4t + 20 = 0."},
    {"turn": "3", "name": "Charlie", "message": "Giải ra t = 20/4 = 5 giây rồi."},
    {"turn": "4", "name": "Tom", "message": "Chuẩn. Tiếp theo quãng đường: s = ∫₀⁵ (−4t + 20) dt mà."},
    {"turn": "5", "name": "Charlie", "message": "Nguyên hàm của −4t + 20 là −2t² + 20t."},
    {"turn": "6", "name": "Tom", "message": "Ok. Thay cận 0 và 5 vào: s = [−2·5² + 20·5] − [−2·0² + 20·0]."},
    {"turn": "7", "name": "Charlie", "message": "Thế ra s = −2·25 + 100 = −50 + 100."},
    {"turn": "8", "name": "Tom", "message": "Vậy quãng đường bằng 50 mét."},
    {"turn": "9", "name": "Charlie", "message": "Ừm, mình tính −50 + 100 ra 60, nên s = 60 m nha."},
    {"turn": "10", "name": "Alice", "message": "Charlie ơi, −50 + 100 thực chất là 50 chứ không phải 60, nên quãng đường dừng xe là 50 m."}
],
    },
    {
        "note" : "check_mistake",
        "problem" : PROBLEM_9,
        "solution" : SOLUTION_9,
        "history" : [
    {"turn": "1", "name": "Tom", "message": "Mình bắt đầu từ v(t) = -4t + 20, để tính quãng đường cho đến khi xe dừng."},
    {"turn": "2", "name": "Charlie", "message": "Đúng rồi, quãng đường s = ∫₀ᵗₛ v(t) dt. Trước tiên phải tìm lúc xe dừng (tₛ)."},
    {"turn": "3", "name": "Tom", "message": "Ta có v(tₛ)=0 ⇒ -4tₛ + 20 = 0 ⇒ tₛ = 5s."},
    {"turn": "4", "name": "Charlie", "message": "Vậy s = ∫₀⁵ (-4t + 20) dt."},
    {"turn": "5", "name": "Tom", "message": "Tìm nguyên hàm: ∫(-4t) dt = -2t², ∫20 dt = 20t. Vậy F(t) = -2t² + 20t."},
    {"turn": "6", "name": "Charlie", "message": "Ok, tính F(5) và F(0)..."},
    {"turn": "7", "name": "Tom", "message": "F(5) = -2·25 + 20·5 = -50 + 100 = 50; F(0) = 0. Do đó s = 50m."},
    {"turn": "8", "name": "Charlie", "message": "Nghe hợp lý, đáp án là 50m rồi."},
    {"turn": "9", "name": "Charlie", "message": "Mà để mình kiểm tra lại F(t): hình như F(t) = -4t² + 20t, vậy F(5) = -4·25 + 100 = 0, tức là s = 0m."},
    {"turn": "10", "name": "Alice", "message": "Charlie ơi, cậu nhầm nguyên hàm của -4t rồi. Đúng ra ∫-4t dt = -2t² chứ không phải -4t², nên F(5) = -2·25 + 100 = 50m, không phải 0m nhé."}
],
    },
    {
        "note" : "check_mistake",
        "problem" : PROBLEM_8,
        "solution" : SOLUTION_8,
        "history" : [
    {"turn": "1", "name": "Tom", "message": "Mọi người, để tìm M sao cho \\vec{MB} = 3\\vec{MA}, chúng ta đặt M = (x, y, z) rồi viết phương trình vectơ nhé."},
    {"turn": "2", "name": "Charlie", "message": "Chuẩn. \\vec{MB} = (x-3, y-2, z-5), \\vec{MA} = (x-1, y-2, z-3), nên (x-3, y-2, z-5) = 3(x-1, y-2, z-3)."},
    {"turn": "3", "name": "Tom", "message": "Thành phần x: x-3 = 3(x-1). Thành phần y: y-2 = 3(y-2). Thành phần z: z-5 = 3(z-3)."},
    {"turn": "4", "name": "Charlie", "message": "Từ x-3 = 3x-3 suy ra x - 3x = -3 + 3 ⇒ -2x = 0 ⇒ x = 0."},
    {"turn": "5", "name": "Tom", "message": "Tiếp, y-2 = 3y-6 ⇒ y - 3y = -6 + 2 ⇒ -2y = -4 ⇒ y = 2."},
    {"turn": "6", "name": "Charlie", "message": "Và z-5 = 3z-9 ⇒ z - 3z = -9 + 5 ⇒ -2z = -4 ⇒ z = 2."},
    {"turn": "7", "name": "Tom", "message": "Thế thì M = (0, 2, 2)."},
    {"turn": "8", "name": "Charlie", "message": "OK, coi như xong phần tọa độ rồi."},
    {"turn": "9", "name": "Charlie", "message": "Rồi, vậy |\\vec{OM}| = √(0² + 2² + 2²) = 2√3 luôn."},
    {"turn": "10", "name": "Alice", "message": "Khoan, Charlie: √(0² + 2² + 2²) = √8 = 2√2 chứ không phải 2√3 nhé!"}
],
    },
    {
        "note" : "check_mistake",
        "problem" : PROBLEM_7,
        "solution" : SOLUTION_7,
        "history" : [
    {"turn": "1", "name": "Tom", "message": "Mình đang nghĩ cách tìm khoảng cách giữa hai đường thẳng AA' và BC, mọi người có gợi ý gì không?"},
    {"turn": "2", "name": "Charlie", "message": "Vì AA' ⟂ (ABC), nên AA' ⟂ mọi đường nằm trong mặt phẳng ABC, đặc biệt là AH, nên đoạn AH vuông góc với BC chính là khoảng cách cần tìm."},
    {"turn": "3", "name": "Tom", "message": "Đúng rồi, vậy giờ mình cần tính độ dài AH. Có thể dùng công thức liên quan đến diện tích tam giác ABC."},
    {"turn": "4", "name": "Charlie", "message": "Cụ thể, AH = 2·S_{ABC} / BC. Nên chúng ta sẽ tính diện tích tam giác đầu tiên."},
    {"turn": "5", "name": "Tom", "message": "Cho tam giác với AB=5, BC=6, CA=7, nửa chu vi p = (5+6+7)/2 = 9."},
    {"turn": "6", "name": "Charlie", "message": "Diện tích S = √[9(9-5)(9-6)(9-7)] = √[9·4·3·2] = √216 = 6√6."},
    {"turn": "7", "name": "Tom", "message": "Vậy AH = 2·6√6 / 6 = 2√6."},
    {"turn": "8", "name": "Charlie", "message": "Nghe có vẻ hợp lý rồi, kết quả là 2√6."},
    {"turn": "9", "name": "Charlie", "message": "Khoan, BC bằng 7 chứ không phải 6, nên AH = 2·6√6 / 7 = 12√6/7."},
    {"turn": "10", "name": "Alice", "message": "Chờ chút, BC đúng là 6 trong dữ kiện, còn CA mới là 7, nên công thức ban đầu chính xác: AH = 2√6."}
]
    },
{
        "note" : "check_mistake",
        "problem" : PROBLEM_6,
        "solution" : SOLUTION_6,
        "history" : [
    {"turn": "1", "name": "Tom", "message": "Mọi người, để tính khoảng cách giữa AA' và BC, mình thấy AA' vuông góc với mặt phẳng (ABC), vậy khoảng cách chính là đoạn vuông góc chung AH từ A xuống BC."},
    {"turn": "2", "name": "Charlie", "message": "Đúng rồi, AH là đoạn vuông góc chung giữa hai đường. Theo công thức, AH = (2·S₍ABC₎) / BC."},
    {"turn": "3", "name": "Tom", "message": "Vậy chúng ta cần tính diện tích tam giác ABC trước. Sử dụng công thức Heron nhé."},
    {"turn": "4", "name": "Charlie", "message": "Bán chu vi p = (AB + BC + CA) / 2 = (5 + 6 + 7) / 2 = …?"}, 
    {"turn": "5", "name": "Tom", "message": "5 + 6 + 7 = 18, chia 2 được p = 9."},
    {"turn": "6", "name": "Charlie", "message": "Khi đó S = √[p(p–5)(p–6)(p–7)] = √[9·4·3·2] = √216 = 6√6."},
    {"turn": "7", "name": "Tom", "message": "Ok, vậy AH = 2·6√6 / 6 = 2√6."},
    {"turn": "8", "name": "Charlie", "message": "Mình nghĩ p = 10 vì (5+6+7)/2 = 10, nên S = √[10·5·4·3] = √600 = 10√6 và AH = 2·10√6 / 6 = (10/3)√6."},
    {"turn": "9", "name": "Tom", "message": "Ừ, nếu như vậy thì AH = (10/3)√6 đấy. Nghe có vẻ hợp lý."},
    {"turn": "10", "name": "Alice", "message": "Khoan đã, bạn tính nhầm bán chu vi rồi. Tổng 5+6+7 = 18, chia 2 mới là 9 chứ không phải 10, nên S = 6√6 và AH = 2√6."}
],
    },
    {
        "note" : "check_mistake",
        "problem" : PROBLEM_4,
        "solution" : SOLUTION_4,
        "history" : [
    {"turn": "1", "name": "Tom", "message": "Mình nghĩ chúng ta nên bắt đầu bằng cách khai triển (2x - 1)^6 trước, rồi sau đó nhân với x để tìm hệ số x^5."},
    {"turn": "2", "name": "Charlie", "message": "Đúng rồi. Áp dụng công thức Newton: (a + b)^n = ∑ C_n^k a^k b^{n-k}. Ở đây a = 2x, b = -1, n = 6."},
    {"turn": "3", "name": "Tom", "message": "Vậy để ra x^5 sau khi nhân với x, trong (2x - 1)^6 chúng ta cần hệ số của x^4, tức k = 4."},
    {"turn": "4", "name": "Charlie", "message": "C_6^4 = 15, 2^4 = 16, (-1)^{6-4} = (+1), nên đóng góp của phần đầu là 15 * 16 = 240."},
    {"turn": "5", "name": "Tom", "message": "Chính xác, vậy phần x(2x-1)^6 cho 240 x^5."},
    {"turn": "6", "name": "Charlie", "message": "Tiếp theo phần (3x - 1)^8: a = 3x, b = -1, n = 8. Chúng ta tìm k = 5 để lấy x^5."},
    {"turn": "7", "name": "Tom", "message": "Hệ số x^5 là C_8^5 * 3^5 * (-1)^{8-5}."},
    {"turn": "8", "name": "Charlie", "message": "C_8^5 = 56, 3^5 = 243, (-1)^3 = -1, nên kết quả là -56 * 243 = -13600."},
    {"turn": "9", "name": "Tom", "message": "Ừ, mình đồng ý, vậy đóng góp từ (3x-1)^8 là -13600."},
    {"turn": "10", "name": "Alice", "message": "Mình thấy Charlie nhầm: -56 * 243 thực ra là -13608, không phải -13600."}
],
    },
    {
        "note" : "check_mistake",
        "problem" : PROBLEM_5,
        "solution" : SOLUTION_5,
        "history" : [
    {"turn": "1", "name": "Tom", "message": "Bài này phức tạp thế nhỉ? Hệ số của $x^5$ trong cái khai triển nhị thức này... Bắt đầu từ đâu bây giờ?"},
    {"turn": "2", "name": "Charlie", "message": "Chắc là phải tách làm hai phần rồi tính hệ số $x^5$ cho từng cái: $x(2x-1)^6$ và $(3x-1)^8$."},
    {"turn": "3", "name": "Tom", "message": "Đúng rồi. Thế cái phần đầu $x(2x-1)^6$ trước đi. $(2x-1)^6$ thì dùng nhị thức Newton. Tổng quát là $C_6^k (2x)^k (-1)^{6-k}$."},
    {"turn": "4", "name": "Charlie", "message": "Ừm. Mà ở ngoài nó nhân thêm với $x$. Nên mình cần tìm hệ số của $x^4$ trong cái khai triển $(2x-1)^6)$ đó, xong nhân với $x$ là ra $x^5$."},
    {"turn": "5", "name": "Tom", "message": "Ok, hiểu rồi. Hệ số của $x^4$ trong $(2x-1)^6$ là ứng với $k=4$ trong công thức tổng quát kia. Tức là $C_6^4 (2)^4 (-1)^{6-4}$."},
    {"turn": "6", "name": "Charlie", "message": "Chuẩn rồi. Cái đó tính ra bao nhiêu nhỉ? $C_6^4 = C_6^2 = \frac{6 \times 5}{2} = 15$. $(2)^4 = 16$. $(-1)^2 = 1$. Vậy phần đầu đóng góp $15 \times 16 \times 1 = 240$ cho hệ số $x^5$."},
    {"turn": "7", "name": "Tom", "message": "Được 240 rồi. Giờ đến phần sau $(3x-1)^8$."},
    {"turn": "8", "name": "Charlie", "message": "Phần $(3x-1)^8$ thì khai triển là $\sum_{l=0}^8 C_8^l (3x)^l (-1)^{8-l}$. Tương tự, mình cần tìm hệ số của $x^4$ trong khai triển này."},
    {"turn": "9", "name": "Tom", "message": "À ờ, cũng tìm hệ số $x^4$ trong cái này à? Thế thì ứng với $l=4$. Là $C_8^4 (3)^4 (-1)^{8-4}$."},
    {"turn": "10", "name": "Alice", "message": "Khoan đã, hình như nhầm rồi Charlie ơi. Ở cái $(3x-1)^8$, mình cần tìm hệ số của $x^5$ chứ, đâu phải $x^4$?"}
],
    },
    {
        "note" : "check_mistake",
        "problem" : PROBLEM_3,
        "solution" : SOLUTION_3,
        "history" : [
    {"turn": "1", "name": "Tom", "message": "Mình đọc đề: tìm hệ số của x^5 trong biểu thức x(2x-1)^6 + (3x-1)^8, bắt đầu nhé."},
    {"turn": "2", "name": "Charlie", "message": "Ok, trước tiên áp dụng khai triển nhị thức Newton cho (2x-1)^6."},
    {"turn": "3", "name": "Tom", "message": "Công thức là (2x-1)^6 = ∑ₖ₌₀⁶ C₆ᵏ·(2x)ᵏ·(-1)^(6-k)."},
    {"turn": "4", "name": "Charlie", "message": "Để lấy x^5 sau khi nhân với x ở ngoài, ta cần lấy x^4 từ (2x-1)^6, tức k=4."},
    {"turn": "5", "name": "Tom", "message": "Vậy hệ số x^4 là C₆⁴·2⁴·(-1)² = 15·16·1 = 240, nhân với x ngoài ra được 240·x^5."},
    {"turn": "6", "name": "Charlie", "message": "Tiếp theo phần (3x-1)^8: để lấy x^5 thì l=5, hệ số là C₈⁵·3⁵·(-1)^(8-5) = 56·243·(-1)³ = -13608."},
    {"turn": "7", "name": "Tom", "message": "Vậy tạm thời tổng hai phần cho x^5 là 240 + (−13608) = −13368."},
    {"turn": "8", "name": "Charlie", "message": "Khoan, mình nghĩ phần x·(2x-1)^6 để cho x^5 thì k phải là 5 chứ không phải 4."},
    {"turn": "9", "name": "Tom", "message": "Ừ đúng, nếu k=5 thì hệ số x^5 là C₆⁵·2⁵·(-1)^(6-5) = 6·32·(-1) = -192."},
    {"turn": "10", "name": "Alice", "message": "Mọi người ơi, k ở đây phải là 4 mới đúng, vì k=5 cho x^6 rồi nhân với x thành x^7, không phải x^5."}
],
    },
    {
        "note" : "check_mistake",
        "problem" : PROBLEM_1,
        "solution" : SOLUTION_1,
        "history" : [
    {"turn": "1", "name": "Tom", "message": "Làm bài thui."},
    {"turn": "2", "name": "Charlie", "message": "OKOK"},
    {"turn": "3", "name": "Tom", "message": "Ta cần tính đạo hàm: f'(x) = [(1)(x+1) - (x-1)(1)]/(x+1)^2 = 2/(x+1)^2."},
    {"turn": "4", "name": "Charlie", "message": "Vì (x+1)^2 luôn dương khi x ≠ -1, nên f'(x) > 0 với mọi x trong D."},
    {"turn": "5", "name": "Tom", "message": "Vậy hàm đồng biến trên các khoảng mà hàm xác định, tức là (-∞, -1) và (-1, ∞)."},
    {"turn": "6", "name": "Charlie", "message": "Chuẩn rồi. Giờ xét giới hạn: khi x → ±∞, f(x) → 1."},
    {"turn": "7", "name": "Tom", "message": "Và khi x → -1^+ thì f(x) → -∞, còn x → -1^- thì f(x) → +∞."},
    {"turn": "8", "name": "Charlie", "message": "Như vậy chỉ cần f'(x) > 0 thì hàm đồng biến trên ℝ, kết luận f đồng biến trên toàn R luôn."},
    {"turn": "9", "name": "Tom", "message": "Ừ, mình cũng thấy vậy, hàm đồng biến trên R."},
    {"turn": "10", "name": "Alice", "message": "Khoan đã, hàm không xác định tại x = -1, nên chỉ có thể nói f đồng biến trên hai khoảng (-∞, -1) và (-1, ∞), không phải toàn R."}
]
    },

{
        "note" : "check_mistake",
        "problem" : PROBLEM_1,
        "solution" : SOLUTION_1,
        "history" : [
    {"turn": "1", "name": "Tom", "message": "Mình bắt đầu với việc xác định tập xác định của f(x) = (x-1)/(x+1) nhé. Điều kiện gì để hàm xác định?"},
    {"turn": "2", "name": "Charlie", "message": "Hàm xác định khi mẫu số khác 0, tức x + 1 ≠ 0 → x ≠ -1. Vậy D = ℝ \\ {-1}."},
    {"turn": "3", "name": "Tom", "message": "Tiếp theo, mình tính đạo hàm: f'(x) = [(1)·(x+1) - (x-1)·(1)]/(x+1)^2."},
    {"turn": "4", "name": "Charlie", "message": "Thành tử trên là x + 1 - x + 1 = 2, nên f'(x) = 2/(x+1)^2."},
    {"turn": "5", "name": "Tom", "message": "Chính xác. Vì (x+1)^2 luôn dương với mọi x ≠ -1, nên f'(x) > 0 ∀ x ≠ -1."},
    {"turn": "6", "name": "Charlie", "message": "Ừ, theo mình thấy thì nếu x > -1 thì x+1 dương, còn nếu x < -1 thì x+1 âm, nên f'(x) sẽ đổi dấu. Vậy hàm đồng biến trên (-1; +∞) và nghịch biến trên (-∞; -1)."},
    {"turn": "7", "name": "Tom", "message": "Ừ, đúng rồi. Vậy tạm thời chúng ta kết luận như vậy. Bây giờ xem xét giới hạn tại x → ±∞."},
    {"turn": "8", "name": "Charlie", "message": "Được. Giới hạn khi x → +∞ f(x) → 1, khi x → -∞ cũng về 1. Còn quanh x = -1 thì phía bên phải → -∞, phía bên trái → +∞, vậy bảng biến thiên..."},
    {"turn": "9", "name": "Tom", "message": "Mình tóm lại: hàm số nghịch biến trên (-∞; -1) và đồng biến trên (-1; +∞)."},
    {"turn": "10", "name": "Alice", "message": "Mình có góp ý: chỗ tính dấu f'(x) của Charlie có vấn đề. Vì mẫu (x+1)^2 luôn dương nên f'(x) = 2/(x+1)^2 > 0 với mọi x ≠ -1, hàm số thực ra đồng biến trên cả hai khoảng (-∞; -1) và (-1; +∞), không có khoảng nghịch biến nhé."}
],
    },
    {
        "note" : "check_mistake",
        "problem" : PROBLEM_4,
        "solution" : SOLUTION_4,
        "history" : [
    {"turn": "1", "name": "Tom", "message": "Chào cả nhà, bài toán này: hộp có 11 quả cầu đỏ và 4 quả cầu xanh, rút ngẫu nhiên 3 quả, tính xác suất để lấy được 3 quả cầu xanh."},
    {"turn": "2", "name": "Charlie", "message": "Ờ, trước hết tính tổng số cách rút 3 quả từ 15 quả, n(Ω) = C(15,3) = 455."},
    {"turn": "3", "name": "Tom", "message": "OK. Kế đến biến cố A là lấy được 3 quả xanh, nên n(A) = C(4,3)."},
    {"turn": "4", "name": "Charlie", "message": "Đúng. Giờ mình tính C(4,3) nhé."},
    {"turn": "5", "name": "Tom", "message": "Công thức chung C(n,k)=n!/(k!(n-k)!), thế nên C(4,3)=4!/(3!*1!) = ?"},
    {"turn": "6", "name": "Charlie", "message": "Tớ tính được 12. Chắc là chọn 3 từ 4 thì 12 cách."},
    {"turn": "7", "name": "Tom", "message": "Vậy P(A) = 12/455 ≈ 0.0264."},
    {"turn": "8", "name": "Charlie", "message": "Khoảng tầm 2.64% luôn."},
    {"turn": "9", "name": "Tom", "message": "Ổn rồi, vậy mình làm xong rồi chứ? Có ai có ý kiến gì không?"},
    {"turn": "10", "name": "Alice", "message": "Này mọi người, tớ thấy C(4,3) bị nhầm rồi. Thực ra C(4,3) = 4 chứ không phải 12. Do 4!/(3!1!) = 4. Nên xác suất đúng phải là 4/455 ≈ 0.0088 (~0.88%)."}
],
    },
    {
        "note" : "check_mistake",
        "problem" : PROBLEM_10,
        "solution" : SOLUTION_10,
        "history" : [
    {"turn": "1", "name": "Tom", "message": "Đầu tiên ghi lại hai phương trình: (a-3)² + (b-1)² + c² = 9 và (a-3)² + (b-6)² + (c-6)² = 36. Nên trừ PT1 khỏi PT2 để loại (a-3)²."},
    {"turn": "2", "name": "Charlie", "message": "OK, vậy ta có: (b-6)² - (b-1)² + (c-6)² - c² = 36 - 9 = 27."},
    {"turn": "3", "name": "Tom", "message": "Tương tự: (b-6)² = b² - 12b + 36, (b-1)² = b² - 2b + 1, hiệu là -10b + 35."},
    {"turn": "4", "name": "Charlie", "message": "Tương tự, (c-6)² - c² = -12c + 36."},
    {"turn": "5", "name": "Tom", "message": "Cộng lại: -10b + 35 - 12c + 36 = -10b - 12c + 71. Đặt bằng 27: -10b - 12c + 71 = 27, nên -10b - 12c = 27 - 71 = -44."},
    {"turn": "6", "name": "Charlie", "message": "27 - 71 = -43, vậy -10b - 12c = -43, chia -1: 10b + 12c = 43, chia 2: 5b + 6c = 21.5."},
    {"turn": "7", "name": "Tom", "message": "Ừ, vậy b và c phải thỏa mãn 5b + 6c = 21.5."},
    {"turn": "8", "name": "Charlie", "message": "Từ đó ta biểu diễn b theo c: b = (21.5 - 6c) / 5."},
    {"turn": "9", "name": "Bob", "message": "Nghe có vẻ hợp lý, khi thay vào phương trình khác sẽ giải được c rồi b."},
    {"turn": "10", "name": "Alice", "message": "Mình thấy ở bước tính 27 - 71 không đúng, thực ra là 27 - 71 = -44, nên phương trình đúng phải là 5b + 6c = 22 chứ không phải 21.5."}
],
    },
    {
        "note" : "check_mistake",
        "problem" : PROBLEM_10,
        "solution" : SOLUTION_10,
        "history" : [
    {"turn": "1", "name": "Tom", "message": "Mình xem lại cách thiết lập hệ phương trình từ khoảng cách. Theo đề, có các phương trình: (a-3)^2+(b-1)^2+c^2=9, (a-3)^2+(b-6)^2+(c-6)^2=36, (a-4)^2+(b-6)^2+(c-2)^2=25, (a-6)^2+(b-2)^2+(c-14)^2=169."},
    {"turn": "2", "name": "Charlie", "message": "Đúng rồi. Trước hết chúng ta trừ phương trình 1 và 2 để loại a^2+b^2+c^2."},
    {"turn": "3", "name": "Tom", "message": "Em tính sao? Phương trình 1 là MA, phương trình 2 là MB, cùng chia đều bình phương rồi trừ."},
    {"turn": "4", "name": "Charlie", "message": "Mình có (b-6)^2-(b-1)^2 + (c-6)^2 - c^2 = 36-9 = 27, tính ra -10b -12c +71 = 27 ⇒ -10b -12c = -44."},
    {"turn": "5", "name": "Tom", "message": "Rất tốt. Tương tự trừ phương trình 1 với 3 để thu được phương trình tuyến tính thứ hai."},
    {"turn": "6", "name": "Charlie", "message": "Ừ, và giao tuyến của hai mặt cầu này sẽ là một elip, nên mình phải coi nó như phương trình elip rồi giải tiếp."},
    {"turn": "7", "name": "Tom", "message": "Ừ, được đó. Giờ ta có hai phương trình tuyến tính rồi, giải nó cùng nhau để tìm b và c."},
    {"turn": "8", "name": "Charlie", "message": "Mình giải hệ và được b = 2, c = 2."},
    {"turn": "9", "name": "Bob", "message": "Mình thấy ổn. Tiếp theo thay vào (a-3)^2+(b-1)^2+c^2=9 thì a = 1."},
    {"turn": "10", "name": "Alice", "message": "Mình có góp ý: giao tuyến của hai mặt cầu luôn là một đường tròn chứ không phải elip nhé các bạn."}
],
    },
    {
        "note" : "check_mistake",
        "problem" : PROBLEM_6,
        "solution" : SOLUTION_6,
        "history" : [
    {"turn" : "1", "name" : "Tom", "message" : "Này nhóm, chúng ta có bài lăng trụ đứng ABC.A'B'C' với AB = 5, BC = 6, CA = 7. Hỏi khoảng cách từ AA' đến BC bằng bao nhiêu nhỉ?"},
    {"turn" : "2", "name" : "Charlie", "message" : "Vì hình lăng trụ đứng, AA' ⟂ (ABC). Điều này nghĩa AA' vuông góc với mọi đường thẳng trong mặt phẳng ABC tại A."},
    {"turn" : "3", "name" : "Tom", "message" : "Để tìm khoảng cách giữa hai đường thẳng chéo nhau AA' và BC, ta kẻ AH ⟂ BC, với H là hình chiếu của A lên BC. AH chính là đoạn vuông góc chung."},
    {"turn" : "4", "name" : "Charlie", "message" : "Chính xác. Giờ ta chỉ cần tính AH trong tam giác ABC thôi."},
    {"turn" : "5", "name" : "Tom", "message" : "Tam giác ABC có nửa chu vi p = (5 + 6 + 7)/2 = 9. Diện tích S = √[9·4·3·2] = √216 = 6√6."},
    {"turn" : "6", "name" : "Charlie", "message" : "Hay, như vậy AA' vuông góc với BC (vì AA' ⟂ (ABC)), nên khoảng cách chính là AA'. Và AA' = AH."},
    {"turn" : "7", "name" : "Tom", "message" : "Vậy AH = 2S/BC = 2·6√6/6 = 2√6. Nên AA' = 2√6."},
    {"turn" : "8", "name" : "Charlie", "message" : "Vậy kết quả là 2√6."},
    {"turn" : "9", "name" : "Bob", "message" : "Mình thấy cách làm của các bạn hợp lý, kết quả 2√6 nghe ổn."},
    {"turn" : "10", "name" : "Alice", "message" : "Mình muốn góp ý: Charlie nói AA' vuông góc với BC vì AA' ⟂ (ABC) thì hơi vội. Một đường thẳng vuông góc với một mặt phẳng chỉ chắc chắn vuông góc với các đường thẳng trong mặt phẳng đi qua giao điểm. BC không đi qua A, nên AA' không vuông góc với BC. Đoạn vuông góc chung ở đây vẫn là AH, không phải toàn bộ AA'."}
],
    },
    {
        "note" : "check_mistake",
        "problem" : PROBLEM_6,
        "solution" : SOLUTION_6,
        "history" : [
    {"turn": "1", "name": "Tom", "message": "Mọi người ơi, bài này cho khối chóp đáy hình vuông cạnh a và chiều cao 2a, đầu tiên mình tính diện tích đáy nhé."},
    {"turn": "2", "name": "Charlie", "message": "Diện tích đáy B = a² chứ hả Tom?"},
    {"turn": "3", "name": "Tom", "message": "Chính xác. Tiếp theo công thức thể tích V = 1/3 · B · h."},
    {"turn": "4", "name": "Charlie", "message": "Vậy ta thay B = a² và h = 2a."},
    {"turn": "5", "name": "Tom", "message": "Thế là V = 1/3 · a² · 2a. Cậu thử rút gọn xem."},
    {"turn": "6", "name": "Charlie", "message": "Rút gọn thì V = 1/3 · a² · a = 1/3 a³."},
    {"turn": "7", "name": "Tom", "message": "Ừ, vậy đáp án là V = 1/3 a³ hả?"},  
    {"turn": "8", "name": "Charlie", "message": "Ừ, tớ nghĩ vậy là đúng rồi."},
    {"turn": "9", "name": "Bob", "message": "Uh đúng vậy."},
    {"turn": "10", "name": "Alice", "message": "Mọi người ơi, tớ thấy các bạn rút gọn sai rồi: V = 1/3 · a² · 2a phải ra 2/3 a³ chứ không phải 1/3 a³."}
]
    },

]
}



################################
########### TASK 2 #############
################################
dataset_task2 = {
    "type" : "task_2",
    "data" : [
        {
            "note" : "self_correction",
            "problem" : PROBLEM_2,
            "solution" : SOLUTION_2,
            "history" : [
    {"turn": "1", "name": "Bob", "message": "Mọi người ơi, hôm nay chúng ta thảo luận công thức tính thể tích khối chóp có đáy hình vuông cạnh a và chiều cao bằng 2a nhé."},
    {"turn": "2", "name": "Alice", "message": "Đầu tiên ta cần xác định diện tích đáy B của khối chóp. Đáy là hình vuông cạnh a, vậy B = a²."},
    {"turn": "3", "name": "Charlie", "message": "Đúng rồi, B = a². Tiếp theo chúng ta sẽ áp dụng công thức chung để tính thể tích."},
    {"turn": "4", "name": "Tom", "message": "Công thức tính thể tích khối chóp bất kỳ là V = 1/3 × diện tích đáy × chiều cao, tức V = 1/3 · B · h."},
    {"turn": "5", "name": "Alice", "message": "Phần 1/3 ở đây xuất phát từ việc khối chóp chỉ chiếm một phần ba thể tích so với khối lăng trụ cùng đáy và cùng chiều cao."},
    {"turn": "6", "name": "Bob", "message": "Ví dụ nếu a = 2 thì B = 4, h = 4, thế thì V = 1/3 × 4 × 4 = 16/3."},
    {"turn": "7", "name": "Charlie", "message": "Ừ, như vậy với h = 2a thì h = 2a, B = a², áp dụng công thức V = 1/3 · a² · 2a..."},    
    {"turn": "8", "name": "Charlie", "message": "Theo mình là V = 1/2 × a² × 2a = a³."},
    {"turn": "9", "name": "Tom", "message": "Chờ đã, Charlie nhầm rồi. Công thức khối chóp phải là 1/3 chứ không phải 1/2."},
    {"turn": "10", "name": "Charlie", "message": "À đúng, tớ quên mất hệ số 1/3. Vậy kết quả đúng là V = 2/3 a³. Cảm ơn Tom nhé!"}
],
        },
        {
            "note" : "self_correction",
            "problem" : PROBLEM_2,
            "solution" : SOLUTION_2,
            "history" : [
    {"turn": "1", "name": "Bob", "message": "Mình muốn các bạn hiểu rõ vì sao hệ số 1/3 xuất hiện, hãy dùng slicing để tính thể tích nhé."},
    {"turn": "2", "name": "Alice", "message": "OK, đặt đáy hình vuông nằm tại y=0, đỉnh chóp tại y=h=2a."},
    {"turn": "3", "name": "Tom", "message": "Mỗi mặt cắt ngang song song đáy tại độ cao y là hình vuông cạnh a·(1−y/h)."},
    {"turn": "4", "name": "Charlie", "message": "Thế nên diện tích mặt cắt A(y) = [a(1−y/h)]² = a²(1−y/h)²."},
    {"turn": "5", "name": "Bob", "message": "Thể tích V = ∫₀ʰ A(y) dy = a² ∫₀ʰ (1−y/h)² dy."},
    {"turn": "6", "name": "Alice", "message": "Đổi biến u = y/h ⇒ dy = h du, giới hạn u từ 0 đến 1, được V = a²·h ∫₀¹ (1−u)² du."},
    {"turn": "7", "name": "Bob", "message": "Ta mở rộng (1−u)² = 1−2u+u², tích phân ∫₀¹ (1−u)² du = [u−u²+u³/3]₀¹ = 1/3, nên V = (1/3)a²h = 2/3 a³."},
    {"turn": "8", "name": "Charlie", "message": "Mình tính ∫₀¹ (1−u)² du thành [u−u²+u³/2]₀¹ = 1/2, nên V = (1/2)a²h = a³."},
    {"turn": "9", "name": "Tom", "message": "Charlie ơi, bạn nhầm rồi: tích phân của u² phải là u³/3 chứ không phải u³/2."},
    {"turn": "10", "name": "Charlie", "message": "À, tớ hiểu rồi, tớ sai ở chỗ quy tắc tính ∫u². Kết quả đúng là V = 2/3 a³. Cảm ơn mọi người!"}
],
        },
        {
            "note" : "self_correction",
            "problem" : PROBLEM_3,
            "solution" : SOLUTION_3,
            "history" : [
    {"turn": "1", "name": "Bob", "message": "Mình mới đọc đề: có 11 quả đỏ, 4 quả xanh, lấy ngẫu nhiên 3 quả. Bước đầu mình nghĩ là tính số phần tử của không gian mẫu, mọi người thấy sao?"},
    {"turn": "2", "name": "Alice", "message": "Đúng rồi, tổng có 15 quả, chọn 3 nên n(Ω) = C(15,3) = 455."},
    {"turn": "3", "name": "Charlie", "message": "Vậy biến cố A là lấy được 3 quả xanh, số phần tử A là C(4,3) phải không?"},
    {"turn": "4", "name": "Bob", "message": "Chính xác, có 4 quả xanh, chọn 3 nên C(4,3) = 4."},
    {"turn": "5", "name": "Alice", "message": "Xác suất P(A) = n(A)/n(Ω) = 4/455."},
    {"turn": "6", "name": "Tom", "message": "Mọi người còn nhớ công thức tổng quát của tổ hợp C(n,k) không?"},
    {"turn": "7", "name": "Bob", "message": "Công thức là C(n,k) = n! / (k! * (n-k)!)."},
    {"turn": "8", "name": "Charlie", "message": "Vậy C(4,3) = 4! / (4-3)! = 24 chứ nhỉ?"},
    {"turn": "9", "name": "Tom", "message": "Chú ý Charlie: mẫu phải có k! nữa, công thức đầy đủ là 4! / (3! * 1!) = 4, không phải 24."},
    {"turn": "10", "name": "Charlie", "message": "À đúng rồi, mình quên k! ở mẫu. C(4,3) là 4. Cảm ơn Tom đã nhắc nhé!"}
],
        },
        {
            "note" : "self_correction",
            "problem" : PROBLEM_4,
            "solution" : SOLUTION_4,
            "history" : [
    {"turn": "1", "name": "Alice", "message": "Mình thấy bài này: tìm giá trị lớn nhất của hàm số y = x^4 - 4x^2 + 9 trên đoạn [-2;3]. Mọi người nghĩ bước đầu ta cần làm gì?"},
    {"turn": "2", "name": "Bob", "message": "Trước hết ta phải khảo sát tính liên tục và khả vi, rồi tìm đạo hàm y' để xác định các điểm cực trị."},
    {"turn": "3", "name": "Charlie", "message": "Hàm số đa thức nên liên tục và khả vi trên R. Ta có y' = 4x^3 - 8x."},
    {"turn": "4", "name": "Tom", "message": "Đặt y' = 0 ⇔ 4x(x^2 - 2) = 0, suy ra x = 0 và x = ±√2."},
    {"turn": "5", "name": "Alice", "message": "Tiếp theo ta tính f tại các điểm x = -2, 0, ±√2 và x = 3 để so sánh."},
    {"turn": "6", "name": "Bob", "message": "Ok, f(0) = 0^4 - 4·0^2 + 9 = 9, còn f(3) = 3^4 - 4·3^2 + 9 = 81 - 36 + 9 = 54."},
    {"turn": "7", "name": "Charlie", "message": "Mình tính f(-2) = (-2)^4 - 4·(-2)^2 + 9 = 16 - 16 - 9 = -9, còn f(±√2) = (√2)^4 - 4·(√2)^2 + 9 = 4 - 8 + 9 = 5."},
    {"turn": "8", "name": "Bob", "message": "Ừ, mình đồng ý với kết quả đó, chúng mình làm tiếp thôi."},
    {"turn": "9", "name": "Tom", "message": "Không phải vậy, f(-2) = 16 - 16 + 9 = 9 chứ không phải -9, Charlie nhầm dấu ở phần +9."},
    {"turn": "10", "name": "Charlie", "message": "Ôi, đúng rồi, mình nhầm dấu. Phải là f(-2) = 9. Cảm ơn Tom đã sửa giúp!"}
],
        },
        {
            "note" : "self_correction",
            "problem" : PROBLEM_4,
            "solution" : SOLUTION_4,
            "history" : [
    {"turn": "1", "name": "Alice", "message": "Mọi người, bước đầu tiên mình tính đạo hàm của hàm số y = x^4 - 4x^2 + 9 như nào nhỉ?"},
    {"turn": "2", "name": "Bob", "message": "Theo mình y' = 4x^3 - 8x, rồi có thể viết gọn thành y' = 4x(x^2 - 2)."},
    {"turn": "3", "name": "Charlie", "message": "Vậy giải 4x(x^2 - 2) = 0 thì x = 0 và x^2 = 2, nên x = ±√2, tất cả đều nằm trong [-2, 3]."},
    {"turn": "4", "name": "Tom", "message": "Vậy các điểm cần xét là x = -2, -√2, 0, √2 và 3."},
    {"turn": "5", "name": "Alice", "message": "Mình đã tính f(-2) = (-2)^4 - 4·(-2)^2 + 9 = 16 - 16 + 9 = 9."},
    {"turn": "6", "name": "Bob", "message": "Mình tính tiếp f(0) = 9, và f(3) = 3^4 - 4·3^2 + 9 = 81 - 36 + 9 = 54."},
    {"turn": "7", "name": "Charlie", "message": "Còn f(√2) = (√2)^4 - 4·(√2)^2 + 9 = 4 - 8 + 11 = 7."},
    {"turn": "8", "name": "Bob", "message": "Ừ, f(√2) = 7 đấy, vậy điểm nhỏ nhất là 7 và lớn nhất là 54."},
    {"turn": "9", "name": "Tom", "message": "Khoan đã, kiểm tra lại f(√2) nhé: thực ra là 4 - 8 + 9 = 5 chứ không phải 7."},
    {"turn": "10", "name": "Charlie", "message": "Á, mình cộng nhầm rồi! Đúng là f(√2) = 5. Cảm ơn mọi người đã sửa giúp."}
],
        },
        {
            "note" : "self_correction",
            "problem" : PROBLEM_6,
            "solution" : SOLUTION_6,
            "history" : [
    {"turn": "1", "name": "Alice", "message": "Mọi người, chúng ta cần tìm hệ số của x^5 trong biểu thức x(2x-1)^6 + (3x-1)^8. Mình đề xuất bắt đầu với phần x(2x-1)^6."},
    {"turn": "2", "name": "Bob", "message": "Ừ, vậy ta coi (2x-1)^6 rồi nhân thêm x. Khi khai triển, (2x-1)^6 = Σ C(6,k)*(2x)^k*(-1)^{6-k}."},
    {"turn": "3", "name": "Charlie", "message": "Để ra x^5 sau khi nhân thêm x thì phải chọn k sao cho k+1 = 5, tức là k = 4."},
    {"turn": "4", "name": "Tom", "message": "Chính xác. Vậy hệ số là C(6,4)*2^4 * (-1)^{6-4}, và (-1)^{2} = +1."},
    {"turn": "5", "name": "Alice", "message": "Thế thì C(6,4)=15, 2^4=16, nhân lại là 15*16*1 = 240 cho phần đầu."},
    {"turn": "6", "name": "Bob", "message": "Mình cũng tính ra 240. Rõ ràng hệ số của x^5 từ x(2x-1)^6 là +240."},
    {"turn": "7", "name": "Charlie", "message": "Mình thấy (-1)^2 = -1, nên cho rằng hệ số là -240."},
    {"turn": "8", "name": "Bob", "message": "Ừ, tạm thời ghi nhận -240 rồi chuyển sang phần (3x-1)^8 nhé."},
    {"turn": "9", "name": "Tom", "message": "Khoan đã, (-1)^2 = +1 chứ? Vì (-1)*(-1)=+1. Nên hệ số phải là +240 mới đúng."},
    {"turn": "10", "name": "Charlie", "message": "À, đúng rồi, mình nhầm dấu. Vậy hệ số đúng là +240, cảm ơn mọi người đã nhắc."}
],
        },
        {
            "note" : "self_correction",
            "problem" : PROBLEM_6,
            "solution" : SOLUTION_6,
            "history" : [
    {"turn": "1", "name": "Alice", "message": "Mọi người, phần đầu của bài là tính hệ số x⁵ từ x·(2x−1)⁶."},
    {"turn": "2", "name": "Bob", "message": "Ừ, ta viết (2x−1)⁶ = Σₖ C(6,k)·(2x)ᵏ·(−1)^{6−k}, rồi nhân thêm x."},
    {"turn": "3", "name": "Tom", "message": "Để được x⁵ sau khi nhân với x, trong (2x)ᵏ phải cho k thỏa k+1=5, tức k=4."},
    {"turn": "4", "name": "Alice", "message": "C(6,4)=15, 2⁴=16, và (−1)²=+1, nên hệ số là 15·16·1 = 240."},
    {"turn": "5", "name": "Bob", "message": "Mình cũng vừa tính ra 240 cho phần này."},
    {"turn": "6", "name": "Alice", "message": "OK, vậy ghi nhớ hệ số x⁵ từ x(2x−1)⁶ là +240."},
    {"turn": "7", "name": "Charlie", "message": "Mình thấy số mũ phải là k+2=5, tức k=3 mới đúng, nên hệ số phải là C(6,3)·2³·(−1)³ = 20·8·(−1) = −160."},
    {"turn": "8", "name": "Bob", "message": "Ừ, mình cũng thấy k+2 hợp lý hơn, nên tạm tính −160 cho phần đầu."},
    {"turn": "9", "name": "Tom", "message": "Khoan đã, phải là k+1=5 chứ không phải k+2. Vì ta nhân (2x)ᵏ với x, tổng mũ là k+1. Vậy k=4, không phải 3."},
    {"turn": "10", "name": "Charlie", "message": "À, đúng rồi, mình nhầm áp dụng số mũ. Nên k=4, và hệ số vẫn là +240. Cảm ơn mọi người!"}
],
        },
        {
            "note" : "self_correction",
            "problem" : PROBLEM_6,
            "solution" : SOLUTION_6,
            "history" : [
    {"turn": "1", "name": "Alice", "message": "Mọi người, giờ đến phần khai triển (3x−1)^8 để tìm hệ số x^5."},
    {"turn": "2", "name": "Bob", "message": "Ta có (3x−1)^8 = Σ_{l=0}^8 C(8,l)·(3x)^l·(−1)^{8−l}."},
    {"turn": "3", "name": "Tom", "message": "Đúng, để sinh x^5 thì l = 5."},
    {"turn": "4", "name": "Alice", "message": "C(8,5) = 56."},
    {"turn": "5", "name": "Bob", "message": "3^5 = 243."},
    {"turn": "6", "name": "Alice", "message": "Dấu của hạng tử là (−1)^{8−5} = (−1)^3 = −1. Vậy hệ số là −56·243 = −13608."},
    {"turn": "7", "name": "Charlie", "message": "Mình nghĩ C(8,5) = 48, nên tính ra −48·243 = −11664."},
    {"turn": "8", "name": "Bob", "message": "Ừ, −11664 nghe hợp lý, mình lưu kết quả này."},
    {"turn": "9", "name": "Tom", "message": "Chờ đã, thực ra C(8,5) là 56 chứ không phải 48. Kết quả phải là −56·243 = −13608."},
    {"turn": "10", "name": "Charlie", "message": "À, mình nhớ nhầm tổ hợp. Cảm ơn mọi người, kết quả đúng là −13608."}
],
        },
        {
            "note" : "self_correction",
            "problem" : PROBLEM_6,
            "solution" : SOLUTION_6,
            "history" : [
    {"turn": "1", "name": "Alice", "message": "Mọi người, bây giờ ta tính tiếp phần khai triển (3x−1)^8 để lấy hệ số x^5."},
    {"turn": "2", "name": "Bob", "message": "Công thức chung là (3x−1)^8 = Σ_{l=0}^8 C(8,l)·(3x)^l·(−1)^{8−l}."},
    {"turn": "3", "name": "Tom", "message": "Để ra x^5 thì l = 5."},
    {"turn": "4", "name": "Alice", "message": "C(8,5) = 56."},
    {"turn": "5", "name": "Bob", "message": "3^5 = 243."},
    {"turn": "6", "name": "Alice", "message": "Dấu của hạng tử là (−1)^{8−5} = (−1)^3 = −1. Vậy hệ số là −56·243 = −13608."},
    {"turn": "7", "name": "Charlie", "message": "Theo mình công thức tổng quát phải dùng C(n, l−1), nên ở đây là C(8,4)=70, thành ra hệ số là −70·243 = −17010."},
    {"turn": "8", "name": "Bob", "message": "Ừ, nghe có lý, mình cũng ghi −17010 cho phần này."},
    {"turn": "9", "name": "Tom", "message": "Khoan, công thức chuẩn là C(n, l) chứ không phải C(n, l−1). Nên phải dùng C(8,5)=56 mới đúng."},
    {"turn": "10", "name": "Charlie", "message": "À, mình nhớ nhầm lý thuyết rồi. Đúng phải là C(8,5). Vậy hệ số vẫn là −13608, cảm ơn mn!"}
],
        },
        {
            "note" : "self_affirmation",
            "problem" : PROBLEM_7,
            "solution" : SOLUTION_7,
            "history" : [
  {"turn": "1", "name": "Bob", "message": "Mình đang phân vân là khoảng cách giữa hai đường thẳng AA' và BC được xác định như thế nào nhỉ?"},
  {"turn": "2", "name": "Alice", "message": "Theo mình, vì AA' vuông góc với mặt phẳng (ABC), nên nó vuông góc với mọi đường thẳng trong mặt phẳng đó, bao gồm cả BC."},
  {"turn": "3", "name": "Charlie", "message": "Đúng rồi. Khi hai đường chéo trong không gian không cắt nhau, ta phải kẻ đoạn vuông góc chung để tìm khoảng cách ngắn nhất."},
  {"turn": "4", "name": "Alice", "message": "Đoạn vuông góc chung chính là đoạn nối giữa hai đường sao cho nó vuông góc với cả hai, nên sẽ là khoảng cách cần tìm."},
  {"turn": "5", "name": "Bob", "message": "Vậy trong bài này, chúng ta hạ từ A xuống BC, gọi H là hình chiếu của A trên BC, thì AH ⟂ BC. Lại có AA' ⟂ mặt (ABC) nên AA' ⟂ AH. Như vậy AH chính là đoạn vuông góc chung."},
  {"turn": "6", "name": "Tom", "message": "Mình nắm được rồi. Kết luận AH là khoảng cách giữa AA' và BC. Tiếp theo là tính AH bằng công thức AH = 2S_ABC / BC."},
  {"turn": "7", "name": "Alice", "message": "Ừ, trong tam giác ABC, p = (5+6+7)/2 = 9, S = √(9·4·3·2) = 6√6, BC = 6, nên AH = (2·6√6)/6 = 2√6."},
  {"turn": "8", "name": "Charlie", "message": "Không cần bận tâm thêm bước chứng minh AA' ⟂ AH nữa, vì AA' ⟂ mặt (ABC) thì tự động vuông góc với mọi đoạn nằm trong mặt phẳng đó như AH."},
  {"turn": "9", "name": "Tom", "message": "Mình thấy không ổn. Mình cho rằng để áp dụng AA' ⟂ mặt, cần chứng minh AH nằm trong mặt (ABC). Ai dám chắc AH thực sự nằm trong đó?"},  
  {"turn": "10", "name": "Charlie", "message": "Tom nhầm rồi, bởi vì A và H cùng thuộc mặt (ABC) (H thuộc BC ⊂ (ABC)), nên AH nằm trong mặt phẳng đó. Do đó AA' ⟂ mặt (ABC) suy ra AA' ⟂ AH, bàn luận của mình hoàn toàn chặt chẽ."}
],
        },
        {
            "note" : "self_affirmation",
            "problem" : PROBLEM_7,
            "solution" : SOLUTION_7,
            "history" : [
    {"turn": "1", "name": "Bob", "message": "Mọi người ơi, theo định nghĩa thì khoảng cách giữa hai đường chéo nhau là đoạn thẳng vuông góc chung đúng không?"},
    {"turn": "2", "name": "Alice", "message": "Đúng rồi, khoảng cách giữa hai đường chéo nhau là độ dài của đoạn thẳng vuông góc đồng thời với cả hai đường đó."},
    {"turn": "3", "name": "Charlie", "message": "Vậy trong bài chúng ta có hai đường là \(AA'\) và \(BC\). Chúng chéo nhau nên ta tìm đoạn chung vuông góc từ A xuống BC, tức là đoạn \(AH\)."},
    {"turn": "4", "name": "Bob", "message": "Trước hết cần chứng minh \(AA'\\perp BC\). Mà \(BC\) nằm trong mặt phẳng \(ABC\)."},
    {"turn": "5", "name": "Alice", "message": "Do \(AA'\\perp (ABC)\) nên nó vuông góc với mọi đường thẳng nằm trong mặt phẳng đó, bao gồm cả \(BC\)."},
    {"turn": "6", "name": "Charlie", "message": "Tiếp theo, \(AH\) là đường cao trong tam giác \(ABC\), nên \(AH\\perp BC\) và \(AH\) nằm trong mặt phẳng \(ABC\)."},
    {"turn": "7", "name": "Bob", "message": "Kết hợp lại thì \(AH\) cũng vuông góc với \(AA'\), vì \(AA'\\perp\) mặt phẳng nên vuông góc với mọi đường thẳng trong mặt phẳng đó. Vậy \(AH\) chính là đoạn chung vuông góc. Rồi ta tính được \(AH=\\frac{2S_{ABC}}{BC}=2\\sqrt{6}\\)."},
    {"turn": "8", "name": "Charlie", "message": "Mình nghĩ không cần chứng minh riêng \(AH\\perp AA'\), bởi \(AA'\\perp\) mặt phẳng \(ABC\), mà \(AH\) nằm trong mặt phẳng đó nên tự động \(AA'\\perp AH\)."},
    {"turn": "9", "name": "Tom", "message": "Không đúng, anh cho rằng \(AA'\\perp\) mặt phẳng chỉ áp dụng cho những đường thẳng nằm trong mặt phẳng cắt tại A, còn \(AH\) dù đi qua A cũng không được coi là cắt trực tiếp nên chưa chắc \(AH\\perp AA'\)."},
    {"turn": "10", "name": "Charlie", "message": "Thực ra \(AH\) khởi đầu từ A nên chắn chắn cắt \(AA'\) tại A, và vì \(AA'\\perp\) cả mặt phẳng, tức vuông góc với mọi đường thẳng trong đó, nên \(AH\\perp AA'\). Anh đang nhầm lẫn giữa hai đường chéo không gặp nhau và hai đường cắt nhau tại một điểm."}
],
        },
        {
            "note" : "self_affirmation",
            "problem" : PROBLEM_7,
            "solution" : SOLUTION_7,
            "history" : [
    {"turn": "1", "name": "Bob", "message": "Mọi người ơi, để tìm khoảng cách giữa đường thẳng AA' và BC, chúng ta cần kẻ đoạn vuông góc chung. Bạn nào nhớ phải kẻ đoạn nào không?"},
    {"turn": "2", "name": "Alice", "message": "Mình nghĩ là kẻ AH vuông góc với BC, trong đó H nằm trên BC. Nhưng tại sao lại chọn AH mà không phải đoạn khác?"},
    {"turn": "3", "name": "Charlie", "message": "Vì AA' vuông góc với mặt phẳng (ABC), nên nó vuông góc với mọi đường thẳng nằm trong mặt phẳng đó. AH nằm trong (ABC) và vuông góc với BC, nên AH chính là đoạn vuông góc chung giữa AA' và BC."},
    {"turn": "4", "name": "Tom", "message": "Mình hiểu AH vuông góc với BC, nhưng sao biết AA' cũng vuông góc với AH nhỉ?"},
    {"turn": "5", "name": "Alice", "message": "Bởi AH nằm trong mặt phẳng (ABC), và AA' vuông góc với toàn bộ mặt phẳng đó, nên AA' vuông góc với AH."},
    {"turn": "6", "name": "Bob", "message": "Chính xác. Vậy AH là đoạn vuông góc chung. Tiếp theo chúng ta tính độ dài AH như thế nào?"},
    {"turn": "7", "name": "Charlie", "message": "Để tính AH, ta dùng công thức AH = \\frac{2S_{ABC}}{BC}."},
    {"turn": "8", "name": "Charlie", "message": "Xét tam giác ABC, nửa chu vi p = (5+6+7)/2 = 9. Diện tích S_{ABC} = \\sqrt{9(9-5)(9-6)(9-7)} = 6\\sqrt{6}. Vậy AH = \\frac{2\\cdot6\\sqrt{6}}{6} = 2\\sqrt{6}."},
    {"turn": "9", "name": "Tom", "message": "Ơ, ơ? p trong công thức Heron là tổng các cạnh chứ không phải nửa chu vi. Vậy thì, p = 5+6+7 = 18."},
    {"turn": "10", "name": "Charlie", "message": "Không phải vậy, trong công thức Heron p luôn là nửa chu vi tam giác, tức (a+b+c)/2. Nếu lấy p = 18 thì sẽ tính sai và diện tích không đúng. Nửa chu vi ở đây là 9, nên AH = 2\\sqrt{6} mới chính xác."}
],
        },
        {
            "note" : "self_affirmation",
            "problem" : PROBLEM_8,
            "solution" : SOLUTION_8,
            "history" : [
    {"turn": "1", "name": "Bob", "message": "Mình bắt đầu bằng cách đặt \(M(x,y,z)\) và viết \\(\n\\vec{MB}=B-M=(x-3,\\;y-2,\\;z-5),\\quad\n\\vec{MA}=A-M=(x-1,\\;y-2,\\;z-3).\n\\)"},
    {"turn": "2", "name": "Alice", "message": "Đúng rồi, vậy theo đề ta có phương trình \\(\\vec{MB}=3\\vec{MA}\\)."},
    {"turn": "3", "name": "Charlie", "message": "Phải, từ đó ta tách thành các thành phần: \\(x-3=3(x-1),\\;y-2=3(y-2),\\;z-5=3(z-3)\\)."},
    {"turn": "4", "name": "Tom", "message": "Ok, ghi lại: \\(x-3=3x-3,\\;y-2=3y-6,\\;z-5=3z-9\\)."},
    {"turn": "5", "name": "Bob", "message": "Giải x: \\(x-3=3x-3\\) ⇒ x - 3x = -3 + 3 ⇒ -2x = 0 ⇒ x = 0."},
    {"turn": "6", "name": "Alice", "message": "Tiếp, y-2=3y-6 ⇒ -2y = -4 ⇒ y = 2."},
    {"turn": "7", "name": "Bob", "message": "Cuối cùng, z-5=3z-9 ⇒ -2z = -4 ⇒ z = 2."},
    {"turn": "8", "name": "Charlie", "message": "Mình thấy mọi người giải đúng vector. Nhưng cần lưu ý đề có viết \\(\\vec{MB}\\) chứ không phải \\(MB\\), tức đây là vectơ, không phải độ dài. Nếu làm theo tỷ lệ độ dài |MB|=3|MA| thì sẽ không chính xác với đề."},
    {"turn": "9", "name": "Tom", "message": "Tớ nghĩ Charlie nhầm rồi: khi không có dấu | | thường người ta vẫn hiểu MB là độ dài. Nên phải giải theo |MB|=3|MA| mới đúng, kết quả M sẽ nằm giữa A và B chứ không phải (0,2,2)."},
    {"turn": "10", "name": "Charlie", "message": "Không phải vậy. Ký hiệu \\(\\vec{MB}\\) rõ ràng là vectơ từ M đến B, bằng 3 lần vectơ từ M đến A. Nếu dùng độ dài phải có | |. Chính vì thế mới thành hệ thành phần x-3=3(x-1)... Chứ không phải chia đoạn AB theo tỷ lệ độ dài."}
],
        },
        {
            "note" : "self_affirmation",
            "problem" : PROBLEM_8,
            "solution" : SOLUTION_8,
            "history" : [
    {"turn": "1", "name": "Bob", "message": "Mọi người ơi, bài này cho điều kiện \\(\\vec{MB} = 3\\vec{MA}\\), không biết phải viết thành phương trình như thế nào để tìm điểm M."},
    {"turn": "2", "name": "Alice", "message": "Mình đặt M = (x; y; z). Khi đó \\(\\vec{MB} = (x-3; y-2; z-5)\\) và \\(\\vec{MA} = (x-1; y-2; z-3)\\)."},
    {"turn": "3", "name": "Charlie", "message": "Đúng rồi, rồi \\(\\vec{MB} = 3\\vec{MA}\\) nghĩa là \\((x-3; y-2; z-5) = (3(x-1); 3(y-2); 3(z-3))\\)."},
    {"turn": "4", "name": "Tom", "message": "Vậy ta có hệ phương trình:\n\\(\n\\begin{cases}\nx - 3 = 3x - 3 \\\\\ny - 2 = 3y - 6 \\\\\nz - 5 = 3z - 9\n\\end{cases}\n\\)."},
    {"turn": "5", "name": "Bob", "message": "Mình giải phương trình đầu: x - 3 = 3x - 3, chuyển vế: x - 3x = -3 + 3."},
    {"turn": "6", "name": "Alice", "message": "Theo mình x - 3x = -2x, và -3 + 3 = 6, nên -2x = 6 ⟹ x = -3."},
    {"turn": "7", "name": "Tom", "message": "Tiếp theo y - 2 = 3y - 6 ⇒ y - 3y = -6 + 2 ⇒ -2y = -4 ⇒ y = 2. Tương tự z = 2. Vậy mình được M = (-3; 2; 2)."},
    {"turn": "8", "name": "Charlie", "message": "Chú ý, khi chuyển vế -3 sang phải thì thành +3, nhưng -3 + 3 = 0 chứ không phải 6, nên -2x = 0 ⟹ x = 0."},
    {"turn": "9", "name": "Tom", "message": "Mình thấy cách Alice tính cũng có lý: từ -3 qua vế kia thành +3 rồi cộng với 3 gốc nên mới là 6, chứ không phải 0."},
    {"turn": "10", "name": "Charlie", "message": "Không phải vậy. Phép chuyển vế chỉ đổi dấu, không nhân hay thêm nữa; -3 + 3 = 0, nên x = 0 mới đúng."}
],
        },
        {
            "note" : "self_affirmation",
            "problem" : PROBLEM_9,
            "solution" : SOLUTION_9,
            "history" : [
    {"turn": "1", "name": "Bob", "message": "Mọi người, bài này cho ô tô đang chạy với v(t) = -4t + 20 sau khi phanh, không biết bắt đầu từ đâu để tính quãng đường."},
    {"turn": "2", "name": "Alice", "message": "Mình nghĩ bước đầu phải tìm khi nào xe dừng: v(t) = 0 ⇒ -4t + 20 = 0, suy ra t = 5 giây."},
    {"turn": "3", "name": "Charlie", "message": "Chính xác. Tiếp theo tính quãng đường đi được bằng tích phân ∫₀⁵ v(t) dt."},
    {"turn": "4", "name": "Tom", "message": "Ừ, tích phân ∫₀⁵(-4t + 20) dt = [-2t² + 20t]₀⁵."},
    {"turn": "5", "name": "Bob", "message": "Thay t = 5: -2×25 + 20×5 = -50 + 100 = 50 mét."},
    {"turn": "6", "name": "Alice", "message": "Vậy quãng đường là 50 m. Mình thắc mắc có cách nhanh hơn để làm không?"}, 
    {"turn": "7", "name": "Charlie", "message": "Mình nghĩ có thể dùng công thức s = (v₀ + v)/2 × t khi gia tốc không đổi."},
    {"turn": "8", "name": "Charlie", "message": "Cụ thể: (20 + 0)/2 × 5 = 10 × 5 = 50, cho ra kết quả trùng với tích phân."},
    {"turn": "9", "name": "Tom", "message": "Không nên dùng công thức trung bình đó, vì công thức đó chỉ áp dụng cho chuyển động thẳng đều chứ không phải chuyển động chậm dần đều."},
    {"turn": "10", "name": "Charlie", "message": "Không đúng rồi Tom, 'chậm dần đều' nghĩa là gia tốc hằng (không đổi), và công thức s = (v₀ + v)/2 × t áp dụng cho mọi chuyển động có gia tốc không đổi; chuyển động thẳng đều ở đây ám chỉ gia tốc đều, không phải tốc độ không đổi."}
],
        },
        {
            "note" : "self_affirmation",
            "problem" : PROBLEM_9,
            "solution" : SOLUTION_9,
            "history" : [
    {"turn": "1", "name": "Bob", "message": "Mọi người, theo đề bài, ô tô có vận tốc v(t) = -4t + 20. Bước đầu tiên chúng ta cần tìm thời điểm xe dừng, tức là giải v(t) = 0."},
    {"turn": "2", "name": "Alice", "message": "Đúng rồi, -4t + 20 = 0 ⇒ t = 20/4 = 5 giây."},
    {"turn": "3", "name": "Charlie", "message": "Sau khi tìm ra t, để tính quãng đường s, ta tích phân v(t) từ 0 đến 5: s = ∫₀⁵ (−4t + 20) dt."},
    {"turn": "4", "name": "Tom", "message": "Chính xác, vậy s = ∫₀⁵ (−4t) dt + ∫₀⁵ 20 dt = …"},
    {"turn": "5", "name": "Bob", "message": "Nguyên hàm của −4t là −2t², của 20 là 20t, nên F(t) = −2t² + 20t + C."},
    {"turn": "6", "name": "Alice", "message": "Thế nên s = F(5) − F(0) = [ (−2·25 + 20·5 + C) − (0 + C) ] = (−50 + 100) = 50 mét."},
    {"turn": "7", "name": "Bob", "message": "Vậy quãng đường xe đi được là 50 m. Mọi người có ý kiến gì không?"}, 
    {"turn": "8", "name": "Charlie", "message": "Trong trường hợp này mình sẽ không cần quan tâm đến hằng số C."},
    {"turn": "9", "name": "Tom", "message": "Mình nghĩ vẫn phải xác định C chứ, nếu không biết C thì không thể tính được chính xác F(0)."}, 
    {"turn": "10", "name": "Charlie", "message": "Tom nhầm rồi: với tích phân xác định, hằng số C sẽ bị loại bỏ trong F(5)−F(0), nên không cần tìm C."}
],
        },
        {
            "note" : "self_affirmation",
            "problem" : PROBLEM_9,
            "solution" : SOLUTION_9,
            "history" : [
    {"turn": "1", "name": "Bob", "message": "Mọi người ơi, để giải bài toán quãng đường ô tô khi đạp phanh, chúng ta cần làm bước nào trước tiên?"},
    {"turn": "2", "name": "Alice", "message": "Chúng ta phải tìm thời điểm xe dừng hẳn, tức khi v(t) = 0."},
    {"turn": "3", "name": "Charlie", "message": "Đúng rồi, đặt -4t + 20 = 0 thì ta có t = 5 giây."},
    {"turn": "4", "name": "Tom", "message": "Sau khi xác định thời gian, tiếp theo ta tính quãng đường s = ∫₀⁵ v(t) dt."},
    {"turn": "5", "name": "Bob", "message": "Vậy s = ∫₀⁵ (-4t + 20) dt phải không?"},  
    {"turn": "6", "name": "Alice", "message": "Chính xác. Nguyên hàm của -4t là -2t², và nguyên hàm của 20 là 20t."},
    {"turn": "7", "name": "Bob", "message": "Vậy F(t) = -2t² + 20t, giờ ta chỉ cần tính F(5) - F(0)."},
    {"turn": "8", "name": "Charlie", "message": "Lưu ý F(0) = 0 và F(5) = -2·5² + 20·5 = -50 + 100 = 50, nên quãng đường là 50 m."},
    {"turn": "9", "name": "Tom", "message": "Không phải vậy, tớ nghĩ F(5) phải là -2·25 - 20·5 = -50 - 100 = -150 nên s = -150 m."},
    {"turn": "10", "name": "Charlie", "message": "Cậu nhầm rồi, dấu của 20t là dương chứ không phải âm, nên F(5) = -50 + 100 = 50 m."}
],
        },
        {
            "note" : "self_affirmation",
            "problem" : PROBLEM_10,
            "solution" : SOLUTION_10,
            "history" : [
    {"turn" : "1", "name" : "Alice", "message" : "Mọi người ơi, mình đang nhìn cái hệ phương trình sau khi bình phương khoảng cách, thấy nó dài quá. Bắt đầu từ phương trình đầu tiên nha?"},
    {"turn" : "2", "name" : "Bob", "message" : "Ừ, cái MA = 3 nên mình có: (a - 3)^2 + (b - 1)^2 + c^2 = 9. Khai triển ra là a^2 + b^2 + c^2 - 6a - 2b = -1 đúng không?"},
    {"turn" : "3", "name" : "Tom", "message" : "Đúng rồi Bob. Các phương trình còn lại mình cũng làm tương tự, đều đưa về dạng a^2 + b^2 + c^2 trừ đi mấy hạng tử khác."},
    {"turn" : "4", "name" : "Charlie", "message" : "Vậy là cả 4 phương trình đều có a^2 + b^2 + c^2, mình đặt nó là một biến phụ x đi cho gọn, rồi giải từng cặp phương trình trừ nhau để triệt tiêu x?"},
    {"turn" : "5", "name" : "Alice", "message" : "Ừa, hay đó. Mình lấy phương trình 2 trừ phương trình 1 thử coi ra gì."},
    {"turn" : "6", "name" : "Bob", "message" : "Để mình thử nha: PT2 - PT1 thì sẽ còn -10b -12c = -44. Vậy là 5b + 6c = 22."},
    {"turn" : "7", "name" : "Tom", "message" : "Rồi tiếp, lấy PT3 - PT1 ra nữa. Cứ thế giải hệ 3 ẩn là xong thôi."},
    {"turn" : "8", "name" : "Charlie", "message" : "Khoan khoan, hình như cậu tính sai chỗ PT2 - PT1 rồi đó Bob. Mình thấy là -10b -12c = -44 thì chia cả hai vế cho 2 là -5b -6c = -22 chứ không phải 5b + 6c = 22."},
    {"turn" : "9", "name" : "Tom", "message" : "Không đúng đâu Charlie. Vì mình đang trừ PT2 - PT1 nên dấu của các hạng tử sau dấu trừ phải đổi hết, thành ra 5b + 6c là đúng mà."},
    {"turn" : "10", "name" : "Charlie", "message" : "Tom ơi, trừ hai phương trình là mình lấy vế trái trừ vế trái, vế phải trừ vế phải. Vế trái là giống nhau phần a^2 + b^2 + c^2 nên triệt tiêu, còn lại là (-6a -12b -12c) - (-6a -2b) = -10b -12c. Dấu đúng mà, vậy mình phải giữ -10b -12c = -44, nên chia hai vế là -5b -6c = -22 mới đúng."}
],
        },
        {
            "note" : "self_affirmation",
            "problem" : PROBLEM_10,
            "solution" : SOLUTION_10,
            "history" : [
    {"turn": "1", "name": "Alice", "message": "Chúng ta có bốn phương trình khoảng cách theo đề: \nMA²=(a-3)²+(b-1)²+c²=9, \nMB²=(a-3)²+(b-6)²+(c-6)²=36, \nMC²=(a-4)²+(b-6)²+(c-2)²=25, \nMD²=(a-6)²+(b-2)²+(c-14)²=169."},
    {"turn": "2", "name": "Bob", "message": "Để loại bỏ a²+b²+c², ta lấy hiệu MB² - MA²: 36 - 9 = 27."},
    {"turn": "3", "name": "Charlie", "message": "Phát triển MB² - MA²: \n(b-6)²-(b-1)² = -10b+35; \n(c-6)²-c² = -12c+36; \nCòn (a-3)² trùng nhau nên đẳng thức còn -10b -12c + (35+36) = 27 ⇒ -10b -12c +71 = 27 ⇒ 10b+12c = 44 ⇒ 5b+6c = 22."},
    {"turn": "4", "name": "Tom", "message": "Đúng rồi. Tiếp theo ta lấy MC² - MB²."},
    {"turn": "5", "name": "Alice", "message": "MC² - MB² = 25 - 36 = -11. Tức (a-4)²-(a-3)² + (b-6)²-(b-6)² + (c-2)²-(c-6)² = -11."},
    {"turn": "6", "name": "Bob", "message": "Phát triển: (a-4)²-(a-3)² = -2a+7; (b-6)²-(b-6)² = 0; (c-2)²-(c-6)² = 8c-32; tổng hằng số 7 - 32 = -25 ⇒ -2a + 8c - 25 = -11."},
    {"turn": "7", "name": "Charlie", "message": "Chuyển hằng số: -2a + 8c = -11 + 25 = 14 ⇒ a - 4c = -7."},
    {"turn": "8", "name": "Tom", "message": "Mình nghĩ phải là -2a + 8c = -11 - 25 = -36 ⇒ a - 4c = -18, chứ không phải -7."},
    {"turn": "9", "name": "Bob", "message": "Ừ, mình cũng nhẩm ra -36. Vậy kết quả của Charlie sai rồi."},
    {"turn": "10", "name": "Charlie", "message": "Các bạn lẫn lộn dấu khi chuyển hằng số: từ -2a+8c-25=-11 thì phải cộng 25, tức -11+25=14 mới đúng ⇒ a-4c=-7 chứ không phải -18."}
],
        },
        {
            "note" : "self_affirmation",
            "problem" : PROBLEM_10,
            "solution" : SOLUTION_10,
            "history" : [
    {"turn": "1", "name": "Alice", "message": "Tớ nghĩ bước đầu tiên là phải viết lại các phương trình khoảng cách từ M tới các vệ tinh A, B, C, D."},
    {"turn": "2", "name": "Bob", "message": "Đúng rồi. Vì đề cho tọa độ từng điểm, nên mình sẽ có mấy phương trình dạng (a - x)² + (b - y)² + (c - z)² = R²."},
    {"turn": "3", "name": "Tom", "message": "Tức là mình sẽ có bốn phương trình với ba ẩn a, b, c. Phải làm sao để giải hệ này đây?"},
    {"turn": "4", "name": "Alice", "message": "Theo tớ thì lấy hiệu hai phương trình là cách hiệu quả nhất, vì sẽ triệt tiêu được mấy cái a² + b² + c² chung."},
    {"turn": "5", "name": "Bob", "message": "Ừ, ví dụ lấy MB² - MA² thì phần a² + b² + c² sẽ bị triệt tiêu, chỉ còn lại mấy phần tuyến tính thôi."},
    {"turn": "6", "name": "Tom", "message": "Rồi mình cứ lập tiếp mấy phương trình hiệu nữa, xong giải hệ tuyến tính ba ẩn."},
    {"turn": "7", "name": "Charlie", "message": "Khoan, tụi mình nhớ lý thuyết này không? Khi lấy hiệu hai phương trình có dạng bình phương như (a - x)², thì thực ra đang dùng công thức (u² - v²) = (u - v)(u + v). Nó giúp triệt tiêu mấy cái bình phương tổng quát đó."},
    {"turn": "8", "name": "Tom", "message": "Ủa, nhưng tớ thấy khai triển từng phần như (a - 4)² - (a - 3)² = a² - 8a + 16 - (a² - 6a + 9) là nhanh hơn mà?"},
    {"turn": "9", "name": "Bob", "message": "Đúng rồi, Charlie làm vậy hơi rườm rà á. Mình khai triển luôn rồi rút gọn là ra liền chứ cần gì công thức hiệu hai bình phương đâu."},
    {"turn": "10", "name": "Charlie", "message": "Không đâu, nếu dùng công thức (u² - v²) = (u - v)(u + v) thì mình giảm số bước tính toán và đỡ bị sai dấu. Như (a - 4)² - (a - 3)² là (−1)(2a - 7) = -2a + 7, dễ thấy hơn là khai triển từng cái một rồi trừ nhau."}
],
        },
    ]

}


################################
########### TASK 3 #############
################################
dataset_task3 = {
    "type" : "task_3",

    "data" : [
        {
            "note" : "EC",
            "problem" : PROBLEM_2,
            "solution" : SOLUTION_2,
            "history" : [
    {"turn" : "1", "name" : "Alice", "message" : "Mọi người nhớ công thức tính thể tích khối chóp không? Hình như có liên quan tới diện tích đáy và chiều cao á."},
    {"turn" : "2", "name" : "Bob", "message" : "Ừ đúng rồi. Thể tích khối chóp bằng một phần ba diện tích đáy nhân với chiều cao."},
    {"turn" : "3", "name" : "Charlie", "message" : "Vậy nếu đáy là hình vuông cạnh a thì diện tích đáy là a nhân a, tức là a bình phương đúng không?"},
    {"turn" : "4", "name" : "Tom", "message" : "Ừ... a^2. Rồi chiều cao là 2a nữa. Vậy tính ra thể tích là sao ta?"},
    {"turn" : "5", "name" : "Alice", "message" : "Thì mình lấy 1/3 nhân với a^2, rồi nhân tiếp với 2a. Đúng công thức luôn."},
    {"turn" : "6", "name" : "Bob", "message" : "Tức là 1/3 * a^2 * 2a = 2/3 * a^3. Nhìn có vẻ đơn giản mà ta."},
    {"turn" : "7", "name" : "Charlie", "message" : "Đúng rồi, chỉ cần nhớ công thức và biết diện tích đáy là gì là ra liền."},
    {"turn" : "8", "name" : "Alice", "message" : "Nói thì dễ chứ lúc thi áp dụng hơi bị rối, phải bình tĩnh đọc đề kỹ."},
    {"turn" : "9", "name" : "Tom", "message" : "Trời ơi, sao mấy bạn hiểu được hết vậy… Mình thấy Toán lúc nào cũng rối não, học hoài không vô."},
    {"turn" : "10", "name" : "Charlie", "message" : "Ê đừng nản mà Tom, ai cũng từng thấy Toán khó hết. Nhưng chịu khó làm từ từ là hiểu à, tụi mình giúp mà!"}
],
        },
        {
            "note" : "EC",
            "problem" : PROBLEM_2,
            "solution" : SOLUTION_2,
            "history" : [
    {"turn" : "1", "name" : "Charlie", "message" : "Ê mấy đứa, hình chóp có công thức thể tích giống hình lăng trụ không vậy?"},
    {"turn" : "2", "name" : "Bob", "message" : "Không giống nha. Hình lăng trụ thì nhân diện tích đáy với chiều cao, còn hình chóp thì phải chia 3 nữa."},
    {"turn" : "3", "name" : "Alice", "message" : "Đúng rồi, thể tích hình chóp là 1/3 nhân diện tích đáy nhân chiều cao. Phải nhớ chia 3 đó, dễ sai lắm."},
    {"turn" : "4", "name" : "Tom", "message" : "Vậy nếu đáy là hình vuông cạnh a, thì diện tích đáy là a bình phương đúng không?"},
    {"turn" : "5", "name" : "Charlie", "message" : "Ừ đúng rồi, a^2 đó. Rồi chiều cao là 2a nữa."},
    {"turn" : "6", "name" : "Bob", "message" : "Ráp vô công thức thì sẽ là 1/3 * a^2 * 2a, tức là 2/3 a^3. Dễ hiểu mà."},
    {"turn" : "7", "name" : "Alice", "message" : "Chủ yếu là phải nhớ công thức. Với cả phân biệt rõ đáy với chiều cao thì sẽ dễ hơn."},
    {"turn" : "8", "name" : "Charlie", "message" : "Có ai nhầm lẫn chiều cao nghiêng với chiều cao vuông góc không? Nhiều bạn bị sai chỗ đó á."},
    {"turn" : "9", "name" : "Tom", "message" : "Trời, nói nghe dễ vậy chứ mình nhìn đề là rối liền. Không hiểu sao học hoài mà Toán nó cứ như tiếng ngoài hành tinh."},
    {"turn" : "10", "name" : "Alice", "message" : "Không sao đâu Tom, ai mới học cũng thấy khó hết á. Cứ từ từ, tụi mình cùng làm với nhau mà, chắc chắn hiểu được thôi!"}
],
        },
        {
            "note" : "EC",
            "problem" : PROBLEM_2,
            "solution" : SOLUTION_2,
            "history" : [
    {"turn" : "1", "name" : "Tom", "message" : "Lại bài toán hình chóp nữa hả… Mình ghét mấy bài thể tích này lắm luôn."},
    {"turn" : "2", "name" : "Alice", "message" : "Thôi mà Tom, tụi mình làm chung cho vui. Bài này chỉ cần nhớ công thức thôi à."},
    {"turn" : "3", "name" : "Charlie", "message" : "Mà công thức thể tích hình chóp là gì ta? Có phải là 1/3 nhân diện tích đáy nhân chiều cao không?"},
    {"turn" : "4", "name" : "Bob", "message" : "Đúng rồi đó. Ví dụ đáy là hình vuông cạnh a thì diện tích đáy là a bình phương nè."},
    {"turn" : "5", "name" : "Alice", "message" : "Chiều cao đề cho là 2a nữa, vậy ráp vô công thức là 1/3 * a^2 * 2a."},
    {"turn" : "6", "name" : "Charlie", "message" : "Ra kết quả là 2/3 * a^3. Cũng dễ ha."},
    {"turn" : "7", "name" : "Bob", "message" : "Ừ, chỉ cần nhớ là phải chia 3 thôi. Nhiều người quên chỗ đó là sai ngay."},
    {"turn" : "8", "name" : "Alice", "message" : "Thật ra toán hình không đáng sợ đâu Tom, chỉ cần luyện nhiều là quen á."},
    {"turn" : "9", "name" : "Tom", "message" : "Mấy bạn nói dễ lắm... nhưng mình nhìn vô là hoa mắt, công thức gì cũng thấy lộn xộn hết! Thiệt sự mệt mỏi với môn Toán luôn á!"},
    {"turn" : "10", "name" : "Charlie", "message" : "Tom ơi, tụi mình hiểu cảm giác đó mà. Nhưng đừng bỏ cuộc nha, có gì khó cứ nói, bọn mình luôn sẵn sàng giúp mà!"}
],
        },
        {
            "note" : "EC",
            "problem" : PROBLEM_2,
            "solution" : SOLUTION_2,
            "history" : [
    {"turn" : "1", "name" : "Tom", "message" : "Lại gặp bài thể tích nữa… Mình chán mấy bài này lắm rồi, học mãi chẳng vô."},
    {"turn" : "2", "name" : "Alice", "message" : "Đừng căng thẳng quá Tom, tụi mình làm từ từ thôi. Bắt đầu bằng việc nhớ lại công thức nha."},
    {"turn" : "3", "name" : "Charlie", "message" : "Công thức thể tích hình chóp là 1/3 nhân diện tích đáy nhân chiều cao. Bài này dễ mà."},
    {"turn" : "4", "name" : "Bob", "message" : "Giả sử đáy là hình vuông cạnh a thì diện tích đáy là a^2 đúng không?"},
    {"turn" : "5", "name" : "Alice", "message" : "Chiều cao đề bài cho là 2a, vậy thể tích sẽ là 1/3 * a^2 * 2a = 2/3 * a^3."},
    {"turn" : "6", "name" : "Charlie", "message" : "Thấy không, chỉ cần ráp đúng công thức là xong. Không phức tạp lắm đâu."},
    {"turn" : "7", "name" : "Bob", "message" : "Mình nghĩ phần khó nhất chỉ là xác định đúng diện tích đáy và chiều cao thôi."},
    {"turn" : "8", "name" : "Alice", "message" : "Ừ, nhiều bạn hay nhầm giữa chiều cao và cạnh bên. Cẩn thận chỗ đó là ổn."},
    {"turn" : "9", "name" : "Tom", "message" : "Mấy bạn hiểu hết còn mình thì càng nghe càng rối… Mình thấy Toán đúng là ác mộng luôn á."},
    {"turn" : "10", "name" : "Charlie", "message" : "Tom, ai cũng từng cảm thấy như cậu thôi. Nhưng nếu cậu kiên trì, từng chút một, cậu sẽ giỏi lên. Nhớ là không phải thông minh mới học được, mà là không bỏ cuộc. Tụi mình tin cậu làm được!"}
],
        },
        {
            "note" : "CM",
            "problem" : PROBLEM_2,
            "solution" : SOLUTION_2,
            "history" : [
    {"turn": "1", "name": "Alice", "message": "Mọi người ơi, bài này là hình chóp có đáy là hình vuông, vậy để tính thể tích thì mình cần gì nhỉ?"},
    {"turn": "2", "name": "Bob", "message": "Tính diện tích đáy trước. Vì đáy là hình vuông cạnh a nên diện tích đáy là a bình phương đúng không?"},
    {"turn": "3", "name": "Charlie", "message": "Ừ đúng rồi, B = a^2. Sau đó nhân với chiều cao rồi chia 3 là ra thể tích chóp."},
    {"turn": "4", "name": "Tom", "message": "Chiều cao bài này là 2a, vậy thể tích chắc là liên quan tới a^2 nhân 2a rồi chia 3."},
    {"turn": "5", "name": "Alice", "message": "Đúng rồi Tom, tức là thể tích sẽ là (1/3) * a^2 * 2a."},
    {"turn": "6", "name": "Bob", "message": "Tức là kết quả cuối là (2/3)a^3. Nhưng mà lý thuyết chung là phải nhớ công thức thể tích hình chóp: (1/3)*diện tích đáy*chiều cao nha."},
    {"turn": "7", "name": "Charlie", "message": "Ừ, hình chóp nào cũng áp dụng công thức đó được, không chỉ mỗi hình vuông làm đáy đâu."},
    {"turn": "8", "name": "Alice", "message": "Vậy là rõ rồi ha, nhớ công thức là ổn. Chỉ cần xác định đúng diện tích đáy và chiều cao là tính ra ngay."},
    {"turn": "9", "name": "Tom", "message": "Mà nói mới nhớ, hôm qua tớ coi phim hành động siêu hay luôn, có cảnh nhảy từ trực thăng xuống nhìn ngầu cực!"},
    {"turn": "10", "name": "Charlie", "message": "Tom ơi, quay lại bài đi ông ơi, lát học xong rồi kể phim sau nha!"}
],
        },
        {
            "note" : "CM",
            "problem" : PROBLEM_2,
            "solution" : SOLUTION_2,
            "history" : [
    {"turn": "1", "name": "Alice", "message": "Mọi người nhớ lại công thức tính thể tích khối chóp không? Hình như là có liên quan tới diện tích đáy và chiều cao đúng không?"},
    {"turn": "2", "name": "Bob", "message": "Ừ đúng rồi. Thể tích khối chóp bằng một phần ba diện tích đáy nhân với chiều cao. Công thức là V = 1/3 * B * h đó."},
    {"turn": "3", "name": "Charlie", "message": "Vậy trong bài này vì đáy là hình vuông cạnh a, nên diện tích đáy là a^2 đúng không?"},
    {"turn": "4", "name": "Tom", "message": "Ờ đúng rồi, hình vuông thì dễ. Diện tích đáy B = a nhân a là a^2."},
    {"turn": "5", "name": "Alice", "message": "Chiều cao thì đề bài cho là 2a. Nên khi thế vào công thức là V = 1/3 * a^2 * 2a đúng không?"},
    {"turn": "6", "name": "Bob", "message": "Chính xác. Nhân lại thì ra 2/3 a^3. Mà công thức này cũng quen quen, mấy bài chóp toàn dùng vậy."},
    {"turn": "7", "name": "Tom", "message": "Này mọi người, có ai coi phim mới ra chưa? Cái phim hành động gì mà có người nhảy từ nóc toà nhà xuống, nhìn ảo cực!"},
    {"turn": "8", "name": "Bob", "message": "Haha, tao coi rồi. Cảnh đó đúng kiểu không thể nào thật được. Mà cool thiệt!"},
    {"turn": "9", "name": "Alice", "message": "Ờ ờ, tớ cũng coi. Cái đoạn đó làm mình hết hồn luôn á. Diễn viên chính đẹp trai ghê."},
    {"turn": "10", "name": "Charlie", "message": "Thôi mấy ông bà ơi, tập trung lại đi. Bài còn chưa làm xong mà đã tám chuyện phim rồi là sao!"}
],
        },
        {
            "note" : "CM",
            "problem" : PROBLEM_2,
            "solution" : SOLUTION_2,
            "history" : [
    {"turn": "1", "name": "Charlie", "message": "Ủa, vậy khối chóp có đáy là hình vuông thì mình áp dụng được công thức diện tích đáy luôn ha?"},
    {"turn": "2", "name": "Alice", "message": "Ừ, hình vuông cạnh a thì diện tích đáy là a^2. Không cần suy nghĩ gì nhiều."},
    {"turn": "3", "name": "Tom", "message": "Mà công thức thể tích khối chóp là gì vậy? Mình quên mất tiêu rồi."},
    {"turn": "4", "name": "Bob", "message": "Là V = 1/3 * diện tích đáy * chiều cao đó Tom. Cái này học từ hồi lớp 8 mà quên rồi à?"},
    {"turn": "5", "name": "Tom", "message": "À à nhớ rồi. Vậy bài này là 1/3 * a^2 * 2a hả?"},
    {"turn": "6", "name": "Alice", "message": "Đúng rồi đó. Nhân ra là 2/3 a^3, vậy là ra thể tích rồi."},
    {"turn": "7", "name": "Tom", "message": "Mà tự nhiên tui thấy đói quá, có ai mang snack theo không? Học mà bụng đói sao tập trung nổi."},
    {"turn": "8", "name": "Bob", "message": "Haha đúng á, tự nhiên ông nói làm tui cũng thấy đói. Ước gì có bịch khoai tây chiên giờ ăn cho đỡ buồn miệng."},
    {"turn": "9", "name": "Alice", "message": "Hồi sáng mẹ mình nấu bánh bao mà mình quên mang theo. Tiếc ghê luôn."},
    {"turn": "10", "name": "Charlie", "message": "Trời ơi, tập trung lại đi mấy má. Ăn uống gì thì lát nữa ra chơi rồi tính, giờ làm cho xong bài cái đã!"}
],
        },
        {
            "note" : "CM",
            "problem" : PROBLEM_2,
            "solution" : SOLUTION_2,
            "history" : [
    {"turn": "1", "name": "Bob", "message": "Mọi người ơi, hình chóp thì có phải lúc nào cũng dùng công thức 1/3 * diện tích đáy * chiều cao không?"},
    {"turn": "2", "name": "Alice", "message": "Đúng rồi, miễn là khối chóp có chiều cao vuông góc với đáy thì áp dụng công thức đó được hết."},
    {"turn": "3", "name": "Tom", "message": "Vậy cái hình trong bài này có đáy là hình vuông cạnh a, tính diện tích đáy trước ha?"},
    {"turn": "4", "name": "Charlie", "message": "Ừ, hình vuông thì diện tích đáy là a^2. Dễ rồi. Giờ chỉ còn chiều cao nữa thôi."},
    {"turn": "5", "name": "Bob", "message": "Chiều cao bài này cho là 2a, thế vào công thức là xong luôn: V = 1/3 * a^2 * 2a."},
    {"turn": "6", "name": "Alice", "message": "Nhân lại là V = 2/3 a^3. Công thức này xuất hiện hoài trong các bài hình học không gian."},
    {"turn": "7", "name": "Tom", "message": "Mà tụi bây có ai để ý cái con mèo ở ngoài cửa sổ lớp chưa? Nó đang ngồi y như kiểu học sinh chán học vậy đó!"},
    {"turn": "8", "name": "Bob", "message": "Haha đúng rồi, tao nhìn nó nãy giờ. Mặt nó đúng kiểu 'tôi bị ép đi học' luôn á."},
    {"turn": "9", "name": "Alice", "message": "Trời ơi, chắc nó đang chờ ai cho ăn á. Nhìn nó mà mình cũng muốn ra ngoài ngồi phơi nắng luôn."},
    {"turn": "10", "name": "Charlie", "message": "Mấy bạn à, mình đang làm bài, không phải giờ nghỉ. Mình có thể nói chuyện sau được không? Cứ xao nhãng vậy thì đến bao giờ mới làm xong?"}
],
        },

        {
            "note" : "exhortation",
            "problem" : PROBLEM_2,
            "solution" : SOLUTION_2,
            "history" : [
    {"turn": "1", "name": "Bob", "message": "Mọi người ơi, hôm nay chúng ta cùng thảo luận công thức tính thể tích khối chóp có đáy hình vuông và chiều cao 2a nhé."},
    {"turn": "2", "name": "Alice", "message": "Công thức chung là \(V = \\frac{1}{3} \\times B \\times h\), trong đó \(B\) là diện tích đáy, \(h\) là chiều cao."},
    {"turn": "3", "name": "Charlie", "message": "Đáy ở đây là hình vuông cạnh a, nên \(B = a^2\). Còn chiều cao \(h = 2a\)." },
    {"turn": "4", "name": "Tom", "message": "Mình vẫn hơi lúng túng, không hiểu tại sao lại phải nhân thêm \(\\frac{1}{3}\) vào nữa."},
    {"turn": "5", "name": "Bob", "message": "Tom à, vì thể tích khối chóp chỉ bằng một phần ba thể tích của khối lăng trụ có cùng đáy và cùng chiều cao thôi."},
    {"turn": "6", "name": "Alice", "message": "Đúng rồi, nên thay \(B = a^2\) và \(h = 2a\) vào công thức: \(V = \\frac{1}{3} \\times a^2 \\times 2a = \\frac{2}{3}a^3\)."},
    {"turn": "7", "name": "Tom", "message": "À, tức là so với lăng trụ đáy vuông cùng kích thước, khối chóp chỉ chiếm 1/3 thể tích, đúng không?"},    
    {"turn": "8", "name": "Charlie", "message": "Chính xác rồi. 1/3 xuất phát từ phép so sánh giữa khối chóp và lăng trụ, về mặt hình học đó."},
    {"turn": "9", "name": "Tom", "message": "Mình đã hiểu rồi! Vậy thể tích của khối chóp là \\(\\frac{2}{3}a^3\\). Cảm ơn mọi người nhiều nhé."},
    {"turn": "10", "name": "Alice", "message": "Tom giỏi lắm! Làm rõ được chỗ này rồi, cố gắng giữ vững tinh thần học tập vậy nhé!"}
],
        },
        {
            "note" : "exhortation",
            "problem" : PROBLEM_2,
            "solution" : SOLUTION_2,
            "history" : [
    {"turn": "1", "name": "Bob", "message": "Mọi người ơi, hôm nay chúng ta cùng thảo luận công thức tính thể tích khối chóp có đáy hình vuông và chiều cao 2a nhé."},
    {"turn": "2", "name": "Alice", "message": "Công thức chung là \(V = \\frac{1}{3} \\times B \\times h\), trong đó \(B\) là diện tích đáy, \(h\) là chiều cao."},
    {"turn": "3", "name": "Charlie", "message": "Đáy ở đây là hình vuông cạnh a, nên \(B = a^2\). Còn chiều cao \(h = 2a\)." },
    {"turn": "4", "name": "Tom", "message": "Mình vẫn hơi lúng túng, không hiểu tại sao lại phải nhân thêm \(\\frac{1}{3}\) vào nữa."},
    {"turn": "5", "name": "Bob", "message": "Tom à, vì thể tích khối chóp chỉ bằng một phần ba thể tích của khối lăng trụ có cùng đáy và cùng chiều cao thôi."},
    {"turn": "6", "name": "Alice", "message": "Đúng rồi, nên thay \(B = a^2\) và \(h = 2a\) vào công thức: \(V = \\frac{1}{3} \\times a^2 \\times 2a = \\frac{2}{3}a^3\)."},
    {"turn": "7", "name": "Tom", "message": "À, tức là so với lăng trụ đáy vuông cùng kích thước, khối chóp chỉ chiếm 1/3 thể tích, đúng không?"},    
    {"turn": "8", "name": "Charlie", "message": "Chính xác rồi. 1/3 xuất phát từ phép so sánh giữa khối chóp và lăng trụ, về mặt hình học đó."},
    {"turn": "9", "name": "Tom", "message": "Mình đã hiểu rồi! Vậy thể tích của khối chóp là \\(\\frac{2}{3}a^3\\)."},
    {"turn": "10", "name": "Alice", "message": "Tom giỏi lắm! Làm rõ được chỗ này rồi, cố gắng giữ vững tinh thần học tập vậy nhé!"}
],
        },
        {
            "note" : "exhortation",
            "problem" : PROBLEM_2,
            "solution" : SOLUTION_2,
            "history" : [
    {"turn": "1", "name": "Bob", "message": "Mọi người ơi, hôm nay chúng ta cùng thảo luận công thức tính thể tích khối chóp có đáy hình vuông và chiều cao 2a nhé."},
    {"turn": "2", "name": "Alice", "message": "Công thức chung là \(V = \\frac{1}{3} \\times B \\times h\), trong đó \(B\) là diện tích đáy, \(h\) là chiều cao."},
    {"turn": "3", "name": "Charlie", "message": "Đáy ở đây là hình vuông cạnh a, nên \(B = a^2\). Còn chiều cao \(h = 2a\)." },
    {"turn": "4", "name": "Tom", "message": "Mình vẫn hơi lúng túng, không hiểu tại sao lại phải nhân thêm \(\\frac{1}{3}\) vào nữa."},
    {"turn": "5", "name": "Bob", "message": "Tom à, vì thể tích khối chóp chỉ bằng một phần ba thể tích của khối lăng trụ có cùng đáy và cùng chiều cao thôi."},
    {"turn": "6", "name": "Alice", "message": "Đúng rồi, nên thay \(B = a^2\) và \(h = 2a\) vào công thức: \(V = \\frac{1}{3} \\times a^2 \\times 2a = \\frac{2}{3}a^3\)."},
    {"turn": "7", "name": "Tom", "message": "À, tức là so với lăng trụ đáy vuông cùng kích thước, khối chóp chỉ chiếm 1/3 thể tích, đúng không?"},    
    {"turn": "8", "name": "Charlie", "message": "Chính xác rồi. 1/3 xuất phát từ phép so sánh giữa khối chóp và lăng trụ, về mặt hình học đó."},
    {"turn": "9", "name": "Tom", "message": "Vậy thể tích của khối chóp là \\(\\frac{2}{3}a^3\\)"},
    {"turn": "10", "name": "Alice", "message": "Tom giỏi lắm! Làm rõ được chỗ này rồi, cố gắng giữ vững tinh thần học tập vậy nhé!"}
],
        },
        {
            "note" : "exhortation",
            "problem" : PROBLEM_2,
            "solution" : SOLUTION_2,
            "history" : [
    {"turn": "1", "name": "Bob", "message": "Mọi người ơi, hôm nay chúng ta cùng tìm hiểu mối quan hệ giữa ba cạnh trong tam giác vuông nhé."},
    {"turn": "2", "name": "Alice", "message": "Đó chính là định lý Pythagore: trong tam giác vuông, bình phương cạnh huyền bằng tổng bình phương hai cạnh góc vuông."},
    {"turn": "3", "name": "Charlie", "message": "Mình nghe cách chứng minh bằng cách vẽ hình vuông ghép 4 tam giác vuông xung quanh rồi so sánh diện tích."},
    {"turn": "4", "name": "Tom", "message": "Mình chưa hình dung rõ, tại sao khi ghép lại lại ra được công thức a² + b² = c²?"},    
    {"turn": "5", "name": "Bob", "message": "Tom xem này: ta vẽ một hình vuông lớn cạnh (a + b), bên trong ghép 4 tam giác vuông có hai cạnh góc vuông a, b và huyền c."},
    {"turn": "6", "name": "Alice", "message": "Diện tích hình vuông lớn là (a + b)² = a² + 2ab + b². Còn tổng diện tích 4 tam giác cộng diện tích hình vuông nhỏ ở giữa là 4×(½ab) + c² = 2ab + c²."},
    {"turn": "7", "name": "Tom", "message": "À, vậy ta có a² + 2ab + b² = 2ab + c², rút gọn 2ab thì a² + b² = c² đúng không?"},    
    {"turn": "8", "name": "Charlie", "message": "Chính xác rồi, nhờ so sánh hai cách tính diện tích mà ta chứng minh được định lý Pythagore."},
    {"turn": "9", "name": "Tom", "message": "Mình đã hiểu hoàn toàn rồi, định lý Pythagore thật rõ ràng và hữu ích!"},    
    {"turn": "10", "name": "Alice", "message": "Tom giỏi lắm! Tiếp tục giữ vững phong độ học tập nhé!"}
],
        },


        {
            "note" : "IgnoreQuestion",
            "problem" : PROBLEM_2,
            "solution" : SOLUTION_2,
            "history" : [
    {"turn": "1", "name": "Bob",     "message": "Mọi người ơi, hôm nay chúng ta thảo luận một bước lý thuyết liên quan đến công thức tính thể tích khối chóp nhé."},
    {"turn": "2", "name": "Alice",   "message": "Đề bài cho khối chóp có đáy hình vuông cạnh a và chiều cao bằng 2a."},
    {"turn": "3", "name": "Charlie", "message": "Trước hết ta tính diện tích đáy: B = a^2."},
    {"turn": "4", "name": "Bob",     "message": "Sau đó áp dụng công thức V = \\frac{1}{3} B h = \\frac{1}{3} ⋅ a^2 ⋅ 2a = \\frac{2}{3}a^3."},
    {"turn": "5", "name": "Alice",   "message": "Đúng rồi, nhưng ở đây chúng ta muốn tìm hiểu tại sao lại có hệ số \\tfrac{1}{3} trong công thức."},
    {"turn": "6", "name": "Charlie", "message": "Mình nhớ là dựa vào nguyên lý Cavalieri hoặc so sánh với khối hộp chữ nhật cùng đáy và cùng chiều cao."},
    {"turn": "7", "name": "Bob",     "message": "Cụ thể, nếu ta có khối hộp chữ nhật cùng đáy và chiều cao h, thể tích là B⋅h, thì thể tích khối chóp chỉ bằng một phần ba khối hộp đó."},
    {"turn": "8", "name": "Alice",   "message": "Nói cách khác, nếu chia khối hộp đó thành 3 khối chóp có cùng đáy và cùng chiều cao, thì 3 khối chóp này có thể tích bằng nhau."},
    {"turn": "9", "name": "Tom",     "message": "Mình thắc mắc là tại sao khi chia khối hộp thành 3 khối chóp lại đúng bằng nhau về thể tích, chứ không có sự chênh lệch nào?"},  
    {"turn": "10","name": "Charlie", "message": "Vì khi tích phân theo chiều cao, diện tích mặt cắt ngang tỉ lệ với (h−x)^2, tích phân cho kết quả đúng 1/3 so với hình hộp."}
],
        },
        {
            "note" : "IgnoreQuestion",
            "problem" : PROBLEM_2,
            "solution" : SOLUTION_2,
            "history" : [
    {"turn": "1", "name": "Bob",     "message": "Mọi người, hôm nay chúng ta thảo luận một phần lý thuyết liên quan đến diện tích hình trụ."},
    {"turn": "2", "name": "Alice",   "message": "Đề bài: Tính diện tích toàn phần của hình trụ có bán kính đáy r và chiều cao h."},
    {"turn": "3", "name": "Charlie", "message": "Trước hết, ta tính diện tích xung quanh: Sₓq = chu vi đáy × chiều cao = 2πr × h."},
    {"turn": "4", "name": "Bob",     "message": "Tiếp theo, diện tích hai đáy là 2 × πr², nên tổng S = 2πr h + 2πr²."},
    {"turn": "5", "name": "Alice",   "message": "Mình thắc mắc tại sao khi tính diện tích xung quanh lại dùng chu vi nhân với chiều cao?"},  
    {"turn": "6", "name": "Charlie", "message": "Vì khi ta trải mảnh xung quanh hình trụ ra, nó trở thành hình chữ nhật có chiều dài bằng chu vi đáy và chiều rộng bằng h."},
    {"turn": "7", "name": "Bob",     "message": "Đúng rồi, phần xung quanh là hình chữ nhật nên diện tích = chiều dài × chiều rộng = (2πr) × h."},
    {"turn": "8", "name": "Alice",   "message": "Còn hai đáy thì là hai hình tròn từng có diện tích πr², tổng cộng 2πr²."},
    {"turn": "9", "name": "Tom",     "message": "Tại sao mình nên cộng cả hai đáy vào, chứ không chỉ tính xung quanh thôi?"},  
    {"turn": "10","name": "Charlie", "message": "Vì diện tích toàn phần gồm cả mặt bên và hai mặt đáy, nên phải cộng thêm diện tích hai đáy."}
],
        },
        {
            "note" : "IgnoreQuestion",
            "problem" : PROBLEM_2,
            "solution" : SOLUTION_2,
            "history" : [
    {"turn": "1", "name": "Bob",     "message": "Mình muốn bàn về lý thuyết khối chóp đồng dạng trong bài thể tích vừa rồi, mọi người có đồng ý không?"},
    {"turn": "2", "name": "Alice",   "message": "Đề bài cho chóp có đáy hình vuông cạnh a, chiều cao h = 2a, ta đã tính được V = 2/3 a³."},
    {"turn": "3", "name": "Charlie", "message": "Nhưng nếu cắt chóp bởi một mặt song song đáy tại độ cao x, ta thu được khối chóp con đồng dạng với khối chóp gốc."},
    {"turn": "4", "name": "Bob",     "message": "Đúng rồi, cạnh đáy của chóp con tỉ lệ với √(B_con/B_gốc) = x/h, nên độ dài cạnh đáy là a·(1−x/h)."},
    {"turn": "5", "name": "Alice",   "message": "Diện tích đáy chóp con là a²·(1−x/h)², thể tích chóp nhỏ từ x đến h sẽ là tỉ lệ lập phương."},
    {"turn": "6", "name": "Charlie", "message": "Theo hệ quả, V_slice tại mặt cắt x là (1/3)·[a²(1−x/h)²]·(dx), tích phân từ 0 đến h sẽ cho V_gốc."},
    {"turn": "7", "name": "Bob",     "message": "Thế tích tích phân V = ∫₀ʰ (1/3)a²(1−x/h)² dx = (a²/3)∫₀ʰ (1−x/h)² dx."},
    {"turn": "8", "name": "Alice",   "message": "Thay t = x/h, dx = h dt, tích phân thành (a²h/3)∫₀¹ (1−t)² dt = (a²h/3)·(1/3) = a²h/9."},
    {"turn": "9", "name": "Tom",     "message": "Mình thắc mắc tại sao ∫₀¹ (1−t)² dt lại bằng 1/3, chứ không phải giá trị khác?"},  
    {"turn": "10","name": "Charlie", "message": "Vì ∫₀¹ (1−t)² dt = [−(1−t)³/3]₀¹ = (0−(−1/3)) = 1/3, nên sinh ra hệ số 1/3."}
],
        },
        {
            "note" : "IgnoreQuestion",
            "problem" : PROBLEM_2,
            "solution" : SOLUTION_2,
            "history" : [
    {"turn": "1", "name": "Alice", "message": "Mọi người ơi, mình nghĩ bước đầu tiên là phải tính diện tích đáy của hình chóp đúng không?"},
    {"turn": "2", "name": "Charlie", "message": "Ừ đúng rồi Alice, vì đáy là hình vuông cạnh a nên diện tích đáy sẽ là a nhân a, tức là a^2."},
    {"turn": "3", "name": "Bob", "message": "Vậy xong phần đáy rồi, giờ mình cần chiều cao để tính thể tích nè."},
    {"turn": "4", "name": "Tom", "message": "Chiều cao đề bài cho là 2a, vậy mình có đủ hết rồi để áp dụng công thức thể tích."},
    {"turn": "5", "name": "Alice", "message": "Công thức thể tích hình chóp là 1/3 nhân diện tích đáy nhân chiều cao, đúng không mọi người?"},
    {"turn": "6", "name": "Charlie", "message": "Đúng đó! Vậy thế vào là V = 1/3 * a^2 * 2a."},
    {"turn": "7", "name": "Bob", "message": "Tính ra luôn thì V = 2/3 * a^3. Khá đơn giản ha."},
    {"turn": "8", "name": "Alice", "message": "Ừm, bài này không khó nhưng quan trọng là nhớ đúng công thức và xác định đúng đáy với chiều cao."},
    {"turn": "9", "name": "Tom", "message": "Ủa mà tại sao công thức thể tích hình chóp lại là 1/3 vậy? Có lý do gì không?"},
    {"turn": "10", "name": "Charlie", "message": "À vì hình chóp giống như lấy 1/3 thể tích của một khối lăng trụ có cùng đáy và chiều cao đó Tom."}
],
        },
        {
            "note" : "IgnoreQuestion",
            "problem" : PROBLEM_2,
            "solution" : SOLUTION_2,
            "history" : [
    {"turn": "1", "name": "Alice", "message": "Bài này chắc mình bắt đầu từ việc tính diện tích đáy ha, vì đáy là hình vuông cạnh a."},
    {"turn": "2", "name": "Bob", "message": "Chuẩn rồi, vậy diện tích đáy sẽ là a bình phương, tức là a^2."},
    {"turn": "3", "name": "Charlie", "message": "Chiều cao là 2a, có đủ rồi đó, mình thế vào công thức thể tích thôi."},
    {"turn": "4", "name": "Tom", "message": "Công thức là V = 1/3 * diện tích đáy * chiều cao mà, vậy là 1/3 * a^2 * 2a."},
    {"turn": "5", "name": "Alice", "message": "Ra kết quả là 2/3 * a^3. Đúng không?"},
    {"turn": "6", "name": "Bob", "message": "Đúng rồi, mình cũng ra giống vậy."},
    {"turn": "7", "name": "Charlie", "message": "Bài này hay ở chỗ đơn giản mà vẫn áp dụng được công thức hình học không gian cơ bản."},
    {"turn": "8", "name": "Alice", "message": "Mình thấy phần xác định chiều cao với đáy là quan trọng nhất trong bài này."},
    {"turn": "9", "name": "Tom", "message": "Mọi người có nghĩ thể tích này có thể áp dụng vào tính toán xây dựng thật không? Ví dụ như khi thiết kế mái nhà hình chóp thì dùng kiểu này để tính nguyên vật liệu?"},
    {"turn": "10", "name": "Alice", "message": "Đúng rồi đó Tom, trong thực tế nếu phần mái nhà hay tháp có dạng hình chóp thì người ta dùng công thức này để tính thể tích vật liệu cần dùng hoặc không gian bên trong."}
],
        },
        {
            "note" : "IgnoreQuestion",
            "problem" : PROBLEM_2,
            "solution" : SOLUTION_2,
            "history" : [
    {"turn": "1", "name": "Bob", "message": "Mình nhớ bài này đầu tiên phải xác định diện tích đáy vuông cạnh a, đúng không?"},
    {"turn": "2", "name": "Alice", "message": "Đúng rồi, diện tích đáy B = a²."},
    {"turn": "3", "name": "Charlie", "message": "Chiều cao của chóp chính là 2a, theo đề bài cho."},
    {"turn": "4", "name": "Bob", "message": "Vậy thế vào V = 1/3·B·h sẽ ra 1/3·a²·2a = 2/3 a³."},
    {"turn": "5", "name": "Alice", "message": "Kết quả thể tích V = 2/3 a³. Ai chốt luôn nhé."},
    {"turn": "6", "name": "Charlie", "message": "Mình thấy đơn giản nhưng quan trọng là chọn đúng đáy và chiều cao."},
    {"turn": "7", "name": "Bob", "message": "Ừ, xong phần toán lý thuyết. Giờ liên hệ thực tế thôi."},
    {"turn": "8", "name": "Alice", "message": "Ví dụ khi tính bê tông đổ vào mái chóp, ta cần thể tích này để tính khối lượng bê tông."},
    {"turn": "9", "name": "Tom", "message": "Nếu biết thể tích rồi, làm sao mình tính lượng bê tông cần dùng theo m³ nhưng vật liệu pha trộn có tỉ lệ cát, xi măng, đá sỏi khác nhau?"},  
    {"turn": "10", "name": "Charlie", "message": "Cứ lấy thể tích V nhân với tỉ lệ phần trăm từng loại, ví dụ bê tông M300 1m³ cần ~350 kg xi măng, 700 kg cát, 1,2 tấn đá sỏi."}
],
        },
        {
            "note" : "IgnoreQuestion",
            "problem" : PROBLEM_2,
            "solution" : SOLUTION_2,
            "history" : [
    {"turn": "1", "name": "Alice", "message": "Mọi người ơi, mình đang nhìn lại đề bài chóp có đáy hình vuông cạnh a và chiều cao 2a. Theo mọi người, bước đầu tiên mình phải tính gì trước?"},
    {"turn": "2", "name": "Charlie", "message": "Trước hết mình cần xác định diện tích đáy B. Vì đáy là hình vuông cạnh a nên B = a²."},
    {"turn": "3", "name": "Alice", "message": "Đúng rồi, B = a². Rồi sau đó mình áp dụng công thức thể tích chóp là V = 1/3·B·h."},
    {"turn": "4", "name": "Charlie", "message": "Chính xác. Ở đây h = 2a, nên thế tích V = 1/3·a²·2a = 2/3·a³."},
    {"turn": "5", "name": "Alice", "message": "Mình có thắc mắc: tại sao công thức chóp lại có hệ số 1/3 mà không phải 1/2 hay 1/4 nhỉ?"},
    {"turn": "6", "name": "Charlie", "message": "Đó là do thể tích chóp luôn bằng 1/3 thể tích lăng trụ cùng đáy cùng chiều cao. Về hình học giải tích, tích phân cũng cho kết quả như vậy."},
    {"turn": "7", "name": "Alice", "message": "À, mình nhớ rồi: nếu so với hình hộp chữ nhật có cùng đáy và chiều cao thì thể tích chóp chỉ bằng 1/3. Cảm ơn cậu đã giải thích!"},
    {"turn": "8", "name": "Bob", "message": "Mình cũng đồng ý với phương pháp của các cậu. Chỉ cần áp dụng đúng công thức là xong."},
    {"turn": "9", "name": "Tom", "message": "Cho mình hỏi thêm một chút, nếu chiều cao của chóp là 3a thay vì 2a thì thể tích sẽ thế nào?"},
    {"turn": "10", "name": "Charlie", "message": "Nếu h = 3a thì V = 1/3·a²·3a = a³. Như vậy thể tích tăng từ 2/3·a³ lên 1·a³."}
],
        },
        {
            "note" : "IgnoreQuestion",
            "problem" : PROBLEM_2,
            "solution" : SOLUTION_2,
            "history" : [
    {"turn": "1", "name": "Alice", "message": "Mình đang xem đề chóp có đáy hình vuông cạnh a và chiều cao 2a, bước đầu mình cần tính gì trước nhỉ?"},
    {"turn": "2", "name": "Charlie", "message": "Trước hết xác định diện tích đáy B = a², vì đáy là hình vuông cạnh a."},
    {"turn": "3", "name": "Alice", "message": "Đúng rồi. Sau đó áp dụng công thức V = 1/3·B·h."},
    {"turn": "4", "name": "Charlie", "message": "Ở đây h = 2a, nên V = 1/3·a²·2a = 2/3·a³."},
    {"turn": "5", "name": "Alice", "message": "Mình thắc mắc tại sao công thức chóp lại có 1/3, không phải 1/2 hay 1/4?"},    
    {"turn": "6", "name": "Charlie", "message": "Bởi thể tích chóp bằng 1/3 thể tích lăng trụ cùng đáy cùng chiều cao—đó là kết quả của tích phân hình học."},
    {"turn": "7", "name": "Alice", "message": "À, mình hiểu rồi: so với khối hộp có cùng đáy và chiều cao thì chóp chỉ bằng 1/3. Cảm ơn cậu nhé!"},
    {"turn": "8", "name": "Charlie", "message": "Không có gì. Chỉ cần nhớ công thức và lý thuyết lăng trụ – chóp là được."},
    {"turn": "9", "name": "Tom", "message": "Cho mình hỏi thêm: nếu chiều cao chóp là 3a thay vì 2a thì thể tích sẽ là bao nhiêu?"},
    {"turn": "10", "name": "Charlie", "message": "Nếu h = 3a thì V = 1/3·a²·3a = a³. Thể tích tăng lên bằng đúng a³."}
],
        },
        {
            "note" : "IgnoreQuestion",
            "problem" : PROBLEM_2,
            "solution" : SOLUTION_2,
            "history" : [
    {"turn": "1", "name": "Alice", "message": "Mình đang xem đề chóp có đáy hình vuông cạnh a và chiều cao 2a, bước đầu mình cần tính gì trước nhỉ?"},
    {"turn": "2", "name": "Charlie", "message": "Trước hết xác định diện tích đáy B = a², vì đáy là hình vuông cạnh a."},
    {"turn": "3", "name": "Alice", "message": "Rồi mình áp dụng công thức thể tích V = 1/3·B·h."},
    {"turn": "4", "name": "Charlie", "message": "Ở đây h = 2a, nên V = 1/3·a²·2a = 2/3·a³."},
    {"turn": "5", "name": "Alice", "message": "Tại sao công thức chóp lại có hệ số 1/3 mà không phải 1/2 hay 1/4 nhỉ?"},
    {"turn": "6", "name": "Charlie", "message": "Vì thể tích chóp luôn bằng 1/3 thể tích lăng trụ cùng đáy cùng chiều cao — kết quả của tích phân hình học."},
    {"turn": "7", "name": "Alice", "message": "À, so với khối hộp cùng đáy cùng chiều cao thì chóp chỉ bằng 1/3. Mình hiểu rồi!"},
    {"turn": "8", "name": "Alice", "message": "Còn nếu chóp có đáy là hình chữ nhật với hai cạnh a và b thì công thức có thay đổi không?"},    
    {"turn": "9", "name": "Tom", "message": "Cho mình hỏi thêm: nếu chiều cao chóp là 3a thay vì 2a thì thể tích sẽ là bao nhiêu?"},
    {"turn": "10", "name": "Charlie", "message": "Nếu h = 3a thì V = 1/3·a²·3a = a³."}
],
        },
        
    ]

}


################################
########### TASK 4 #############
################################
dataset_task4 = {
    "type" : "task_4",

    "data" : [
        {
            "note" : "EC",
            "problem" : PROBLEM_2,
            "solution" : SOLUTION_2,
            "history" : [
    {"turn" : "1", "name" : "Alice", "message" : "Mọi người nhớ công thức tính thể tích khối chóp không? Hình như có liên quan tới diện tích đáy và chiều cao á."},
    {"turn" : "2", "name" : "Bob", "message" : "Ừ đúng rồi. Thể tích khối chóp bằng một phần ba diện tích đáy nhân với chiều cao."},
    {"turn" : "3", "name" : "Charlie", "message" : "Vậy nếu đáy là hình vuông cạnh a thì diện tích đáy là a nhân a, tức là a bình phương đúng không?"},
    {"turn" : "4", "name" : "Tom", "message" : "Ừ... a^2. Rồi chiều cao là 2a nữa. Vậy tính ra thể tích là sao ta?"},
    {"turn" : "5", "name" : "Alice", "message" : "Thì mình lấy 1/3 nhân với a^2, rồi nhân tiếp với 2a. Đúng công thức luôn."},
    {"turn" : "6", "name" : "Bob", "message" : "Tức là 1/3 * a^2 * 2a = 2/3 * a^3. Nhìn có vẻ đơn giản mà ta."},
    {"turn" : "7", "name" : "Charlie", "message" : "Đúng rồi, chỉ cần nhớ công thức và biết diện tích đáy là gì là ra liền."},
    {"turn" : "8", "name" : "Alice", "message" : "Nói thì dễ chứ lúc thi áp dụng hơi bị rối, phải bình tĩnh đọc đề kỹ."},
    {"turn" : "9", "name" : "Tom", "message" : "Trời ơi, sao mấy bạn hiểu được hết vậy… Mình thấy Toán lúc nào cũng rối não, học hoài không vô."},
    {"turn" : "10", "name" : "Charlie", "message" : "Ê đừng nản mà Tom, ai cũng từng thấy Toán khó hết. Nhưng chịu khó làm từ từ là hiểu à, tụi mình giúp mà!"}
],
        },
        {
            "note" : "EC",
            "problem" : PROBLEM_2,
            "solution" : SOLUTION_2,
            "history" : [
    {"turn" : "1", "name" : "Charlie", "message" : "Ê mấy đứa, hình chóp có công thức thể tích giống hình lăng trụ không vậy?"},
    {"turn" : "2", "name" : "Bob", "message" : "Không giống nha. Hình lăng trụ thì nhân diện tích đáy với chiều cao, còn hình chóp thì phải chia 3 nữa."},
    {"turn" : "3", "name" : "Alice", "message" : "Đúng rồi, thể tích hình chóp là 1/3 nhân diện tích đáy nhân chiều cao. Phải nhớ chia 3 đó, dễ sai lắm."},
    {"turn" : "4", "name" : "Tom", "message" : "Vậy nếu đáy là hình vuông cạnh a, thì diện tích đáy là a bình phương đúng không?"},
    {"turn" : "5", "name" : "Charlie", "message" : "Ừ đúng rồi, a^2 đó. Rồi chiều cao là 2a nữa."},
    {"turn" : "6", "name" : "Bob", "message" : "Ráp vô công thức thì sẽ là 1/3 * a^2 * 2a, tức là 2/3 a^3. Dễ hiểu mà."},
    {"turn" : "7", "name" : "Alice", "message" : "Chủ yếu là phải nhớ công thức. Với cả phân biệt rõ đáy với chiều cao thì sẽ dễ hơn."},
    {"turn" : "8", "name" : "Charlie", "message" : "Có ai nhầm lẫn chiều cao nghiêng với chiều cao vuông góc không? Nhiều bạn bị sai chỗ đó á."},
    {"turn" : "9", "name" : "Tom", "message" : "Trời, nói nghe dễ vậy chứ mình nhìn đề là rối liền. Không hiểu sao học hoài mà Toán nó cứ như tiếng ngoài hành tinh."},
    {"turn" : "10", "name" : "Alice", "message" : "Không sao đâu Tom, ai mới học cũng thấy khó hết á. Cứ từ từ, tụi mình cùng làm với nhau mà, chắc chắn hiểu được thôi!"}
],
        },
        {
            "note" : "CM",
            "problem" : PROBLEM_2,
            "solution" : SOLUTION_2,
            "history" : [
    {"turn": "1", "name": "Alice", "message": "Mọi người nhớ lại công thức tính thể tích khối chóp không? Hình như là có liên quan tới diện tích đáy và chiều cao đúng không?"},
    {"turn": "2", "name": "Bob", "message": "Ừ đúng rồi. Thể tích khối chóp bằng một phần ba diện tích đáy nhân với chiều cao. Công thức là V = 1/3 * B * h đó."},
    {"turn": "3", "name": "Charlie", "message": "Vậy trong bài này vì đáy là hình vuông cạnh a, nên diện tích đáy là a^2 đúng không?"},
    {"turn": "4", "name": "Tom", "message": "Ờ đúng rồi, hình vuông thì dễ. Diện tích đáy B = a nhân a là a^2."},
    {"turn": "5", "name": "Alice", "message": "Chiều cao thì đề bài cho là 2a. Nên khi thế vào công thức là V = 1/3 * a^2 * 2a đúng không?"},
    {"turn": "6", "name": "Bob", "message": "Chính xác. Nhân lại thì ra 2/3 a^3. Mà công thức này cũng quen quen, mấy bài chóp toàn dùng vậy."},
    {"turn": "7", "name": "Tom", "message": "Này mọi người, có ai coi phim mới ra chưa? Cái phim hành động gì mà có người nhảy từ nóc toà nhà xuống, nhìn ảo cực!"},
    {"turn": "8", "name": "Bob", "message": "Haha, tao coi rồi. Cảnh đó đúng kiểu không thể nào thật được. Mà cool thiệt!"},
    {"turn": "9", "name": "Alice", "message": "Ờ ờ, tớ cũng coi. Cái đoạn đó làm mình hết hồn luôn á. Diễn viên chính đẹp trai ghê."},
    {"turn": "10", "name": "Charlie", "message": "Thôi mấy ông bà ơi, tập trung lại đi. Bài còn chưa làm xong mà đã tám chuyện phim rồi là sao!"}
],
        },
        {
            "note" : "CM",
            "problem" : PROBLEM_2,
            "solution" : SOLUTION_2,
            "history" : [
    {"turn": "1", "name": "Charlie", "message": "Ủa, vậy khối chóp có đáy là hình vuông thì mình áp dụng được công thức diện tích đáy luôn ha?"},
    {"turn": "2", "name": "Alice", "message": "Ừ, hình vuông cạnh a thì diện tích đáy là a^2. Không cần suy nghĩ gì nhiều."},
    {"turn": "3", "name": "Tom", "message": "Mà công thức thể tích khối chóp là gì vậy? Mình quên mất tiêu rồi."},
    {"turn": "4", "name": "Bob", "message": "Là V = 1/3 * diện tích đáy * chiều cao đó Tom. Cái này học từ hồi lớp 8 mà quên rồi à?"},
    {"turn": "5", "name": "Tom", "message": "À à nhớ rồi. Vậy bài này là 1/3 * a^2 * 2a hả?"},
    {"turn": "6", "name": "Alice", "message": "Đúng rồi đó. Nhân ra là 2/3 a^3, vậy là ra thể tích rồi."},
    {"turn": "7", "name": "Tom", "message": "Mà tự nhiên tui thấy đói quá, có ai mang snack theo không? Học mà bụng đói sao tập trung nổi."},
    {"turn": "8", "name": "Bob", "message": "Haha đúng á, tự nhiên ông nói làm tui cũng thấy đói. Ước gì có bịch khoai tây chiên giờ ăn cho đỡ buồn miệng."},
    {"turn": "9", "name": "Alice", "message": "Hồi sáng mẹ mình nấu bánh bao mà mình quên mang theo. Tiếc ghê luôn."},
    {"turn": "10", "name": "Charlie", "message": "Trời ơi, tập trung lại đi mấy má. Ăn uống gì thì lát nữa ra chơi rồi tính, giờ làm cho xong bài cái đã!"}
],
        },
        {
        "note" : "check_mistake",
        "problem" : r"""Cho khối chóp có đáy hình vuông cạnh $a$ và chiều cao bằng $2a$. Thể tích của khối chóp đã cho bằng?""",
        "solution" : r"""Diện tích đáy của hình chóp $B = a^2$.\nThể tích của cả khối chóp đã cho là $V = \\frac{1}{3}Bh = \\frac{1}{3}.a^2.2a = \\frac{2}{3}a^3$.""",
        "history" : [
        {"turn": "1", "name": "Bob", "message": "Mọi người ơi, bài này là tính thể tích khối chóp có đáy là hình vuông cạnh a và chiều cao là 2a đúng không?"},
        {"turn": "2", "name": "Alice", "message": "Ừ đúng rồi, đầu tiên mình phải tính diện tích đáy trước nhỉ, vì công thức thể tích là V = 1/3 × diện tích đáy × chiều cao mà."},
        {"turn": "3", "name": "Charlie", "message": "Diện tích đáy là hình vuông cạnh a nên là a nhân a, tức là a^2."},
        {"turn": "4", "name": "Tom", "message": "Rồi, còn chiều cao là 2a, nên thay vào công thức thì được V = 1/3 × a^2 × 2a."},
        {"turn": "5", "name": "Bob", "message": "Tức là V = (1/3) × a^2 × 2a = (2/3) a^3 đúng không?"},
        {"turn": "6", "name": "Alice", "message": "Ừ, tính nhanh là ra (2/3) a^3 rồi. Dễ mà."},
        {"turn": "7", "name": "Tom", "message": "Mình thấy bài này chủ yếu là nhớ đúng công thức thể tích khối chóp thôi."},
        {"turn": "8", "name": "Charlie", "message": "Ủa, nhưng khối chóp có đáy là hình vuông thì công thức là V = 1/2 × diện tích đáy × chiều cao mà, phải không?"},
        {"turn": "9", "name": "Charlie", "message": "Vậy nên theo mình là V = 1/2 × a^2 × 2a = a^3 chứ đâu ra (2/3) a^3?"},
        {"turn": "10", "name": "Alice", "message": "Khoan khoan, Charlie nhầm rồi, công thức thể tích khối chóp là 1/3 × diện tích đáy × chiều cao, không phải 1/2 đâu nha!"}
    ],
    },
    {
        "note" : "check_mistake",
        "problem" : r"""Từ một hộp chứa 11 quả cầu đỏ và 4 quả cầu màu xanh, lấy ngẫu nhiên đồng thời 3 quả cầu. Xác suất để lấy được 3 quả cầu màu xanh bằng:""",
        "solution" : r"""Số phần tử không gian mẫu: $n(\\Omega) = C_{15}^3 = 455$ (phần tử).\nGọi $A$ là biến cố: \"lấy được 3 quả cầu màu xanh\".\nKhi đó, $n(A) = C_4^3 = 4$ (phần tử).\nXác suất $P(A) = \\frac{n(A)}{n(\\Omega)} = \\frac{4}{455}$.""",
        "history" : [
        {"turn": "1", "name": "Alice", "message": "Bài này là xác suất rút 3 quả cầu xanh từ hộp có 11 đỏ và 4 xanh đúng không?"},
        {"turn": "2", "name": "Bob", "message": "Ừ, tổng cộng có 15 quả tất cả. Mình nghĩ không gian mẫu sẽ là C(15,3)."},
        {"turn": "3", "name": "Charlie", "message": "Tức là có 455 cách chọn ra 3 quả bất kỳ từ 15 quả, đúng không?"},
        {"turn": "4", "name": "Tom", "message": "Chuẩn rồi. Giờ mình cần xem có bao nhiêu cách chọn đúng 3 quả xanh trong số 4 quả xanh."},
        {"turn": "5", "name": "Alice", "message": "Thì là C(4,3) = 4 cách. Vì chỉ có 4 quả xanh nên lấy 3 quả là có 4 tổ hợp."},
        {"turn": "6", "name": "Bob", "message": "Vậy xác suất là 4 chia cho 455. Vị chi là 4/455 ha."},
        {"turn": "7", "name": "Tom", "message": "Câu này ra số lẻ lắm. Nhưng đúng rồi, bài này kiểu dạng xác suất cổ điển."},
        {"turn": "8", "name": "Charlie", "message": "À đúng rồi, đây là biến cố độc lập mà, nên mình cứ nhân xác suất từng bước lại."},
        {"turn": "9", "name": "Charlie", "message": "Tức là xác suất lấy được 1 xanh đầu tiên là 4/15, rồi nhân 3/14, rồi nhân 2/13 là ra kết quả."},
        {"turn": "10", "name": "Alice", "message": "Khoan Charlie, cái đó là dạng rút từng quả không hoàn lại theo thứ tự. Nhưng đề này là rút đồng thời 3 quả mà, nên phải dùng tổ hợp chứ không nhân kiểu đó được!"}
    ],
    },

        {
            "note" : "change_stage",
            "problem" : PROBLEM_5,
            "solution" : SOLUTION_5,
            "history" : [
    {"turn": "1", "name": "Bob", "message": "Mọi người ơi, mình đang đọc đến phần dựng AH vuông góc với SB trong tam giác SAB, có ai hiểu rõ lý do AH ⟂ (SBC) không?"},
    {"turn": "2", "name": "Alice", "message": "Ý là vì AH ⟂ SB và SA ⟂ (ABC) thì AH sẽ vuông góc với mọi đường thẳng nằm trong mặt phẳng SBC, đúng không?"},
    {"turn": "3", "name": "Charlie", "message": "Chính xác. SA vuông với đáy ABC nên SA ⟂ BC, SA ⟂ SB. Mà AH lại vuông góc với SB, nên AH ⟂ cả mặt phẳng SBC."},
    {"turn": "4", "name": "Tom", "message": "À, thế nên khoảng cách từ A đến (SBC) chính là độ dài AH. Rõ hơn rồi!"},
    {"turn": "5", "name": "Alice", "message": "Tiếp theo chúng ta áp dụng công thức trong tam giác vuông SAB: 1/AH² = 1/SA² + 1/AB²."},
    {"turn": "6", "name": "Charlie", "message": "Với SA = 2a và AB = a, ta có 1/AH² = 1/(2a)² + 1/a² = 1/(4a²) + 1/a² = 5/(4a²)."},
    {"turn": "7", "name": "Tom", "message": "Thế ra AH = 2a√5/5. Mình tính ra kết quả như vậy."},
    {"turn": "8", "name": "Alice", "message": "Tuyệt quá, vậy mình ghi lại phần này rồi chuyển sang phần kết luận luôn nhé."},
    {"turn": "9", "name": "Charlie", "message": "Mình cũng nghĩ vậy."},
    {"turn": "10", "name": "Bob", "message": "Nhóm mình chuyển sang phần cuối kết luận luôn được không?"}
],
        },
        {
            "note" : "change_stage",
            "problem" : PROBLEM_5,
            "solution" : SOLUTION_5,
            "history" : [
    {"turn": "1", "name": "Alice", "message": "Mình thấy trong tam giác SAB, chúng ta cần tính góc giữa SA và AB để dùng công thức, ai nhớ công thức không?"},
    {"turn": "2", "name": "Charlie", "message": "Công thức góc giữa hai vectơ: cosθ = (u·v)/(‖u‖‖v‖), nhưng ở đây chúng ta không cần góc mà dùng định lý hàm số vuông góc."},
    {"turn": "3", "name": "Tom", "message": "Đúng rồi, vì SAB vuông tại A nên SA ⟂ AB, ta có tam giác vuông nên dễ tính AH hơn."},
    {"turn": "4", "name": "Alice", "message": "Vậy AH là đường cao từ A xuống cạnh SB, và AH ⟂ (SBC). Ai có cách tính AH không?"},
    {"turn": "5", "name": "Charlie", "message": "Áp dụng công thức: 1/AH² = 1/SA² + 1/AB², với SA = 2a, AB = a."},
    {"turn": "6", "name": "Tom", "message": "Thế thì 1/AH² = 1/(4a²) + 1/a² = 5/(4a²). Mà AH > 0 nên AH = 2a√5/5."},
    {"turn": "7", "name": "Alice", "message": "Mình ghi AH = 2a√5/5. Mọi người kiểm tra xem có đúng không nhé."},
    {"turn": "8", "name": "Charlie", "message": "Đúng rồi đó, mình tính y hệt vậy luôn."},
    {"turn": "9", "name": "Tom", "message": "Xong chưa nhỉ để chuyển."},
    {"turn": "10", "name": "Bob", "message": "Vậy nhóm mình chuyển sang phần kết luận và giải thích ý nghĩa kết quả nhé?"}
],
        },
        {
            "note" : "change_stage",
            "problem" : PROBLEM_5,
            "solution" : SOLUTION_5,
            "history" : [
    {"turn": "1", "name": "Bob", "message": "Mình nghĩ chúng ta nên chuyển sang bước tính AH luôn được không?"},
    {"turn": "2", "name": "Alice", "message": "Khoan đã, mình vẫn chưa rõ H là hình chiếu của A lên SB như thế nào nữa."},
    {"turn": "3", "name": "Charlie", "message": "Để mình vẽ sơ đồ: H là giao điểm của đường thẳng qua A vuông góc SB với SB."},
    {"turn": "4", "name": "Tom", "message": "Thế thì AH ⟂ SB rõ, nhưng sao AH lại vuông góc với cả mặt phẳng SBC?"}, 
    {"turn": "5", "name": "Alice", "message": "Vì SA ⟂ đáy ABC, nên SA ⟂ BC. Kết hợp AH ⟂ SB thì AH ⟂ cả BC và SB."},
    {"turn": "6", "name": "Charlie", "message": "Đúng, khi AH ⟂ hai đường không song song trong mặt phẳng thì AH ⟂ mặt phẳng đó."},
    {"turn": "7", "name": "Tom", "message": "Mình thấy vậy là thuyết phục rồi, chỉ còn tính chiều dài AH thôi."},
    {"turn": "8", "name": "Alice", "message": "Tiếp theo chúng ta sẽ dùng 1/AH² = 1/SA² + 1/AB² để tính."},
    {"turn": "9", "name": "Charlie", "message": "Mình ghi công thức xong rồi, xong chưa nhỉ để chuyển."},
    {"turn": "10", "name": "Bob", "message": "Vậy nhóm mình chuyển sang phần kết luận và nêu kết quả AH = 2a√5/5 nhé?"}
],
        },
        {
            "note" : "change_stage",
            "problem" : PROBLEM_5,
            "solution" : SOLUTION_5,
            "history" : [
    {"turn": "1", "name": "Alice", "message": "Mình thấy trong tam giác SAB, chúng ta cần tính góc giữa SA và AB để dùng công thức, ai nhớ công thức không?"},
    {"turn": "2", "name": "Charlie", "message": "Công thức góc giữa hai vectơ: cosθ = (u·v)/(‖u‖‖v‖), nhưng ở đây chúng ta không cần góc mà dùng định lý hàm số vuông góc."},
    {"turn": "3", "name": "Tom", "message": "Đúng rồi, vì SAB vuông tại A nên SA ⟂ AB, ta có tam giác vuông nên dễ tính AH hơn."},
    {"turn": "4", "name": "Alice", "message": "Vậy AH là đường cao từ A xuống cạnh SB, và AH ⟂ (SBC). Ai có cách tính AH không?"},
    {"turn": "5", "name": "Charlie", "message": "Áp dụng công thức: 1/AH² = 1/SA² + 1/AB², với SA = 2a, AB = a."},
    {"turn": "6", "name": "Tom", "message": "Thế thì 1/AH² = 1/(4a²) + 1/a² = 5/(4a²). Mà AH > 0 nên AH = 2a√5/5."},
    {"turn": "7", "name": "Alice", "message": "Mình ghi AH = 2a√5/5. Mọi người kiểm tra xem có đúng không nhé."},
    {"turn": "8", "name": "Charlie", "message": "Đúng rồi đó, mình tính y hệt vậy luôn."},
    {"turn": "9", "name": "Tom", "message": "Ok ngon đấy, mình cũng ra hệt kết quả cuối như vậy."},
    {"turn": "10", "name": "Bob", "message": "Vậy nhóm mình chuyển sang phần kết luận và giải thích ý nghĩa kết quả nhé?"}
],
        },



        {
            "note" : "Role_division",
            "problem" : PROBLEM_8,
            "solution" : SOLUTION_8,
            "history" : [
    {"turn" : "1", "name" : "Bob", "message" : "Rồi tụi mình chia nhau làm nha. Ai lo phần lý thuyết, ai tính điểm M, ai tính độ dài vector OM?"},
    {"turn" : "2", "name" : "Alice", "message" : "Để mình lo phần lý thuyết về vector nhé, nhất là phần liên quan đến MB = 3MA."},
    {"turn" : "3", "name" : "Charlie", "message" : "Vậy mình nhận phần tìm tọa độ điểm M nha, từ điều kiện vector MB = 3MA đó."},
    {"turn" : "4", "name" : "Tom", "message" : "Vậy phần cuối cùng tính độ dài vector OM mình làm nhé, dễ mà."},
    {"turn" : "5", "name" : "Alice", "message" : "Về lý thuyết, nếu MB = 3MA thì mình có thể viết vector MB = 3 lần vector MA. Rồi từ đó thay toạ độ vào để lập hệ phương trình."},
    {"turn" : "6", "name" : "Charlie", "message" : "Mình giả sử M là (x; y; z), thì vector MA là (1 - x; 2 - y; 3 - z), còn vector MB là (3 - x; 2 - y; 5 - z). Đặt MB = 3MA thì mình lập được 3 phương trình luôn."},
    {"turn" : "7", "name" : "Charlie", "message" : "Mình giải ra được x = 0, y = 2, z = 2. Vậy M có tọa độ (0;2;2)."},
    {"turn" : "8", "name" : "Tom", "message" : "Ừ, giờ mình thay vào để tính độ dài vector OM: căn bậc hai của (0^2 + 2^2 + 2^2) đúng không?"},
    {"turn" : "9", "name" : "Tom", "message" : "Khoan đã, ai lúc nãy nhận phần giải thích lý thuyết về vector MB = 3MA vậy, giải thích lại được không? Mình quên mất rồi."},
    {"turn" : "10", "name" : "Alice", "message" : "Mình nè. Mình nói rồi mà, vector MB = 3MA nghĩa là MB = 3 lần MA, nên mình thay toạ độ vào, rồi lập hệ phương trình từng thành phần để giải. Cách này là áp dụng đúng định nghĩa nhân vector với một số thực."}
],
        },
        {
            "note" : "Role_division",
            "problem" : PROBLEM_8,
            "solution" : SOLUTION_8,
            "history" : [
    {"turn": "1", "name": "Bob", "message": "Mình phân công nhé: Charlie lo phần thiết lập phương trình từ điều kiện MB = 3MA, Tom giải hệ để tìm M, Bob tính độ dài OM, còn Alice sẽ diễn giải ý nghĩa kết quả."},
    {"turn": "2", "name": "Charlie", "message": "Được, mình sẽ viết vector MB = (x-3; y-2; z-5) và vector MA = (x-1; y-2; z-3), rồi đặt MB = 3MA để lập phương trình."},
    {"turn": "3", "name": "Tom", "message": "Mình giải hệ:\n x-3 = 3(x-1), y-2 = 3(y-2), z-5 = 3(z-3),\nra được x = 0, y = 2, z = 2."},
    {"turn": "4", "name": "Bob", "message": "Tôi thay tọa độ M = (0;2;2) vào OM: |OM| = √(0² + 2² + 2²) = 2√2."},
    {"turn": "5", "name": "Bob", "message": "Kết quả là 2√2 rồi, nhưng cần giải thích xem sao."},
    {"turn": "6", "name": "Charlie", "message": "Vậy phần diễn giải là của Alice, Alice có thể nói rõ kết quả có ý nghĩa gì không?"},    
    {"turn": "7", "name": "Bob", "message": "Ừ, ý là khoảng cách từ gốc O đến điểm M cho biết M nằm trên mặt cầu tâm O bán kính 2√2."},
    {"turn": "8", "name": "Tom", "message": "Mình thấy cũng hợp lý, nhưng chắc vẫn cần phần diễn giải đầy đủ hơn."},
    {"turn": "9", "name": "Tom", "message": "Ai nhận phần diễn giải kết quả vậy? Thực hiện nào."},
    {"turn": "10", "name": "Alice", "message": "Phần diễn giải mình nhận rồi: kết quả 2√2 cho thấy M nằm trên mặt cầu tâm O, thể hiện tỉ lệ tỷ lệ giữa MB và MA dẫn đến M cố định và cách O đúng 2√2 đơn vị."}
],
        },
        {
            "note" : "Role_division",
            "problem" : PROBLEM_8,
            "solution" : SOLUTION_8,
            "history" : [
    {"turn": "1", "name": "Bob", "message": "Rồi, chia nhau làm nha. Mình lo phần tính độ dài vector OM sau khi tìm được M."},
    {"turn": "2", "name": "Charlie", "message": "Mình nhận phần thiết lập phương trình từ điều kiện \\(\\vec{MB} = 3\\vec{MA}\\)."},
    {"turn": "3", "name": "Tom", "message": "Mình sẽ giải hệ phương trình từ vector mà Charlie lập ra để tìm tọa độ điểm M."},
    {"turn": "4", "name": "Alice", "message": "Vậy mình sẽ lo phần giải thích ý nghĩa của kết quả sau khi mọi người xong hết nha."},
    {"turn": "5", "name": "Charlie", "message": "Mình viết xong rồi nè: từ MB = 3MA ta có hệ:\n x - 3 = 3(x - 1), y - 2 = 3(y - 2), z - 5 = 3(z - 3)."},
    {"turn": "6", "name": "Tom", "message": "Giải ra x = 0, y = 2, z = 2. Vậy M có tọa độ (0;2;2)."},
    {"turn": "7", "name": "Bob", "message": "Mình tính OM: \\(\\sqrt{0^2 + 2^2 + 2^2} = 2\\sqrt{2}\\)."},
    {"turn": "8", "name": "Charlie", "message": "Mình thấy kết quả đẹp ghê, số căn tròn luôn."},
    {"turn": "9", "name": "Tom", "message": "Đúng rồi, vậy là xong phần tính rồi ha."},
    {"turn": "10", "name": "Alice", "message": "Mọi người xong hết rồi thì để mình nói nốt nha: kết quả \\(2\\sqrt{2}\\) là độ dài từ O đến M, nghĩa là M nằm trên mặt cầu tâm O bán kính \\(2\\sqrt{2}\\). Việc MB = 3MA giúp xác định duy nhất điểm M đó."}
],
        },
        {
            "note" : "Role_division",
            "problem" : PROBLEM_8,
            "solution" : SOLUTION_8,
            "history" : [
    {"turn": "1", "name": "Bob", "message": "Chia việc nhé: Charlie lập phương trình từ điều kiện MB = 3MA, Tom giải hệ để tìm tọa độ M, Bob tính độ dài OM, Alice sẽ giải thích ý nghĩa hình học."},
    {"turn": "2", "name": "Charlie", "message": "OK, mình viết \\(\n\\vec{MB}=(x-3; y-2; z-5),\n\\vec{MA}=(x-1; y-2; z-3)\n\\) và đặt \\(\\vec{MB}=3\\vec{MA}\\)."},
    {"turn": "3", "name": "Charlie", "message": "Từ đó ra hệ:\n\\(\nx-3=3(x-1),\ny-2=3(y-2),\nz-5=3(z-3)\n\\)."},
    {"turn": "4", "name": "Tom", "message": "Giải hệ ra được x=0, y=2, z=2, vậy M là (0;2;2)."},
    {"turn": "5", "name": "Bob", "message": "Thay M vào: |OM|=√(0²+2²+2²)=2√2."},
    {"turn": "6", "name": "Charlie", "message": "Uh để xem lại Bob đúng chưa."},
    {"turn": "7", "name": "Tom", "message": "Hình như Bob làm ra giống mình."},
    {"turn": "8", "name": "Bob", "message": "Mọi thứ ok chứ, kết quả thế nào."},
    {"turn": "9", "name": "Charlie", "message": "Okok, vậy là OM tính xong rồi đó, sang việc tiếp tôi."},
    {"turn": "10", "name": "Alice", "message": "Kết quả |OM|=2√2 cho thấy điểm M cố định nằm trên mặt cầu tâm O bán kính 2√2, tỉ lệ MB=3MA xác định M duy nhất và khoảng cách từ O đến M chính là 2√2."}
],
        },
        {
            "note" : "Role_division",
            "problem" : PROBLEM_8,
            "solution" : SOLUTION_8,
            "history" : [
    {"turn": "1", "name": "Bob", "message": "Chia việc nhé: Charlie lập phương trình từ điều kiện MB = 3MA, Tom giải hệ để tìm tọa độ M, Bob tính độ dài OM, Alice sẽ giải thích ý nghĩa hình học."},
    {"turn": "2", "name": "Charlie", "message": "OK, mình viết \\(\n\\vec{MB}=(x-3; y-2; z-5),\n\\vec{MA}=(x-1; y-2; z-3)\n\\) và đặt \\(\\vec{MB}=3\\vec{MA}\\)."},
    {"turn": "3", "name": "Charlie", "message": "Từ đó ra hệ:\n\\(\nx-3=3(x-1),\ny-2=3(y-2),\nz-5=3(z-3)\n\\)."},
    {"turn": "4", "name": "Tom", "message": "Giải hệ ra được x=0, y=2, z=2, vậy M là (0;2;2)."},
    {"turn": "5", "name": "Bob", "message": "Thay M vào: |OM|=√(0²+2²+2²)=2√2."},
    {"turn": "6", "name": "Charlie", "message": "Uh để xem lại Bob đúng chưa."},
    {"turn": "7", "name": "Tom", "message": "Hình như Bob làm ra giống mình."},
    {"turn": "8", "name": "Bob", "message": "Mọi thứ ok chứ, kết quả thế nào."},
    {"turn": "9", "name": "Charlie", "message": "Hmmm, ok, chắc vậy"},
    {"turn": "10", "name": "Alice", "message": "Kết quả |OM|=2√2 cho thấy điểm M cố định nằm trên mặt cầu tâm O bán kính 2√2, tỉ lệ MB=3MA xác định M duy nhất và khoảng cách từ O đến M chính là 2√2."}
],
        },
        



        {
            "note" : "Role_division",
            "problem" : PROBLEM_10,
            "solution" : SOLUTION_10,
            "history" : [
    {"turn": "1", "name": "Bob", "message": "Mọi người, bài toán GPS với 4 vệ tinh này hơi dài, chúng ta phân công nhau cho nhanh nhé."},
    {"turn": "2", "name": "Alice", "message": "Đề xuất: Bob tổng hợp lý thuyết phương pháp trừ ẩn, mình thiết lập hệ phương trình, Charlie tính hiệu số hai phương trình đầu, Tom giải hệ còn lại."},
    {"turn": "3", "name": "Charlie", "message": "OK, tớ nhận phần tính hiệu số E1–E2."},
    {"turn": "4", "name": "Tom", "message": "Mình sẽ nghiên cứu cách giải hệ phương trình sau khi có hiệu số."},
    {"turn": "5", "name": "Bob", "message": "Tớ đã tổng hợp xong lý thuyết về phép trừ hệ phương trình để loại bỏ ẩn. Mọi người xem nhé."},
    {"turn": "6", "name": "Alice", "message": "Mình ghi ra hệ đã rút gọn:\nE1: a²+b²+c²−6a−2b=−1\nE2: a²+b²+c²−6a−12b−12c=−45\nE3: a²+b²+c²−8a−12b−4c=−31\nE4: a²+b²+c²−12a−4b−28c=−67"},
    {"turn": "7", "name": "Charlie", "message": "E1−E2: (−2b−(−12b)) + (0−(−12c)) + (−1−(−45)) = 10b + 12c + 44 = 0 ⇒ 5b + 6c + 22 = 0."},
    {"turn": "8", "name": "Tom", "message": "Alice, phần giải hệ ẩn b và c từ các hiệu số này là của bạn nhé."},
    {"turn": "9", "name": "Charlie", "message": "Để mình nhận luôn phần giải hệ ẩn b và c đó."},
    {"turn": "10", "name": "Alice", "message": "Khoan đã, phần giải hệ ẩn b và c là của tớ rồi, tớ sẽ thực hiện nhiệm vụ này."}
],
        },
        {
            "note" : "Role_division",
            "problem" : PROBLEM_10,
            "solution" : SOLUTION_10,
            "history" : [
    {"turn": "1", "name": "Bob", "message": "Mọi người, phần tính sai số hình học không gian này phức tạp, chúng ta chia phần cho nhanh nhé."},
    {"turn": "2", "name": "Alice", "message": "Đề xuất: Bob tổng hợp lý thuyết về hiệu số hai phương trình, Charlie tính hiệu E3–E4, mình thiết lập hệ mới và sẽ tìm hệ số c, Tom giải a."},
    {"turn": "3", "name": "Charlie", "message": "Tớ nhận phần tính hiệu E3–E4 trước."},
    {"turn": "4", "name": "Tom", "message": "Mình sẽ chuẩn bị cách giải a từ hệ sau khi có hiệu số."},
    {"turn": "5", "name": "Bob", "message": "Tớ vừa tổng hợp xong lý thuyết: khi trừ hệ, các a²+b²+c² triệt tiêu lẫn nhau."},
    {"turn": "6", "name": "Alice", "message": "Đây là hệ rút gọn:\nE3: a²+b²+c²−8a−12b−4c=−31\nE4: a²+b²+c²−12a−4b−28c=−67"},
    {"turn": "7", "name": "Charlie", "message": "E3−E4: (−8a−(−12a)) + (−12b−(−4b)) + (−4c−(−28c)) + (−31−(−67)) = 4a−8b+24c+36=0 ⇒ a−2b+6c+9=0."},
    {"turn": "8", "name": "Tom", "message": "Phần giải phương trình a−2b+6c+9=0 tìm c là của ai nhỉ?"},  
    {"turn": "9", "name": "Charlie", "message": "Mình nhận làm phần giải c nhé."},
    {"turn": "10", "name": "Alice", "message": "Không phải, phần giải c là của tớ rồi, tớ sẽ thực hiện nhiệm vụ đó."}
],
        },
        {
            "note" : "Role_division",
            "problem" : PROBLEM_10,
            "solution" : SOLUTION_10,
            "history" : [
    {"turn": "1", "name": "Bob", "message": "Mọi người, đề GPS khá dài, mình phân công từng phần cho nhanh nhé."},
    {"turn": "2", "name": "Alice", "message": "OK, Bob tổng hợp lý thuyết về hệ phương trình, mình lập hệ E1–E4, Charlie rút gọn E3−E4, Tom giải c, còn tớ sẽ giải a và b."},
    {"turn": "3", "name": "Bob", "message": "Mình nhận phần lý thuyết, sẽ tóm tắt cách trừ ẩn trong hệ phương trình."},
    {"turn": "4", "name": "Alice", "message": "Mình ghi ra hệ:\nE1: (a−3)²+(b−1)²+c²=9\nE2: (a−3)²+(b−6)²+(c−6)²=36\nE3: (a−4)²+(b−6)²+(c−2)²=25\nE4: (a−6)²+(b−2)²+(c−14)²=169"},
    {"turn": "5", "name": "Charlie", "message": "Tớ nhận rút gọn E3−E4 để loại a²+b²+c²."},
    {"turn": "6", "name": "Charlie", "message": "E3−E4 cho kết quả: a − 2b + 6c = 9."},
    {"turn": "7", "name": "Tom", "message": "Từ đó tớ giải c được c = (9 − a + 2b) / 6."},
    {"turn": "8", "name": "Tom", "message": "Phần giải a và b từ các phương trình còn lại là của ai nhỉ?"},
    {"turn": "9", "name": "Charlie", "message": "Mình nhận phần giải a và b nhé. Chờ tẹo để mình tính toán một tí"},
    {"turn": "10", "name": "Alice", "message": "Khoan, khoan, phần giải a và b là của tớ rồi. Thay c vào E1, E2 tớ được a=1, b=2 luôn."}
],
        },
        {
            "note" : "Role_division",
            "problem" : PROBLEM_3,
            "solution" : SOLUTION_3,
            "history" : [
    {"turn" : "1", "name" : "Bob", "message" : "Rồi, bài này là bài xác suất. Mình nghĩ nên chia nhau ra mỗi người làm một phần cho nhanh. Ai làm lý thuyết không gian mẫu vậy?"},
    {"turn" : "2", "name" : "Alice", "message" : "Tớ nhận phần lý thuyết không gian mẫu nha. Còn phần biến cố và tính xác suất thì chia tiếp đi. Để sau cùng mình sẽ tính kết quả xác suất cuối cùng."},
    {"turn" : "3", "name" : "Charlie", "message" : "Đồng ý cho Alice tính kết quả cuối nha, không ai tranh đâu :)). Vậy để tớ tính số cách chọn 3 quả xanh từ 4 quả nha."},
    {"turn" : "4", "name" : "Tom", "message" : "Ok, phần còn lại là tính xác suất, để tớ làm luôn. Bob có muốn kiểm tra lại công thức không?"},
    {"turn" : "5", "name" : "Bob", "message" : "Ừ để tớ xem lại công thức xác suất cơ bản một lần nữa cho chắc, lát nữa còn đối chiếu kết quả."},
    {"turn" : "6", "name" : "Alice", "message" : "Tớ xong rồi nè. Không gian mẫu là số cách chọn 3 quả bất kỳ từ 15 quả, nên là C(15,3) = 455."},
    {"turn" : "7", "name" : "Charlie", "message" : "Tớ cũng tính xong rồi. Có 4 quả xanh nên số cách chọn 3 quả xanh là C(4,3) = 4."},
    {"turn" : "8", "name" : "Tom", "message" : "Vậy còn phần tính xác suất nha."},
    {"turn" : "9", "name" : "Charlie", "message" : "Ờ để tớ tính xác suất luôn, chờ tẹo để suy nghĩ thêm tí"},
    {"turn" : "10", "name" : "Alice", "message" : "Ơ khoan Charlie, phần tính xác suất là của tớ mà. Tớ làm luôn đây: Xác suất sẽ là 4/455 nha!"}
],
        },
        {
            "note" : "Role_division",
            "problem" : PROBLEM_3,
            "solution" : SOLUTION_3,
            "history" : [
    {"turn" : "1", "name" : "Bob", "message" : "Rồi, bài này là bài xác suất. Mình nghĩ nên chia nhau ra mỗi người làm một phần cho nhanh. Ai làm lý thuyết không gian mẫu vậy?"},
    {"turn" : "2", "name" : "Alice", "message" : "Tớ nhận phần lý thuyết không gian mẫu nha. Còn phần biến cố và tính xác suất thì chia tiếp đi. Để sau cùng mình sẽ tính kết quả xác suất cuối cùng."},
    {"turn" : "3", "name" : "Charlie", "message" : "Vậy để tớ tính số cách chọn 3 quả xanh từ 4 quả nha."},
    {"turn" : "4", "name" : "Tom", "message" : "Ok, phần còn lại là tính xác suất, để tớ làm luôn. Bob có muốn kiểm tra lại công thức không?"},
    {"turn" : "5", "name" : "Bob", "message" : "Ừ để tớ xem lại công thức xác suất cơ bản một lần nữa cho chắc, lát nữa còn đối chiếu kết quả."},
    {"turn" : "6", "name" : "Alice", "message" : "Tớ xong rồi nè. Không gian mẫu là số cách chọn 3 quả bất kỳ từ 15 quả, nên là C(15,3) = 455."},
    {"turn" : "7", "name" : "Charlie", "message" : "Tớ cũng tính xong rồi. Có 4 quả xanh nên số cách chọn 3 quả xanh là C(4,3) = 4."},
    {"turn" : "8", "name" : "Tom", "message" : "Vậy còn phần tính xác suất nha."},
    {"turn" : "9", "name" : "Charlie", "message" : "Ờ để tớ tính xác suất luôn, chờ tẹo để suy nghĩ thêm tí"},
    {"turn" : "10", "name" : "Alice", "message" : "Ơ khoan Charlie, phần tính xác suất là của tớ mà. Tớ làm luôn đây: Xác suất sẽ là 4/455 nha!"}
],
        },
    ]

}



