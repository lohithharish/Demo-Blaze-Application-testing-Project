<div align="center">

# 🛒 DemoBlaze E-Commerce — Quality Assurance Testing Project

[![Testing Type](https://img.shields.io/badge/Testing-Manual-blue?style=for-the-badge&logo=testcafe)](https://github.com/)
[![Status](https://img.shields.io/badge/Status-In%20Progress-yellow?style=for-the-badge)](https://github.com/)
[![Automation](https://img.shields.io/badge/Automation-Coming%20Soon-orange?style=for-the-badge&logo=selenium)](https://github.com/)
[![Bug Tracking](https://img.shields.io/badge/Bug%20Tracking-Jira-0052CC?style=for-the-badge&logo=jira)](https://www.atlassian.com/software/jira)
[![Test Cases](https://img.shields.io/badge/Test%20Cases-1000%2B-green?style=for-the-badge)](https://github.com/)
[![License](https://img.shields.io/badge/License-MIT-red?style=for-the-badge)](LICENSE)

<br/>

> **A comprehensive, industry-standard QA portfolio project** demonstrating end-to-end manual testing of the [DemoBlaze](https://www.demoblaze.com/) e-commerce application — covering exploratory testing, structured test scenario design, detailed test case execution, and defect lifecycle management via Jira.

<br/>

**🔗 Application Under Test:** [https://www.demoblaze.com](https://www.demoblaze.com)

---

</div>

## 📋 Table of Contents

- [Project Overview](#-project-overview)
- [Testing Scope & Objectives](#-testing-scope--objectives)
- [Test Artifacts](#-test-artifacts)
- [Test Coverage Summary](#-test-coverage-summary)
- [Module-wise Test Case Breakdown](#-module-wise-test-case-breakdown)
- [Testing Methodologies](#-testing-methodologies)
- [Bug Reporting & Defect Management](#-bug-reporting--defect-management)
- [Tools & Technologies](#-tools--technologies)
- [Project Structure](#-project-structure)
- [Test Execution Results](#-test-execution-results)
- [Roadmap — Automation Phase](#-roadmap--automation-phase)
- [Key Learnings & Highlights](#-key-learnings--highlights)
- [Author](#-author)

---

## 🧭 Project Overview

**DemoBlaze** is a publicly accessible e-commerce product store used widely in the QA community as a practice and demonstration platform. This project represents a **full-cycle manual QA engagement** — simulating the kind of real-world testing workflow expected at top-tier software companies.

This repository showcases:

- 📌 Structured **Test Scenario** design aligned with business requirements
- 📝 Detailed **Test Case** authoring with clear steps, expected results, and priority tagging
- 🔍 **Exploratory Testing** sessions to uncover edge cases beyond scripted scenarios
- 🐛 **Defect Reporting** with complete bug lifecycle tracking in **Jira**
- 📊 Organized, professional **test documentation** ready for stakeholder review

> This project is actively maintained and will be extended with an **Automation Testing suite** using Selenium/Cypress/Playwright in the upcoming phase.

---

## 🎯 Testing Scope & Objectives

### In Scope

| Domain | Coverage |
|--------|----------|
| Functional Testing | All core user flows — Sign Up, Login, Logout, Cart, Orders |
| UI/UX Testing | Layout, navigation, visual consistency |
| Boundary & Negative Testing | Invalid inputs, empty fields, edge values |
| Cross-Browser Testing | Chrome, Firefox, Safari, Edge |
| Mobile Responsiveness Testing | Multiple screen resolutions and device simulations |
| Exploratory Testing | Unscripted discovery of hidden defects |

### Out of Scope (Current Phase)

- Performance / Load Testing
- Security / Penetration Testing
- API Testing *(planned for automation phase)*
- Database Testing

### Objectives

1. Validate that all critical user journeys function correctly end-to-end
2. Identify and document defects with clear reproduction steps
3. Ensure cross-browser and cross-device compatibility
4. Produce professional-grade QA artifacts demonstrating industry readiness

---

## 📁 Test Artifacts

| Artifact | Description | Status |
|----------|-------------|--------|
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

---

## 📊 Test Coverage Summary

```
┌─────────────────────────────────────────────────────────────┐
│                   TEST COVERAGE AT A GLANCE                 │
├─────────────────────────┬───────────────────────────────────┤
│  Total Test Scenarios   │  20 Scenarios                     │
│  Total Test Cases       │  1,000+                           │
│  Priority P0 Scenarios  │  12 (Critical)                    │
│  Priority P1 Scenarios  │  8  (High)                        │
│  Modules Covered        │  12 Functional Modules            │
│  Cross-Browser Cases    │  120 Cases (4 Browsers)           │
│  Mobile Responsive Cases│  121 Cases (Multiple Viewports)   │
│  Bug Tracking Tool      │  Jira                             │
│  Test Case Format       │  Excel (XLSX)                     │
└─────────────────────────┴───────────────────────────────────┘
```

---

## 🗂 Module-wise Test Case Breakdown

| # | Module | Test Scenario ID | Test Cases | Priority | Description |
|---|--------|-----------------|------------|----------|-------------|
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

### 1. Exploratory Testing
Conducted unscripted exploratory sessions to discover defects that scripted testing might miss. This included:
- Navigating application with no predefined path
- Attempting unexpected user behaviors (rapid clicks, back button abuse, direct URL manipulation)
- Session boundary testing across multiple tabs
- Documenting findings in structured session notes

### 2. Black-Box Functional Testing
All test cases were written from an end-user perspective without knowledge of internal code structure:
- **Equivalence Partitioning** — Grouped inputs into valid/invalid classes
- **Boundary Value Analysis** — Tested values at min, max, and edge boundaries
- **Decision Table Testing** — Mapped input conditions to expected outputs for forms
- **State Transition Testing** — Validated user states (logged in vs. logged out)

### 3. Regression Mindset
Test cases were structured to be reusable across builds, allowing for quick regression cycles when defects are fixed or features are updated.

### 4. Negative Testing
Every functional module includes negative test cases designed to:
- Validate proper error message display
- Ensure the application does not crash on invalid input
- Confirm no unintended data persistence or state corruption

---

## 🐛 Bug Reporting & Defect Management

All identified defects were logged, tracked, and managed using **Jira** with the following defect lifecycle:

```
New → Open → In Progress → Fixed → Retest → Closed
                              ↓
                          Reopened (if fix fails)
```

### Bug Report Template Used in Jira

| Field | Details |
|-------|---------|
| **Bug ID** | Auto-generated by Jira |
| **Title** | Clear, concise one-liner |
| **Severity** | Critical / Major / Minor / Trivial |
| **Priority** | P0 / P1 / P2 / P3 |
| **Module** | Affected module/feature |
| **Environment** | Browser, OS, Screen Size |
| **Steps to Reproduce** | Numbered, precise steps |
| **Expected Result** | What should happen |
| **Actual Result** | What actually happened |
| **Screenshots/Videos** | Attached evidence |
| **Test Case Ref** | Linked test case ID |

---

## 🛠 Tools & Technologies

| Category | Tool | Purpose |
|----------|------|---------|
| Test Documentation | Microsoft Excel / Google Sheets | Test scenarios & test cases |
| Bug Tracking | **Jira** | Defect lifecycle management |
| Browser Testing | Chrome, Firefox, Edge, Safari | Cross-browser compatibility |
| Mobile Testing | Chrome DevTools (Device Emulation) | Responsive design validation |
| Screen Capture | Snipping Tool / Lightshot | Bug evidence capture |
| Version Control | **Git & GitHub** | Repository and artifact management |
| Communication | Confluence *(planned)* | Test reports & documentation hub |
| **Automation (Upcoming)** | Selenium / Cypress / Playwright | Automated regression suite |
| **Framework (Upcoming)** | TestNG / JUnit / Mocha | Test execution framework |
| **CI/CD (Upcoming)** | GitHub Actions / Jenkins | Continuous testing pipeline |

---

## 📂 Project Structure

```
📦 demoblaze-qa-testing/
│
├── 📁 Test-Scenarios/
│   └── DemoBlaze_Test_Scenarios.xlsx          # Master scenario document
│
├── 📁 Test-Cases/
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
├── 📁 Bug-Reports/
│   └── [Jira exported bug reports - PDF/Screenshots]
│
├── 📁 Test-Reports/
│   └── [Execution summary reports]
│
├── 📁 Automation/                             # 🚧 Coming Soon
│   ├── src/
│   ├── tests/
│   ├── reports/
│   └── README.md
│
└── README.md                                  # ← You are here
```

---

## 📈 Test Execution Results

> ⚠️ *Execution in progress. Results will be updated upon completion of each module's test cycle.*

| Module | Total TCs | Executed | Passed | Failed | Blocked | Pass % |
|--------|-----------|----------|--------|--------|---------|--------|
| Sign Up | 50 | — | — | — | — | — |
| Login | 63 | — | — | — | — | — |
| Logout | 70 | — | — | — | — | — |
| Home Page | 79 | — | — | — | — | — |
| Contact | 90 | — | — | — | — | — |
| Product Categories | 79 | — | — | — | — | — |
| Product Details | 89 | — | — | — | — | — |
| Cart | 99 | — | — | — | — | — |
| Place Order | 114 | — | — | — | — | — |
| Order Confirmation | 99 | — | — | — | — | — |
| Cross-Browser | 119 | — | — | — | — | — |
| Mobile Responsive | 120 | — | — | — | — | — |
| **TOTAL** | **~1,071** | — | — | — | — | — |

---

## 🚀 Roadmap — Automation Phase

The next phase of this project will implement a full **Automation Testing Suite**. Here is the planned roadmap:

```
Phase 1 — Manual Testing (✅ Current)
  └── Exploratory, Functional, Cross-browser, Mobile Responsive

Phase 2 — Automation Framework Setup (🔜 Upcoming)
  ├── Tool Selection: Selenium WebDriver / Cypress / Playwright
  ├── Language: Java / JavaScript / Python
  ├── Framework: Page Object Model (POM)
  └── Test Runner: TestNG / Mocha / pytest

Phase 3 — Test Automation (🔜 Upcoming)
  ├── Automate Smoke Test Suite (P0 critical paths)
  ├── Automate Regression Suite
  ├── Data-Driven Testing with Excel/JSON
  └── Parallel Execution across browsers

Phase 4 — CI/CD Integration (🔜 Upcoming)
  ├── GitHub Actions pipeline
  ├── Automated test triggers on every push/PR
  └── Allure / Extent Reports for test dashboards

Phase 5 — API Testing (🔜 Upcoming)
  └── REST API testing with Postman / RestAssured
```

---

## 💡 Key Learnings & Highlights

- 🔎 **Exploratory Testing** revealed several edge-case bugs that were entirely missed during scripted test design — demonstrating the critical value of unscripted testing sessions
- 📋 Writing **1,000+ test cases** across 12 modules developed strong analytical skills in requirement decomposition and test condition identification
- 🐛 Working with **Jira** throughout the bug lifecycle reinforced professional defect communication skills essential in Agile/Scrum team environments
- 📱 **Cross-browser and mobile testing** exposed inconsistencies in CSS rendering and responsive breakpoints that are commonly overlooked
- 📊 Structuring test cases with **Boundary Value Analysis** and **Equivalence Partitioning** demonstrated the ability to design effective, minimal, yet comprehensive test suites

---

## 👤 Author

<div align="center">

**MH Lohith**
*QA Engineer | Manual Tester | Automation Enthusiast*

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0077B5?style=for-the-badge&logo=linkedin)]([https://linkedin.com/](https://www.linkedin.com/in/lohith-harish-computer-engineer-aiandml/))
[![GitHub](https://img.shields.io/badge/GitHub-Follow-181717?style=for-the-badge&logo=github)]([https://github.com/](https://github.com/lohithharish))
[![Email](https://img.shields.io/badge/Email-Contact-D14836?style=for-the-badge&logo=gmail)](mailto:lohithharishmv@gmail.com)

</div>

---

<div align="center">

### ⭐ If this project helped you or impressed you, please consider giving it a star!

*This project is part of an active QA portfolio — regularly updated with new test artifacts, execution results, and soon, automation scripts.*

**Built with dedication, tested with precision. 🎯**

</div>
