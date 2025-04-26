# 🍅 HỆ THỐNG NHẬN DIỆN BỆNH TRÊN CÂY CÀ CHUA BẰNG HÌNH ẢNH

Ứng dụng nhận diện bệnh cây cà chua được xây dựng bằng Flutter, kết nối với backend YOLOv12 Nano (FastAPI) để quét ảnh lá cây và dự đoán bệnh.

## 🔗 Liên kết dự án

🧠 **Backend (FastAPI + YOLOv12 Nano):**  
👉 [Tomato Disease Detection Backend](https://github.com/aresu-1704/tomato-disease-detect_backend-yolov12)

💻 **Frontend (Flutter):**  
👉 [Tomato Disease Detection Frontend](https://github.com/aresu-1704/tomato_detect_app_frontend)

---

## 📌 Mô tả

Hệ thống nhận diện bệnh trên cây cà chua gồm **2 thành phần chính**:

- 📱 **Ứng dụng di động Flutter (Frontend):**  
  Giúp người dùng dễ dàng chụp ảnh lá cây, gửi ảnh lên server và hiển thị kết quả dự đoán. Giao diện thân thiện, dễ sử dụng cho cả nông dân và kỹ thuật viên.

- 🧠 **Hệ thống phân tích bệnh (Backend - FastAPI + YOLOv12 Nano):**  
  Nhận ảnh từ người dùng, chạy mô hình học sâu (YOLOv12 Nano) để xác định vùng lá bệnh và phân loại loại bệnh (mốc sương, xoăn lá, đốm vi khuẩn, v.v.).

### ✅ Các tính năng nổi bật:

- **Chụp ảnh hoặc chọn ảnh lá cây từ thư viện.**
- **Tự động khoanh vùng vùng bệnh bằng mô hình YOLOv12.**
- **Dự đoán loại bệnh chính xác bằng AI.**
- **Hiển thị kết quả trực quan và dễ hiểu.**
- **Lưu lịch sử ảnh.**

### 🎯 Mục tiêu dự án

Hỗ trợ nông dân và kỹ thuật viên nông nghiệp **phát hiện sớm** và **xử lý kịp thời** các loại bệnh thường gặp trên cây cà chua, giúp **giảm thiểu thiệt hại mùa vụ**, tăng hiệu quả sản xuất.

---

# 🛠️ Tomato Disease Detection BACKEND API - YOLOv12 Nano (FastAPI)

Đây là backend API được xây dựng bằng [FastAPI](https://fastapi.tiangolo.com/) cho hệ thống **Nhận diện bệnh cây Cà Chua** bằng mô hình **YOLOv12 Nano**.

## 🚀 Tính năng chính

### 🔐 Authentication
- `POST /auth/login`: Đăng nhập
- `POST /auth/register`: Đăng ký tài khoản
- `POST /auth/reset-password`: Đặt lại mật khẩu
- `POST /auth/send-otp`: Gửi mã OTP
- `POST /auth/verify-otp`: Xác minh mã OTP

### 🔬 Dự đoán bệnh cây cà chua
- `POST /predict/predict-image`: Tải ảnh lên để dự đoán bệnh lá cà chua

### 🧾 Lịch sử dự đoán
- `POST /disease-history/save`: Lưu lại lịch sử dự đoán bệnh
- `GET /disease-history/get-by-id/{user_id}`: Lấy lịch sử dự đoán theo `user_id`

---

## 🧠 Mô hình sử dụng
- **YOLOv12 Nano**: phát hiện lá bị bệnh cây cà chua (bounding box)
- Sau khi cắt vùng chứa lá bệnh, sử dụng CNN để phân loại loại bệnh cụ thể

---

## 🧰 Công nghệ
- `FastAPI` – backend framework
- `YOLOv12 Nano` – phát hiện lá bệnh
- `CNN` – phân loại bệnh
- `Pydantic`, `Uvicorn`, `PostgreSQL`

---

## 📦 Cài đặt Backend

### ⚙️ Yêu cầu:
- Python 3.11+
- pip

### 🧪 Các bước setup:

```bash

# Clone repo
git clone https://github.com/aresu-1704/tomato-disease-detect_backend-yolov12.git
cd tomato-disease-detect_backend-yolov12

# Tạo môi trường ảo
python -m venv venv
source venv/bin/activate  # Windows: .\venv\Scripts\activate

# Cài đặt thư viện
pip install -r requirements.txt

# Chạy server
uvicorn main:app --reload
```
---

## 🗃️ Cài đặt Cơ sở Dữ liệu

### ⚙️ Yêu cầu:
- PostgreSQL

### 🧪 Các bước setup:

```bash

#Chạy Script database
psql -U your_postgres_user -d your_database_name -f .DATABASE_SCHEMAS/postgreSQL_database.sql
```

## **⚠️ Lưu ý:**

- Đảm bảo bạn đã cài đặt PostgreSQL và đã tạo một cơ sở dữ liệu trống.

- Thay your_postgres_user bằng tên người dùng PostgreSQL của bạn.

- Thay your_database_name bằng tên cơ sở dữ liệu mà bạn muốn sử dụng.

---



### 🖼️ Hình ảnh giao diện ứng dụng

#### 🔐 Xác thực người dùng
<p align="center">
  <img src="images/UI/login.jpg" width="150"/>
  <img src="images/UI/register.jpg" width="150"/>
  <img src="images/UI/forgot-password.jpg" width="150"/>
  <img src="images/UI/verify-otp.jpg" width="150"/>
  <img src="images/UI/reset-password.jpg" width="150"/>
</p>

---

#### 🌿 Nhận diện bệnh cây
<p align="center">
  <img src="images/UI/camera-upload.jpg" width="300"/>
  <img src="images/UI/predict-result.jpg" width="300"/>
</p>

---

#### 📜 Lịch sử & chi tiết dự đoán
<p align="center">
  <img src="images/UI/history.jpg" width="300"/>
</p>

---

#### 📡 Giao diện API (Swagger UI)
<p align="center">
  <img src="images/API/api.jpg" width="800"/>
</p>




