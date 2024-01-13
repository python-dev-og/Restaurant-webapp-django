![Python 3.11](https://img.shields.io/badge/python-3.11-blue.svg)
![Django](https://img.shields.io/badge/django-5.0.1-092E20.svg)
![SQLite](https://img.shields.io/badge/sqlite-3.x-07405E.svg)
![Web Frameworks](https://img.shields.io/badge/web%20frameworks-Django-blue.svg)


# Django Restaurant Web App Portal

## Overview
This restaurant web app is a Django-based web application that showcases a variety of gourmet meals. 
It provides users with an elegant interface to explore different meal options ranging from starters to desserts. 
The application includes features for viewing detailed information about each meal item, including its price, availability, and description. 
This README provides an overview of the project setup, structure, and usage.

### Prerequisites
- Python (3.x)
- Django (2.x or 3.x)
- Database (SQLite by default, configurable to PostgreSQL, MySQL, etc.)

### Installation
1. **Clone the Repository**
   ```
   git clone [repository-url]
   cd [repository-name]
   ```

2. **Create and Activate Virtual Environment** (Optional but recommended)
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**
   ```
   pip install -r requirements.txt
   ```

4. **Database Migrations**
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create Superuser** (Optional but recommended for admin access)
   ```
   python manage.py createsuperuser
   ```

6. **Run the Server**
   ```
   python manage.py runserver
   ```

### Features
- **Menu Listing**: Users can view a list of all available meals, sorted by their creation date.
- **Meal Categories**: Meals are categorized into Starters, Salads, Main Dishes, and Desserts.
- **Detailed Meal Information**: Clicking on a meal item shows detailed information, including its description, price, and availability.
- **Admin Interface**: Admins can add, edit, or delete meal items through Django's admin interface.

### Application Structure
- **Models (`models.py`)**: Defines the `Item` model with fields like `meal`, `description`, `price`, `meal_type`, `author`, `status`, `date_created`, and `date_updated`.
- **Views (`views.py`)**: Contains `MenuList` for listing meals and `MenuItemDetail` for showing meal details.
- **Templates**: HTML templates for rendering the meal list (`index.html`) and meal details (`menu_item_detail.html`).

### Contributing
Contributions to GourmetHub are welcome. Please follow the standard procedures for contributing to open-source projects:
1. Fork the repository.
2. Create a new branch for your feature.
3. Commit and push your changes.
4. Create a pull request.


## License
This project is licensed under the MIT License 

**Note**: Replace `[repository-link]` and `[app-directory]` with actual values. Ensure to provide correct database configurations in `settings.py`. This README assumes a standard Django project structure and default settings.

## Final Look

![homepage.png](images%2Fhomepage.png)

![meal.png](images%2Fmeal.png)