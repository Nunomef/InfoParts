# InfoParts

**InfoParts** is a training project developed during a web development formation, aimed at learning and applying advanced Django concepts using [Django Oscar](https://django-oscar.readthedocs.io/en/latest/), a powerful and extensible e-commerce framework. The project simulates a functional e-commerce platform, demonstrating key features such as product management, templating, and modular architecture.

## Features

- **Django Oscar Integration** for a comprehensive e-commerce foundation  
- **Custom Templates** under `templates/oscar/` to personalize the storefront  
- **Organized Static and Media Files** for easy asset management  
- **Modular App Structure** in `apps/` for future extensibility and experimentation  

## Project Structure

```
InfoParts/
├── apps/                   # Custom Django apps
├── infoparts/              # Project configuration
├── media/                  # Media files (user uploads)
├── static/                 # Static files (CSS, JS, images)
│   └── img/                # Image assets
├── templates/
│   └── oscar/              # Django Oscar templates
├── manage.py               # Django management script
└── requirements.txt        # Python dependencies
```

## Getting Started

### Requirements

Before you begin, make sure you have the following installed:

- Python 3.8 or higher
- `pip` (Python package manager)
- (Optional) `virtualenv` for environment isolation

### Setup Instructions

1. **Clone the repository**  
   Clone the project to your local machine:
   ```bash
   git clone https://github.com/Nunomef/InfoParts.git
   cd InfoParts
   ```

2. **Create a virtual environment**  
   This helps keep your dependencies isolated:
   ```bash
   python -m venv env
   source env/bin/activate        # On Linux/macOS
   # OR
   env\Scripts\activate           # On Windows
   ```

3. **Install dependencies**  
   Use the provided `requirements.txt` to install all Python packages:
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

4. **Apply database migrations**  
   Set up the database schema:
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser**  
   Create an admin account to access the Django admin dashboard:
   ```bash
   python manage.py createsuperuser
   ```

6. **Start the development server**  
   Run the server locally:
   ```bash
   python manage.py runserver
   ```
   Then open your browser and go to: [http://127.0.0.1:8000](http://127.0.0.1:8000)

## Purpose

This project was built as part of a formation program to:

- Learn Django architecture and extend it
- Customize templates and app behavior
- Practice full-stack development and deployment basics

## License

This project is released under the [MIT License](LICENSE).
