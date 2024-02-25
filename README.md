# User Authentication System

## Table of Contents
- Introduction
- Features
- Prerequisites
- Installation
- Usage
- License

## Introduction
This project is a User Authentication System built with Flask. It provides a secure way for users to sign up and sign in using OTP (One-Time Password) authentication. The system uses bcrypt for password hashing, enhancing the security of user data.

## Features
- User sign up with username and password.
- Passwords are securely hashed using bcrypt.
- User sign in with username and hashed password.
- OTP generation for secure sign in.
- QR code generation for OTP.

## Prerequisites
- Python 3.9 or higher

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/cj-praveen/user-authentication-system.git
    ```
2. Install the Python dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Run the application:
    ```bash
    python main.py
    ```

## Usage
- To sign up, go to `/sign-up` and enter your username and password. The password will be hashed using bcrypt before being stored.
- To sign in, go to `/sign-in` and enter your username and password. The entered password will be hashed and compared with the stored hashed password. You will be prompted to enter the OTP.

## License
This project is licensed under the terms of the Creative Commons. See the LICENSE file for details.
