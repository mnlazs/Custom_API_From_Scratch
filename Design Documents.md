# Design Documents

## 1. Writeups of the Design

### 1.1 Overview

Describe the purpose of your application. Include information about the theme, which is "Astronomy Picture of the Day," and explain how your application fits within this theme.

### 1.2 Features

### User Registration:

#### Description:
Users will be able to create accounts on our platform, allowing them to personalize their experience and receive tailored content.

#### Implementation:
1. **Sign-up Form:** Users will fill out a registration form with essential details (username, email, password).
2. **Email Verification:** A verification email will be sent to the provided email address to confirm the user's identity.
3. **Account Management:** Users can log in, update their profile, and manage their account settings.

### 2. Alert System:

#### Description:
To keep users engaged, the application will offer an alert system to notify them when a new Astronomy Picture of the Day is available.

#### Implementation:
1. **User Preferences:** Users can set preferences for the frequency and timing of alerts.
2. **Push Notifications:** Alerts will be sent as push notifications to the user's device.
3. **Email Notifications:** An option for users to receive alerts via email.

### 3. NASA API Integration:

#### Description:
The application will connect to NASA's API to retrieve the Astronomy Picture of the Day, ensuring the content is up-to-date and accurate.

#### Implementation:
1. **API Key Authentication:** Users will provide their NASA API key during the initial setup.
2. **API Request:** The application will make a daily request to NASA's API to fetch the Astronomy Picture of the Day.
3. **Error Handling:** Implement mechanisms to handle API errors and ensure a smooth user experience.

### 4. Database Storage:

#### Description:
The application will store user-selected dates and associated images to personalize the user experience and allow them to revisit their favorite pictures.

#### Implementation:
1. **User Data Storage:** User profiles and preferences will be stored in a user database.
2. **Image Storage:** Images fetched from NASA's API will be stored in a secure and scalable image database.
3. **Date-Image Mapping:** A mapping system will associate selected dates with the corresponding Astronomy Pictures of the Day.


### 1.3 Technology Stack

List the tools and technologies you plan to use for the project:

- **Frontend:** [e.g., React, Angular, or Vue]
- **Backend:** [e.g., Node.js, Django, Flask, or Express]
- **Database:** [e.g., MongoDB, MySQL, or PostgreSQL]
- **NASA API:** [Provide the link to the API documentation]
- **Hosting:** [e.g., Heroku, AWS, or Azure]

### 1.4 Development Timeline

Estimate the time you expect to spend on each part of the development:

- **User Registration:** [Estimated time]
- **Alert System:** [Estimated time]
- **NASA API Integration:** [Estimated time]
- **Database Setup:** [Estimated time]
- **Testing and Debugging:** [Estimated time]

## 2. API Documentation

Provide a detailed document on how your application will interact with NASA's API. Include:

- Endpoints used
- Authentication process (using the API key)
- Expected response format
- Error handling mechanisms

## 3. Database Documentation

Create UML diagrams or similar documentation to illustrate the database structure. Include:

- Entity-Relationship Diagram (ERD)
- Data types for each attribute
- Relationships between tables
- Primary and foreign keys

## 4. Wireframes

Create wireframes for the user interface (UI) of your application. Include screens for:

- User Registration
- User Dashboard
- Alert Settings
- Display of Astronomy Picture of the Day
- Date Selection and Image Storage

Ensure that the wireframes convey the flow of user interactions and the overall user experience.

Once you have these documents ready, organize them in a directory named "Design Documents" and store it in your Git repository. This will serve as a comprehensive guide for both you and your team during the development phase.
