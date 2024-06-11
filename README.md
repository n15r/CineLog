<div align="center">
  <img src="https://github.com/nashunch0/CineLog/blob/main/media/OIG2.png" alt="Logo CineLog" style="width:200px;height:200px;")>
<h1>  CineLog</h1>
<p>Python Flask-Based Movie Rating Application </p>
<p>
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/python-3.8%2B-blue.svg" alt="Python"></a>
  <a href="https://flask.palletsprojects.com/"><img src="https://img.shields.io/badge/Flask-1.1.2-blue.svg" alt="Flask"></a>
  <a href="https://www.sqlalchemy.org/"><img src="https://img.shields.io/badge/SQLAlchemy-1.3.23-blue.svg" alt="SQLAlchemy"></a>
  <a href="https://wtforms.readthedocs.io/"><img src="https://img.shields.io/badge/WTForms-2.3.3-blue.svg" alt="WTForms"></a>
  <a href="https://www.sqlite.org/"><img src="https://img.shields.io/badge/SQLite-3-blue.svg" alt="SQLite"></a>
  <a href="https://www.themoviedb.org/documentation/api"><img src="https://img.shields.io/badge/MovieDBAPI-3-blue.svg" alt="Movie DB API"></a>
  <a href="https://github.com/nashunch0/CineLog/blob/main/LICENSE"><img src="https://img.shields.io/badge/license-MIT-green.svg" alt="License"></a>
<br>
<br>  
 <h2>  <a href="https://cinelog-zzt2.onrender.com">Live Demo</a> </h2>

</p>
</div>

## Interface
<div align="center">
  <img src="https://github.com/n15r/CineLog/blob/main/media/demonstration.gif" alt="Screenshot" style="width:100%;height:100%;">
</div>



## Technologies Used 
#### Programming Languages:
* Python 3.7.4
* HTML & CSS & JS  
#### Frameworks and Libraries:
* Flask 1.1.1
* WTForms
* SQLAlchemy
* Bootstrap 3.3.7
#### Database:
* SQLite
#### APIs:
* **Movie DB API** 

## Application Arborescence
```bash
├── app.py
├── forms.py
├── models.py
├── instance
│   └── movies-project.db
├── static
│   ├── css
│   │   └── files.css
│   └── logo.png
├── templates
    ├── base.html
    ├── add.html
    ├── catalogue.html
    ├── edit.html    
    └──  index.html
```
## Application Structure
### Files
* **app.py**: The heart of our app, where Flask magic happens.
* **models.py**: Defines our movie and user entities using SQLAlchemy.
* **forms.py**: Contains WTForms for adding and rating movies.

### Directories
* **templates/**: Home to the html/Jinga2 templates
* **static/**: Holds the css files
## Features ✨
### Movie Management
* **Search for movies** by title using the Movie DB API.
* **Add movies** to the database with ease.
* **Delete movies** from the DB instance.
* **Modify rating** and comments.

## Local Run

1. **Clone and install prerequisites**
   
     Run in your terminal, you can copy this (On Windows, use `venv\Scripts\activate` instead)
   ```bash
   sudo apt-get update # bash only
   git clone https://github.com/n15r/Cinelog.git
   cd Cinelog
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```
   
3. **Set Up the API**  
   
   You can get your TMDB key from their [website](https://www.themoviedb.org/documentation/api) (you need to create an account), then create a .env file in the project directory and add your TMDB API key to it.
   
   The .env file should look like this: (**friendly reminder** to always encapsulate your API keys)
   
<div align="center">
    <img src="https://github.com/n15r/CineLog/assets/130777185/5d13b4f9-02b3-43fa-ab57-0bb9419cceea" alt=".env screenshot">
</div>

<br>

3. **Run the project**

After decommenting the lines indicated in the app.py file, you ou can now run the project by using the command`python3 app.py`, you should see output similar to the following:

```bash
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 646-082-58
```
Go to your browser and input the link (or CTRL click on the link)


## Features to be added 

* **A Front-end overhaul.**
* **Merge the add and select apps with the main page using some js magic.**
* **Introduce user authentication for account creation and saving ratings and reviews.**
* **Enhance movie search to allow filtering by year, genre, and more.**
* **Display top-rated movies on the home page for a quick pick-me-up.**


## Context
  This project, conducted as part of the third year curriculum at the Moroccan School of Engineering Sciences 
  
## Author

👤 **Nassim Lachkar**

* Email: nassim.lachkar@emsi-edu.ma
* Github: [@n15r](https://github.com/n15r/)
* LinkedIn: [https://www.linkedin.com/in/nlachkar/](https://www.linkedin.com/in/nlachkar/)

## Show your support

Give a ⭐️ if this project helped you!
