<div align="center">

# 🛒 DemoBlaze E-Commerce — End-to-End Quality Assurance Project

<img src="https://img.shields.io/badge/Testing%20Type-Manual%20%7C%20Functional-blue?style=for-the-badge&logo=testcafe" />
<img src="https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge" />
<img src="https://img.shields.io/badge/Test%20Scenarios-18-purple?style=for-the-badge" />
<img src="https://img.shields.io/badge/Test%20Cases-1000%2B-orange?style=for-the-badge" />
<img src="https://img.shields.io/badge/Bugs%20Reported-72-critical?style=for-the-badge&logo=jira" />
<img src="https://img.shields.io/badge/Bug%20Tracking-Jira%20%7C%20DBPS-0052CC?style=for-the-badge&logo=jira" />
<img src="https://img.shields.io/badge/Automation-Selenium%20%7C%20Python-yellow?style=for-the-badge&logo=selenium" />
<img src="https://img.shields.io/badge/License-MIT-red?style=for-the-badge" />

<br/>

> **A comprehensive, industry-standard QA portfolio project** demonstrating full-cycle software testing of the [DemoBlaze](https://www.demoblaze.com/) e-commerce platform — spanning exploratory testing, structured test design, execution, Jira-tracked defect management, and Selenium-based automation.

<br/>

**🔗 Application Under Test:** [https://www.demoblaze.com](https://www.demoblaze.com) &nbsp;|&nbsp; **🐛 Jira Project:** [DBPS on Jira](https://lohithharishmaney.atlassian.net/jira/software/projects/DBPS/summary)

---

</div>

## 📋 Table of Contents

- [Project Overview](#-project-overview)
- [Testing Scope & Objectives](#-testing-scope--objectives)
- [Test Artifacts](#-test-artifacts)
- [Test Coverage Summary](#-test-coverage-summary)
- [Module-Wise Test Scenario Breakdown](#-module-wise-test-scenario-breakdown)
- [Testing Methodologies](#-testing-methodologies)
- [Live Bug Report — Jira (DBPS)](#-live-bug-report--jira-dbps)
- [Bug Statistics Dashboard](#-bug-statistics-dashboard)
- [Automation Suite](#-automation-suite)
- [Tools & Technologies](#-tools--technologies)
- [Project Structure](#-project-structure)
- [Key Learnings & Highlights](#-key-learnings--highlights)
- [Author](#-author)

---

## 🧭 Project Overview

**DemoBlaze** is a publicly accessible e-commerce product store widely used in the QA community as a realistic testing target. This project represents a **complete QA engagement** — simulating the end-to-end testing workflow expected at enterprise-level software organizations.

| Capability | Details |
|---|---|
| 📌 **Test Planning** | 18 structured test scenarios aligned to business requirements |
| 📝 **Test Case Design** | 1,000+ detailed test cases with steps, expected results, and priority tagging |
| 🔍 **Exploratory Testing** | Unscripted sessions to surface hidden edge cases |
| 🐛 **Defect Management** | 72 bugs logged and tracked end-to-end in **Jira (Project: DBPS)** |
| 🤖 **Test Automation** | Selenium WebDriver automation suite (HTML + Python + CSS) |
| 📊 **QA Documentation** | Professional, stakeholder-ready test documentation |

---

## 🎯 Testing Scope & Objectives

### ✅ In Scope

| Domain | Coverage |
|---|---|
| Functional Testing | All core user flows — Sign Up, Login, Cart, Contact, Orders |
| UI/UX Testing | Layout, navigation, visual consistency, accessibility |
| Boundary & Negative Testing | Invalid inputs, empty fields, space-only inputs, edge values |
| Security Testing | XSS, SQL Injection, CSRF vulnerability checks |
| Cross-Browser Testing | Chrome, Firefox, Safari, Edge |
| Mobile Responsiveness Testing | Multiple screen resolutions and device simulations |
| Exploratory Testing | Unscripted discovery of hidden defects |
| Test Automation | Selenium WebDriver automation suite |

### ❌ Out of Scope (Current Phase)

- Performance / Load Testing
- API Testing *(planned for next phase)*
- Database Testing

### 🎯 Objectives

1. Validate all critical user journeys function correctly end-to-end
2. Identify and document defects with clear reproduction steps in Jira
3. Ensure cross-browser and cross-device compatibility
4. Probe for security vulnerabilities (XSS, SQLi, CSRF)
5. Automate key regression scenarios using Selenium
6. Produce professional-grade QA artifacts demonstrating industry readiness

---

## 📁 Test Artifacts

| # | Artifact | Description | Status |
|---|---|---|---|
| 01 | `Project Documentation` | Project scope, objectives, and test plan | ✅ Complete |
| 02 | `Exploratory Testing Notes` | Session-based exploratory testing records | ✅ Complete |
| 03 | `Test Scenarios` | 18 master test scenarios across all modules | ✅ Complete |
| 04 | `Test Cases` | 1,000+ detailed test cases (all modules) | ✅ Complete |
| 05 | `Executed Test Cases` | Test execution results per module | ✅ Complete |
| 06 | `Defect Reports` | 72 bugs tracked in Jira (DBPS project) | ✅ Complete |
| 07 | `Application Screenshots` | Visual evidence captured during testing | ✅ Complete |
| 08 | `Demoblaze Automation/` | Selenium WebDriver automation suite | ✅ Available |

---

## 📊 Test Coverage Summary

```
┌──────────────────────────────────────────────────────────────────┐
│                    TEST COVERAGE AT A GLANCE                     │
├──────────────────────────────┬───────────────────────────────────┤
│  Total Test Scenarios        │  18 Scenarios                     │
│  Total Test Cases            │  1,000+                           │
│  Modules Covered             │  7 Functional Modules             │
│  Total Bugs Reported (Jira)  │  72 Bugs (Project: DBPS)          │
│  Epics in Jira               │  5 Epics                          │
│  Priority: Highest Bugs      │  16 Bugs                          │
│  Priority: High Bugs         │  41 Bugs                          │
│  Priority: Low Bugs          │  11 Bugs                          │
│  Priority: Lowest Bugs       │   4 Bugs                          │
│  Bug Tracking Tool           │  Jira — lohithharishmaney.atlassian.net │
│  Automation Language         │  Python + Selenium WebDriver      │
│  Test Case Format            │  Excel (XLSX)                     │
└──────────────────────────────┴───────────────────────────────────┘
```

---

## 🗂 Module-Wise Test Scenario Breakdown

| # | Module | Bugs Found | Priority Highlight |
|---|---|---|---|
| 1 | 🔐 Sign Up | **8 bugs** | XSS script injection accepted in username field |
| 2 | 🔑 Login | **6 bugs** | Space-only username accepted, no caps lock warning |
| 3 | 🛒 Cart | **14 bugs** | Empty cart allows order placement, no cart count in navbar |
| 4 | 📬 Contact | **25 bugs** | SQLi, XSS, CSRF, HTML injection — all accepted |
| 5 | 🎬 About Us | **6 bugs** | Video not reset on modal close, unrelated video content |
| 6 | 🌐 Cross-Browser | **13 bugs** | Touch gestures broken on iOS/Android, deprecated jQuery |
| 7 | 📱 Mobile Responsive | *(covered in Cross-Browser)* | Cart overflow, scroll issues on small screens |

---

## 🧪 Testing Methodologies

### 1. 🔍 Exploratory Testing
Unscripted sessions to discover defects beyond scripted scenarios:
- Navigating the application with no predefined path
- Rapid clicks, back button abuse, direct URL manipulation
- Session boundary testing across multiple tabs
- Space-only inputs, empty field submissions, sequential rapid form submits

### 2. ⬛ Black-Box Functional Testing
End-user perspective testing employing:
- **Equivalence Partitioning** — Valid/invalid input classes
- **Boundary Value Analysis** — Min, max, and edge boundary values
- **Decision Table Testing** — Input conditions mapped to expected outputs
- **State Transition Testing** — Logged-in vs. logged-out state validation

### 3. 🔒 Security Testing
Probed key input fields for:
- **XSS (Cross-Site Scripting)** — Script injection in username and contact fields
- **SQL Injection** — Malicious query inputs accepted in forms (DBPS-50)
- **CSRF** — Cross-site request forgery vulnerability on form submission (DBPS-51)
- **HTML Injection** — Raw HTML accepted as form input (DBPS-52)

### 4. ❌ Negative Testing
Every module contains negative test cases validating:
- Proper error messages on invalid input
- No crash on malformed or empty data
- No unintended data persistence or state corruption

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
| DBPS-14 | Video scale should be 320px but does not match specification | 🔴 High |
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
| DBPS-36 | Email field accepts input without a domain (e.g., no '.com') | 🔴 High |
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
| DBPS-51 | CSRF (Cross-Site Request Forgery) vulnerability not mitigated | 🔴🔴 Highest |
| DBPS-52 | Input fields accept and render raw HTML from users | 🔴🔴 Highest |
| DBPS-53 | No rate limiting — form submitted 10+ times consecutively without block | 🔴 High |
| DBPS-54 | No loading indicator displayed on 3G network conditions | 🔴 High |
| DBPS-55 | Field labels are missing from the contact form | 🔴 High |
| DBPS-56 | Trimmed space inputs are still read as valid by the form | 🔴 High |
| DBPS-57 | User can send 5 messages rapidly back-to-back without any throttle | 🔴 High |
| DBPS-58 | No failure indication shown to user when server is down on submission | 🔴 High |

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
| DBPS-69 | Cart table overflows screen and requires horizontal scroll on Android Chrome | 🔴🔴 Highest |
| DBPS-70 | Console warnings across browsers: deprecated jQuery `.size()` in Bootstrap 3 | 🔴🔴 Highest |
| DBPS-71 | Missing `aria-label` attributes on UI elements affecting screen reader accessibility | 🟡 Low |
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
  │ 🌐 CrossBrowser  │  13   │ ███████████████░░░░░░░░░░░░░░░  18%│
  │ 🔐 Signup        │   8   │ ██████████░░░░░░░░░░░░░░░░░░░░  11%│
  │ 🔑 Login         │   6   │ ███████░░░░░░░░░░░░░░░░░░░░░░░   8%│
  │ 🎬 About Us      │   6   │ ███████░░░░░░░░░░░░░░░░░░░░░░░   8%│
  └──────────────────┴───────┴────────────────────────────────────┘

  BUG LIFECYCLE (All 72 bugs in Jira):
  New → Open → In Progress → Fixed → Retest → Closed
                                 ↓
                            Reopened (if fix fails)

  Current Status: All 72 bugs in [ To Do ] — awaiting developer fixes for retest cycle
```

---

## 🤖 Automation Suite

The repository includes a **Selenium WebDriver automation suite** located in the `Demoblaze automation/` directory — built with HTML, Python, and CSS to cover key regression scenarios on the DemoBlaze platform.

| Layer | Technology |
|---|---|
| Browser Automation | Selenium WebDriver |
| Scripting Language | Python |
| UI / Reporting | HTML + CSS |
| Target Browser | Chrome (primary) |

**Planned Enhancements:**

```
Phase 2 — Framework Enhancement
  ├── Page Object Model (POM) refactoring
  ├── Data-Driven Testing with Excel / JSON datasets
  ├── Parallel cross-browser execution
  └── Allure / Extent Reports integration

Phase 3 — CI/CD Pipeline
  ├── GitHub Actions automated trigger on push / PR
  └── Live test dashboard with pass/fail reporting
```

---

## 🛠 Tools & Technologies

| Category | Tool / Technology | Purpose |
|---|---|---|
| Test Documentation | Microsoft Excel | Test scenarios & test cases |
| Bug Tracking | **Jira (Project: DBPS)** | 72 bugs tracked end-to-end |
| Automation | **Selenium WebDriver + Python** | Automated regression testing |
| Browser Testing | Chrome, Firefox, Edge, Safari | Cross-browser compatibility |
| Mobile Testing | Chrome DevTools (Device Emulation) | Responsive design validation |
| Screen Capture | Snipping Tool / Lightshot | Bug evidence capture |
| Version Control | **Git & GitHub** | Repository and artifact management |
| Reporting (Planned) | Allure / Extent Reports | Test execution dashboards |
| CI/CD (Planned) | GitHub Actions | Continuous testing pipeline |

---

## 📂 Project Structure

```
📦 Demo-Blaze-Application-testing-Project/
│
├── 📁 01_Project_Documentation/
│   └── Project scope, objectives, and test planning documents
│
├── 📁 02_Exploratory Testing/
│   └── Session-based exploratory testing notes and findings
│
├── 📁 03_Test scenario/
│   └── DemoBlaze_Test_Scenarios.xlsx    # 18 master test scenarios
│
├── 📁 04_Test Cases/
│   ├── Signup_Test_Cases.xlsx
│   ├── Login_Test_Cases.xlsx
│   ├── Logout_Test_Cases_Updated.xlsx
│   ├── HomePage_Test_Cases_Updated.xlsx
│   ├── Contact_Test_Cases_Updated.xlsx
│   ├── ProductCategories_Test_Cases_Updated.xlsx
│   ├── ProductDetails_Test_Cases_Updated.xlsx
│   ├── Cart_Test_Cases_Updated.xlsx
│   ├── PlaceOrder_Test_Cases_Updated.xlsx
│   ├── OrderConfirmation_Test_Cases_Updated.xlsx
│   ├── CrossBrowser_Test_Cases_Updated.xlsx
│   └── MobileResponsive_Test_Cases_Updated.xlsx
│
├── 📁 05_Executed test cases/
│   └── Test execution results and pass/fail records
│
├── 📁 06_Defect Reports/
│   └── 72 bugs tracked in Jira — DBPS-1 through DBPS-78
│
├── 📁 08_Application_Screenshots/
│   └── Application screenshots used as test evidence
│
├── 📁 Demoblaze automation/             # ✅ Selenium Automation Suite
│   ├── HTML test files
│   ├── Python automation scripts
│   └── CSS styling / report templates
│
├── LICENSE
└── README.md                           # ← You are here
```

---

## 💡 Key Learnings & Highlights

- 🔐 **Security vulnerabilities discovered** — XSS, SQL Injection, CSRF, and HTML injection were all confirmed in the Contact module (DBPS-49 to DBPS-52), demonstrating a security-aware testing mindset beyond basic functional coverage.

- 🐛 **72 bugs logged in Jira (Project: DBPS)** across 6 modules with complete defect lifecycle tracking, reflecting practical experience with enterprise-grade bug management in Agile/Scrum environments.

- 📋 **18 test scenarios + 1,000+ test cases** authored across 12 module files — demonstrating strong skills in requirement decomposition, test condition identification, and comprehensive coverage design.

- 🤖 **Selenium WebDriver automation suite** built alongside manual testing, bridging the gap between manual and automated QA — a skill set highly valued in modern engineering roles.

- 📱 **Cross-browser and mobile testing** exposed critical rendering inconsistencies — swipe gesture failures on iOS Safari and Android Chrome (DBPS-64, DBPS-67), cart overflow issues (DBPS-66, DBPS-69), and deprecated jQuery warnings affecting all browsers (DBPS-70).

- 📊 **Testing techniques applied** — Boundary Value Analysis, Equivalence Partitioning, State Transition Testing, Decision Table Testing, and Negative Testing, reflecting structured and methodical QA engineering practices.

---

## 👤 Author

<div align="center">

**MH Lohith**
*QA Engineer | Manual Testing | Selenium Automation | Security Testing*

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0077B5?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/in/lohithharish)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-181717?style=for-the-badge&logo=github)](https://github.com/lohithharish)
[![Jira](https://img.shields.io/badge/Jira-DBPS%20Project-0052CC?style=for-the-badge&logo=jira)](https://lohithharishmaney.atlassian.net/jira/software/projects/DBPS/summary)
[![Email](https://img.shields.io/badge/Email-Contact-D14836?style=for-the-badge&logo=gmail)](mailto:lohithharishmv@gmail.com)

---

### ⭐ If this project impressed you, please consider giving it a star!

*This project is part of an active QA portfolio — continuously updated with new bug reports, test executions, and automation enhancements.*

**72 bugs found. 18 scenarios covered. Tested with precision. 🎯**

</div>
