# Eden Springs SDA Church Camp Meeting 2025 - Setup Guide

This Django project creates a beautiful, responsive landing page for the Eden Springs SDA Church Camp Meeting 2025 with M-Pesa integration for contributions.

## Features

- **Responsive Design**: Beautiful, modern design using TailwindCSS and DaisyUI
- **Real-time Countdown**: Live countdown timer to the event
- **Contribution Tracking**: Real-time progress tracking with visual progress bars
- **M-Pesa Integration**: STK Push integration for seamless mobile payments
- **Admin Dashboard**: Django admin interface for managing contributions
- **Real-time Updates**: Live statistics updates without page refresh

## Project Structure

```
camp_meeting_project/
├── camp_meeting/
│   ├── models.py          # Contribution and Settings models
│   ├── views.py           # Main views and API endpoints
│   ├── forms.py           # Contribution form
│   ├── admin.py           # Admin interface configuration
│   ├── urls.py            # URL patterns
│   └── migrations/        # Database migrations
├── templates/
│   └── camp_meeting/
│       └── landing.html   # Main landing page template
├── static/               # Static files (CSS, JS, Images)
├── requirements.txt      # Python dependencies
└── settings.py          # Django settings
```

## Installation & Setup

### 1. Clone and Setup Virtual Environment

```bash
# Create project directory
mkdir camp_meeting_project
cd camp_meeting_project

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Environment Configuration

Create a `.env` file in your project root:

```env
SECRET_KEY=your-django-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Database (if using PostgreSQL)
DB_NAME=camp_meeting_db
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=localhost
DB_PORT=5432

# M-Pesa Configuration
MPESA_ENVIRONMENT=sandbox
MPESA_CONSUMER_KEY=your_consumer_key
MPESA_CONSUMER_SECRET=your_consumer_secret
MPESA_SHORTCODE=your_shortcode
MPESA_PASSKEY=your_passkey
MPESA_CALLBACK_URL=https://yourdomain.com/api/mpesa/callback/

# Email Configuration
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your_email@gmail.com
EMAIL_HOST_PASSWORD=your_email_password
DEFAULT_FROM_EMAIL=noreply@edensprings.org
```

### 4. Database Setup

```bash
# Create and apply migrations
python manage.py makemigrations
python manage.py migrate

# Create superuser for admin access
python manage.py createsuperuser
```

### 5. Create Required Directories

```bash
mkdir -p logs
mkdir -p static
mkdir -p media
mkdir -p templates/camp_meeting
```

### 6. Collect Static Files

```bash
python manage.py collectstatic
```

### 7. Run Development Server

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` to see your site!

## M-Pesa Integration Setup

### 1. Safaricom Developer Account

1. Register at [Safaricom Developer Portal](https://developer.safaricom.co.ke/)
2. Create a new app
3. Get your Consumer Key and Consumer Secret
4. For production, get Business Shortcode and Passkey

### 2. STK Push Configuration

The project includes a basic M-Pesa STK Push implementation. You'll need to:

1. Complete the M-Pesa API integration in `views.py`
2. Set up callback URL handling
3. Implement transaction verification
4. Add proper error handling

### 3. Testing

For sandbox testing:
- Use test credentials from Safaricom
- Test phone number: 254708374149
- Use small amounts for testing

## Admin Interface

Access the admin at `http://127.0.0.1:8000/admin/`

### Features:
- View all contributions
- Filter by status, verification, and date
- Manually verify contributions
- Export contribution data
- Manage camp meeting settings

## Customization

### 1. Styling

The project uses TailwindCSS and DaisyUI. Customize:
- Colors in the template
- Layout components
- Animation effects

### 2. Content

Update content in `templates/camp_meeting/landing.html`:
- Event dates and details
- Church information
- Target amount
- Contact information

### 3. Features

Add additional features:
- Email notifications
- SMS confirmations
- Contribution certificates
- Social media integration

## Deployment

### 1. Production Settings

Update settings for production:
- Set `DEBUG = False`
- Configure proper `ALLOWED_HOSTS`
- Use PostgreSQL database
- Set up SSL certificates
- Configure email backend

### 2. Static Files

```bash
python manage.py collectstatic --noinput
```

### 3. Database

```bash
python manage.py migrate
```

### 4. Web Server

Use Gunicorn + Nginx for production:

```bash
gunicorn camp_meeting_project.wsgi:application
```

## Security Considerations

1. **HTTPS**: Always use HTTPS in production
2. **Secret Key**: Use a strong, unique secret key
3. **Database**: Secure database with proper authentication
4. **M-Pesa**: Validate all callback data
5. **CSRF**: Ensure CSRF protection is enabled
6. **Rate Limiting**: Implement rate limiting for contribution endpoints

##