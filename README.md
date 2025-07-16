# Detecting the Number of Columns in MySQL using UNION Injection

## Description
Hands-on business security lab for discovering the exact number of columns in a vulnerable MySQL query using both ORDER BY and NULL-based UNION injection techniques in the Acme Research Portal.

## Objectives
- Identify SQL injection via a GET/POST parameter
- Use ORDER BY to find the number of columns
- Use NULL placeholders in UNION SELECT to determine column count
- Understand why column count is critical for UNION-based attacks

## Difficulty
Beginner

## Estimated Time
20-40 minutes

## Prerequisites
- Basic SQL syntax
- Understanding of HTTP requests
- Familiarity with SQL injection fundamentals
- Ability to use a web browser and a proxy tool like Burp Suite or OWASP ZAP

## Skills Learned
- SQL injection enumeration
- MySQL error-based testing
- Payload crafting for UNION SELECT
- Security analysis of web parameters

## Project Structure
- folder: build
- folder: deploy
- folder: test
- folder: docs
- file: README.md
- file: .gitignore

## Quick Start
**Prerequisites:** Docker or a local Python/MySQL stack

**Installation:**
1. Clone the repo.
2. Launch the vulnerable app with `docker-compose -f deploy/docker-compose.yaml up --build`.
3. Access the app at [http://localhost:5000/lab](http://localhost:5000/lab).

## Issue Tracker
For issues, visit: https://github.com/your-organization/ctf-labs/issues 