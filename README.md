# Python MongoDB Storage
![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)
<br>

## Description
This is my first Python application that will use MongoDB for storage. It will exercise all basic CRUD operations to manipulate the database.
<br>

### ***Some notes about the Python pymongo module:***<br>
 - The module provides classes and methods to connect to a MongoDB server, select databases and collections, and perform operations on documents within collections.<br>
 - You can perform CRUD operations (Create, Read, Update, Delete) on documents using methods like insert_one(), find(), update_one(), delete_one(), etc.<br>
 - Pymongo can handle different data types, including strings, numbers, dates, arrays, embedded documents, and more.<br>
 - It also supports both synchronous and asynchronous programming paradigms, allowing you to choose the style that best fits your application's needs.<br>

### ***Some notes about the Python uuid module:***<br>
 - UUIDs are useful for generating unique identifiers in various applications, such as database records, distributed systems, and network protocols.<br>
 - UUIDs are typically represented as strings in the format "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx", where each "x" represents a hexadecimal digit.<br>
 - You can convert a UUID to and from its string representation using the str() and uuid.UUID() functions, respectively.<br>

### ***Some notes about the Python json module:***<br>
 - The json module allows you to encode (serialize) Python objects into JSON format and decode (deserialize) JSON data into Python objects.<br>
 - json.dumps() is used to convert a Python object into a JSON string representation.<br>
 - json.loads() is used to parse a JSON string and convert it back into a Python object.<br>
 - The module supports pretty printing of JSON data for better readability using the json.dumps() function with the indent parameter.<br>

## *Installation & Usage*
To install this app, simply clone the repository and run the `mongo.py` file in your terminal.<br>
I have left the username and password in the code so anyone can play with this database in the cloud.<br>
<br>
<img src="images/screenshot.JPG" alt="screenshot" width="500"/>
<br>


### When prompted:<br>
Choose one of the options by typing the corresponding number and pressing enter.<br>

- If you choose to create a new container, you will be prompted to enter the container's information.<br>
<img src="images/screenshot1.JPG" alt="screenshot1" width="500"/><br>

- If you choose to Read, it will display ALL of the containers and their content.<br>
<img src="images/screenshot2.JPG" alt="screenshot2" width="500"/><br>

- If you choose to update a container, you will be prompted to enter the container_id of the container you wish to update, and then you will select which data you wish to change.<br>
<img src="images/screenshot3.JPG" alt="screenshot3" width="500"/><br>

- If you choose to delete a container, you will be prompted to enter the container_id of the container you wish to delete, then asked for confirmation to delete.<br>
<img src="images/screenshot4.JPG" alt="screenshot4" width="500"/><br>

- If you choose to exit the application, the application will close.<br>
<br>
<br>

## *Questions*
<h3>Portfolio:&emsp;<a href="https://jk377y.dev" target="_blank">https://jk377y.dev</a></h3>
<h3>Email:&emsp;<a href="mailto:jk377y@gmail.com" target="_blank">jk377y@gmail.com</a></h3>
<h3>LinkedIn:&emsp;<a href="https://www.linkedin.com/in/james-kelly-software-developer/" target="_blank">https://www.linkedin.com/in/james-kelly-software-developer/</a></h3>
<h3>GitHub:&emsp;<a href="https://github.com/jk377y" target="_blank">https://github.com/jk377y</a></h3>
<br>

## *License*
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
<br>Copyright (c) 2023 James Kelly
<br>Information on this license can be found at: (https://opensource.org/licenses/MIT)