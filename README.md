# Contact Management System

## Overview

The Contact Management System is a web-based application that allows users to efficiently manage contact information. Users can add, view, update, and delete contacts through an intuitive interface. The system helps organize contact details securely and provides easy access to stored information.

## Features

* Add new contacts
* View all contacts
* Update existing contact details
* Delete contacts
* Search contacts
* User-friendly interface
* Secure database storage

## Technologies Used

### Frontend

* HTML
* CSS
* JavaScript

### Backend

* Node.js
* Express.js

### Database

* MongoDB
* Mongoose

## Project Structure

```text
contact-management-system/
│
├── config/
│   └── db.js
│
├── models/
│   └── Contact.js
│
├── routes/
│   └── contactRoutes.js
│
├── controllers/
│   └── contactController.js
│
├── server.js
├── package.json
├── .env
└── README.md
```

## Installation

1. Clone the repository:

```bash
git clone <repository-url>
```

2. Navigate to the project folder:

```bash
cd contact-management-system
```

3. Install dependencies:

```bash
npm install
```

4. Configure environment variables in `.env`:

```env
PORT=5000
MONGO_URI=your_mongodb_connection_string
```

5. Start the server:

```bash
npm start
```

6. Open your browser or Postman to test the API.

## API Endpoints

### Create Contact

```http
POST /api/contacts
```

### Get All Contacts

```http
GET /api/contacts
```

### Get Contact By ID

```http
GET /api/contacts/:id
```

### Update Contact

```http
PUT /api/contacts/:id
```

### Delete Contact

```http
DELETE /api/contacts/:id
```

## Testing

Use Postman to test all CRUD operations.

## Future Enhancements

* User Authentication
* Contact Categories
* Export Contacts
* Advanced Search and Filtering

## Author

Developed as part of a web development learning project.
