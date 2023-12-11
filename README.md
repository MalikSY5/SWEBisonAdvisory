# AI Student Advisor Backend (WIP)

This is the backend for a project that is an AI-powered student advisor that helps students plan their courses, track their progress towards graduation, and generate PINs for registration. The backend is built with Django and uses APIs and databases to manage and retrieve data.

## Features

- Robust backend built with Django
- Data management through APIs and databases

## Backend Technologies

- Django: A high-level Python Web framework that encourages rapid development and clean, pragmatic design.
- APIs: Used for communication between different software components.
- Databases: Used for storing and retrieving user data and course information.

## Getting Started

To get started with the AI Student Advisor, follow these steps:

1. Clone the repository to your local machine
2. Install the required dependencies using `pip install -r requirements.txt`
3. Set up the database and run migrations
4. Run the Django server using `python manage.py runserver`
5. Navigate to `http://localhost:8000` in your web browser

## Usage

Need to run the backend server before the frontend so they can connect.

## To Be Implemented

- [x] Login Functionality
  - [x] Login can redirect to multiple dashboards
  - [x] Login takes a user_id and password
  - [x] Login cross references the database
- [x] Account Functionality
  - [x] User has roles: Student, Admin, Advisor
  - [x] Account Info page will display at the account/ endpoint
- [ ] Student Functionality
  - Only Need to implement two to three aspects
  - [ ] Students can view their past courses
  - [ ] Students will get AI suggested courses for next semester (MUST)
  - [ ] Students can fill out a registration form
  - [ ] Upon successful form completion students will receive their registration PIN
  - [ ] Upon successful registration the website updates the class participants
  - [ ] Upon successful registration the website updates their checklist
  - [ ] Anything else yall can think of
- [ ] Advisor Functionality
  - [ ] Advisors can see their assigned students
  - [ ] Advisors can view, create, and edit a student checklist
  - [ ] Advisors can view and sign error registration forms
  - [ ] Anything else yall can think of
- [ ] Admin Functionality
  - [ ] Admin can change course descriptions
  - [ ] Admin can assign professors to teach a class
  - [ ] Admin can set valid electives for each major
  - [ ] Anything else yall can think of
