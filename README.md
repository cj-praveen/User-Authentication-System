# User Authentication System

## Table of Contents
- Introduction
- Features
- Installation
- Usage
- License

## Introduction
This project is a User Authentication System built with Flask. It provides a secure way for users to sign up and sign in using OTP (One-Time Password) authentication.

## Features
- User sign up with username and password.
- User sign in with username and password.
- OTP generation for secure sign in.
- QR code generation for OTP.

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/cj-praveen/user-authentication-system.git
    ```
2. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Generate the CSS file with Tailwind CSS:
    ```bash
    npx tailwindcss -i assets/css/tw.css -o assets/css/style.css
    ```
4. Run the application:
    ```bash
    python main.py
    ```

## Usage
- To sign up, go to `/sign-up` and enter your username and password.
- To sign in, go to `/sign-in` and enter your username and password. You will be prompted to enter the OTP.

## License
This project is licensed under the terms of the Creative Commons license. See the LICENSE file for details.
