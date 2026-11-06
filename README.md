# Fintech Fieldnotes

Sổ tay tiếng Việt để luyện nói phỏng vấn Software Engineer — Bank Solutions.

## Đọc tài liệu

- Website: **https://tonminhce.github.io/learn-fintech/** khi GitHub Pages được triển khai.
- Offline: tải [`index.html`](index.html), mở bằng Chrome, Edge, Firefox hoặc Safari. CSS, script và nội dung đều nằm trong file; không cần cài dependency hay chạy server.
- GitHub hiển thị HTML dạng source. Dùng link website hoặc tải file để xem giao diện.

## Nội dung

- **39 script lý thuyết**: OOP/SOLID/design patterns, Java concurrency, Spring, database, messaging, bảo mật và vận hành.
- **5 mẫu kể kinh nghiệm**: giới thiệu, hệ thống hiện tại, incident, tối ưu và bất đồng thiết kế. Điền phần `[ngoặc vuông]` bằng trải nghiệm thật.
- **1 bài system design 35–40 phút**: rút tiền từ ví về ngân hàng, có timeline, API, schema, state machine, SQL minh họa và failure cases. Thời lượng bao gồm vẽ và hỏi sâu, không chỉ đọc script.
- **1 phần mở rộng**: đổi đề sang Payment Gateway, eWallet, Loyalty, Notification và bài tập Rate Limiter.
- Câu hỏi đào sâu, điểm dễ mất điểm và đường dẫn tài liệu chính thức.

Đây là tài liệu luyện tập dựa trên JD và các chủ đề được yêu cầu, không phải đề phỏng vấn nội bộ. Con số capacity là giả định minh họa. Java 21 và nội dung nâng cao được đánh dấu để phân biệt với nền tảng Java 8/Spring Boot 2 trong JD.

## Tính năng

- Mục lục theo chủ đề, tìm kiếm hỗ trợ tiếng Việt không dấu, lọc ưu tiên/đã lưu/chưa luyện.
- Ẩn script để tự trả lời, bộ đếm giờ có tạm dừng/làm lại.
- Đánh dấu đã luyện và ghi chú cá nhân, lưu bằng `localStorage` trên trình duyệt.
- Giao diện sáng/tối, cỡ chữ 16–24px, bố cục mobile và bản in phần đang lọc.
- Nội dung vẫn đọc được khi JavaScript bị tắt.

Không có backend, analytics, tài khoản hay dịch vụ nhận ghi chú. Dữ liệu luyện không tự đồng bộ giữa thiết bị. Trình duyệt có thể hạn chế hoặc xóa local storage, đặc biệt ở chế độ riêng tư hay khi mở file trực tiếp. Tránh đưa secret hoặc dữ liệu riêng của công ty/khách hàng vào ghi chú.

## Chỉnh sửa

Yêu cầu build: Python 3.10+ (chỉ standard library). Node chỉ dùng nếu muốn kiểm tra cú pháp JavaScript.

```sh
python scripts/build.py
node --check app.js
python -m http.server 8765 --bind 127.0.0.1
```

- `content/guide.py`: nội dung script và câu hỏi đào sâu.
- `styles.css`: giao diện.
- `app.js`: tương tác local trong trình duyệt.
- `scripts/build.py`: template và build ra `index.html` tự chứa.
- `index.html`: artifact được commit để mở trực tiếp hoặc phục vụ qua Pages.

Sau khi sửa source, chạy build và commit cả source lẫn HTML. Không sửa riêng HTML rồi quên source, vì lần build sau sẽ ghi đè.

## GitHub Pages

Repo dùng site tĩnh, không cần pipeline build. Pages có thể phục vụ nhánh `main`, thư mục `/` (root); `.nojekyll` bỏ qua xử lý Jekyll. Không cần token trong source hoặc file cấu hình.

## Nhịp luyện đề xuất

1. Đọc một script để nắm mạch **khái niệm → cơ chế → ví dụ → trade-off**.
2. Ẩn script, bấm giờ, nói lại bằng lời của mình.
3. Mở câu hỏi đào sâu và tự kiểm tra failure case.
4. Điền câu chuyện thật theo **bối cảnh → trách nhiệm → lựa chọn → bằng chứng → bài học**.
5. Luyện bài thiết kế theo timeline, vẽ trên giấy và giữ invariants nhất quán khi được hỏi thêm.

Cập nhật nội dung: 06/11/2026.
