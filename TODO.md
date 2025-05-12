# Issues

## Coding
1. Cần đặt các helper function ra ngoài:
    - current_stage_desc

2. Chạy quá nhanh không kịp cho user nói
    >> Cần có thêm `def analysis()` để gọi user

    >> Thêm random (5-10s) để dừng lại

    >> Chỉnh prompt


## Stage management
1. Code để dựa vào context có sẵn (problem, solution) để **tạo** ra các phases/stages --> ``Materials Content Generator Module``?


2. Tuân theo thiết kế **Backward design**: learning outcome <-- learning objectives <-- learning activities <-- learning unit ?


3. Ở các task trong các agents thảo luận rất lâu mới chuyển sang task mới?


4. Cần mở rộng prompt cho nhiều settings khác không đơn giản là môn toán


5. Thiết kế các tín hiệu `start/continue/next` cho cả stage và step in stage


6. Xem xét có cần `description: "Khi đã giải quyết được câu các nhiệm vụ trên và nắm được các mục tiêu, đề nghị cả nhóm sang bước mới là \"Lên kế hoạch\"."` không?


7. CHƯA CẬP NHẬT [DONE] (cần sửa lại file: conversation_phase_manager.py)


8. Hiện tượng do nhìn các tin nhắn trước, Manager cập nhật stage quá nhanh, không đúng => cần chỉnh lại



## Behaviours of Agents
1. Chưa đem lại nhiều thông tin hữu ích luôn, mà hay hỏi

2. Cân bằng giữa độ dài từng lượt nói (ví dụ lúc cần nói dài - cung cấp thông tin, nói ngắn - động viên, đồng ý):
    >> Solution 1: Lúc thinking cho agent quyết định nói ``{ngắn/tb/dài}`` --> thêm vào prompt của speaking

    >> Solution 2:

3. Bob có hiện tượng nhắc lại (trước đó đã trả lời user - e.g x khác -1 , nhưng lượt sau lại nhắc lại điều tương tự - để mình giải thích...)


## Hướng dẫn agent cách Thinking hiệu quả
1. Kiểm tra lại đây có phải THO của agent đó hay của chung các agent?


2. Có nên cho agent thấy được suy nghĩ của các agent khác =)))?


3. Chưa có "Poor Thinking"



## Evaluator
1. Sửa lại hàm tính điểm cuối cùng



