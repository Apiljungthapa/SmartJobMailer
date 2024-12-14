# 📧 Cold Mail Generator

The **Cold Mail Generator** is a tool designed for service companies to generate personalized cold emails to potential clients based on job listings extracted from their careers page. This app uses `Groq`, `LangChain`, and `Streamlit` to automate the process of crafting effective cold emails by leveraging job descriptions and matching them with relevant portfolio links.

## Overview

Imagine a scenario where a company is looking to hire for a specific role. Instead of letting the company go through a lengthy hiring process, your business development team can reach out to them with a personalized cold email, proposing your company's services to fill the required role more efficiently. This tool helps generate such emails dynamically by analyzing job listings and highlighting relevant expertise and portfolio projects.

## Architecture Diagram

The architecture of this tool is illustrated below:

![Architecture Diagram](imgs/architecture.png)

## Features

- **Web Scraping**: Extracts job listings from the careers page of any company.
- **AI-Powered Analysis**: Uses Groq's API and LangChain to analyze job descriptions.
- **Cold Email Generation**: Automatically generates personalized cold emails based on job descriptions and matches them with relevant portfolio links.
- **Integration with Vector Databases**: Retrieves relevant portfolio links using vector similarity searches based on job description.

## Installation and Setup

Follow the steps below to clone the repository, set up environment variables, install dependencies, and run the application:

### Step 1: Clone the Repository

Clone the repository from GitHub to your local machine:

```bash
git clone https://github.com/Apiljungthapa/SmartJobMailer.git

```

### Step 2: Set Up Environment Variables

1. Create an .env file in the app directory.

2. Obtain an API_KEY from Groq by visiting Groq Console. https://console.groq.com/keys.

3. Add the API_KEY to your .env file:

```bash
GROQ_API_KEY=your_api_key_here


```


### Step 3: Install Dependencies
Install the required dependencies using pip:

```bash
pip install -r requirements.txt

```

### Step 4: Run the Streamlit App

Run the Streamlit app with the following command:

```bash
streamlit run app/main.py
```

### License

This software is licensed under the Apil License. You are free to use, modify, and distribute this software for personal, educational, or non-commercial purposes. Commercial use of this software is strictly prohibited without prior written permission from the author.

For more details, please see the [LICENSE](https://github.com/Apiljungthapa/SmartJobMailer/blob/main/LICENSE) file.


### Contributors

We would like to thank the following contributors for their invaluable contributions to this project:

Apil Thapa - https://github.com/Apiljungthapa/


Feel free to reach out to any of us for more information or collaboration!

### How to Use This README

- **Copy the Markdown code** above into a `README.md` file in the root directory of your project.
- **Ensure all image paths** and references are correctly pointing to your `imgs` folder (e.g., `imgs/architecture.png`).
- **Push the updated README** to your GitHub repository to make it accessible to anyone cloning your repository.

This README provides comprehensive setup instructions and properly credits contributors, making it professional and informative.






