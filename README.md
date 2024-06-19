# NVDI Image Processing

[NVDI Image Processing](https://en.wikipedia.org/wiki/Normalized_difference_vegetation_index)

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Introduction

NVDI (Normalized Difference Vegetation Index) Image Processing is a Django-based project designed for processing satellite images, specifically focusing on band 4 and band 5. This project aims to analyze vegetation by calculating the NVDI from these bands.

## Features

- Process satellite images for NVDI calculation.
- Support for band 4 and band 5 image inputs.
- Django-based web interface for uploading and processing images.
- Visualization of NVDI results.

## Installation

### Prerequisites

- Python 3.x
- Django 3.x or higher
- pip (Python package installer)

### Steps

1. **Clone the repository:**

    ```sh
    git clone https://github.com/string-TIRTH/NVDI-image-processing.git
    cd NVDI-image-processing
    ```

2. **Create and activate a virtual environment:**

    ```sh
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. **Apply the migrations:**

    ```sh
    python manage.py migrate
    ```

4. **Start the development server:**

    ```sh
    python manage.py runserver
    ```

5. **Access the application:**

    Open your web browser and navigate to `http://127.0.0.1:8000`.

## Usage

1. **Upload Images:**

    - Navigate to the upload section.
    - Upload band 4 and band 5 images.

2. **Process Images:**
- **manage.py**: Django command-line utility.
- **nvdi_app/**: Main application directory.
  - **migrations/**: Database migrations.
  - **static/**: Static files (CSS, JavaScript, images).
  - **templates/**: HTML templates.
  - **admin.py**: Django admin configurations.
  - **apps.py**: Application configuration.
  - **models.py**: Database models.
  - **tests.py**: Unit tests.
  - **urls.py**: URL routing.
  - **views.py**: Application views.

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.

## Contact

- **Name**: Tirth
- **GitHub**: [string-TIRTH](https://github.com/string-TIRTH)
- **Email**: tirthprajapati26@gmail.com

Feel free to reach out if you have any questions or suggestions!


    - Click on the "Process" button to calculate the NVDI.
    - View the results and NVDI visualization.

## Project Structure

