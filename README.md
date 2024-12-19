Object-Oriented Programming Final Project:

Overview

This repository contains my final project for the Object-Oriented Programming (OOP) course. The project demonstrates the application of OOP principles by utilizing the New York Times (NYT) API to fetch and organize article metadata into CSV files. Users can query articles based on keywords and time intervals, and the project applies basic filtering to save relevant data.

Features

Integration with the NYT API: Fetches real-time data from the New York Times.

Article Metadata Extraction: Organizes article data into CSV files for easy analysis.

Flexible Query System: Allows users to customize queries and time intervals.

Data Filtering: Filters articles based on keywords in headlines or metadata.

Object-Oriented Design: Leverages OOP principles like encapsulation and modularity to structure the code.

Prerequisites

Python: Ensure Python (version 3.8 or later) is installed on your system.

API Key: Obtain an API key from the New York Times Developer Portal to access the NYT API.

Installation

Clone the repository:

git clone git clone https://github.com/Kyle-Raymundo/oop-final-project.git

Navigate to the project directory:

cd oop-final-project

Install the required dependencies:

pip install -r requirements.txt

Configuration

Create a .env file in the project root.

Add your NYT API key to the .env file:

NYT_API_KEY=your_api_key_here

Modify the query and time interval in the script if needed:

query = "Your Query Here"
years = range(start_year, end_year)
months = range(start_month, end_month)

Usage

Run the main script:

python main.py

The script will fetch articles, filter them based on the query, and save the metadata as CSV files in the project directory.

Project Structure

main.py: Entry point of the application.

api_handler.py: Handles interactions with the NYT API.

filters.py: Implements the filtering logic.

models.py: Defines the OOP models used in the project.

utils.py: Includes utility functions for data processing.

Learning Objectives

Apply OOP principles to design and implement a real-world application.

Gain hands-on experience working with RESTful APIs.

Understand how to process and filter JSON data programmatically.

Future Enhancements

Add a graphical user interface (GUI) for improved user experience.

Enhance filtering options with more advanced criteria.

Include unit tests for better code reliability.

License

This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgments

The New York Times for providing a comprehensive API.

My OOP instructor for guidance and support throughout the course.

