# Lạc Hồng Viên — congviennghiatrang.com

Website đa trang bằng HTML, CSS hiện đại và JavaScript ES modules. Không cần cài thư viện, không có bước build phía trình duyệt. 13 trang nội dung và trang 404; giao diện responsive, menu điện thoại, lọc khuôn viên, thư viện ảnh có dialog, tìm kiếm cẩm nang và soạn nội dung tư vấn.

## Cấu trúc

- `build.py`: nội dung và bộ tạo HTML bằng Python 3 (thư viện tiêu chuẩn).
- `dist/`: website sẵn sàng triển khai, ảnh lưu trong dự án.
- `dist/assets/style.css`: hệ thống giao diện và responsive.
- `dist/assets/app.js`: các tương tác trình duyệt.
- `scripts/check_site.py`: kiểm tra tham chiếu nội bộ, anchor, H1, metadata và ALT.

## Cập nhật

Sửa nội dung trong `build.py`, chạy `python3 build.py`. Sửa giao diện và tương tác trong `dist/assets/`. Chạy `python3 scripts/check_site.py` và `node --check dist/assets/app.js` trước khi triển khai.

Xem cục bộ: `python3 -m http.server 8000 --directory dist` rồi mở http://localhost:8000.

## Nội dung và liên hệ

Hotline 0971 999 470 và ảnh lấy từ congviennghiatrang.com ngày 20/10/2026. Chưa công bố giá khi không có bảng giá xác nhận. Không tự nhận là website chính thức chủ đầu tư. Trang dịch vụ trình bày các nhóm việc cần trao đổi và xác nhận.

Biểu mẫu chỉ soạn nội dung tại thiết bị, không gửi/lưu dữ liệu. Cần tích hợp backend hoặc CRM nếu muốn nhận đăng ký khách hàng. Không có tài khoản quản trị CMS trong phiên bản này.

## SEO và triển khai

Giữ URL bảng giá `/gia-dat-nghia-trang-lac-hong-vien/`. Từng trang có Title, Description, H1, canonical và JSON-LD riêng. Trang chủ tập trung thương hiệu/tổng quan; trang giá tập trung chi phí.

Bản xem trước dùng `noindex,nofollow` và robots Disallow để tránh ảnh hưởng website đang hoạt động. Trước khi thay thế site thật: kiểm tra nội dung/giá/hồ sơ, hoàn thành kiểm tra trình duyệt, tích hợp tiếp nhận liên hệ nếu cần, đổi robots sang Allow và bỏ noindex trong `build.py`, tạo lại HTML, kiểm tra canonical/sitemap và lập chuyển hướng cho các URL WordPress cũ. Sitemap hiện có sẵn trong dist.

## Đưa lên GitHub

Tạo repository riêng tư mới tên `congviennghiatrang-lac-hong-vien`. Đẩy toàn bộ thư mục dự án (ngoại trừ `.openai`, `.git` và thông tin đăng nhập). Không thay đổi website đang chạy hay DNS khi chưa chuẩn bị chuyển đổi.

```sh
git init -b main
git add .
git commit -m "Build Lac Hong Vien information website"
git remote add origin https://github.com/YOUR-ACCOUNT/congviennghiatrang-lac-hong-vien.git
git push -u origin main
```

Với hosting tĩnh, dùng `dist` làm thư mục xuất bản ở gốc domain. Các đường dẫn bắt đầu bằng `/`; nếu dùng GitHub Pages dưới một subpath repository, cần sửa base path hoặc dùng custom domain. Phiên bản này không tự bật GitHub Pages, không đổi DNS và không thay thế WordPress.

## Kiểm tra đã thực hiện

- 14 tệp HTML (13 nội dung + 404).
- 398 tham chiếu nội bộ hợp lệ, kiểm tra H1 và metadata.
- Kiểm tra cú pháp JavaScript bằng Node.
- Kiểm tra giao diện trực tiếp chưa hoàn tất vì môi trường trình duyệt bị timeout.
