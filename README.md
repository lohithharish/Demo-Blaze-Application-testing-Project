<div align="center">

# 🛒 DemoBlaze E-Commerce — Manual QA Testing Project

![Testing Type](https://img.shields.io/badge/Testing%20Type-Manual%20%7C%20Functional-blue?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen?style=for-the-badge)
![Test Scenarios](https://img.shields.io/badge/Test%20Scenarios-20-purple?style=for-the-badge)
![Test Cases](https://img.shields.io/badge/Test%20Cases-1000%2B-orange?style=for-the-badge)
![Bugs Reported](https://img.shields.io/badge/Bugs%20Reported-72-critical?style=for-the-badge&logo=jira)
![Bug Tracking](https://img.shields.io/badge/Bug%20Tracking-Jira%20%7C%20DBPS-0052CC?style=for-the-badge&logo=jira)
![License](https://img.shields.io/badge/License-MIT-red?style=for-the-badge)

<br/>

> **A comprehensive, industry-standard manual QA portfolio project** demonstrating full-cycle software testing of the [DemoBlaze](https://www.demoblaze.com/) e-commerce platform — spanning exploratory testing, structured test design, execution, and Jira-tracked defect management.

<br/>

**🔗 Application Under Test:** [https://www.demoblaze.com](https://www.demoblaze.com) &nbsp;|&nbsp; **🐛 Jira Project:** [DBPS on Jira](https://lohithharishmaney.atlassian.net/jira/software/projects/DBPS/summary)

---

</div>

## 📋 Table of Contents

- [Project Overview](#-project-overview)
- [Testing Scope & Objectives](#-testing-scope--objectives)
- [Test Artifacts](#-test-artifacts)
- [Test Coverage Summary](#-test-coverage-summary)
- [Module-Wise Breakdown](#-module-wise-breakdown)
- [Testing Methodologies](#-testing-methodologies)
- [Exploratory Testing](#-exploratory-testing)
- [Live Bug Report — Jira (DBPS)](#-live-bug-report--jira-dbps)
- [Bug Statistics Dashboard](#-bug-statistics-dashboard)
- [Test Environment](#-test-environment)
- [Tools & Technologies](#-tools--technologies)
- [Project Structure](#-project-structure)
- [Author](#-author)

---

## 🧭 Project Overview

**DemoBlaze** is a publicly accessible e-commerce product store widely used in the QA community as a realistic testing target. This project represents a **complete manual QA engagement** — simulating the end-to-end testing workflow expected at enterprise-level software organizations.

| Capability | Details |
|---|---|
| 📌 **Test Planning** | Test plan and strategy documents covering full QA approach |
| 📝 **Test Case Design** | 1,000+ detailed test cases with steps, expected results, and priority tagging |
| 🔍 **Exploratory Testing** | Unscripted sessions across 8 pages to surface hidden edge cases |
| 🐛 **Defect Management** | 72 bugs logged and tracked end-to-end in **Jira (Project: DBPS)** |
| 📊 **QA Documentation** | Professional, stakeholder-ready test documentation |

---

## 🎯 Testing Scope & Objectives

### ✅ In Scope

| Domain | Coverage |
|---|---|
| Functional Testing | All core user flows — Sign Up, Login, Logout, Cart, Contact, Orders |
| UI/UX Testing | Layout, navigation, visual consistency, accessibility |
| Boundary & Negative Testing | Invalid inputs, empty fields, space-only inputs, edge values |
| Security Testing | XSS, SQL Injection, CSRF, HTML Injection checks |
| Cross-Browser Testing | Chrome, Firefox, Safari, Edge |
| Mobile Responsiveness Testing | 7 viewport sizes via Chrome DevTools |
| Exploratory Testing | Unscripted discovery sessions across all major pages |

### ❌ Out of Scope

- Performance / Load Testing
- API Testing
- Database Testing
- Test Automation

### 🎯 Objectives

1. Validate all critical user journeys function correctly end-to-end
2. Identify and document defects with clear reproduction steps in Jira
3. Ensure cross-browser and cross-device compatibility
4. Probe for security vulnerabilities (XSS, SQLi, CSRF, HTML Injection)
5. Produce professional-grade QA artifacts demonstrating industry readiness

---

## 📁 Test Artifacts

| # | Artifact | Description | Status |
|---|---|---|---|
| 01 | `Project Documentation/` | Test plan, test strategy, project scope | ✅ Complete |
| 02 | `Exploratory Testing/` | Session-based exploratory test reports (8 pages) | ✅ Complete |
| 03 | `Test Scenarios/` | 20 master test scenarios across all modules | ✅ Complete |
| 04 | `Test Cases/` | 1,000+ detailed test cases (12 module files) | ✅ Complete |
| 05 | `Executed Test Cases/` | Test execution results per module | ✅ Complete |
| 06 | `Defect Reports/` | 72 bugs tracked in Jira (DBPS project) | ✅ Complete |
| 07 | `Application Screenshots/` | Visual evidence captured during testing | ✅ Complete |

---

## 📊 Test Coverage Summary

```
┌──────────────────────────────────────────────────────────────────┐
│                    TEST COVERAGE AT A GLANCE                     │
├──────────────────────────────┬───────────────────────────────────┤
│  Total Test Scenarios        │  20 Scenarios (TS_001–TS_020)     │
│  Total Test Cases            │  1,000+                           │
│  Modules Covered             │  12 Modules                       │
│  Total Bugs Reported (Jira)  │  72 Bugs (Project: DBPS)          │
│  Epics in Jira               │  5 Epics                          │
│  Priority: Highest Bugs      │  16 Bugs                          │
│  Priority: High Bugs         │  41 Bugs                          │
│  Priority: Low Bugs          │  11 Bugs                          │
│  Priority: Lowest Bugs       │   4 Bugs                          │
│  Bug Tracking Tool           │  Jira Cloud                       │
│  Test Case Format            │  Excel (XLSX)                     │
│  Execution Status            │  Complete — All Phases            │
└──────────────────────────────┴───────────────────────────────────┘
```

---

## 🗂 Module-Wise Breakdown

| # | Module | Test Scenario | Test Cases | Bugs Found |
|---|---|---|---|---|
| 1 | 🔐 User Registration (Sign Up) | TS_001 | 50 | **8 bugs** |
| 2 | 🔑 User Authentication (Login) | TS_002 | 63 | **6 bugs** |
| 3 | 🚪 User Logout | TS_003 | 70 | — |
| 4 | 🏠 Home Page Load & Display | TS_004 | 79 | — |
| 5 | 📬 Contact Page & Form | TS_006, TS_007 | 90 | **25 bugs** |
| 6 | 🎬 About Us Page | TS_005 | — | **6 bugs** |
| 7 | 🗂 Product Categories | TS_008 | 79 | — |
| 8 | 📦 Product Details Page | TS_009 | 89 | — |
| 9 | 🛒 Shopping Cart | TS_012 | 99 | **14 bugs** |
| 10 | 💳 Place Order / Checkout | TS_013, TS_019 | 114 | — |
| 11 | ✅ Order Confirmation | TS_014, TS_020 | 99 | — |
| 12 | 🌐 Cross-Browser & Mobile | TS_016, TS_017 | 239 | **13 bugs** |

---

## 🧪 Testing Methodologies

### 1. 🔍 Exploratory Testing
Unscripted, time-boxed sessions to discover defects beyond scripted scenarios:
- Navigating the application with no predefined path
- Rapid clicks, back button abuse, direct URL manipulation
- Session boundary testing across multiple tabs
- Space-only inputs, empty field submissions, sequential rapid form submits

### 2. ⬛ Black-Box Functional Testing
End-user perspective testing employing:
- **Equivalence Partitioning** — Valid/invalid input class testing across all form fields
- **Boundary Value Analysis** — Min, max, and edge-boundary testing
- **Decision Table Testing** — Input combination coverage for login, signup, checkout
- **State Transition Testing** — Session states (login/logout), cart states

### 3. 🔒 Security Testing
Probed key input fields for:
- **XSS (Cross-Site Scripting)** — Script injection in username and contact fields
- **SQL Injection** — Malicious query inputs tested in all form fields (DBPS-50)
- **CSRF** — Cross-site request forgery vulnerability on form submission (DBPS-51)
- **HTML Injection** — Raw HTML accepted as form input (DBPS-52)

### 4. ❌ Negative Testing
Every module contains dedicated negative test cases validating:
- Proper error messages on invalid input
- No crash on malformed or empty data
- No unintended data persistence or state corruption

### 5. 🌐 Cross-Browser & Responsive Testing
- **4 Browsers** tested: Chrome, Firefox, Edge, Safari
- **7 Viewport sizes** tested via Chrome DevTools device emulation

---

## 🔍 Exploratory Testing

Exploratory testing was conducted using the **Exploratory Tester** Chrome extension across **8 pages** of the application on **04 March 2026** (Chrome 145.0 / Windows 10/11).

| Page | Total Checks | ✅ Passed | ❌ Failed | ⚠️ Warnings |
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

### Key Findings from Exploratory Sessions

| ID | Severity | Issue | Affected Pages |
|---|---|---|---|
| BUG-01 | 🔴 High | 70+ buttons site-wide have no text or ARIA labels — inaccessible to screen readers | All 8 pages |
| BUG-02 | 🔴 High | Password fields enforce no minimum length (`min: -1`) | Login, Signup |
| BUG-03 | 🟠 Medium | Email field uses `type="text"` — no email format validation | Contact |
| BUG-04 | 🟠 Medium | `a#cat` navigation link has an empty `href` | Home, Login, Signup, Categories |
| BUG-05 | 🟠 Medium | Login and Signup modal forms have no semantic submit button | Login, Signup, Contact |
| BUG-06 | 🟡 Low | Page title is 5 chars ("STORE"); no `<meta description>`; no `<h1>` on any page | All 8 pages |
| BUG-07 | 🟡 Low | No Open Graph tags, no canonical link, no keywords meta | All 8 pages |
| BUG-08 | 🟡 Low | Input fields missing visible labels and placeholder text | Login, Contact, Cart |
| BUG-09 | 🟡 Low | Text areas have no `maxlength` — unlimited input accepted | All 8 pages |

---

## 🐛 Live Bug Report — Jira (DBPS)

> All 72 bugs tracked at: **[https://lohithharishmaney.atlassian.net/jira/software/projects/DBPS](https://lohithharishmaney.atlassian.net/jira/software/projects/DBPS)**

---

### 🔐 Sign Up Module — 8 Bugs

| Bug ID | Summary | Priority |
|---|---|---|
| DBPS-1 | Signup account gets created with only spaces in username | 🔴 High |
| DBPS-2 | Password created with spaces — spaces counted as valid characters | 🔴 High |
| DBPS-3 | Enter key does not work to submit the signup form | 🔴 High |
| DBPS-4 | Form labels are not properly displayed | 🔴 High |
| DBPS-5 | User is able to type XSS script in the username field | 🔴 High |
| DBPS-6 | No auto-fill in the password field | 🟡 Low |
| DBPS-7 | Inputs accepted even when username and password contain only spaces | 🔴 High |
| DBPS-8 | Signup inputs get deleted after page refresh | 🟡 Low |

---

### 🔑 Login Module — 6 Bugs

| Bug ID | Summary | Priority |
|---|---|---|
| DBPS-73 | Login accepted with a username containing only spaces | 🔴🔴 Highest |
| DBPS-74 | No labels present on any input fields | 🟡 Low |
| DBPS-75 | Username and password fields do not trim leading/trailing spaces | 🔴 High |
| DBPS-76 | Login credentials not retained after page refresh | 🟡 Low |
| DBPS-77 | Autofill is not working on login form | 🟢 Lowest |
| DBPS-78 | No caps lock warning shown when caps lock is enabled | 🟡 Low |

---

### 🎬 About Us Module — 6 Bugs

| Bug ID | Summary | Priority |
|---|---|---|
| DBPS-11 | Icons are not decorative and not interactive | 🟢 Lowest |
| DBPS-13 | Video does not reset after closing the modal | 🔴 High |
| DBPS-14 | Video scale does not match specification (320px) | 🔴 High |
| DBPS-15 | Video playback issues on 3G network conditions | 🔴 High |
| DBPS-16 | Screen reader option is not visible | 🟡 Low |
| DBPS-17 | Video shown is not related to the web application | 🔴 High |

---

### 🛒 Cart Module — 14 Bugs

| Bug ID | Summary | Priority |
|---|---|---|
| DBPS-19 | Cart page shows nothing when empty — no empty state message | 🔴 High |
| DBPS-20 | Cart displays no currency symbol after adding a product | 🔴 High |
| DBPS-21 | Same product added twice appears as separate line items | 🔴 High |
| DBPS-22 | After adding a product, user can navigate back to product detail page | 🟡 Low |
| DBPS-23 | Cart total shows in plain number format, not currency format | 🔴 High |
| DBPS-24 | No delete confirmation dialog before removing cart item | 🟡 Low |
| DBPS-25 | No undo option after deleting an item from cart | 🟡 Low |
| DBPS-26 | No ability to undo product deletion from cart | 🟢 Lowest |
| DBPS-27 | User can place an order even when the cart is empty | 🔴 High |
| DBPS-28 | No cart item count badge visible in the navigation bar | 🔴 High |
| DBPS-29 | Small screen scrolling is not responsive | 🔴 High |
| DBPS-30 | Guest cart items are lost after user logs in | 🔴 High |
| DBPS-31 | Cart server error shows no error message to the user | 🔴 High |
| DBPS-32 | No feedback provided to user after network failure | 🔴 High |

---

### 📬 Contact Module — 25 Bugs

| Bug ID | Summary | Priority |
|---|---|---|
| DBPS-34 | Message sent successfully without a valid email address | 🔴 High |
| DBPS-35 | Email field accepts input without '@' sign | 🔴 High |
| DBPS-36 | Email field accepts input without a domain | 🔴 High |
| DBPS-37 | Email field accepts spaces as valid input | 🔴 High |
| DBPS-38 | Email field accepts only spaces | 🔴 High |
| DBPS-39 | Form submits when name field is empty | 🔴 High |
| DBPS-40 | Form accepts name field filled with only spaces | 🔴 High |
| DBPS-41 | Form submits when message field is empty | 🔴 High |
| DBPS-42 | Form submits when message field contains only spaces | 🔴 High |
| DBPS-43 | Form submits when all fields are completely empty | 🔴 High |
| DBPS-44 | Form submits when only the email field is filled | 🔴 High |
| DBPS-45 | Form submits when only the name field is filled | 🔴 High |
| DBPS-46 | No placeholder text in any contact form fields | 🟢 Lowest |
| DBPS-47 | No processing indicator shown after submit — risk of duplicate submissions | 🔴🔴 Highest |
| DBPS-48 | No error message displayed when invalid data is submitted | 🔴🔴 Highest |
| DBPS-49 | XSS script injection not prevented in form message field | 🔴🔴 Highest |
| DBPS-50 | Input fields accept SQL injection queries | 🔴🔴 Highest |
| DBPS-51 | CSRF vulnerability not mitigated | 🔴🔴 Highest |
| DBPS-52 | Input fields accept and render raw HTML from users | 🔴🔴 Highest |
| DBPS-53 | No rate limiting — form submitted 10+ times consecutively without block | 🔴 High |
| DBPS-54 | No loading indicator displayed on 3G network conditions | 🔴 High |
| DBPS-55 | Field labels are missing from the contact form | 🔴 High |
| DBPS-56 | Trimmed space inputs are still read as valid by the form | 🔴 High |
| DBPS-57 | User can send 5 messages rapidly back-to-back without any throttle | 🔴 High |
| DBPS-58 | No failure indication shown when server is down on submission | 🔴 High |

---

### 🌐 Cross-Browser Module — 13 Bugs

| Bug ID | Summary | Priority |
|---|---|---|
| DBPS-60 | All form validation errors present in Chrome Browser | 🔴🔴 Highest |
| DBPS-61 | All form validation errors present in Firefox Browser | 🔴🔴 Highest |
| DBPS-62 | All form validation errors present in Safari Browser | 🔴 High |
| DBPS-63 | All form validation errors present in Edge Browser | 🔴 High |
| DBPS-64 | Hero slider swipe gesture not working on iOS Safari | 🔴🔴 Highest |
| DBPS-65 | Incorrect virtual keyboard type triggered for form fields on iOS Safari | 🔴🔴 Highest |
| DBPS-66 | Cart table requires horizontal scroll on iOS Safari (not responsive) | 🔴🔴 Highest |
| DBPS-67 | Hero slider swipe gesture not working on Android Chrome | 🔴🔴 Highest |
| DBPS-68 | Incorrect keyboard type triggered for form fields on Android Chrome | 🔴🔴 Highest |
| DBPS-69 | Cart table overflows screen on Android Chrome | 🔴🔴 Highest |
| DBPS-70 | Console warnings: deprecated jQuery `.size()` across all browsers | 🔴🔴 Highest |
| DBPS-71 | Missing `aria-label` attributes affecting screen reader accessibility | 🟡 Low |
| DBPS-72 | Missing ARIA attributes (`aria-label`, `aria-required`) on form elements | 🟡 Low |

---

## 📈 Bug Statistics Dashboard

```
  TOTAL BUGS REPORTED: 72   |   Jira Project: DBPS
  ─────────────────────────────────────────────────

  BY PRIORITY:
  ┌──────────────┬───────┬──────────────────────────────────────┐
  │ 🔴🔴 Highest │  16   │ █████████████░░░░░░░░░░░░░░░░░  22% │
  │ 🔴 High      │  41   │ ████████████████████████████████ 57% │
  │ 🟡 Low       │  11   │ █████████░░░░░░░░░░░░░░░░░░░░░  15% │
  │ 🟢 Lowest    │   4   │ ███░░░░░░░░░░░░░░░░░░░░░░░░░░░   6% │
  └──────────────┴───────┴──────────────────────────────────────┘

  BY MODULE:
  ┌──────────────────┬───────┬────────────────────────────────────┐
  │ 📬 Contact       │  25   │ ██████████████████████████████  35%│
  │ 🛒 Cart          │  14   │ █████████████████░░░░░░░░░░░░░  19%│
  │ 🌐 Cross-Browser │  13   │ ███████████████░░░░░░░░░░░░░░░  18%│
  │ 🔐 Signup        │   8   │ ██████████░░░░░░░░░░░░░░░░░░░░  11%│
  │ 🔑 Login         │   6   │ ███████░░░░░░░░░░░░░░░░░░░░░░░   8%│
  │ 🎬 About Us      │   6   │ ███████░░░░░░░░░░░░░░░░░░░░░░░   8%│
  └──────────────────┴───────┴────────────────────────────────────┘

  BUG LIFECYCLE (All 72 bugs tracked in Jira):
  New → Open → In Progress → Fixed → Retest → Closed
                                          ↓
                                     Reopened (if fix fails)
```

---

## 🌐 Test Environment

### Browser Matrix

| Browser | Version | Platform | Priority |
|---|---|---|---|
| Google Chrome | Latest Stable | Windows 10/11, macOS | P0 – Primary |
| Mozilla Firefox | Latest Stable | Windows 10/11, macOS | P0 – Primary |
| Microsoft Edge | Latest Stable | Windows 10/11 | P0 – Primary |
| Apple Safari | Latest Stable | macOS, iOS | P0 – Primary |

### Device & Viewport Matrix

| Device Type | Resolution | Test Method |
|---|---|---|
| Desktop Full HD | 1920 × 1080 | Physical machine |
| Desktop Standard | 1366 × 768 | Chrome DevTools |
| Tablet Landscape | 1024 × 768 | Chrome DevTools |
| Tablet Portrait (iPad) | 768 × 1024 | Chrome DevTools |
| Mobile (iPhone 14 Pro) | 393 × 852 | Chrome DevTools |
| Mobile (iPhone SE) | 375 × 667 | Chrome DevTools |
| Mobile (Galaxy S21) | 360 × 800 | Chrome DevTools |

---

## 🛠 Tools & Technologies

| Category | Tool | Purpose |
|---|---|---|
| Test Documentation | Microsoft Excel | Test scenarios & test cases |
| Bug Tracking | **Jira Cloud (Project: DBPS)** | 72 bugs tracked end-to-end |
| Exploratory Testing | Exploratory Tester (Chrome Extension) | Automated checks & report generation |
| Primary Browser | Google Chrome + DevTools | Test execution & responsive emulation |
| Cross-Browser | Firefox, Edge, Safari | Compatibility testing |
| Screen Capture | Snipping Tool / Lightshot | Bug evidence screenshots |
| Screen Recording | ShareX / Loom | Video evidence for defect reproduction |
| Version Control | Git & GitHub | Repository and artifact management |

---

## 📂 Project Structure

```
📦 demoblaze-qa/
│
├── 📁 01_Project_Documentation/
│   ├── DemoBlaze_Test_Plan.docx         # Overall QA strategy & scope
│   └── DemoBlaze_Test_Strategy.docx    # Org-level QA methodology document
│
├── 📁 02_Exploratory Testing/
│   └── Exploratory test reports for 8 pages (PDF format)
│
├── 📁 03_Test Scenarios/
│   └── DemoBlaze_Test_Scenarios.xlsx   # 20 high-level scenarios (TS_001–TS_020)
│
├── 📁 04_Test Cases/
│   ├── TC_Signup.xlsx                   # 50 test cases
│   ├── TC_Login.xlsx                    # 63 test cases
│   ├── TC_Logout.xlsx                   # 70 test cases
│   ├── TC_HomePage.xlsx                 # 79 test cases
│   ├── TC_Contact.xlsx                  # 90 test cases
│   ├── TC_ProductCategories.xlsx        # 79 test cases
│   ├── TC_ProductDetails.xlsx           # 89 test cases
│   ├── TC_Cart.xlsx                     # 99 test cases
│   ├── TC_PlaceOrder.xlsx               # 114 test cases
│   ├── TC_OrderConfirmation.xlsx        # 99 test cases
│   ├── TC_CrossBrowser.xlsx             # 119 test cases
│   └── TC_MobileResponsive.xlsx         # 120 test cases
│
├── 📁 05_Executed Test Cases/
│   └── Execution records and pass/fail results per module
│
├── 📁 06_Defect Reports/
│   └── Bug_Reports_Jira_Export.pdf     # Defect lifecycle records from Jira
│
├── 📁 07_Application Screenshots/
│   └── Visual test evidence captured during execution
│
├── LICENSE
└── README.md
```

---

## 💡 Key Highlights

- 🔐 **Security vulnerabilities confirmed** — XSS, SQL Injection, CSRF, and HTML injection were all accepted in the Contact module (DBPS-49 to DBPS-52), demonstrating a security-aware testing mindset beyond basic functional coverage.

- 🐛 **72 bugs logged in Jira (Project: DBPS)** across 6 modules with complete defect lifecycle tracking, reflecting hands-on experience with enterprise-grade bug management.

- 📋 **20 test scenarios + 1,000+ test cases** authored across 12 module files, demonstrating strong skills in requirement decomposition, test condition identification, and comprehensive coverage design.

- 🌐 **Cross-browser and mobile testing** exposed critical rendering issues — swipe gesture failures on iOS Safari and Android Chrome (DBPS-64, DBPS-67), cart overflow (DBPS-66, DBPS-69), and deprecated jQuery warnings across all browsers (DBPS-70).

- 📊 **Multiple testing techniques applied** — Equivalence Partitioning, Boundary Value Analysis, State Transition Testing, Decision Table Testing, and Negative Testing — reflecting structured and methodical QA engineering practice.

- 🔍 **8-page exploratory testing sweep** using structured tooling, identifying 9 consolidated defects including a site-wide accessibility failure (70+ unlabeled buttons) and missing password minimum enforcement.

---

## 🗺️ Testing Roadmap

### Phase 1 — Manual Testing ✅ Complete

| Phase | Activity | Status |
|---|---|---|
| Phase 0 | Exploratory Testing — Full Application Discovery | ✅ Complete |
| Phase 1 | Test Scenario Design — 20 Scenarios | ✅ Complete |
| Phase 2 | Test Case Authoring — 12 Modules, 1,000+ TCs | ✅ Complete |
| Phase 3 | Test Execution — P0 Modules | ✅ Complete |
| Phase 4 | Test Execution — P1 Modules | ✅ Complete |
| Phase 5 | Cross-Browser & Mobile Responsive Testing | ✅ Complete |
| Phase 6 | Defect Reporting, Re-testing & Closure | ✅ Complete |
| Phase 7 | Test Summary Report Generation | ✅ Complete |

---

## 👤 Author

<div align="center">

**MH Lohith**
*QA Engineer | Manual Testing | Security Testing | Cross-Browser Testing*

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0077B5?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/in/lohithharish)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-181717?style=for-the-badge&logo=github)](https://github.com/lohithharish)
[![Jira](https://img.shields.io/badge/Jira-DBPS%20Project-0052CC?style=for-the-badge&logo=jira)](https://lohithharishmaney.atlassian.net/jira/software/projects/DBPS/summary)
[![Email](https://img.shields.io/badge/Email-Contact-D14836?style=for-the-badge&logo=gmail)](mailto:lohithharishmv@gmail.com)

---

*This project is part of an active QA portfolio — demonstrating full-cycle manual testing expertise.*

**72 bugs found. 20 scenarios covered. 1,000+ test cases. Tested with precision. 🎯**

</div>
