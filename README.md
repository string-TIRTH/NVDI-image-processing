# NVDI Image Processing

![NVDI Image Processing](url_to_your_banner_image)

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

3. **Install the dependencies:**

    ```sh
    pip install -r requirements.txt
    ```

4. **Apply the migrations:**

    ```sh
    python manage.py migrate
    ```

5. **Start the development server:**

    ```sh
    python manage.py runserver
    ```

6. **Access the application:**

    Open your web browser and navigate to `http://127.0.0.1:8000`.

## Usage

1. **Upload Images:**

    - Navigate to the upload section.
    - Upload band 4 and band 5 images.

2. **Process Images:**

    - Click on the "Process" button to calculate the NVDI.
    - View the results and NVDI visualization.

## Project Structure

