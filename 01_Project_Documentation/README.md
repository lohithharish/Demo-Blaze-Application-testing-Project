# 🛒 DemoBlaze QA Testing Project

> **Comprehensive manual QA testing engagement for the [DemoBlaze E-Commerce Web Application](https://www.demoblaze.com)**
>
> Prepared by **MH Lohith** · QA Engineer / Manual Tester · v1.0 · January–February 2026

---

## 📋 Project Overview

This repository contains the complete quality assurance documentation, test cases, and defect tracking artifacts for the **DemoBlaze Product Store** — a publicly accessible e-commerce SPA used as an industry-recognized QA practice platform.

| Attribute | Details |
|---|---|
| **Application** | DemoBlaze Product Store |
| **URL** | https://www.demoblaze.com |
| **App Type** | Single-Page Application (SPA) — HTML5, CSS3, JavaScript, REST API |
| **Testing Phase** | Phase 1 — Manual Testing |
| **Total Test Cases** | 1,000+ across 12 modules |
| **Test Scenarios** | 20 high-level scenarios |
| **Status** | Execution Complete |

---

## 📁 Repository Structure

```
demoblaze-qa/
├── README.md                          # This file
├── docs/
│   ├── DemoBlaze_Test_Plan.docx       # Overall QA strategy & scope
│   └── DemoBlaze_Test_Strategy.docx  # Org-level QA methodology document
├── test-scenarios/
│   └── DemoBlaze_Test_Scenarios.xlsx  # 20 high-level scenarios (TS_001–TS_020)
├── test-cases/
│   ├── TC_Signup.xlsx                 # 50 test cases — User Registration
│   ├── TC_Login.xlsx                  # 63 test cases — Authentication
│   ├── TC_Logout.xlsx                 # 70 test cases — Session Termination
│   ├── TC_HomePage.xlsx               # 79 test cases — Home Page
│   ├── TC_Contact.xlsx                # 90 test cases — Contact Form
│   ├── TC_ProductCategories.xlsx      # 79 test cases — Category Browsing
│   ├── TC_ProductDetails.xlsx         # 89 test cases — Product Pages
│   ├── TC_Cart.xlsx                   # 99 test cases — Shopping Cart
│   ├── TC_PlaceOrder.xlsx             # 114 test cases — Checkout Flow
│   ├── TC_OrderConfirmation.xlsx      # 99 test cases — Order Confirmation
│   ├── TC_CrossBrowser.xlsx           # 119 test cases — 4 Browsers
│   └── TC_MobileResponsive.xlsx       # 120 test cases — 7 Viewport Sizes
└── bug-reports/
    └── Bug_Reports_Jira_Export.pdf    # Defect lifecycle records from Jira
```

---

## 🧪 Test Coverage

### Functional Modules

| Module | Priority | Test Scenario | Test Cases |
|---|---|---|---|
| User Registration (Sign Up) | P0 – Critical | TS_001 | 50 |
| User Authentication (Login) | P0 – Critical | TS_002 | 63 |
| User Logout | P0 – Critical | TS_003 | 70 |
| Home Page Load & Display | P0 – Critical | TS_004 | 79 |
| About Us Page | P1 – High | TS_005 | — |
| Contact Page & Form | P0 – Critical | TS_006, TS_007 | 90 |
| Product Categories | P0 – Critical | TS_008 | 79 |
| Product Details Page | P0 – Critical | TS_009 | 89 |
| Home Page Slider | P1 – High | TS_010 | — |
| Next/Previous Navigation | P1 – High | TS_011 | — |
| Shopping Cart | P0 – Critical | TS_012 | 99 |
| Place Order / Checkout | P0 – Critical | TS_013, TS_019 | 114 |
| Order Confirmation | P0 – Critical | TS_014, TS_020 | 99 |
| 404 / Error Page Handling | P1 – High | TS_015 | — |
| Cross-Browser Compatibility | P0 – Critical | TS_016 | 119 |
| Mobile Responsiveness | P0 – Critical | TS_017 | 120 |
| Page Load Performance | P1 – High | TS_018 | — |
| Link Integrity | P1 – High | TS_019 | — |

### Testing Techniques Applied

- **Equivalence Partitioning** — valid/invalid input class testing across all form fields
- **Boundary Value Analysis** — min, max, and edge-boundary testing
- **Decision Table Testing** — input combination coverage for login, signup, checkout
- **State Transition Testing** — session states (login/logout), cart states
- **Negative Testing** — error handling with invalid, empty, and malformed inputs
- **Exploratory Testing** — unscripted, time-boxed sessions for hidden defect discovery
- **Cross-Browser Testing** — Chrome, Firefox, Edge, Safari
- **Responsive Design Testing** — 7 viewport sizes via Chrome DevTools

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

## 📊 Quality Metrics & Targets

| Metric | Target |
|---|---|
| Test Case Pass Rate | ≥ 90% overall; 100% on P0 paths |
| Test Execution Rate | 100% per module |
| Defect Resolution Rate | ≥ 95% before exit criteria met |
| Critical Defect (P0) Open Count | 0 at exit |
| Blocked Test Case Rate | < 5% per module |
| Re-test Pass Rate | ≥ 95% |

---

## 🐛 Defect Management

All defects are tracked via **Jira Cloud** using the following lifecycle:

```
New → Open → In Progress → Fixed → Retest → Closed
                                           ↘ Reopened → (back to In Progress)
                                  Deferred / Rejected / Duplicate
```

### Severity Classification

| Severity | Definition | SLA |
|---|---|---|
| S1 – Critical | App crash, data loss, complete feature failure | Immediate — fix before further testing |
| S2 – Major | Feature partially broken, significant UX degradation | Within current sprint |
| S3 – Minor | Feature partially degraded, low-frequency scenario | Next sprint |
| S4 – Trivial | Cosmetic issue with no functional impact | Maintenance cycle |

---

## 🗺️ Testing Roadmap

### Phase 1 — Manual Testing ✅ Complete

| Phase | Activity | Status |
|---|---|---|
| Phase 0 | Exploratory Testing — Full Application Discovery (3 days) | ✅ Complete |
| Phase 1 | Test Scenario Design — 20 Scenarios (2 days) | ✅ Complete |
| Phase 2 | Test Case Authoring — 12 Modules, 1,000+ TCs (7 days) | ✅ Complete |
| Phase 3 | Test Execution — P0 Modules (4 days) | ✅ Complete |
| Phase 4 | Test Execution — P1 Modules (3 days) | ✅ Complete |
| Phase 5 | Cross-Browser & Mobile Responsive Testing (3 days) | ✅ Complete |
| Phase 6 | Defect Reporting, Re-testing & Closure (2 days) | ✅ Complete |
| Phase 7 | Test Summary Report Generation (1 day) | ✅ Complete |

### Phase 2 — Automation Testing 🔜 Planned

| Phase | Activity | Tools |
|---|---|---|
| 2.1 | Framework Setup — Page Object Model architecture | Selenium / Cypress + Java/JS |
| 2.2 | Smoke Suite — 15–20 critical P0 test cases, < 5 min runtime | TestNG / Mocha |
| 2.3 | Full Regression Suite — 500+ automated TCs, data-driven | POM + Excel/JSON |
| 2.4 | Cross-Browser Automation — parallel execution | Selenium Grid / Playwright |
| 2.5 | CI/CD Integration — trigger on every push/PR | GitHub Actions / Jenkins |
| 2.6 | API Testing — REST endpoint validation independent of UI | Postman / RestAssured |
| 2.7 | Performance Testing — load & stress testing | Apache JMeter / k6 |

---

## 🛠️ Tools Used

| Tool | Category | Purpose |
|---|---|---|
| Microsoft Excel | Test Documentation | Test case authoring & execution tracking |
| Jira Cloud | Defect Tracking | Bug lifecycle management |
| Google Chrome + DevTools | Primary Browser | Test execution & responsive emulation |
| Mozilla Firefox | Cross-Browser | Compatibility testing |
| Microsoft Edge | Cross-Browser | Compatibility testing |
| Apple Safari | Cross-Browser | Compatibility & iOS simulation |
| Snipping Tool / Lightshot | Evidence Capture | Screenshots for defect reports |
| ShareX / Loom | Screen Recording | Video evidence for defect reproduction |
| Git + GitHub | Version Control | Repository for all QA artifacts |

---

## 👤 Author

**MH Lohith**
QA Engineer / Manual Tester

---

## 📄 License

This repository is intended for QA portfolio and internal reference purposes only. All test artifacts are proprietary to this project engagement.
