# AirBnB Clone - The Console | ALX SE Program

[![HolBnB clone](https://github.com/monoprosito/AirBnB_clone/raw/feature/console/hBnB.png?raw=true)](https://github.com/monoprosito/AirBnB_clone/blob/feature/console/hBnB.png?raw=true)

The AirBnB Clone - The Console project is part of the ALX SE Program and aims to create a command-line interface (CLI) to manipulate the storage system.

## Description

The AirBnB Clone - The Console project is part of the ALX SE Program and aims to create a command-line interface (CLI) that replicates some of the functionality of the popular online accommodation marketplace, Airbnb. The project focuses on developing a functional console that allows users to interact with the application through a command-line interface, providing features for managing and manipulating data related to properties, users, and bookings.

The console provides a convenient way to create, update, and delete instances of various classes, such as User, Place, City, State, Amenity, and Review.

The project implements a model-view-controller (MVC) architecture, where the console acts as the controller. It interacts with the application's data models to perform operations and retrieve information. The console also incorporates features such as input validation, error handling, and data serialization to ensure data integrity and smooth user experience.

## Usage

To use the HBNB Console, follow these steps:

1.  Clone the repository from GitHub to your local machine `git clone https://github.com/Ahmedsaed/AirBnB_clone`
    
2.  Install Dependencies: `python3.8.5`, `pycodestyle` and `gnu make`
    
3.  Run the program by typing the following command: `python3.8 console.py` or `./console.py` or `make run`
    
4.  Once the console is running, you can type commands into the command prompt and the program will execute them.
  

## Features

The HBNB console program supports the following features:

-   Command-line interface (CLI) for interacting with the application
-   Classes for managing various types of data:
    -   User
    -   Place
    -   City
    -   State
    -   Amenity
    -   Review
-   Create objects and save them to storage
-   Retrieve objects from storage
-   Update object attributes and save them to storage
-   Delete objects from storage
-   Display all objects or all instances of a specific class
-   Count the number of objects or instances of a specific class

## Examples

**Launching the console**

```
$ ./console.py
(hbnb)

```

**Creating a new object**

```
(hbnb) create
** class name missing **
(hbnb) create User
7a541f64-8368-4b2f-85d5-43561273420d

```

**Show an object**

```
(hbnb) show User
** instance id missing **
(hbnb) show User 14018c12-d362-4203-a1e3-9e2b6084ba73
[User] (14018c12-d362-4203-a1e3-9e2b6084ba73) <{'id': '14018c12-d362-4203-a1e3-9e2b6084ba73', 'created_at': datetime.datetime(2023, 7, 15, 17, 43, 26, 908852), 'updated_at': datetime.datetime(2023, 7, 15, 17, 43, 26, 908880)}>

```

**Update an object**

```
(hbnb) all
[User] (70f71c16-962b-48ad-9df8-9203fe23d612) {'created_at': datetime.datetime(2020, 2, 19, 18, 11, 32, 341144), 'id': '70f71c16-962b-48ad-9df8-9203fe23d612', 'updated_at': datetime.datetime(2020, 2, 19, 18, 11, 32, 341161)}">
(hbnb) update
** class name missing **
(hbnb) update User
** instance id missing **
(hbnb) update User 70f71c16-962b-48ad-9df8-9203fe23d612
** attribute name missing **
(hbnb) update User 70f71c16-962b-48ad-9df8-9203fe23d612  Age "20"
(hbnb) all
[User] (70f71c16-962b-48ad-9df8-9203fe23d612) {'created_at': datetime.datetime(2020, 2, 19, 18, 11, 32, 341144), 'id': '70f71c16-962b-48ad-9df8-9203fe23d612', 'updated_at': datetime.datetime(2020, 2, 19, 18, 11, 32, 341161), 'Age': '20'}">

```

## Authors

This program was developed by [patrice OKLOU](https://www.github.com/patrice012) and [Salome ESSIEN](https://www.github.com/Salome007) as part of the ALX SE Program.

