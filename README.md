## Blog App

### Requirements
```
- python v3.12.3
- mysql database
- internet connection for the cdn (ajax, jquery, icons)
```

### Setup
1. Install the latest version of Python from its official documentation. Then add it to your system environment.
2. Navigate to the desired locaiton. Setup Django virtual environment using `py -m venv project-name`. Activate it using `project-name\Scripts\activate.bat`.
3. Clone this repository. Open a terminal in the project.
4. Install the dependencies by running `pip install -r requirements.txt`.
5. Start your database server. The system uses the database specified in the `.env` file.
6. Run `python manage.py makemigrations` to generate migration files.
7. Run `python manage.py migrate` to run these migrations.
8. Start the system by running `python manage.py runserver`.

### UI / Features Completed
1. Create an account by navigating to `Login` > `Create an account`. Then login using the credentials you provided.
2. Click `My Blogs` button to see the blogs you've created.
3. Create blog by clicking `Create Blog` button. The newly created blog will appear in `My Blogs` and `Home` pages.
4. The `edit` and `delete` functionalities are included in `My Blogs` page.
5. View blogs by clicking on the titles.

