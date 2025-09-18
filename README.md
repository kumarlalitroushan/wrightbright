# 📝 WriteBright – Blog Application

A full-stack blog application built with **Django** and **Django REST Framework** featuring:  
- User registration, login, logout, and password reset
- Blog CRUD operations (Create, Read, Update, Delete)  
- Secure authentication using **JWT tokens**  
- Role-based access (Users manage their own blogs, Admins manage all blogs)  
- UI built with **Django Templates + Bootstrap**  
- API endpoints documented with **Swagger / OpenAPI**  
- Pagination (5 blogs per page on homepage)  
- “Read More” functionality for viewing full blog posts  

---

## 🚀 Features  

- **Authentication**  
  - Signup, Login, Logout  
  - JWT-based authentication for APIs  
  - Password reset via email (Forget Email feature)  

- **Blog Management**  
  - Logged-in users can create, update, and delete their own blogs  
  - Admins can manage all blogs via the Django Admin panel  
  - Blogs contain: `title`, `body`, `author`, `created_at`  

- **Frontend UI**  
  - Homepage showing all blog posts (paginated)  
  - Blog detail view with “Read More”  
  - Bootstrap-styled templates for login, signup, blog list, and forms  

- **REST API**  
  - Full CRUD operations on blogs  
  - JWT-secured endpoints for Create, Update, Delete  
  - Public can view blogs without login  

---

## 🛠️ Tech Stack  

- **Backend:** Django, Django REST Framework  
- **Authentication:** JWT (djangorestframework-simplejwt)  
- **Frontend:** Django Templates, Bootstrap  
- **Database:** SQLite (default, can be swapped with PostgreSQL/MySQL)  
- **Testing:** Pytest (with requests for API testing)  
- **API Docs:** Swagger / drf-yasg  

---

## ⚡ Installation & Setup  

1. Clone this repository:  
   ```bash
   git clone https://github.com/yourusername/writebright.git
   cd writebright
   ```

2. Create and activate a virtual environment:  
   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux/Mac
   venv\Scripts\activate      # Windows
   ```

3. Install dependencies:  
   ```bash
   pip install -r requirements.txt
   ```

4. Run migrations:  
   ```bash
   python manage.py migrate
   ```

5. Create superuser (for admin access):  
   ```bash
   python manage.py createsuperuser
   ```

6. Start the server:  
   ```bash
   python manage.py runserver
   ```

---

## 🌐 API Endpoints  

### Authentication  
- `POST /token/` – Get JWT token (login)  
- `POST /token/refresh/` – Refresh JWT token  
- `POST /auth/signup/` – Signup new user  
- `POST /auth/logout/` – Logout user  
- `POST /auth/password-reset/` – Request password reset email  
- `POST /auth/password-reset-confirm/` – Reset password with token  

### Blogs  
- `GET /api/blogs/` – List all blogs (public)  
- `POST /api/blogs/` – Create new blog (auth required)  
- `GET /api/blogs/{id}/` – Get single blog details  
- `PUT /api/blogs/{id}/` – Update own blog (auth required)  
- `DELETE /api/blogs/{id}/` – Delete own blog (auth required)  

---

## 🎨 UI Pages  

- `/` → Homepage with paginated blogs  
- `/signup/` → User signup page  
- `/login/` → Login page  
- `/logout/` → Logout user  
- `/create/` → Create blog form (auth required)  
- `/blogs/{id}/` → Blog detail page with full content  
- `/password-reset/` → Request reset link  
- `/password-reset-confirm/{uid}/{token}/` → Enter new password  

---

## 📌 Project Relevance to Testing  

- Demonstrates knowledge of **JWT authentication testing**  
- Covers **unit, API, and integration testing** using pytest  
- Includes **end-to-end tests with real HTTP requests**  
- Showcases ability to test role-based permissions (User vs Admin)  
