# Endpoint Audit

Date: 2026-04-16

Scope:
- Project URLs: lifesource/urls.py
- App URLs: core/urls.py, about/urls.py, services/urls.py, gallery/urls.py, contact/urls.py, newsletter/urls.py
- Views: all app views.py files (function-based views only; no class-based views found)
- Forms/templates: contact/forms.py and template form/link usage

## Route Inventory

| Route / Path | Method | Classification | Expected Params / Body | Expected Response / Status | Source of Implementation |
|---|---|---|---|---|---|
| / | GET | Public page | None | HTML page, 200 | core/urls.py:7, core/views.py:8 |
| /about/ | GET | Public page | None | HTML page, 200 | about/urls.py:7, about/views.py:5 |
| /services/ | GET | Redirect | None | Redirect to /services/irrigation/, usually 302 | services/urls.py:7, services/views.py:154, services/views.py:160 |
| /services/<slug>/ | GET | Public page (dynamic) | slug path variable (e.g., irrigation, gardening, lighting, terrace-refurbishment) | HTML page, 200 for known/active slug; 404 for unknown slug | services/urls.py:8, services/views.py:163 |
| /gallery/ | GET | Public page | Optional query param: category=<slug> | HTML page, 200 | gallery/urls.py:7, gallery/views.py:67, gallery/views.py:69 |
| /contact/ | GET | Public page | None | HTML page, 200 | contact/urls.py:7, contact/views.py:8 |
| /contact/ | POST | Form submission | form fields: first_name, last_name, email, phone, services_needed (multi), optional referral_source, optional message | On valid submission redirects to /contact/success/ (302). With CSRF protection and missing token, expect 403 in Postman. | contact/views.py:10, contact/views.py:43, contact/forms.py:11, contact/forms.py:21, templates/contact/contact.html:29 |
| /contact/success/ | GET | Success page | None | HTML page, 200 | contact/urls.py:8, contact/views.py:53 |
| /newsletter/ | GET | Public page | None | HTML page, 200 | newsletter/urls.py:7, newsletter/views.py:8 |
| /newsletter/<slug>/ | GET | Public page (dynamic) | slug path variable for published newsletter | HTML page, 200 for published slug, 404 otherwise | newsletter/urls.py:9, newsletter/views.py:18 |
| /newsletter/subscribe/ | POST | Form submission (redirect flow) | email, optional next | Redirect to next/referrer (302). With missing/invalid email, still redirect with message. With missing CSRF token in Postman, expect 403. | newsletter/urls.py:8, newsletter/views.py:32, newsletter/views.py:45, newsletter/views.py:66, templates/newsletter/newsletter_list.html:38, templates/newsletter/newsletter_list.html:40, templates/newsletter/newsletter_detail.html:79, templates/newsletter/newsletter_detail.html:81, templates/base.html:106 |
| /newsletter/subscribe/ | POST | Form submission (AJAX) | email, AJAX header X-Requested-With=XMLHttpRequest | JSON body with success/message, 200 when accepted. Missing CSRF token in Postman can produce 403. | newsletter/views.py:36, newsletter/views.py:43, newsletter/views.py:63, static/js/main.js:98, static/js/main.js:102 |

## Query-Parameter Routes

| Route | Query Param | Behavior | Source |
|---|---|---|---|
| /gallery/ | category=<slug> | Filters projects by ProjectCategory slug | gallery/views.py:69, templates/gallery/gallery.html:105 |
| /gallery/ links from service page | category={{ service.slug }} | Deep-link into gallery filtered by current service | templates/services/service_detail.html:292 |

## Redirect and Success Behavior

| Behavior | Trigger | Result | Source |
|---|---|---|---|
| Service root redirect | GET /services/ | Redirect to /services/irrigation/ | services/views.py:160 |
| Contact success flow | POST /contact/ valid form | Redirect to /contact/success/ | contact/views.py:43 |
| Contact success page | GET /contact/success/ | Success confirmation page | contact/views.py:53 |
| Newsletter subscribe redirect flow | POST /newsletter/subscribe/ non-AJAX | Redirect to next/referrer URL | newsletter/views.py:45, newsletter/views.py:66 |
| Newsletter subscribe AJAX flow | POST /newsletter/subscribe/ with X-Requested-With header | JSON success/error response | newsletter/views.py:36, newsletter/views.py:43, newsletter/views.py:63 |

## Notes on Non-Public / Non-Page Endpoints

- /admin/ and /summernote/ exist at project level (lifesource/urls.py:13-14) but are not treated as public marketing-site endpoints for this collection.
- Template links like tel:, mailto:, social media share links, and external URLs are not Django HTTP routes.
- No class-based view routes were found in app views.py files.
- GET /newsletter/subscribe/ is not implemented as a valid handler path in views logic (POST branch only), so it is intentionally excluded as a testable public endpoint.
