<!-- TABLE OF CONTENTS -->

# Table of Contents

- [Habitko](#habitko)
  - [Habitko's Core Functionality](#habitkos-core-functionality)
- [Getting Started](#getting-started)
  - [Dependencies](#dependencies)
  - [How To Run the Program](#how-to-run-the-program)
  - [Test](#test)
- [Contributing](#contributing)
- [Contact](#contact)

# Habitko

Good habits are behaviors that we develop over time and can have a positive impact on our lives. Good habits can help us achieve our goals and improve our lives. There are many strategies for developing good habits, and one is using an app.

With this habit tracker, you can easily track your daily, weekly, monthly, or yearly habits and monitor your progress over time. This app offers a simple and attractive interface that allows you to check off your habits as you complete them. You can see details of your missed dates and completed dates. The program is a part of _IU University's_ _DLMCSPSE01_ course and uses Django 4.2.2.

## Habitko's Core Functionality

The habit tracker essentially allows a user to:

- Add a habit
- Delete a habit
- Edit a habit
- Mark a habit completed
- See all completed dates for a habit
- See all missed dates for a habit

# Getting Started

**Important**: Make sure that Python 3.8 + is installed on your OS. You can download the latest version of Python from [this link.](https://www.python.org/downloads/)

**Set Up a Virtual Environment in Python**

You can install venv to your host Python by running this command in your terminal:

```
pip3 install virtualenv
```

To use venv in your project, in your terminal, create a new project folder, cd to the project folder in your terminal, and run the following command:

```
python<version> -m venv <virtual-environment-name>
```

Like so:

```
 mkdir Habitko
 cd habitko
 python3 -m venv env
```

**How to Activate the Virtual Environment**

```
source env/bin/activate
```

This will activate your virtual environment. Immediately, you will notice that your terminal path includes env, signifying an activated virtual environment.

**Cloning Habitko**

While you're in the Habitko folder that you just created, clone the repo:

```
git clone https://github.com/DannyGetch/Full_Stack_Habit_Tracker
```

## Dependencies

To install the dependencies, please run the following command in the environment:

```
cd Full_Stack_Habit_Tracker
pip3 install -r requirements.txt
```

## How To Run the Program

After installing the dependencies, make sure you have them all by running the following command:

```
pip list
```

You should see the installed packages:

```
Package             Version
------------------- --------
asgiref             3.7.2
certifi             2023.5.7
charset-normalizer  3.2.0
crispy-bootstrap4   2022.1
Django              4.2.2
django-crispy-forms 1.14.0
django-extensions   3.2.3
exceptiongroup      1.1.2
Faker               12.0.1
freezegun           1.2.2
idna                3.4
iniconfig           2.0.0
mixer               7.2.2
packaging           23.1
pip                 21.2.4
pluggy              1.2.0
pytest              7.4.0
pytest-django       4.5.2
python-dateutil     2.8.2
setuptools          58.0.4
six                 1.16.0
sqlparse            0.4.4
test-utils          0.1.0
tomli               2.0.1
typing_extensions   4.6.3
urllib3             2.0.3
```

You can then start the server with the following command:

```
python3 manage.py runserver
```

If successful, the server will run:

```
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
July 17, 2023 - 08:58:36
Django version 4.2.2, using settings 'habitTracker.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

Since the server is running on port 8000, we can go to any browser and type the address like this to see our web app:

```
http://localhost:8000/
```

or

```
http://127.0.0.1:8000/
```

# Test

To test the functionalities just run:

```
pytest
```

# Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

# Contact

Daniel Mekonnen - [Email](mailto:dannygetch@gmail.com)

Project Link: [https://github.com/DannyGetch/Habit_Tracker](https://github.com/DannyGetch/Habit_Tracker)
