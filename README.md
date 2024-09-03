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
- **Integration with Vector Databases**: Retrieves relevant portfolio links using vector similarity searches based on job descriptions.

## Installation and Setup

Follow the steps below to clone the repository, set up environment variables, install dependencies, and run the application:

### Step 1: Clone the Repository

Clone the repository from GitHub to your local machine:

```bash
git clone https://github.com/Apiljungthapa/SmartJobMailer.git

```

### Step 2: Install Dependencies
Install the required dependencies using pip:

```bash
pip install -r requirements.txt

```

### Step 3: Run the Streamlit App

Run the Streamlit app with the following command:

```bash
streamlit run app/main.py
```





