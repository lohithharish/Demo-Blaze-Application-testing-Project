# 🧪 DemoBlaze — Manual & Exploratory Testing Project

> **Project Type:** Manual Testing | Exploratory Testing | Defect Reporting  
> **Application Under Test:** [DemoBlaze Product Store](https://www.demoblaze.com)  
> **Testing Environment:** Web (Chrome, Firefox, Edge, Safari)  
> **Project Status:** ✅ Test Execution Complete | 🔄 Automation Phase Planned  

---

## 📋 Table of Contents

- [Project Overview](#project-overview)
- [Application Under Test](#application-under-test)
- [Test Scope](#test-scope)
- [Repository Structure](#repository-structure)
- [Test Summary](#test-summary)
- [Defects Found](#defects-found)
- [Tools & Technologies](#tools--technologies)
- [How to Navigate This Repository](#how-to-navigate-this-repository)
- [Future Scope — Automation](#future-scope--automation)
- [Author](#author)

---

## Project Overview

This repository contains end-to-end manual and exploratory testing artifacts for the **DemoBlaze e-commerce web application**. The project follows a structured QA lifecycle — from requirement analysis and test planning through test design, execution, defect reporting, and summary reporting — simulating a real-world enterprise QA engagement.

All testing was conducted independently, covering functional, UI, cross-browser, and mobile responsive testing aspects of the application.

---

## Application Under Test

| Attribute         | Details                                      |
|-------------------|----------------------------------------------|
| **Application**   | DemoBlaze — Product Store                    |
| **URL**           | https://www.demoblaze.com                    |
| **Type**          | E-Commerce Web Application                   |
| **Tech Stack**    | HTML, CSS, JavaScript (Front-end SPA)        |
| **Modules Tested**| Home, Login, Signup, Product Catalog, Cart, Place Order, Order Confirmation, Contact, Cross-Browser, Mobile Responsive |

---

## Test Scope

### ✅ In Scope

| Module                  | Testing Type                            |
|-------------------------|-----------------------------------------|
| User Registration       | Functional, Boundary, Negative Testing  |
| Login / Logout          | Functional, Security, Negative Testing  |
| Home Page               | UI, Navigation, Functional Testing      |
| Product Categories      | Functional, UI Testing                  |
| Product Details Page    | Functional, UI Testing                  |
| Shopping Cart           | Functional, E2E Testing                 |
| Place Order             | Functional, E2E, Boundary Testing       |
| Order Confirmation      | Functional, Validation Testing          |
| Contact Form            | Functional, Negative Testing            |
| Cross-Browser Testing   | Compatibility Testing (Chrome, Firefox, Edge) |
| Mobile Responsiveness   | Responsive/UI Testing                   |

### ❌ Out of Scope

- Backend / API testing
- Performance & load testing
- Payment gateway integration testing (live)
- Automated regression testing *(planned for future)*

---

## Repository Structure

```
demoblaze-testing-project/
│
├── README.md                          ← You are here
│
├── 01_Project_Documentation/
│   ├── Test_Plan.docx                 ← Scope, approach, schedule, resources
│   ├── Test_Strategy.docx             ← Testing methodology & standards
│   └── Requirement_Scope.md          ← Feature list & acceptance criteria
│
├── 02_Exploratory_Testing/
│   └── Exploratory_Testing_Notes.xlsx ← Session-based charter notes & findings
│
├── 03_Test_Scenarios/
│   └── Test_Scenarios.xlsx            ← High-level scenarios for all modules
│
├── 04_Test_Cases/
│   ├── Login_Test_Cases.xlsx
│   ├── Signup_Test_Cases.xlsx
│   ├── HomePage_Test_Cases.xlsx
│   ├── ProductCategories_Test_Cases.xlsx
│   ├── ProductDetails_Test_Cases.xlsx
│   ├── Cart_Test_Cases.xlsx
│   ├── PlaceOrder_Test_Cases.xlsx
│   ├── OrderConfirmation_Test_Cases.xlsx
│   ├── Logout_Test_Cases.xlsx
│   ├── Contact_Test_Cases.xlsx
│   ├── CrossBrowser_Test_Cases.xlsx
│   └── MobileResponsive_Test_Cases.xlsx
│
├── 05_Test_Execution/
│   └── Test_Execution_Report.xlsx     ← Pass/Fail status, run date, tester name
│
├── 06_Defect_Reports/
│   ├── Jira_Bug_Report.html           ← Exported Jira board with all bug entries
│   ├── Bug_01_Add_To_Cart.png         ← Screenshot — Cart bug
│   ├── Bug_02_Login_Issue.png         ← Screenshot — Login bug
│   └── Bug_03_Product_Display.png     ← Screenshot — Product display bug
│
├── 07_Test_Summary_Report/
│   └── Test_Summary_Report.docx       ← Final sign-off report with metrics
│
├── 08_Screenshots/
│   └── Application_Screenshots/       ← UI screenshots taken during testing
│
└── 09_Automation_Testing (Future)/
    ├── selenium-tests/                ← Selenium WebDriver scripts (planned)
    ├── test_scripts/                  ← Reusable helper methods (planned)
    └── test_reports/                  ← Automation run reports (planned)
```

---

## Test Summary

| Metric                        | Count     |
|-------------------------------|-----------|
| **Total Test Cases Written**  | 120+      |
| **Total Test Cases Executed** | 120+      |
| **Test Cases Passed**         | 108       |
| **Test Cases Failed**         | 9         |
| **Test Cases Blocked**        | 3         |
| **Defects Raised**            | 9         |
| **Critical Defects**          | 2         |
| **Modules Covered**           | 11        |
| **Browsers Tested**           | 3 (Chrome, Firefox, Edge) |

### Pass/Fail Distribution

```
Passed   ████████████████████████████████████  90%
Failed   ████                                   7.5%
Blocked  █                                      2.5%
```

---

## Defects Found

| Bug ID   | Module          | Severity | Priority | Status     | Summary                                      |
|----------|-----------------|----------|----------|------------|----------------------------------------------|
| BUG-001  | Cart            | High     | High     | Open       | Product added to cart without user login     |
| BUG-002  | Login           | High     | High     | Open       | No error message on invalid credentials      |
| BUG-003  | Product Display | Medium   | Medium   | Open       | Category ID exposed as `cat` in DOM          |
| BUG-004  | SEO / HTML      | Low      | Low      | Open       | Meta description and author tags are empty   |
| BUG-005  | Signup          | Medium   | Medium   | In Review  | Password field accepts single character      |
| BUG-006  | Cart            | Medium   | High     | Open       | Cart total not updating on item removal      |
| BUG-007  | Contact Form    | Low      | Medium   | Open       | Form submits successfully with all empty fields |
| BUG-008  | Mobile          | Medium   | Medium   | Open       | Navigation menu overlaps content on mobile   |
| BUG-009  | Cross-Browser   | Low      | Low      | Open       | Minor layout shift observed in Firefox       |

> 📎 Full Jira bug reports with steps to reproduce, screenshots, and severity ratings are available in [`06_Defect_Reports/`](./06_Defect_Reports/)

---

## Tools & Technologies

| Category              | Tool / Technology                    |
|-----------------------|--------------------------------------|
| Test Management       | Microsoft Excel, Jira (bug tracking) |
| Bug Tracking          | Jira Software                        |
| Documentation         | Microsoft Word, Markdown             |
| Browser Testing       | Chrome, Firefox, Microsoft Edge      |
| Screen Capture        | Snipping Tool / ShareX               |
| Version Control       | Git & GitHub                         |
| Automation (Planned)  | Selenium WebDriver, Python / Java    |

---

## How to Navigate This Repository

1. **Start with** [`01_Project_Documentation/Test_Plan.docx`](./01_Project_Documentation/Test_Plan.docx) — understand the scope and approach.
2. **Review test scenarios** in [`03_Test_Scenarios/`](./03_Test_Scenarios/) for a high-level overview of what was tested.
3. **Dive into test cases** module-by-module in [`04_Test_Cases/`](./04_Test_Cases/).
4. **Check execution results** in [`05_Test_Execution/Test_Execution_Report.xlsx`](./05_Test_Execution/Test_Execution_Report.xlsx).
5. **Review defects** in [`06_Defect_Reports/`](./06_Defect_Reports/) — HTML Jira export + screenshots.
6. **Read the final summary** in [`07_Test_Summary_Report/`](./07_Test_Summary_Report/).

---

## Future Scope — Automation

The `09_Automation_Testing/` folder is reserved for the upcoming automation phase using **Selenium WebDriver**.

**Planned coverage:**
- Login and Signup flows (smoke + regression)
- Add to Cart and Place Order end-to-end flow
- Cross-browser execution via Selenium Grid
- CI integration via GitHub Actions

**Tech stack planned:**
```
Language  : Python 3.x
Framework : Selenium WebDriver + pytest
Reporting : Allure Reports
CI/CD     : GitHub Actions
```

---

## Author

**Lohith Harish**  
*Manual QA Tester | Aspiring Automation Engineer*  

[![GitHub](https://img.shields.io/badge/GitHub-lohithharish-181717?style=flat&logo=github)](https://github.com/lohithharish)

---

> ⭐ *If this project helped you understand manual testing structure, feel free to star the repository!*
