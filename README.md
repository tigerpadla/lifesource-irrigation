# LifeSource Irrigation 🌿

A professional website for **LifeSource Irrigation** - a full-service irrigation, gardening, and exterior lighting company serving New York City for over three decades.

![Django](https://img.shields.io/badge/Django-6.0-green)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-purple)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Neon-blue)
![Heroku](https://img.shields.io/badge/Deployed-Heroku-purple)

## 🌐 Live Site

**Production:** [https://lifesource-irrigation-f72e2fb66193.herokuapp.com/](https://lifesource-irrigation-f72e2fb66193.herokuapp.com/)

**Admin Panel:** `/admin/`

---

## ⚠️ Development Prototype

**This is a development prototype** created to showcase the initial design concept and functionality based on the client's email requirements and the Canva wireframes provided.

### Purpose
- Demonstrate the proposed website structure and design
- Show how all requested features could be implemented
- Provide a working prototype for client review and feedback

### Flexibility
- **All features are customizable** - Any elements can be modified, added, or removed based on feedback
- **Tech stack is flexible** - The current stack (Django/PostgreSQL/Heroku) can be changed if different technologies are preferred
- **Additional features from the email** (CRM integration, cookie compliance, team profiles, etc.) can be implemented upon request
- **Design and branding** can be adjusted to match final brand guidelines

### Why This Tech Stack?

**Django + PostgreSQL + Heroku** was chosen for this prototype because:

| Benefit | Description |
|---------|-------------|
| **No-Code Content Management** | The site owner can manage ALL content through the Admin Panel — no coding required |
| **User-Friendly Admin** | Add services, upload gallery images, manage testimonials, create newsletters, view contact inquiries — all from a simple web interface |
| **Reliable & Scalable** | Industry-standard technologies used by Instagram, Pinterest, and Spotify |
| **Cost-Effective Hosting** | Heroku provides easy deployment with free/low-cost tiers |
| **Secure** | Built-in protection against common web vulnerabilities |
| **Easy Updates** | Content changes appear instantly without developer involvement |

### Owner Self-Service (No Developer Needed)

The business owner can independently manage:
- ✏️ **Services** - Add, edit, or remove services and sub-services
- 🖼️ **Gallery** - Upload new project photos with descriptions
- 💬 **Testimonials** - Add client quotes that rotate on the site
- 📰 **Newsletters** - Create and publish newsletters with Irish Corner content
- 📧 **Subscribers** - View and manage newsletter email list
- 📋 **Contact Inquiries** - Review all form submissions from potential clients

*All of this is done through a simple admin interface — no need to access or modify any code.*

---

## 📋 Project Overview

This website was developed based on the client's requirements to replace their outdated website with a modern, professional online presence. The design emphasizes simplicity, white space, and clear navigation across dedicated pages.

### Client Requirements ✅

| Requirement | Status | Implementation |
|-------------|--------|----------------|
| Dedicated pages (not one long page) | ✅ | Separate pages for Home, About, Services, Gallery, Newsletter, Contact |
| White space — simple, straightforward | ✅ | Clean Bootstrap 5 design with generous spacing |
| Eye-catching landing page | ✅ | Hero section with background image, company intro, CTAs |
| About section with team info | ✅ | Company story, Declan's bio, Irish heritage section, room for team members |
| Services with subsections | ✅ | Irrigation, Gardening, Lighting, Terrace Refurbishment with detailed sub-services |
| Gallery with testimonials | ✅ | Project images with lightbox modal + rotating testimonials carousel |
| Contact form with service selection | ✅ | Smart form with checkboxes (inspired by rrirrigation.com) |
| Newsletter signup emphasis | ✅ | Persistent signup bar on all pages + newsletter archive |
| Newsletter archive (like a blog) | ✅ | Dedicated newsletter section with past issues |
| Mobile & tablet responsive | ✅ | Fully responsive design tested on all screen sizes |
| Irish-American feel | ✅ | "Irish Corner" section in About & Newsletters with heritage content |

### Competitor Analysis

The design takes inspiration from competitor sites while maintaining LifeSource's unique identity:
- [Rooftop Drops](https://www.rooftopdrops.com/) - Clean layout reference
- [New York Plantings](https://newyorkplantings.com/) - Service presentation
- [Plantwell Irrigation](https://www.plantwellirrigation.com/) - Gallery approach

---

## ✨ Features

### 🏠 Public Pages

| Page | Description |
|------|-------------|
| **Home** | Hero section, services overview (3 cards), gallery preview (8 images), testimonials carousel, trust indicators (30+ years, 500+ projects, etc.) |
| **About** | Company story, Declan Keane's bio with placeholder photo, Irish-American heritage section with flag heart, expandable for team members |
| **Services** | 4 main services (Irrigation, Gardening, Lighting, Terrace Refurbishment) each with detailed sub-services, sidebar navigation, contact CTA |
| **Gallery** | Project showcase with category filters, lightbox modal showing description & location, testimonials carousel |
| **Newsletter** | Archive of past newsletters displayed as cards, each with "Irish Corner" section, subscriber signup |
| **Contact** | Smart form with: name, email, phone, address, property type, service checkboxes, referral source, message |

### 🔐 Admin Features

All content is manageable through Django Admin:

- **Service Categories** - Add/edit main services with icons and hero images
- **Sub Services** - Detailed offerings under each service category
- **Gallery Projects** - Upload images with title, description, location, category
- **Testimonials** - Client quotes displayed in rotating carousel (up to 10)
- **Newsletters** - Rich content with Irish Corner section
- **Contact Inquiries** - View all form submissions with service requests
- **Newsletter Subscribers** - Manage email list

### ⚡ Technical Features

- 📱 **Fully Responsive** - Mobile, tablet, and desktop optimized
- 🚀 **Performance Optimized** - Preload critical assets, lazy loading images, deferred JavaScript
- 🖼️ **WebP Images** - Optimized image format for faster loading
- ☁️ **Cloudinary CDN** - Media storage and delivery
- 🔒 **PostgreSQL** - Production database (Neon cloud)
- ✉️ **AJAX Newsletter** - Subscribe without page reload, modal confirmation
- ✅ **Form Validation** - Client-side validation for phone, email, required services
- 🎠 **Testimonials Carousel** - Auto-rotating with navigation controls

---

## 🛠️ Tech Stack

| Category | Technology |
|----------|------------|
| Backend | Django 6.0 |
| Frontend | Bootstrap 5.3, Custom CSS |
| Database | PostgreSQL (Neon) |
| Media Storage | Cloudinary |
| Static Files | WhiteNoise |
| Forms | Django Crispy Forms + Bootstrap 5 |
| Server | Gunicorn |
| Hosting | Heroku |

---

## 🎨 Brand Identity

### Colors

| Color | Hex | Usage |
|-------|-----|-------|
| Brand Green | `#A4BB4B` | Logo color, decorative accents |
| Accessible Green | `#6B7A30` | Buttons, links, text (WCAG AA compliant) |
| Dark Green | `#4A5522` | Hover states |
| Light Green | `#C5D67A` | Subtle backgrounds |

### Typography

- **Headings:** Playfair Display (serif)
- **Body:** Open Sans (sans-serif)

---

## 📁 Project Structure

```
lifesource-irrigation/
├── core/               # Home page app
├── about/              # About page app
├── services/           # Services & sub-services app
├── gallery/            # Project gallery app
├── contact/            # Contact form & inquiries app
├── newsletter/         # Newsletters & subscribers app
├── templates/          # HTML templates
│   ├── base.html       # Main layout (nav, footer, newsletter bar)
│   ├── core/
│   ├── about/
│   ├── services/
│   ├── gallery/
│   ├── contact/
│   └── newsletter/
├── static/
│   ├── css/style.css   # Custom styles
│   ├── js/main.js      # JavaScript (carousel, validation, AJAX)
│   ├── images/         # Static images (logo, hero, service images)
│   └── favicon/        # Favicon files
├── media/              # User uploaded content (via Cloudinary in production)
├── lifesource/         # Project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── Procfile            # Heroku process file
├── requirements.txt    # Python dependencies
├── runtime.txt         # Python version
└── README.md
```

---

## 🚀 Deployment

### Heroku Setup

The site is deployed on Heroku with the following configuration:

**Config Vars (Environment Variables):**
- `SECRET_KEY` - Django secret key
- `DATABASE_URL` - Neon PostgreSQL connection string
- `CLOUDINARY_URL` - Cloudinary credentials

**Buildpacks:**
- `heroku/python`

**Automatic Deployments:**
- Connected to GitHub repository
- Pushes to `main` branch trigger automatic deployment

---

## 💻 Local Development

### Prerequisites
- Python 3.12+
- Git

### Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/lifesource-irrigation.git
   cd lifesource-irrigation
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   ```

3. **Activate virtual environment**
   ```bash
   # Windows
   venv\Scripts\activate
   
   # Mac/Linux
   source venv/bin/activate
   ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Create `env.py`** (in project root)
   ```python
   import os
   
   os.environ['SECRET_KEY'] = 'your-secret-key-here'
   os.environ['DATABASE_URL'] = 'your-neon-database-url'
   os.environ['CLOUDINARY_URL'] = 'cloudinary://your-cloudinary-url'
   ```

6. **Run migrations**
   ```bash
   python manage.py migrate
   ```

7. **Create superuser**
   ```bash
   python manage.py createsuperuser
   ```

8. **Run development server**
   ```bash
   python manage.py runserver
   ```

9. **Access the site**
   - Frontend: http://127.0.0.1:8000/
   - Admin: http://127.0.0.1:8000/admin/

---

## 📝 Admin User Guide

### Adding/Editing Services

1. Go to **Admin → Service Categories**
2. Click **Add Service Category**
3. Fill in:
   - **Title:** e.g., "Irrigation"
   - **Slug:** e.g., "irrigation" (auto-generated)
   - **Short Description:** Brief text for cards
   - **Full Description:** Detailed text for service page
   - **Icon:** Bootstrap icon class (e.g., `bi-droplet`)
   - **Hero Image:** Background image for service page
4. Save, then add **Sub Services** for detailed offerings

### Adding Gallery Projects

1. Go to **Admin → Projects**
2. Click **Add Project**
3. Fill in:
   - **Title:** Project name
   - **Image:** Upload photo
   - **Description:** What was done
   - **Location:** NYC neighborhood
   - **Category:** (optional) for filtering
   - **Featured:** ✅ Check to show on home page
4. Save

### Managing Testimonials

1. Go to **Admin → Testimonials**
2. Add client testimonials with:
   - **Client Name:** e.g., "Sarah M."
   - **Quote:** Their testimonial text
   - **Location:** e.g., "Upper West Side"
   - **Is Active:** ✅ Check to display
3. Up to 10 testimonials rotate in the carousel

### Creating Newsletters

1. Go to **Admin → Newsletters**
2. Click **Add Newsletter**
3. Fill in:
   - **Title:** Newsletter title
   - **Slug:** URL-friendly version
   - **Content:** Main newsletter content
   - **Irish Corner Title:** e.g., "Did You Know?"
   - **Irish Corner Content:** Irish heritage facts/stories
   - **Is Published:** ✅ Check when ready to display
4. Save - it will appear in the Newsletter archive

### Viewing Contact Inquiries

1. Go to **Admin → Contact Inquiries**
2. View all form submissions with:
   - Contact details
   - Property information
   - Services requested (checkboxes they selected)
   - Message
   - Submission date

---

## 🔮 Future Enhancements

- **CRM Integration** - Connect to Bigin CRM for lead management
- **Cookie Consent** - GDPR/legal compliance banner
- **Email Notifications** - Send confirmations to customers
- **Blog Section** - Expand newsletters into full blog
- **Online Scheduling** - Book consultations directly
- **Team Member Profiles** - Add Leo, FG, Junior bios
- **SEO Optimization** - Meta tags, sitemap, schema markup

---

*Prototype built to demonstrate proposed website design for LifeSource Irrigation, NYC.*
