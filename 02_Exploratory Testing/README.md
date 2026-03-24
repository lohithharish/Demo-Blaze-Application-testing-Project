# 02_Exploratory Testing

> Manual exploratory test reports for [DemoBlaze](https://www.demoblaze.com) — a demo e-commerce web application. Each report was generated using the **Exploratory Tester** browser extension on **Chrome 145.0 / Windows 10/11** on **04 March 2026**, and exported as a structured PDF.

---

## 📁 Folder Contents

| File | Page Tested | URL |
|---|---|---|
| `Demo-Blaze Exploratory Test report (Cart page).pdf` | Cart | `https://www.demoblaze.com/cart.html` |
| `Demo-Blaze Exploratory Test report (Contact page).pdf` | Contact (modal) | `https://www.demoblaze.com/cart.html` |
| `Demo-Blaze Exploratory Test report (Home page).pdf` | Home | `https://www.demoblaze.com/index.html` |
| `Demo-Blaze Exploratory Test report (Login page).pdf` | Login (modal) | `https://www.demoblaze.com/index.html` |
| `Demo-Blaze Exploratory Test report (Signup page).pdf` | Signup (modal) | `https://www.demoblaze.com/index.html` |
| `Laptop category.pdf` | Laptop Category | `https://www.demoblaze.com/index.html#` |
| `Monitor category.pdf` | Monitor Category | `https://www.demoblaze.com/index.html#` |
| `product category.pdf` | Product Detail | `https://www.demoblaze.com/prod.html?idp_=3` |

---

## 📊 Overall Summary

| Page | Total | ✅ Passed | ❌ Failed | ⚠️ Warnings |
|---|---|---|---|---|
| Cart | 33 | 12 | 13 | 8 |
| Contact | 37 | 12 | 15 | 10 |
| Home | 34 | 12 | 14 | 8 |
| Login | 37 | 12 | 16 | 9 |
| Signup | 36 | 12 | 16 | 8 |
| Laptop Category | 38 | 12 | 14 | 12 |
| Monitor Category | 35 | 12 | 14 | 9 |
| Product Detail | 33 | 13 | 13 | 7 |
| **Total** | **273** | **97** | **115** | **71** |

---

## 📄 Report Breakdown

---

### 1. Cart Page — `Demo-Blaze Exploratory Test report (Cart page).pdf`

**URL:** `https://www.demoblaze.com/cart.html`
**Result:** 33 checks — 12 Passed · 13 Failed · 8 Warnings

| Category | Result | Detail |
|---|---|---|
| API/Network | ✅ Pass | All 2 API calls successful |
| Button Functionality | ❌ Fail | 10 individual buttons have no text/label; 70 total unlabeled buttons on page |
| Checkboxes & Radio | ✅ Pass | 1 checkbox has a label |
| Date Fields | N/A | No date fields on page |
| Dropdown Fields | N/A | No visible dropdowns |
| Email Fields | N/A | No email fields |
| Error Messages | ✅ Pass | No errors visible |
| Form Submission | N/A | No visible forms on page |
| Images | ✅ Pass | All 12 images loaded |
| Input Fields Status | ✅ Pass | All inputs enabled |
| Input Placeholders | ⚠️ Warning | `textarea #ait_clipboard` has no placeholder/label |
| Links Check | ✅ Pass | All 8 links have valid URLs |
| Page Loading | ✅ Pass | Page fully loaded |
| Resource Loading | ✅ Pass | All resources loaded |
| SEO Meta Tags | ❌ Fail | Title too short ("STORE", 5 chars); missing `<meta description>`; no `<h1>` tag |
| SEO Meta Tags | ⚠️ Warning | No `<meta keywords>`, no canonical URL, no Open Graph tags |
| Slow Network | ✅ Pass | All requests completed quickly |
| Spelling | ⚠️ Warning | Informal word: "pic" → use "picture" |
| Text Areas | ⚠️ Warning | 2 text areas have no character limit (`#ask`, `#ait_clipboard`) |

**Screenshots captured:** 2

---

### 2. Contact Page — `Demo-Blaze Exploratory Test report (Contact page).pdf`

**URL:** `https://www.demoblaze.com/cart.html` (Contact modal)
**Result:** 37 checks — 12 Passed · 15 Failed · 10 Warnings

| Category | Result | Detail |
|---|---|---|
| API/Network | ✅ Pass | All 2 API calls successful |
| Button Functionality | ❌ Fail | 10 individual buttons have no text/label; 70 total unlabeled buttons |
| Checkboxes & Radio | ✅ Pass | 1 checkbox has a label |
| Email Field Validation | ❌ Fail | `#recipient-email` uses `type="text"` — no email format validation |
| Error Messages | ✅ Pass | No errors visible |
| Form Submission | ❌ Fail | Form #1 has no submit button |
| Images | ✅ Pass | All 12 images loaded |
| Input Fields Status | ✅ Pass | All inputs enabled |
| Input Placeholders | ⚠️ Warning | `#recipient-email` and `#ait_clipboard` both missing placeholder/label |
| Links Check | ✅ Pass | All 8 links have valid URLs |
| Page Loading | ✅ Pass | Page fully loaded |
| Resource Loading | ✅ Pass | All resources loaded |
| SEO Meta Tags | ❌ Fail | Missing `<meta description>`; no `<h1>`; title too short |
| SEO Meta Tags | ⚠️ Warning | No keywords tag, no canonical URL, no Open Graph tags |
| Slow Network | ✅ Pass | All requests completed quickly |
| Spelling | ⚠️ Warning | Informal word: "pic" → use "picture" |
| Text Areas | ⚠️ Warning | 3 text areas have no character limit (`#message-text`, `#ask`, `#ait_clipboard`) |

**Screenshots captured:** 4

---

### 3. Home Page — `Demo-Blaze Exploratory Test report (Home page).pdf`

**URL:** `https://www.demoblaze.com/index.html`
**Result:** 34 checks — 12 Passed · 14 Failed · 8 Warnings

| Category | Result | Detail |
|---|---|---|
| API/Network | ✅ Pass | All 2 API calls successful |
| Button Functionality | ❌ Fail | 10 individual buttons have no text/label; 70 total unlabeled buttons |
| Checkboxes & Radio | ✅ Pass | 1 checkbox has a label |
| Error Messages | ✅ Pass | No errors visible |
| Form Submission | ✅ Pass | Form `#frm` has a submit button |
| Images | ✅ Pass | All 23 images loaded |
| Input Fields Status | ✅ Pass | All inputs enabled |
| Input Placeholders | ⚠️ Warning | `#ait_clipboard` has no placeholder/label |
| Links Check | ❌ Fail | `a#cat` has an empty `href` |
| Page Loading | ✅ Pass | Page fully loaded |
| Resource Loading | ✅ Pass | All resources loaded |
| SEO Meta Tags | ❌ Fail | Missing `<meta description>`; no `<h1>`; title too short |
| SEO Meta Tags | ⚠️ Warning | No keywords tag, no canonical URL, no Open Graph tags |
| Slow Network | ✅ Pass | All requests completed quickly |
| Spelling | ⚠️ Warning | Suspicious word: "htc" — may be informal |
| Text Areas | ⚠️ Warning | 2 text areas have no character limit (`#ask`, `#ait_clipboard`) |

**Screenshots captured:** 3

---

### 4. Login Page — `Demo-Blaze Exploratory Test report (Login page).pdf`

**URL:** `https://www.demoblaze.com/index.html` (Login modal)
**Result:** 37 checks — 12 Passed · 16 Failed · 9 Warnings

| Category | Result | Detail |
|---|---|---|
| API/Network | ✅ Pass | All 2 API calls successful |
| Button Functionality | ❌ Fail | 10 individual buttons have no text/label; 70 total unlabeled buttons |
| Checkboxes & Radio | ✅ Pass | 1 checkbox has a label |
| Error Messages | ✅ Pass | No errors visible |
| Form Submission | ❌ Fail | Form #1 (login modal) has no submit button |
| Form Submission | ✅ Pass | Form #2 (`#frm`) has a submit button |
| Images | ✅ Pass | All 22 images loaded |
| Input Fields Status | ✅ Pass | All inputs enabled |
| Input Placeholders | ⚠️ Warning | `#loginusername` and `#ait_clipboard` missing placeholder/label |
| Links Check | ❌ Fail | `a#cat` has an empty `href` |
| Page Loading | ✅ Pass | Page fully loaded |
| Password Fields | ❌ Fail | `#loginpassword` allows any length password (`min: -1`) — no minimum enforced |
| Resource Loading | ✅ Pass | All resources loaded |
| SEO Meta Tags | ❌ Fail | Missing `<meta description>`; no `<h1>`; title too short |
| SEO Meta Tags | ⚠️ Warning | No keywords tag, no canonical URL, no Open Graph tags |
| Slow Network | ✅ Pass | All requests completed quickly |
| Spelling | ⚠️ Warning | Suspicious word: "htc" — may be informal |
| Text Areas | ⚠️ Warning | 2 text areas have no character limit (`#ask`, `#ait_clipboard`) |

**Screenshots captured:** 5

---

### 5. Signup Page — `Demo-Blaze Exploratory Test report (Signup page).pdf`

**URL:** `https://www.demoblaze.com/index.html` (Signup modal)
**Result:** 36 checks — 12 Passed · 16 Failed · 8 Warnings

| Category | Result | Detail |
|---|---|---|
| API/Network | ✅ Pass | All 2 API calls successful |
| Button Functionality | ❌ Fail | 10 individual buttons have no text/label; 70 total unlabeled buttons |
| Checkboxes & Radio | ✅ Pass | 1 checkbox has a label |
| Error Messages | ✅ Pass | No errors visible |
| Form Submission | ❌ Fail | Form #1 (signup modal) has no submit button |
| Form Submission | ✅ Pass | Form #2 (`#frm`) has a submit button |
| Images | ✅ Pass | All 22 images loaded |
| Input Fields Status | ✅ Pass | All inputs enabled |
| Input Placeholders | ⚠️ Warning | `#ait_clipboard` has no placeholder/label |
| Links Check | ❌ Fail | `a#cat` has an empty `href` |
| Page Loading | ✅ Pass | Page fully loaded |
| Password Fields | ❌ Fail | `#sign-password` allows any length password (`min: -1`) |
| Resource Loading | ✅ Pass | All resources loaded |
| SEO Meta Tags | ❌ Fail | Missing `<meta description>`; no `<h1>`; title too short |
| SEO Meta Tags | ⚠️ Warning | No keywords tag, no canonical URL, no Open Graph tags |
| Slow Network | ✅ Pass | All requests completed quickly |
| Spelling | ⚠️ Warning | Suspicious word: "htc" — may be informal |
| Text Areas | ⚠️ Warning | 2 text areas have no character limit (`#ask`, `#ait_clipboard`) |

**Screenshots captured:** 5

---

### 6. Laptop Category — `Laptop category.pdf`

**URL:** `https://www.demoblaze.com/index.html#`
**Result:** 38 checks — 12 Passed · 14 Failed · 12 Warnings

| Category | Result | Detail |
|---|---|---|
| API/Network | ✅ Pass | All 4 API calls successful |
| Button Functionality | ❌ Fail | 10 individual buttons have no text/label; 70 total unlabeled buttons |
| Checkboxes & Radio | ✅ Pass | 1 checkbox has a label |
| Error Messages | ✅ Pass | No errors visible |
| Form Submission | ✅ Pass | Form `#frm` has a submit button |
| Images | ✅ Pass | All 19 images loaded |
| Input Fields Status | ✅ Pass | All inputs enabled |
| Input Placeholders | ⚠️ Warning | `#ait_clipboard` has no placeholder/label |
| Links Check | ❌ Fail | `a#cat` has an empty `href` |
| Page Loading | ✅ Pass | Page fully loaded |
| Resource Loading | ✅ Pass | All resources loaded |
| SEO Meta Tags | ❌ Fail | Missing `<meta description>`; no `<h1>`; title too short |
| SEO Meta Tags | ⚠️ Warning | No keywords tag, no canonical URL, no Open Graph tags |
| Slow Network | ✅ Pass | All requests completed quickly |
| Spelling | ⚠️ Warning | 5 technical terms flagged: "ghz", "mhz", "rpm", "sdhc", "sdxc" (likely false positives) |
| Text Areas | ⚠️ Warning | 2 text areas have no character limit (`#ask`, `#ait_clipboard`) |

**Screenshots captured:** 3

---

### 7. Monitor Category — `Monitor category.pdf`

**URL:** `https://www.demoblaze.com/index.html#`
**Result:** 35 checks — 12 Passed · 14 Failed · 9 Warnings

| Category | Result | Detail |
|---|---|---|
| API/Network | ✅ Pass | All 5 API calls successful |
| Button Functionality | ❌ Fail | 10 individual buttons have no text/label; 70 total unlabeled buttons |
| Checkboxes & Radio | ✅ Pass | 1 checkbox has a label |
| Error Messages | ✅ Pass | No errors visible |
| Form Submission | ✅ Pass | Form `#frm` has a submit button |
| Images | ✅ Pass | All 15 images loaded |
| Input Fields Status | ✅ Pass | All inputs enabled |
| Input Placeholders | ⚠️ Warning | `#ait_clipboard` has no placeholder/label |
| Links Check | ❌ Fail | `a#cat` has an empty `href` |
| Page Loading | ✅ Pass | Page fully loaded |
| Resource Loading | ✅ Pass | All resources loaded |
| SEO Meta Tags | ❌ Fail | Missing `<meta description>`; no `<h1>`; title too short |
| SEO Meta Tags | ⚠️ Warning | No keywords, no canonical URL, no Open Graph tags |
| Slow Network | ✅ Pass | All requests completed quickly |
| Spelling | ⚠️ Warning | 2 technical terms flagged: "tft", "lcd" (likely false positives) |
| Text Areas | ⚠️ Warning | 2 text areas have no character limit (`#ask`, `#ait_clipboard`) |

**Screenshots captured:** 3

---

### 8. Product Detail Page — `product category.pdf`

**URL:** `https://www.demoblaze.com/prod.html?idp_=3`
**Result:** 33 checks — 13 Passed · 13 Failed · 7 Warnings

| Category | Result | Detail |
|---|---|---|
| API/Network | ✅ Pass | All 2 API calls successful |
| Button Functionality | ❌ Fail | 10 individual buttons have no text/label; 70 total unlabeled buttons |
| Checkboxes & Radio | ✅ Pass | 1 checkbox has a label |
| Error Messages | ✅ Pass | No errors visible |
| Form Submission | N/A | No visible forms on page |
| Images | ✅ Pass | All 13 images loaded |
| Input Fields Status | ✅ Pass | All inputs enabled |
| Input Placeholders | ⚠️ Warning | `#ait_clipboard` has no placeholder/label |
| Links Check | ✅ Pass | All 9 links have valid URLs |
| Page Loading | ✅ Pass | Page fully loaded |
| Resource Loading | ✅ Pass | All resources loaded |
| SEO Meta Tags | ❌ Fail | Missing `<meta description>`; no `<h1>`; title too short |
| SEO Meta Tags | ⚠️ Warning | No keywords tag, no canonical URL, no Open Graph tags |
| Slow Network | ✅ Pass | All requests completed quickly |
| Spelling | ✅ Pass | No spelling mistakes detected |
| Text Areas | ⚠️ Warning | 2 text areas have no character limit (`#ask`, `#ait_clipboard`) |

**Screenshots captured:** 2

---

## 🐛 Consolidated Defect Register

| ID | Severity | Category | Description | Affected Pages |
|---|---|---|---|---|
| BUG-01 | 🔴 High | Accessibility | 70+ buttons across the site have no text or ARIA labels — screen readers cannot identify them | All 8 pages |
| BUG-02 | 🔴 High | Security | Password fields (`#loginpassword`, `#sign-password`) enforce no minimum length (`min: -1`) | Login, Signup |
| BUG-03 | 🟠 Medium | Validation | Email field (`#recipient-email`) uses `type="text"` — accepts any input without email format check | Contact |
| BUG-04 | 🟠 Medium | Navigation | `a#cat` link has an empty `href` — clicking it goes nowhere | Home, Login, Signup, Laptop, Monitor |
| BUG-05 | 🟠 Medium | Forms | Login and Signup modal forms (Form #1) have no semantic submit button — rely solely on JS | Login, Signup, Contact |
| BUG-06 | 🟡 Low | SEO | Page title is only 5 characters ("STORE"); no `<meta name="description">`; no `<h1>` on any page | All 8 pages |
| BUG-07 | 🟡 Low | SEO | No Open Graph tags, no canonical `<link>` tag, no keywords meta tag | All 8 pages |
| BUG-08 | 🟡 Low | UX | Input fields missing placeholder text and visible labels (`#loginusername`, `#recipient-email`, `#ait_clipboard`) | Login, Contact, Cart |
| BUG-09 | 🟡 Low | UX | Text areas have no `maxlength` attribute — unlimited input accepted | All 8 pages |

---

## 🧪 Test Coverage by Category

| Check Category | Coverage |
|---|---|
| API / Network | ✅ Tested on all 8 pages |
| Button Accessibility | ✅ Tested on all 8 pages |
| Checkboxes & Radio | ✅ Tested on all 8 pages |
| Email Validation | ✅ Tested where applicable (Contact) |
| Form Submission | ✅ Tested where applicable |
| Image Loading | ✅ Tested on all 8 pages |
| Input Placeholders & Labels | ✅ Tested on all 8 pages |
| Link Validity | ✅ Tested on all 8 pages |
| Page & Resource Loading | ✅ Tested on all 8 pages |
| Password Strength | ✅ Tested where applicable (Login, Signup) |
| SEO Meta Tags | ✅ Tested on all 8 pages |
| Slow Network Requests | ✅ Tested on all 8 pages |
| Spelling & Informal Language | ✅ Tested on all 8 pages |
| Text Area Limits | ✅ Tested on all 8 pages |

---

## 🛠️ Tools Used

| Tool | Purpose |
|---|---|
| Exploratory Tester (Chrome Extension) | Automated checks & report generation |
| Chrome 145.0 | Test execution browser |
| Windows 10/11 | Test execution OS |
| PDF export | Archiving test evidence |

---

*Reports generated on 04/03/2026. Part of the DemoBlaze QA Portfolio.*
