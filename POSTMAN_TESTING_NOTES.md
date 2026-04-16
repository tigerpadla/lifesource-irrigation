# Postman Testing Notes

Date: 2026-04-16
Project: Lifesource Irrigation (Django server-rendered site)
Production URL for manual cross-check: https://lifesource-irrigation-c72210771a40.herokuapp.com/

## What Was Found

- This project is primarily server-rendered HTML routes, not an API-first backend.
- Public user-facing routes are in:
  - core, about, services, gallery, contact, newsletter apps
- Important behavior from source:
  - /services/ is a redirect route (to /services/irrigation/)
  - /contact/ is both GET page and POST form submit
  - /newsletter/subscribe/ supports POST-only flows:
    - normal form POST (redirect)
    - AJAX POST (JSON response)
  - /gallery/ supports filtering via query param category
- No class-based views were found for these public routes.

## What Is Covered By Postman

- GET page regression checks now cover:
  - /, /about/, /services/<slug>/, /gallery/, /gallery/?category=<slug>, /contact/, /contact/success/, /newsletter/, /newsletter/<slug>/
- For each working GET page request, tests assert:
  - expected status code
  - Content-Type includes text/html
  - meaningful page-specific text content
- Redirect checks now cover:
  - /services/ returns 301 or 302
  - Location header targets /services/irrigation/
- Negative-path checks now cover:
  - /services/<invalid-slug>/ => 404
  - /newsletter/<invalid-slug>/ => 404
  - /gallery/?category=<invalid-slug> => graceful 200 HTML render with gallery heading present

## What Was Fixed From Earlier Generated Collection

Collection path updated:
- postman/collections/lifesource irrigation website/

Structural fixes:
- Reorganized requests into folders:
  - Pages/
  - Forms/
  - Redirects/
- Updated collection metadata variables in .resources/definition.yaml:
  - baseUrl
  - serviceSlug
  - galleryCategory
  - newsletterSlug
  - nextPath
  - csrfToken

Coverage fixes:
- Added missing real endpoints:
  - GET /newsletter/<slug>/
  - POST /newsletter/subscribe/ (form redirect flow)
  - POST /newsletter/subscribe/ (AJAX JSON flow)
  - GET /gallery/ (unfiltered) plus filtered request with category query
- Kept and validated existing real endpoints:
  - GET /, /about/, /services/<slug>/, /gallery/, /contact/, /contact/success/, /newsletter/
  - GET /services/ redirect
  - POST /contact/
- Removed old flat request files after replacement with grouped, endpoint-accurate requests.

Behavior/test fixes:
- Added basic Postman tests to each request for:
  - expected status code checks
  - redirect location checks where relevant
  - JSON shape checks for AJAX newsletter subscription

## Which Routes Are Not True API Endpoints

These are not API resources and should be treated as HTML page routes or admin tooling:
- / (home), /about/, /services/<slug>/, /gallery/, /contact/, /contact/success/, /newsletter/, /newsletter/<slug>/

Not included as public marketing-site endpoints in this collection:
- /admin/ (admin backend)
- /summernote/ (editor integration)

Not Django routes:
- tel:, mailto:, and external social/share links used in templates

Excluded from collection due unclear/unsupported direct behavior:
- GET /newsletter/subscribe/ (view implements POST flow only)

## Recommended Postman Test Coverage

1. Pages (HTML rendering)
- Verify status 200 and Content-Type containing text/html for:
  - /, /about/, /services/<slug>/, /gallery/, /contact/, /contact/success/, /newsletter/

2. Dynamic page coverage
- /services/<slug>/ with known slug (irrigation) => 200
- /services/<slug>/ with unknown slug => 404 (manual variant)
- /newsletter/<slug>/ with known published slug => 200
- /newsletter/<slug>/ unknown slug => 404

3. Redirect coverage
- GET /services/ => redirect to /services/irrigation/
- POST /contact/ valid form => redirect to /contact/success/
- POST /newsletter/subscribe/ form => redirect to next/referrer

4. Query parameter coverage
- GET /gallery/?category=<valid slug> => 200
- GET /gallery/?category=<invalid slug> => 200 with likely empty gallery state

5. AJAX flow coverage
- POST /newsletter/subscribe/ with X-Requested-With=XMLHttpRequest:
  - status 200 when accepted
  - JSON includes success and message

## Limitations of Postman for This Django Site

- CSRF protection:
  - Django form POST routes typically require valid CSRF cookie/token pair.
  - Raw Postman requests without token often produce 403.
  - Collection requests include csrfToken variable and tests that tolerate expected 403 in token-missing scenarios.
- Server-rendered UX behavior:
  - Flash messages, template rendering differences, and client-side behaviors are better validated in browser/E2E tests.
- Data-dependent routes:
  - /newsletter/<slug>/ requires real published DB data.
  - /gallery/?category=<slug> behavior depends on existing category/project records.

## Manual Verification Against Heroku (Do Not Assume)

Source code was used as the primary truth. Manually verify in production:
- That trailing slash behavior and redirects match settings/middleware in deployed environment
- That newsletter slug(s) exist and resolve
- That CSRF/session behavior for form posts matches production security settings
- That category slugs in gallery data match expected test variables
