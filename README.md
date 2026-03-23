<div align="center">

# 🛒 DemoBlaze E-Commerce — End-to-End Quality Assurance Project

<img src="https://img.shields.io/badge/Testing%20Type-Manual%20%7C%20Functional-blue?style=for-the-badge&logo=testcafe" />
<img src="https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge" />
<img src="https://img.shields.io/badge/Test%20Cases-1000%2B-orange?style=for-the-badge" />
<img src="https://img.shields.io/badge/Bug%20Tracking-Jira-0052CC?style=for-the-badge&logo=jira" />
<img src="https://img.shields.io/badge/Automation-Selenium%20%7C%20Python-yellow?style=for-the-badge&logo=selenium" />
<img src="https://img.shields.io/badge/License-MIT-red?style=for-the-badge" />

<br/>

> **A comprehensive, industry-standard QA portfolio project** demonstrating full-cycle software testing of the [DemoBlaze](https://www.demoblaze.com/) e-commerce platform — spanning exploratory testing, structured test design, execution, defect lifecycle management, and Selenium-based automation.

<br/>

**🔗 Application Under Test:** [https://www.demoblaze.com](https://www.demoblaze.com)

---

</div>

## 📋 Table of Contents

- [Project Overview](#-project-overview)
- [Testing Scope & Objectives](#-testing-scope--objectives)
- [Test Artifacts](#-test-artifacts)
- [Test Coverage Summary](#-test-coverage-summary)
- [Module-Wise Test Case Breakdown](#-module-wise-test-case-breakdown)
- [Testing Methodologies](#-testing-methodologies)
- [Automation Suite](#-automation-suite)
- [Bug Reporting & Defect Management](#-bug-reporting--defect-management)
- [Tools & Technologies](#-tools--technologies)
- [Project Structure](#-project-structure)
- [Key Learnings & Highlights](#-key-learnings--highlights)
- [Author](#-author)

---

## 🧭 Project Overview

**DemoBlaze** is a publicly accessible e-commerce product store widely used in the QA community as a realistic testing target. This project represents a **complete QA engagement** — simulating the end-to-end testing workflow expected at enterprise-level software organizations.

This repository showcases:

| Capability | Details |
|---|---|
| 📌 **Test Planning** | Structured test scenarios aligned to business requirements |
| 📝 **Test Case Design** | 1,000+ detailed test cases with steps, expected results, and priority tagging |
| 🔍 **Exploratory Testing** | Unscripted sessions to surface hidden edge cases |
| 🤖 **Test Automation** | Selenium WebDriver automation suite (HTML + Python + CSS) |
| 🐛 **Defect Management** | Full bug lifecycle tracking using **Jira** |
| 📊 **QA Documentation** | Professional, stakeholder-ready test documentation |

---

## 🎯 Testing Scope & Objectives

### ✅ In Scope

| Domain | Coverage |
|---|---|
| Functional Testing | All core user flows — Sign Up, Login, Logout, Cart, Orders |
| UI/UX Testing | Layout, navigation, visual consistency |
| Boundary & Negative Testing | Invalid inputs, empty fields, edge values |
| Cross-Browser Testing | Chrome, Firefox, Safari, Edge |
| Mobile Responsiveness Testing | Multiple screen resolutions and device simulations |
| Exploratory Testing | Unscripted discovery of hidden defects |
| **Test Automation** | **Selenium WebDriver automation suite (HTML/Python/CSS)** |

### ❌ Out of Scope (Current Phase)

- Performance / Load Testing
- Security / Penetration Testing
- API Testing *(planned for next phase)*
- Database Testing

### 🎯 Objectives

1. Validate that all critical user journeys function correctly end-to-end
2. Identify and document defects with clear reproduction steps
3. Ensure cross-browser and cross-device compatibility
4. Automate key regression scenarios using Selenium
5. Produce professional-grade QA artifacts demonstrating industry readiness

---

## 📁 Test Artifacts

| Artifact | Description | Status |
|---|---|---|
| `DemoBlaze_Test_Scenarios.xlsx` | Master test scenarios document — 20 scenarios across all modules | ✅ Complete |
| `Signup_Test_Cases.xlsx` | Test cases for user registration module | ✅ Complete |
| `Login_Test_Cases.xlsx` | Test cases for authentication module | ✅ Complete |
| `Logout_Test_Cases_Updated.xlsx` | Session termination and redirect validation | ✅ Complete |
| `HomePage_Test_Cases_Updated.xlsx` | Home page UI, slider, and navigation | ✅ Complete |
| `Contact_Test_Cases_Updated.xlsx` | Contact form validation and submission | ✅ Complete |
| `ProductCategories_Test_Cases_Updated.xlsx` | Category filter and product listing | ✅ Complete |
| `ProductDetails_Test_Cases_Updated.xlsx` | Product page content, images, pricing | ✅ Complete |
| `Cart_Test_Cases_Updated.xlsx` | Cart operations, total calculation, item management | ✅ Complete |
| `PlaceOrder_Test_Cases_Updated.xlsx` | Checkout form validation and order placement | ✅ Complete |
| `OrderConfirmation_Test_Cases_Updated.xlsx` | Order confirmation display and data accuracy | ✅ Complete |
| `CrossBrowser_Test_Cases_Updated.xlsx` | Chrome, Firefox, Edge, Safari compatibility | ✅ Complete |
| `MobileResponsive_Test_Cases_Updated.xlsx` | Responsive design across device sizes | ✅ Complete |
| `Demoblaze Automation/` | Selenium-based automation suite (HTML + Python + CSS) | ✅ Available |

---

## 📊 Test Coverage Summary

```
┌─────────────────────────────────────────────────────────────────┐
│                    TEST COVERAGE AT A GLANCE                    │
├─────────────────────────────┬───────────────────────────────────┤
│  Total Test Scenarios       │  20 Scenarios                     │
│  Total Test Cases           │  1,000+                           │
│  Priority P0 Scenarios      │  12 (Critical)                    │
│  Priority P1 Scenarios      │  8  (High)                        │
│  Modules Covered            │  12 Functional Modules            │
│  Cross-Browser Cases        │  119 Cases (4 Browsers)           │
│  Mobile Responsive Cases    │  120 Cases (Multiple Viewports)   │
│  Bug Tracking Tool          │  Jira                             │
│  Test Case Format           │  Excel (XLSX)                     │
│  Automation Language        │  Python + Selenium WebDriver      │
└─────────────────────────────┴───────────────────────────────────┘
```

---

## 🗂 Module-Wise Test Case Breakdown

| # | Module | Test Scenario ID | Test Cases | Priority | Description |
|---|---|---|---|---|---|
| 1 | 🔐 Sign Up | TS_001 | 50 | P0 | Registration form, duplicate users, validation |
| 2 | 🔑 Login | TS_002 | 63 | P0 | Valid/invalid credentials, session handling |
| 3 | 🚪 Logout | TS_003 | 70 | P0 | Session clearing, redirect after logout |
| 4 | 🏠 Home Page | TS_004, TS_005, TS_010, TS_011 | 79 | P0/P1 | Page elements, slider, navigation buttons |
| 5 | 📬 Contact Page | TS_006, TS_007 | 90 | P0 | Contact form validation and submission |
| 6 | 🗂 Product Categories | TS_008 | 79 | P0 | Category filters, product listing display |
| 7 | 📦 Product Details | TS_009 | 89 | P0 | Product images, pricing, add to cart |
| 8 | 🛒 Cart | TS_012 | 99 | P0 | Cart management, price calculation |
| 9 | 💳 Place Order | TS_013, TS_019 | 114 | P0 | Checkout flow, form validation |
| 10 | ✅ Order Confirmation | TS_014, TS_020 | 99 | P0 | Confirmation message, order data accuracy |
| 11 | 🌐 Cross-Browser | TS_016 | 119 | P0 | Chrome, Firefox, Safari, Edge |
| 12 | 📱 Mobile Responsive | TS_017 | 120 | P0 | Various screen sizes and touch interactions |

---

## 🧪 Testing Methodologies

### 1. 🔍 Exploratory Testing
Conducted unscripted exploratory sessions to discover defects that scripted testing might miss:
- Navigating application with no predefined path
- Attempting unexpected user behaviors (rapid clicks, back button abuse, direct URL manipulation)
- Session boundary testing across multiple tabs
- Documenting findings in structured session notes

### 2. ⬛ Black-Box Functional Testing
All test cases were authored from an end-user perspective, employing:
- **Equivalence Partitioning** — Grouped inputs into valid/invalid classes
- **Boundary Value Analysis** — Tested values at min, max, and edge boundaries
- **Decision Table Testing** — Mapped input conditions to expected outputs for forms
- **State Transition Testing** — Validated user states (logged in vs. logged out)

### 3. 🔁 Regression Testing Mindset
Test cases were structured to be reusable across builds, enabling quick regression cycles when defects are fixed or features are updated.

### 4. ❌ Negative Testing
Every functional module includes negative test cases designed to:
- Validate proper error message display
- Ensure the application does not crash on invalid input
- Confirm no unintended data persistence or state corruption

---

## 🤖 Automation Suite

The repository includes a **Selenium WebDriver automation suite** built with HTML, Python, and CSS. The automation project is located in the `Demoblaze automation/` directory and covers key regression scenarios on the DemoBlaze platform.

**Tech Stack:**

| Layer | Technology |
|---|---|
| Browser Automation | Selenium WebDriver |
| Language | Python |
| UI/Reporting | HTML + CSS |
| Target Browser | Chrome (primary) |

**Upcoming Automation Enhancements:**

```
Phase 2 — Framework Enhancement (Planned)
  ├── Page Object Model (POM) refactoring
  ├── Data-Driven Testing with Excel/JSON
  ├── Parallel cross-browser execution
  └── Allure / Extent Reports integration

Phase 3 — CI/CD Integration (Planned)
  ├── GitHub Actions pipeline
  ├── Automated test triggers on push/PR
  └── Test dashboard with reporting
```

---

## 🐛 Bug Reporting & Defect Management

All identified defects were logged, tracked, and managed using **Jira** with the following defect lifecycle:

```
New  →  Open  →  In Progress  →  Fixed  →  Retest  →  Closed
                                    ↓
                               Reopened  (if fix fails)
```

### Bug Report Template Used in Jira

| Field | Details |
|---|---|
| **Bug ID** | Auto-generated by Jira |
| **Title** | Clear, concise one-liner |
| **Severity** | Critical / Major / Minor / Trivial |
| **Priority** | P0 / P1 / P2 / P3 |
| **Module** | Affected module/feature |
| **Environment** | Browser, OS, Screen Size |
| **Steps to Reproduce** | Numbered, precise steps |
| **Expected Result** | What should happen |
| **Actual Result** | What actually happened |
| **Screenshots / Videos** | Attached evidence |
| **Test Case Reference** | Linked test case ID |

---

## 🛠 Tools & Technologies

| Category | Tool / Technology | Purpose |
|---|---|---|
| Test Documentation | Microsoft Excel | Test scenarios & test cases |
| Bug Tracking | **Jira** | Defect lifecycle management |
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
│   └── Project scope, objectives, and planning documents
│
├── 📁 02_Exploratory Testing/
│   └── Exploratory testing session notes and findings
│
├── 📁 03_Test scenario/
│   └── DemoBlaze_Test_Scenarios.xlsx        # Master scenario document (20 scenarios)
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
│   └── Jira-exported bug reports and defect logs
│
├── 📁 08_Application_Screenshots/
│   └── Application screenshots used as test evidence
│
├── 📁 Demoblaze automation/                 # ✅ Selenium Automation Suite
│   ├── HTML test files
│   ├── Python scripts
│   └── CSS styling / reports
│
├── LICENSE
└── README.md                                # ← You are here
```

---

## 💡 Key Learnings & Highlights

- 🔎 **Exploratory Testing** revealed several edge-case bugs entirely missed during scripted test design — demonstrating the critical value of unscripted testing sessions alongside formal test case execution.

- 📋 **Designing 1,000+ test cases** across 12 modules developed strong analytical skills in requirement decomposition, test condition identification, and systematic coverage mapping.

- 🤖 **Building a Selenium automation suite** alongside manual testing demonstrates the ability to bridge both disciplines — a highly sought-after skill in modern QA roles.

- 🐛 **Working with Jira** throughout the complete bug lifecycle reinforced professional defect communication skills essential in Agile/Scrum environments.

- 📱 **Cross-browser and mobile testing** exposed inconsistencies in CSS rendering and responsive breakpoints that are commonly overlooked yet critical for user experience.

- 📊 Structuring test cases with **Boundary Value Analysis** and **Equivalence Partitioning** demonstrated the ability to design effective, lean, yet comprehensive test suites.

---

## 👤 Author

<div align="center">

**MH Lohith**
*QA Engineer | Manual Tester | Selenium Automation*

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0077B5?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/in/lohithharish)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-181717?style=for-the-badge&logo=github)](https://github.com/lohithharish)
[![Email](https://img.shields.io/badge/Email-Contact-D14836?style=for-the-badge&logo=gmail)](mailto:lohithharishmv@gmail.com)

---

### ⭐ If this project impressed you, please consider giving it a star!

*This project is part of an active QA portfolio — continuously updated with new test artifacts, execution results, and automation enhancements.*

**Built with dedication. Tested with precision. 🎯**

</div>
