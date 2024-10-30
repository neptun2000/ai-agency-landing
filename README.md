# AI Agency Landing Page

A modern AI agency landing page built with Flask and Vanilla JavaScript. This project showcases a responsive, animated landing page with a contact form and an admin dashboard for managing inquiries.

## Features

- 🎨 Modern, responsive design with Bootstrap dark theme
- ✨ Smooth animations and transitions
- 🌈 Rainbow illumination effects
- 📝 Contact form with database integration
- 🔐 Admin dashboard for managing inquiries
- 🚀 Easy deployment on Replit

## Technologies Used

- Backend: Flask (Python)
- Frontend: HTML5, CSS3, Vanilla JavaScript
- Database: PostgreSQL
- Styling: Bootstrap 5 (Dark Theme)
- Icons: Feather Icons
- Fonts: Inter (Google Fonts)

## Installation

1. Clone this repository to your Replit workspace
2. Install required dependencies:
   ```bash
   python -m pip install flask flask-sqlalchemy flask-login werkzeug
   ```
3. Set up the following environment variables in your Replit secrets:
   - `DATABASE_URL`: PostgreSQL connection string
   - `FLASK_SECRET_KEY`: Secret key for Flask sessions

## Usage

1. Run the Flask application:
   ```bash
   python main.py
   ```
2. The application will be available at `http://localhost:5000`

### Main Features:
- **Hero Section**: Showcases your brand with animated text effects
- **Services Section**: Displays your AI services with hover animations
- **Contact Form**: Allows visitors to send inquiries
- **Responsive Design**: Works seamlessly on all devices

## Admin Dashboard

Access the admin dashboard to view contact form submissions:

1. Navigate to `/admin/login`
2. Login credentials:
   - Username: `admin`
   - Password: `admin123`
3. View and manage contact form submissions in the dashboard

### Admin Features:
- Secure login system
- View all contact form submissions
- Submissions sorted by date (newest first)
- Logout functionality

## Deployment on Replit

1. Fork this repository to your Replit account
2. Set up the required environment variables in Replit Secrets
3. Click "Run" to start the application
4. Your site will be live at your Replit URL

## Project Structure

```
├── app.py           # Main Flask application
├── models.py        # Database models
├── extensions.py    # Flask extensions
├── static/
│   ├── css/        # Stylesheets
│   ├── js/         # JavaScript files
│   └── img/        # Images and SVGs
└── templates/
    ├── index.html   # Main landing page
    └── admin/       # Admin dashboard templates
```

## Customization

1. **Colors**: Update the Bootstrap theme variables in `static/css/style.css`
2. **Content**: Modify the content in `templates/index.html`
3. **Services**: Add or modify services in the services section
4. **Animations**: Adjust animation parameters in `static/css/style.css`

## Security Notes

- Change the default admin credentials in production
- Keep your `FLASK_SECRET_KEY` secure
- Regular database backups recommended
- Use HTTPS in production

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is open-source and available under the MIT License.
