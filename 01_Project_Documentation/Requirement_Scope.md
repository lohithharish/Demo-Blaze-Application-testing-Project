# 📋 Requirement Scope Document
## DemoBlaze E-Commerce Web Application

---

<div align="center">

| Field | Details |
|---|---|
| **Project Name** | DemoBlaze QA Testing Project |
| **Application** | DemoBlaze Product Store |
| **Application URL** | https://www.demoblaze.com |
| **Document Type** | Requirement Scope |
| **Version** | 1.0 |
| **Prepared By** | MH Lohith |
| **Role** | QA Engineer — Manual Tester |
| **Date** | March 2026 |
| **Testing Phase** | Phase 1 — Manual Testing |
| **Status** | Active |

</div>

---

## 📑 Table of Contents

1. [Introduction](#1-introduction)
2. [Application Overview](#2-application-overview)
3. [Scope of Testing](#3-scope-of-testing)
4. [Functional Requirements](#4-functional-requirements)
   - [FR-01 · User Registration (Sign Up)](#fr-01--user-registration-sign-up)
   - [FR-02 · User Authentication (Login)](#fr-02--user-authentication-login)
   - [FR-03 · User Logout](#fr-03--user-logout)
   - [FR-04 · Home Page](#fr-04--home-page)
   - [FR-05 · About Us](#fr-05--about-us)
   - [FR-06 · Contact Page](#fr-06--contact-page)
   - [FR-07 · Product Categories](#fr-07--product-categories)
   - [FR-08 · Product Details Page](#fr-08--product-details-page)
   - [FR-09 · Home Page Slider](#fr-09--home-page-slider)
   - [FR-10 · Next / Previous Navigation](#fr-10--next--previous-navigation)
   - [FR-11 · Shopping Cart](#fr-11--shopping-cart)
   - [FR-12 · Place Order / Checkout](#fr-12--place-order--checkout)
   - [FR-13 · Order Confirmation](#fr-13--order-confirmation)
5. [Non-Functional Requirements](#5-non-functional-requirements)
   - [NFR-01 · Cross-Browser Compatibility](#nfr-01--cross-browser-compatibility)
   - [NFR-02 · Mobile Responsiveness](#nfr-02--mobile-responsiveness)
   - [NFR-03 · Performance (Observational)](#nfr-03--performance-observational)
   - [NFR-04 · Usability](#nfr-04--usability)
6. [Out of Scope](#6-out-of-scope)
7. [Assumptions and Dependencies](#7-assumptions-and-dependencies)
8. [Requirement Traceability Matrix (RTM)](#8-requirement-traceability-matrix-rtm)
9. [Glossary](#9-glossary)

---

## 1. Introduction

### 1.1 Purpose

This Requirement Scope document defines and consolidates all functional and non-functional requirements identified for the **DemoBlaze e-commerce web application** through thorough exploratory testing, application analysis, and QA investigation.

It serves as the **single source of truth** for:
- What the application is expected to do (functional requirements)
- How the application is expected to perform and behave (non-functional requirements)
- What is explicitly included and excluded from the QA engagement
- The traceability linkage between requirements, test scenarios, and test cases

> **Note:** DemoBlaze does not ship a formal Business Requirements Document (BRD) or Software Requirements Specification (SRS). All requirements documented here have been derived from **exploratory testing sessions**, **observable application behaviour**, **industry-standard e-commerce conventions**, and **user expectation baselines**.

### 1.2 Scope of This Document

This document covers all requirements for the manual testing phase (Phase 1) of the DemoBlaze QA project. Requirements documented here form the basis for:

- Test scenario design (`DemoBlaze_Test_Scenarios.xlsx`)
- Test case authoring across all 12 module-level XLSX files (1,000+ test cases)
- Defect severity classification in Jira
- Go/No-Go quality gate decisions at the end of Phase 1

### 1.3 Requirement Identification Method

Since DemoBlaze has no formal specification, requirements were derived using the following techniques:

| Method | Description |
|---|---|
| **Exploratory Testing** | Unscripted, charter-based sessions across all application modules |
| **Black-Box Observation** | Observing input → processing → output behaviour across all features |
| **E-Commerce Convention Analysis** | Benchmarking against standard e-commerce UX and functional patterns |
| **Negative Testing Probing** | Attempting invalid/empty/boundary inputs to infer validation requirements |
| **Cross-Browser Observation** | Identifying rendering and behaviour differences across browsers |
| **Session Analysis** | Observing localStorage/cookie-based session management behaviour |

---

## 2. Application Overview

### 2.1 Application Summary

DemoBlaze is a publicly accessible, JavaScript-driven **Single-Page Application (SPA)** simulating a real-world e-commerce product store. It is widely used as a QA practice and portfolio-demonstration platform.

| Attribute | Detail |
|---|---|
| **Application Name** | DemoBlaze Product Store |
| **URL** | https://www.demoblaze.com |
| **Application Type** | Single-Page Application (SPA) |
| **Front-End Stack** | HTML5, CSS3, Bootstrap 4, JavaScript (jQuery) |
| **Back-End / API** | REST API — `https://api.demoblaze.com` |
| **Data Persistence** | Server-side (user accounts, cart, orders) |
| **Session Management** | Browser `localStorage` + REST API token-based auth |
| **Payment** | Simulated — no real payment gateway |
| **Product Catalogue** | Phones, Laptops, Monitors |
| **User Roles** | Guest (browse only) · Registered User (full flow) |

### 2.2 Core User Journeys

The following end-to-end journeys represent the primary business flows:

| Journey ID | Description | Modules Involved |
|---|---|---|
| **UJ-01** | New user creates an account | Sign Up |
| **UJ-02** | Registered user authenticates and ends session | Login → Home → Logout |
| **UJ-03** | User browses products by category and views details | Home → Categories → Product Detail |
| **UJ-04** | User adds products to cart and manages cart | Product Detail → Cart |
| **UJ-05** | User completes a full end-to-end purchase | Cart → Place Order → Order Confirmation |
| **UJ-06** | User submits a contact enquiry | Contact Page |
| **UJ-07** | User navigates via home slider and pagination | Home Slider · Next/Prev Navigation |

### 2.3 Application Architecture (QA Perspective)

```
┌─────────────────────────────────────────────────────────────┐
│                     BROWSER (CLIENT)                        │
│                                                             │
│   Navigation Bar → [ Logo | Categories | Login | Signup ]  │
│   Home Page     → [ Carousel Slider | Product Grid ]       │
│   Modals        → [ Login | Signup | Contact | Video ]     │
│   Cart Page     → [ Item List | Total | Place Order ]       │
│   Checkout Form → [ Personal + Payment Details ]           │
│                         │                                   │
│              JavaScript (jQuery/Bootstrap)                  │
└─────────────────────────┬───────────────────────────────────┘
                          │ REST API Calls (AJAX/Fetch)
                          ▼
┌─────────────────────────────────────────────────────────────┐
│              API SERVER — api.demoblaze.com                  │
│                                                             │
│   /signup       /login        /logout                       │
│   /bycat        /entries      /view                         │
│   /addtocart    /viewcart     /deleteitem                   │
│   /placeorder   /check                                      │
└─────────────────────────────────────────────────────────────┘
```

---

## 3. Scope of Testing

### 3.1 In Scope

| # | Module | Type | Priority | Scenario ID |
|---|---|---|---|---|
| 1 | User Registration (Sign Up) | Functional | 🔴 P0 — Critical | TS_001 |
| 2 | User Authentication (Login) | Functional | 🔴 P0 — Critical | TS_002 |
| 3 | User Logout | Functional | 🔴 P0 — Critical | TS_003 |
| 4 | Home Page Load & Display | Functional + UI | 🔴 P0 — Critical | TS_004 |
| 5 | About Us Page | Functional + UI | 🟡 P1 — High | TS_005 |
| 6 | Contact Page & Form | Functional + Form Validation | 🔴 P0 — Critical | TS_006, TS_007 |
| 7 | Product Categories | Functional + Filter | 🔴 P0 — Critical | TS_008 |
| 8 | Product Details Page | Functional + UI | 🔴 P0 — Critical | TS_009 |
| 9 | Home Page Slider | UI + Functional | 🟡 P1 — High | TS_010 |
| 10 | Next / Previous Navigation | Functional + Pagination | 🟡 P1 — High | TS_011 |
| 11 | Shopping Cart | Functional + Calculation | 🔴 P0 — Critical | TS_012 |
| 12 | Place Order / Checkout | Functional + Form Validation | 🔴 P0 — Critical | TS_013, TS_019 |
| 13 | Order Confirmation | Functional + Data Accuracy | 🔴 P0 — Critical | TS_014, TS_020 |
| 14 | Cross-Browser Compatibility | Non-Functional | 🔴 P0 — Critical | TS_016 |
| 15 | Mobile Responsiveness | Non-Functional | 🔴 P0 — Critical | TS_017 |
| 16 | Page Load Performance | Non-Functional (Observational) | 🟡 P1 — High | TS_018 |
| 17 | Link Integrity | Functional | 🟡 P1 — High | TS_019 |
| 18 | 404 / Error Handling | Negative | 🟡 P1 — High | TS_015 |

### 3.2 Out of Scope

| # | Area | Reason |
|---|---|---|
| 1 | Automated Regression Testing | Planned for Phase 2 |
| 2 | API / Backend Testing | Planned for Phase 2 (Postman / RestAssured) |
| 3 | Performance / Load Testing | Planned for Phase 2 (JMeter / k6) |
| 4 | Security / Penetration Testing | Planned for Phase 2 (OWASP ZAP) |
| 5 | Accessibility Testing (WCAG) | Planned for Phase 2 (Axe / Lighthouse) |
| 6 | Database-level Testing | No database access available |
| 7 | Real Payment Gateway Testing | Application uses a simulated checkout — no live payment |
| 8 | Localisation / i18n Testing | Application is English-only |
| 9 | Unit Testing | Source code not accessible (black-box engagement) |
| 10 | Email / Notification Testing | Application does not send confirmation emails |

---

## 4. Functional Requirements

> **Requirement ID Format:** `FR-[Module Number]-[Requirement Number]`
> **Priority Legend:** 🔴 Critical · 🟡 High · 🟢 Medium · ⚪ Low

---

### FR-01 · User Registration (Sign Up)

**Module:** Sign Up Modal  
**Trigger:** User clicks "Sign up" in the navigation bar  
**Scenario Reference:** `TS_001`  
**Test Cases:** `Signup_Test_Cases.xlsx` (~50 TCs)

| Req ID | Requirement Description | Priority | Type |
|---|---|---|---|
| FR-01-01 | The Sign Up option shall be visible and accessible from the navigation bar on all pages | 🔴 Critical | Functional |
| FR-01-02 | Clicking "Sign up" shall open a modal dialog without navigating away from the current page | 🔴 Critical | Functional |
| FR-01-03 | The Sign Up modal shall contain a **Username** input field and a **Password** input field | 🔴 Critical | Functional |
| FR-01-04 | The Sign Up modal shall contain a **Close** button and a **Sign up** submit button | 🟡 High | Functional |
| FR-01-05 | Submitting a valid, unique username and password shall register the user and display a success confirmation alert | 🔴 Critical | Functional |
| FR-01-06 | The system shall prevent registration with a username that already exists in the system — an appropriate error alert must be displayed | 🔴 Critical | Functional |
| FR-01-07 | Submitting the form with an empty **Username** field shall trigger an alert prompting the user to fill in the field | 🔴 Critical | Negative |
| FR-01-08 | Submitting the form with an empty **Password** field shall trigger an alert prompting the user to fill in the field | 🔴 Critical | Negative |
| FR-01-09 | Submitting the form with both fields empty shall trigger a validation alert | 🔴 Critical | Negative |
| FR-01-10 | Username and Password fields shall accept alphanumeric characters and common special characters | 🟡 High | Boundary |
| FR-01-11 | The modal shall be dismissible via the Close button and clicking outside the modal overlay | 🟢 Medium | Functional |
| FR-01-12 | After successful registration, the modal shall close and the user shall remain on the same page (not auto-logged in) | 🟡 High | Functional |
| FR-01-13 | Password field shall mask entered characters (input type="password") | 🟡 High | Security/UI |
| FR-01-14 | Whitespace-only entries in Username or Password fields shall not be accepted as valid input | 🟡 High | Negative |

---

### FR-02 · User Authentication (Login)

**Module:** Login Modal  
**Trigger:** User clicks "Log in" in the navigation bar  
**Scenario Reference:** `TS_002`  
**Test Cases:** `Login_Test_Cases.xlsx` (~63 TCs)

| Req ID | Requirement Description | Priority | Type |
|---|---|---|---|
| FR-02-01 | The "Log in" option shall be visible and accessible from the navigation bar on all pages for unauthenticated users | 🔴 Critical | Functional |
| FR-02-02 | Clicking "Log in" shall open a modal dialog without navigating away from the current page | 🔴 Critical | Functional |
| FR-02-03 | The Login modal shall contain a **Username** field, a **Password** field, a **Close** button, and a **Log in** submit button | 🔴 Critical | Functional |
| FR-02-04 | Submitting valid, registered credentials shall authenticate the user and close the modal | 🔴 Critical | Functional |
| FR-02-05 | Upon successful login, the navigation bar shall update to display the logged-in username and a **Log out** option, replacing the Log in / Sign up links | 🔴 Critical | Functional |
| FR-02-06 | The authenticated user's name shall be displayed in the navigation bar in the format "Welcome, [username]" | 🟡 High | Functional |
| FR-02-07 | Submitting an incorrect password for a valid username shall display an error alert — the user shall not be authenticated | 🔴 Critical | Negative |
| FR-02-08 | Submitting a non-existent username shall display an error alert — the user shall not be authenticated | 🔴 Critical | Negative |
| FR-02-09 | Submitting the form with an empty **Username** field shall trigger a validation alert | 🔴 Critical | Negative |
| FR-02-10 | Submitting the form with an empty **Password** field shall trigger a validation alert | 🔴 Critical | Negative |
| FR-02-11 | Submitting both fields empty shall trigger a validation alert | 🔴 Critical | Negative |
| FR-02-12 | Login credentials shall be case-sensitive | 🟡 High | Functional |
| FR-02-13 | Session state shall persist across page navigation within the same browser tab | 🔴 Critical | Session |
| FR-02-14 | Session shall persist upon browser page refresh | 🟡 High | Session |
| FR-02-15 | The modal shall be dismissible via the Close button and clicking outside the modal overlay | 🟢 Medium | Functional |
| FR-02-16 | Password field shall mask entered characters | 🟡 High | Security/UI |
| FR-02-17 | The "Log in" and "Sign up" navigation links shall be hidden from authenticated users | 🟡 High | Functional |

---

### FR-03 · User Logout

**Module:** Navigation Bar — Logout  
**Trigger:** Authenticated user clicks "Log out" in the navigation bar  
**Scenario Reference:** `TS_003`  
**Test Cases:** `Logout_Test_Cases_Updated.xlsx` (~70 TCs)

| Req ID | Requirement Description | Priority | Type |
|---|---|---|---|
| FR-03-01 | The "Log out" option shall be visible in the navigation bar only for authenticated users | 🔴 Critical | Functional |
| FR-03-02 | Clicking "Log out" shall terminate the user's session immediately | 🔴 Critical | Functional |
| FR-03-03 | Upon logout, the navigation bar shall revert to displaying "Log in" and "Sign up" links, and the username display shall be removed | 🔴 Critical | Functional |
| FR-03-04 | After logout, navigating to the cart page shall not display the previously logged-in user's cart contents | 🟡 High | Session |
| FR-03-05 | After logout, clicking the browser Back button shall not restore the authenticated session | 🔴 Critical | Session |
| FR-03-06 | After logout, attempting to place an order shall not be possible without re-authentication | 🔴 Critical | Session |
| FR-03-07 | Logout shall clear all session data stored in localStorage for the authenticated user | 🔴 Critical | Session |
| FR-03-08 | Logout shall function correctly regardless of which page the user is currently viewing | 🟡 High | Functional |

---

### FR-04 · Home Page

**Module:** Home Page  
**Trigger:** User navigates to `https://www.demoblaze.com` or clicks the DemoBlaze logo  
**Scenario Reference:** `TS_004`  
**Test Cases:** `HomePage_Test_Cases_Updated.xlsx` (~79 TCs)

| Req ID | Requirement Description | Priority | Type |
|---|---|---|---|
| FR-04-01 | The home page shall load successfully and display all primary UI elements without errors | 🔴 Critical | Functional |
| FR-04-02 | The navigation bar shall display: DemoBlaze logo, Home, Contact, About Us, Cart, Log in, Sign up | 🔴 Critical | UI |
| FR-04-03 | The DemoBlaze logo shall be clickable and shall navigate the user to the home page from any page | 🟡 High | Functional |
| FR-04-04 | The home page shall display a **product carousel / image slider** in the hero section | 🟡 High | UI |
| FR-04-05 | The home page shall display a **product grid** listing available products with product name, image, and price | 🔴 Critical | Functional |
| FR-04-06 | Each product in the grid shall be clickable and shall navigate to that product's detail page | 🔴 Critical | Functional |
| FR-04-07 | The home page shall display a **left sidebar** containing product category filters: "Phones", "Laptops", "Monitors" | 🔴 Critical | Functional |
| FR-04-08 | The home page shall display **Next** and **Previous** navigation buttons below the product grid for pagination | 🟡 High | Functional |
| FR-04-09 | The page footer shall be present and display copyright information | 🟢 Medium | UI |
| FR-04-10 | All navigation bar links (Home, Contact, About Us, Cart) shall be functional and navigate to the correct destination | 🔴 Critical | Functional |
| FR-04-11 | The "Cart" icon/link in the navigation shall display a cart icon and navigate to the cart page | 🔴 Critical | Functional |
| FR-04-12 | The home page shall display all in-stock products by default (no category filter applied on initial load) | 🟡 High | Functional |

---

### FR-05 · About Us

**Module:** About Us Modal  
**Trigger:** User clicks "About us" in the navigation bar  
**Scenario Reference:** `TS_005`  
**Test Cases:** Covered in `HomePage_Test_Cases_Updated.xlsx`

| Req ID | Requirement Description | Priority | Type |
|---|---|---|---|
| FR-05-01 | Clicking "About us" shall open a modal containing a promotional video and descriptive content | 🟡 High | Functional |
| FR-05-02 | The video within the About Us modal shall be playable using a visible play control | 🟡 High | Functional |
| FR-05-03 | The video shall pause when the modal is closed — it shall not continue playing in the background | 🟡 High | Functional |
| FR-05-04 | The About Us modal shall be dismissible via the Close button and clicking outside the modal overlay | 🟢 Medium | Functional |
| FR-05-05 | The modal shall open without navigating away from the current page | 🟡 High | Functional |

---

### FR-06 · Contact Page

**Module:** Contact Modal / Form  
**Trigger:** User clicks "Contact" in the navigation bar  
**Scenario Reference:** `TS_006`, `TS_007`  
**Test Cases:** `Contact_Test_Cases_Updated.xlsx` (~90 TCs)

| Req ID | Requirement Description | Priority | Type |
|---|---|---|---|
| FR-06-01 | Clicking "Contact" shall open a Contact modal containing a contact form | 🔴 Critical | Functional |
| FR-06-02 | The Contact form shall contain the following fields: **Contact Email**, **Contact Name**, **Message** | 🔴 Critical | Functional |
| FR-06-03 | The form shall contain a **Send message** submit button and a **Close** button | 🔴 Critical | Functional |
| FR-06-04 | Submitting the form with all fields correctly populated shall trigger a success confirmation alert | 🔴 Critical | Functional |
| FR-06-05 | Submitting the form with the **Contact Email** field empty shall trigger a validation alert | 🔴 Critical | Negative |
| FR-06-06 | Submitting the form with the **Contact Name** field empty shall trigger a validation alert | 🔴 Critical | Negative |
| FR-06-07 | Submitting the form with the **Message** field empty shall trigger a validation alert | 🔴 Critical | Negative |
| FR-06-08 | Submitting the form with all fields empty shall trigger a validation alert | 🔴 Critical | Negative |
| FR-06-09 | The **Contact Email** field shall validate that the entered value is a properly formatted email address | 🟡 High | Validation |
| FR-06-10 | After successful submission, the form shall reset / the modal shall close | 🟡 High | Functional |
| FR-06-11 | The Contact modal shall be dismissible via the Close button and clicking outside the modal | 🟢 Medium | Functional |
| FR-06-12 | The form shall function correctly for both authenticated and unauthenticated users | 🟡 High | Functional |

---

### FR-07 · Product Categories

**Module:** Category Sidebar Filter  
**Trigger:** User clicks a category label ("Phones", "Laptops", or "Monitors") in the sidebar  
**Scenario Reference:** `TS_008`  
**Test Cases:** `ProductCategories_Test_Cases_Updated.xlsx` (~79 TCs)

| Req ID | Requirement Description | Priority | Type |
|---|---|---|---|
| FR-07-01 | The category sidebar shall display three filter options: **Phones**, **Laptops**, **Monitors** | 🔴 Critical | Functional |
| FR-07-02 | Clicking a category label shall filter the product grid to display only products belonging to that category | 🔴 Critical | Functional |
| FR-07-03 | The filtered product grid shall update dynamically without a full page reload | 🔴 Critical | Functional |
| FR-07-04 | Each category shall display at least one product in the filtered grid | 🔴 Critical | Functional |
| FR-07-05 | Products displayed in a filtered category shall not include products from other categories | 🔴 Critical | Functional |
| FR-07-06 | Each product in the filtered grid shall display: product image, product name, and price | 🔴 Critical | UI |
| FR-07-07 | Products displayed in the filtered grid shall be clickable and navigate to the correct product detail page | 🔴 Critical | Functional |
| FR-07-08 | Clicking the active category again shall not cause errors or unexpected behaviour | 🟡 High | Negative |
| FR-07-09 | Switching between categories shall correctly update the product grid each time | 🔴 Critical | Functional |
| FR-07-10 | Category filtering shall function identically for both authenticated and guest users | 🟡 High | Functional |
| FR-07-11 | The sidebar "Categories" heading shall be visually present and legible | 🟢 Medium | UI |

---

### FR-08 · Product Details Page

**Module:** Product Detail Page  
**Trigger:** User clicks on a product from the home page or category-filtered grid  
**Scenario Reference:** `TS_009`  
**Test Cases:** `ProductDetails_Test_Cases_Updated.xlsx` (~89 TCs)

| Req ID | Requirement Description | Priority | Type |
|---|---|---|---|
| FR-08-01 | Clicking a product shall navigate to a dedicated product detail page | 🔴 Critical | Functional |
| FR-08-02 | The product detail page shall display the **product name** | 🔴 Critical | UI |
| FR-08-03 | The product detail page shall display the **product price** in USD format | 🔴 Critical | UI |
| FR-08-04 | The product detail page shall display at least one **product image** | 🔴 Critical | UI |
| FR-08-05 | The product detail page shall display a **product description** | 🟡 High | UI |
| FR-08-06 | The product detail page shall contain an **"Add to cart"** button | 🔴 Critical | Functional |
| FR-08-07 | Clicking **"Add to cart"** shall add the product to the user's cart and display a confirmation alert | 🔴 Critical | Functional |
| FR-08-08 | The "Add to cart" function shall work correctly for both authenticated and guest users | 🔴 Critical | Functional |
| FR-08-09 | Clicking "Add to cart" multiple times for the same product shall add duplicate entries to the cart | 🟡 High | Functional |
| FR-08-10 | The page shall provide a navigational path back to the home page (via logo, browser back, or breadcrumb) | 🟡 High | Functional |
| FR-08-11 | The product detail page URL shall be unique per product and directly accessible | 🟡 High | Functional |
| FR-08-12 | The product name and price on the detail page shall match the values displayed on the home page / category listing | 🔴 Critical | Data Integrity |

---

### FR-09 · Home Page Slider

**Module:** Hero Image Carousel / Slider  
**Location:** Top of home page  
**Scenario Reference:** `TS_010`  
**Test Cases:** Covered in `HomePage_Test_Cases_Updated.xlsx`

| Req ID | Requirement Description | Priority | Type |
|---|---|---|---|
| FR-09-01 | The home page shall display an image carousel/slider in the hero section | 🟡 High | UI |
| FR-09-02 | The slider shall contain multiple slides (minimum 3 slides) | 🟡 High | UI |
| FR-09-03 | The slider shall auto-advance through slides at a defined interval without user interaction | 🟡 High | Functional |
| FR-09-04 | The slider shall display **Previous** (left arrow) and **Next** (right arrow) manual navigation controls | 🟡 High | Functional |
| FR-09-05 | Clicking the Next arrow shall advance the slider to the next slide | 🟡 High | Functional |
| FR-09-06 | Clicking the Previous arrow shall navigate the slider to the previous slide | 🟡 High | Functional |
| FR-09-07 | The slider shall display slide indicator dots corresponding to the number of slides | 🟢 Medium | UI |
| FR-09-08 | Clicking on an indicator dot shall navigate directly to the corresponding slide | 🟢 Medium | Functional |
| FR-09-09 | The slider shall loop continuously — clicking Next on the last slide shall return to the first slide | 🟢 Medium | Functional |
| FR-09-10 | Slider images shall be fully visible and not cropped or distorted on desktop viewport | 🟡 High | UI |

---

### FR-10 · Next / Previous Navigation

**Module:** Product Grid Pagination  
**Location:** Below the product grid on the home page  
**Scenario Reference:** `TS_011`  
**Test Cases:** Covered in `HomePage_Test_Cases_Updated.xlsx`

| Req ID | Requirement Description | Priority | Type |
|---|---|---|---|
| FR-10-01 | The home page product grid shall display **Next** and **Previous** navigation buttons below the product listing | 🟡 High | Functional |
| FR-10-02 | Clicking **Next** shall load and display the next set of products in the grid | 🟡 High | Functional |
| FR-10-03 | Clicking **Previous** shall load and display the previous set of products in the grid | 🟡 High | Functional |
| FR-10-04 | When on the first page, the **Previous** button shall be disabled or shall not navigate to a previous (non-existent) page | 🟡 High | Negative |
| FR-10-05 | When on the last page, the **Next** button shall be disabled or shall not navigate to a next (non-existent) page | 🟡 High | Negative |
| FR-10-06 | Navigating via Next/Previous shall not disrupt the currently applied category filter | 🟢 Medium | Functional |
| FR-10-07 | The product grid shall update dynamically without a full page reload on Next/Previous navigation | 🟡 High | Functional |

---

### FR-11 · Shopping Cart

**Module:** Cart Page  
**Trigger:** User clicks "Cart" in the navigation bar  
**Scenario Reference:** `TS_012`  
**Test Cases:** `Cart_Test_Cases_Updated.xlsx` (~99 TCs)

| Req ID | Requirement Description | Priority | Type |
|---|---|---|---|
| FR-11-01 | The Cart page shall be accessible via the "Cart" link in the navigation bar from any page | 🔴 Critical | Functional |
| FR-11-02 | The Cart page shall display all products that the user has added, with each entry showing: **product name** and **price** | 🔴 Critical | Functional |
| FR-11-03 | The Cart page shall display a **Total** figure representing the sum of all item prices in the cart | 🔴 Critical | Functional |
| FR-11-04 | The cart total shall be arithmetically correct — it shall equal the exact sum of all item prices displayed | 🔴 Critical | Calculation |
| FR-11-05 | Each cart item row shall display a **Delete** button that removes that specific item from the cart | 🔴 Critical | Functional |
| FR-11-06 | Clicking **Delete** on an item shall remove only that item from the cart and update the total accordingly | 🔴 Critical | Functional |
| FR-11-07 | After deleting an item, the cart total shall update immediately to reflect the removal | 🔴 Critical | Calculation |
| FR-11-08 | An empty cart shall display no items and show a total of $0 | 🟡 High | Functional |
| FR-11-09 | The Cart page shall display a **Place Order** button | 🔴 Critical | Functional |
| FR-11-10 | The cart shall persist item additions across page navigation within the same session | 🔴 Critical | Session |
| FR-11-11 | Adding the same product multiple times from the product detail page shall create multiple line entries in the cart | 🟡 High | Functional |
| FR-11-12 | Cart items added during a guest session shall be accessible after login within the same browser session | 🟢 Medium | Session |
| FR-11-13 | The cart shall display correctly regardless of the number of items added (1 item to many items) | 🟡 High | Boundary |

---

### FR-12 · Place Order / Checkout

**Module:** Place Order Modal (Checkout Form)  
**Trigger:** User clicks "Place Order" from the Cart page  
**Scenario Reference:** `TS_013`, `TS_019`  
**Test Cases:** `PlaceOrder_Test_Cases_Updated.xlsx` (~114 TCs)

| Req ID | Requirement Description | Priority | Type |
|---|---|---|---|
| FR-12-01 | Clicking "Place Order" on the Cart page shall open a checkout modal with a purchase form | 🔴 Critical | Functional |
| FR-12-02 | The checkout form shall contain the following fields: **Name**, **Country**, **City**, **Credit Card**, **Month**, **Year** | 🔴 Critical | Functional |
| FR-12-03 | The checkout form shall display a **Purchase** submit button and a **Close** button | 🔴 Critical | Functional |
| FR-12-04 | The checkout modal shall display a **Total** field showing the cart total amount | 🔴 Critical | Functional |
| FR-12-05 | Submitting the form with all required fields correctly populated shall successfully place the order | 🔴 Critical | Functional |
| FR-12-06 | Submitting the form with the **Name** field empty shall trigger a validation alert | 🔴 Critical | Negative |
| FR-12-07 | Submitting the form with the **Credit Card** field empty shall trigger a validation alert | 🔴 Critical | Negative |
| FR-12-08 | Submitting the form with all fields empty shall trigger a validation alert | 🔴 Critical | Negative |
| FR-12-09 | The **Month** and **Year** fields shall accept plausible date inputs (month 1–12, valid year) | 🟡 High | Validation |
| FR-12-10 | The total displayed in the checkout modal shall match the total displayed on the Cart page | 🔴 Critical | Data Integrity |
| FR-12-11 | The checkout form shall be functional for authenticated users | 🔴 Critical | Functional |
| FR-12-12 | The checkout modal shall be dismissible via the Close button without placing an order | 🟡 High | Functional |
| FR-12-13 | Special characters in name/city/country fields shall not crash the form or produce a server error | 🟡 High | Negative |
| FR-12-14 | Extremely long strings in text fields shall be handled gracefully without crashing the application | 🟡 High | Boundary |

---

### FR-13 · Order Confirmation

**Module:** Order Confirmation Modal  
**Trigger:** User successfully submits the checkout form  
**Scenario Reference:** `TS_014`, `TS_020`  
**Test Cases:** `OrderConfirmation_Test_Cases_Updated.xlsx` (~99 TCs)

| Req ID | Requirement Description | Priority | Type |
|---|---|---|---|
| FR-13-01 | Upon successful order placement, a confirmation modal shall be displayed to the user | 🔴 Critical | Functional |
| FR-13-02 | The confirmation modal shall display a success message (e.g., "Thank you for your purchase!") | 🔴 Critical | Functional |
| FR-13-03 | The confirmation modal shall display a unique **Order ID** for the completed transaction | 🔴 Critical | Functional |
| FR-13-04 | The confirmation modal shall display the **purchaser's name** as entered in the checkout form | 🔴 Critical | Data Integrity |
| FR-13-05 | The confirmation modal shall display the **order amount / total** matching the cart total | 🔴 Critical | Data Integrity |
| FR-13-06 | The confirmation modal shall display the **credit card number** used (may be masked) | 🟡 High | Data Integrity |
| FR-13-07 | The confirmation modal shall display the **date** of the transaction | 🟡 High | Functional |
| FR-13-08 | The confirmation modal shall contain an **OK** button that closes the modal | 🔴 Critical | Functional |
| FR-13-09 | Clicking **OK** on the confirmation modal shall clear the cart | 🔴 Critical | Functional |
| FR-13-10 | Clicking **OK** shall redirect the user to the home page | 🟡 High | Functional |
| FR-13-11 | The Order ID displayed shall be unique per transaction | 🟡 High | Data Integrity |

---

## 5. Non-Functional Requirements

---

### NFR-01 · Cross-Browser Compatibility

**Scenario Reference:** `TS_016`  
**Test Cases:** `CrossBrowser_Test_Cases_Updated.xlsx` (~119 TCs)

| Req ID | Requirement Description | Priority | Browsers |
|---|---|---|---|
| NFR-01-01 | All functional features shall operate correctly on **Google Chrome** (latest stable) | 🔴 Critical | Chrome |
| NFR-01-02 | All functional features shall operate correctly on **Mozilla Firefox** (latest stable) | 🔴 Critical | Firefox |
| NFR-01-03 | All functional features shall operate correctly on **Microsoft Edge** (latest stable) | 🔴 Critical | Edge |
| NFR-01-04 | All functional features shall operate correctly on **Apple Safari** (latest stable) | 🔴 Critical | Safari |
| NFR-01-05 | The UI layout and styling shall be visually consistent across all supported browsers with no major rendering differences | 🔴 Critical | All |
| NFR-01-06 | Modal dialogs (Login, Signup, Contact, Checkout, Confirmation) shall open, function, and close correctly on all browsers | 🔴 Critical | All |
| NFR-01-07 | JavaScript-driven interactions (category filter, cart updates, slider) shall function on all supported browsers | 🔴 Critical | All |
| NFR-01-08 | Font rendering, button styling, and spacing shall not differ significantly across browsers | 🟡 High | All |
| NFR-01-09 | The application shall not throw unhandled JavaScript console errors during normal use on any supported browser | 🟡 High | All |

---

### NFR-02 · Mobile Responsiveness

**Scenario Reference:** `TS_017`  
**Test Cases:** `MobileResponsive_Test_Cases_Updated.xlsx` (~120 TCs)

| Req ID | Requirement Description | Priority | Viewport |
|---|---|---|---|
| NFR-02-01 | The application layout shall be fully usable and readable at **1920×1080** (Full HD Desktop) | 🔴 Critical | Desktop |
| NFR-02-02 | The application layout shall be fully usable and readable at **1366×768** (Standard Desktop) | 🔴 Critical | Desktop |
| NFR-02-03 | The application layout shall adapt correctly at **1024×768** (Tablet Landscape) — no horizontal scrolling | 🔴 Critical | Tablet |
| NFR-02-04 | The application layout shall adapt correctly at **768×1024** (Tablet Portrait) | 🔴 Critical | Tablet |
| NFR-02-05 | The application shall be fully usable at **393×852** (iPhone 14 Pro — Mobile Large) | 🔴 Critical | Mobile |
| NFR-02-06 | The application shall be fully usable at **375×667** (iPhone SE — Mobile Small) | 🔴 Critical | Mobile |
| NFR-02-07 | The application shall be fully usable at **360×800** (Android Standard Mobile) | 🔴 Critical | Mobile |
| NFR-02-08 | The navigation bar shall collapse to a hamburger menu or equivalent on mobile viewports | 🔴 Critical | Mobile |
| NFR-02-09 | All product images shall scale proportionally and not overflow their containers on any viewport | 🟡 High | All |
| NFR-02-10 | All buttons and interactive elements shall have sufficient tap target size (minimum 44×44px) on mobile | 🟡 High | Mobile |
| NFR-02-11 | Modal dialogs shall display correctly and remain scrollable on mobile viewports | 🔴 Critical | Mobile |
| NFR-02-12 | Text content shall not overflow or be truncated on mobile viewports without scrolling | 🟡 High | Mobile |
| NFR-02-13 | The product grid shall reflow to an appropriate number of columns on smaller viewports | 🟡 High | Tablet/Mobile |
| NFR-02-14 | The image slider shall be visible and functional on all viewport sizes | 🟡 High | All |

---

### NFR-03 · Performance (Observational)

**Scenario Reference:** `TS_018`

| Req ID | Requirement Description | Priority | Type |
|---|---|---|---|
| NFR-03-01 | The home page shall visually load and display product content within an acceptable timeframe (< 5 seconds on standard broadband) | 🟡 High | Performance |
| NFR-03-02 | Category filter operations shall produce a visible result within 3 seconds of clicking | 🟡 High | Performance |
| NFR-03-03 | The application shall not display a blank white screen for more than 2 seconds during any navigation event | 🟡 High | Performance |
| NFR-03-04 | Modal dialogs shall open with no perceptible delay (< 500ms) after user interaction | 🟢 Medium | Performance |
| NFR-03-05 | Product images shall load progressively — the page shall be usable before all images have fully rendered | 🟢 Medium | Performance |

> **Note:** Performance requirements at this phase are observational — no automated performance testing tools (JMeter, k6) are used in Phase 1. Violations are logged as defects if observed during manual execution.

---

### NFR-04 · Usability

| Req ID | Requirement Description | Priority | Type |
|---|---|---|---|
| NFR-04-01 | All interactive elements (buttons, links, form fields) shall provide clear visual feedback on hover and focus | 🟡 High | Usability |
| NFR-04-02 | Error messages and validation alerts shall be clearly worded and specific enough for the user to understand the corrective action | 🔴 Critical | Usability |
| NFR-04-03 | The navigation structure shall be consistent and predictable across all pages | 🔴 Critical | Usability |
| NFR-04-04 | Product pricing shall be displayed consistently in USD format throughout the application | 🟡 High | Usability |
| NFR-04-05 | Confirmation dialogs (after order placement, successful sign-up) shall clearly communicate the outcome to the user | 🔴 Critical | Usability |
| NFR-04-06 | The application shall not leave the user in a broken or dead-end state after any standard user action | 🔴 Critical | Usability |

---

## 6. Out of Scope

The following requirements and areas are **explicitly excluded** from Phase 1 of this QA engagement:

| # | Excluded Area | Justification | Future Phase |
|---|---|---|---|
| 1 | **Automated Regression Testing** | Manual-only phase | Phase 2 |
| 2 | **REST API / Backend Endpoint Testing** | No API test tooling in Phase 1 | Phase 2 (Postman / RestAssured) |
| 3 | **Performance / Load Testing** | Requires dedicated tooling | Phase 2 (JMeter / k6) |
| 4 | **Security Testing** | Requires security tooling and expertise | Phase 2 (OWASP ZAP) |
| 5 | **Accessibility Testing (WCAG 2.1)** | Requires specialised tooling | Phase 2 (Axe / Lighthouse) |
| 6 | **Database / Server-Side Validation** | No database access | Phase 2 |
| 7 | **Email / Notification Delivery** | Application does not send emails | N/A |
| 8 | **Real Payment Processing** | Simulated checkout only | N/A |
| 9 | **Unit Testing** | Source code not accessible | N/A |
| 10 | **Localisation / Internationalisation** | English-only application | N/A |
| 11 | **Third-Party Integrations** | No integrations present | N/A |

---

## 7. Assumptions and Dependencies

### 7.1 Assumptions

| # | Assumption |
|---|---|
| A-01 | The DemoBlaze application at `https://www.demoblaze.com` remains accessible and functionally stable throughout the testing period |
| A-02 | All requirements have been derived from exploratory testing and observable behaviour — no formal BRD or SRS is available |
| A-03 | The application behaviour observed during exploratory testing represents the intended design |
| A-04 | User accounts created via the Signup flow will persist for the duration of the test cycle |
| A-05 | Product catalogue contents (names, prices, categories) will not change significantly during test execution |
| A-06 | Cart and order data persisted to the server during testing may be visible to other testers using the same accounts |
| A-07 | Browser DevTools device emulation is an acceptable substitute for physical device testing in Phase 1 |
| A-08 | The "latest stable" version of each browser is used — specific version numbers may vary by test machine |
| A-09 | All testing is conducted in English locale — no localisation testing is assumed |
| A-10 | Internet connectivity is stable and consistent during all test execution sessions |

### 7.2 Dependencies

| # | Dependency | Type | Owner |
|---|---|---|---|
| D-01 | Application must be accessible at `https://www.demoblaze.com` | Technical | DemoBlaze Infrastructure |
| D-02 | Jira project board must be configured before defect logging commences | Process | QA Engineer |
| D-03 | Test user accounts must be created via Signup before login-dependent test cases can execute | Data | QA Engineer |
| D-04 | Chrome, Firefox, Edge, and Safari must be installed and updated to latest stable versions | Environment | QA Engineer |
| D-05 | Chrome DevTools must be available for mobile/responsive viewport simulation | Environment | QA Engineer |
| D-06 | All 12 module-level XLSX test case files must be authored before execution begins | Documentation | QA Engineer |

---

## 8. Requirement Traceability Matrix (RTM)

> The RTM maps each requirement to its associated test scenario, test case file, and Jira defect tracking.

| Req ID | Requirement Summary | Test Scenario | Test Case File | Jira Label | Status |
|---|---|---|---|---|---|
| FR-01-01 to FR-01-14 | User Registration (Sign Up) | TS_001 | `Signup_Test_Cases.xlsx` | `SIGNUP` | ✅ TC Authored |
| FR-02-01 to FR-02-17 | User Authentication (Login) | TS_002 | `Login_Test_Cases.xlsx` | `LOGIN` | ✅ TC Authored |
| FR-03-01 to FR-03-08 | User Logout | TS_003 | `Logout_Test_Cases_Updated.xlsx` | `LOGOUT` | ✅ TC Authored |
| FR-04-01 to FR-04-12 | Home Page Display | TS_004, TS_005 | `HomePage_Test_Cases_Updated.xlsx` | `HOMEPAGE` | ✅ TC Authored |
| FR-05-01 to FR-05-05 | About Us Modal | TS_005 | `HomePage_Test_Cases_Updated.xlsx` | `ABOUTUS` | ✅ TC Authored |
| FR-06-01 to FR-06-12 | Contact Page & Form | TS_006, TS_007 | `Contact_Test_Cases_Updated.xlsx` | `CONTACT` | ✅ TC Authored |
| FR-07-01 to FR-07-11 | Product Categories | TS_008 | `ProductCategories_Test_Cases_Updated.xlsx` | `CATEGORIES` | ✅ TC Authored |
| FR-08-01 to FR-08-12 | Product Details Page | TS_009 | `ProductDetails_Test_Cases_Updated.xlsx` | `PRODUCTS` | ✅ TC Authored |
| FR-09-01 to FR-09-10 | Home Page Slider | TS_010 | `HomePage_Test_Cases_Updated.xlsx` | `SLIDER` | ✅ TC Authored |
| FR-10-01 to FR-10-07 | Next / Previous Navigation | TS_011 | `HomePage_Test_Cases_Updated.xlsx` | `NAVIGATION` | ✅ TC Authored |
| FR-11-01 to FR-11-13 | Shopping Cart | TS_012 | `Cart_Test_Cases_Updated.xlsx` | `CART` | ✅ TC Authored |
| FR-12-01 to FR-12-14 | Place Order / Checkout | TS_013, TS_019 | `PlaceOrder_Test_Cases_Updated.xlsx` | `ORDER` | ✅ TC Authored |
| FR-13-01 to FR-13-11 | Order Confirmation | TS_014, TS_020 | `OrderConfirmation_Test_Cases_Updated.xlsx` | `CONFIRMATION` | ✅ TC Authored |
| NFR-01-01 to NFR-01-09 | Cross-Browser Compatibility | TS_016 | `CrossBrowser_Test_Cases_Updated.xlsx` | `CROSSBROWSER` | ✅ TC Authored |
| NFR-02-01 to NFR-02-14 | Mobile Responsiveness | TS_017 | `MobileResponsive_Test_Cases_Updated.xlsx` | `MOBILE` | ✅ TC Authored |
| NFR-03-01 to NFR-03-05 | Performance (Observational) | TS_018 | All module files | `PERFORMANCE` | 🔄 Embedded |
| NFR-04-01 to NFR-04-06 | Usability | All scenarios | All module files | `USABILITY` | 🔄 Embedded |

### RTM Summary

| Metric | Count |
|---|---|
| Total Functional Requirements | **107** |
| Total Non-Functional Requirements | **38** |
| **Total Requirements** | **145** |
| Requirements with Test Cases Authored | **145 / 145** |
| Requirements with Test Cases Executed | Pending execution |
| Requirements with Open Defects | Pending execution |
| Requirements Coverage (%) | **100%** |

---

## 9. Glossary

| Term | Definition |
|---|---|
| **AUT** | Application Under Test — DemoBlaze (`https://www.demoblaze.com`) |
| **BRD** | Business Requirements Document — formal document specifying business needs (not available for DemoBlaze) |
| **BVA** | Boundary Value Analysis — test design technique focusing on values at input boundaries |
| **EP** | Equivalence Partitioning — dividing inputs into valid/invalid classes for efficient testing |
| **FR** | Functional Requirement — defines what the system shall do |
| **NFR** | Non-Functional Requirement — defines how the system shall perform or behave |
| **P0** | Priority 0 — Critical; must be resolved before release |
| **P1** | Priority 1 — High; should be resolved before release |
| **P2** | Priority 2 — Medium; should be resolved in the next cycle |
| **P3** | Priority 3 — Low; cosmetic or low-impact; deferred |
| **RTM** | Requirement Traceability Matrix — maps requirements to test cases and defects |
| **SPA** | Single-Page Application — web app that loads a single HTML page and updates dynamically via JavaScript |
| **SRS** | Software Requirements Specification — formal document detailing software requirements (not available for DemoBlaze) |
| **TC** | Test Case — a set of conditions and steps used to verify a specific requirement |
| **TS** | Test Scenario — a high-level description of a testable business condition |
| **UAT** | User Acceptance Testing — testing performed to verify the system meets business needs |

---

<div align="center">

---

**DemoBlaze QA Testing Project**  
*Requirement Scope v1.0 — Prepared by MH Lohith — March 2026*  
*Phase 1: Manual Testing | Phase 2: Automation (Upcoming)*

---

</div>
