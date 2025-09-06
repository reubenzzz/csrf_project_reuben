# CSRF Middleware and Protections: Research, Crawler & PoC

## Overview

This repository contains research and practical implementations related to **Cross-Site Request Forgery (CSRF)** attacks and protections. The project includes:

- A detailed explanation of CSRF and how middleware protects against it.
- A **crawler** that scans web applications for missing CSRF tokens in forms or headers.
- A **Proof of Concept (PoC)** HTML page demonstrating a CSRF vulnerability exploiting an example vulnerable web page.

---

## Project Structure

- `crawler.py`  
  Python script that crawls target web applications to detect forms lacking CSRF tokens.

- `vulnerable.html`  
  An example vulnerable page simulating a CSRF weakness (e.g., profile update without token validation).

- `csrf_poc.html`  
  A CSRF Proof of Concept page that automatically triggers an unauthorized action on the vulnerable page.

- `README.md`  
  This documentation file.

---

## How to Use

### 1. Research and Understand CSRF

- Review the concepts of CSRF attacks and protections in web applications.
- Learn how CSRF tokens are used in middleware to validate legitimate requests.

### 2. Run the Crawler

- Make sure Python 3 is installed.
- Install required packages (e.g., `requests`, `beautifulsoup4`):

How it works:

  When the victim visits the PoC page, the form submits a GET request to the vulnerable page with ?name=HackedName123.

The vulnerable page reads this and updates the name without any CSRF protection.

No user click needed; the attack happens automatically.

## What to do next?

Save the vulnerable page as vulnerable.html.

Save the CSRF PoC as csrf_poc.html.

Open vulnerable.html in browser to see original name.

Open csrf_poc.html — the name on the vulnerable page changes automatical

  ```bash
  pip install -r requirements.txt
