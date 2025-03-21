📚 Research Paper Fetcher
📌 Project Overview
This project is a Python-based CLI tool that fetches research papers from the PubMed database using the NCBI API. It helps researchers, students, and professionals filter out papers authored by non-academic researchers affiliated with pharmaceutical or biotech companies.

The tool takes a search query (such as "cancer research") and performs the following actions:
✅ Fetches relevant research papers from PubMed
✅ Extracts author details, including affiliations
✅ Identifies authors working in pharma or biotech companies
✅ Saves the filtered results to a CSV file

🎯 Key Features
🔹 PubMed API Integration – Fetches research papers programmatically
🔹 Non-Academic Author Filtering – Identifies authors in industry (pharmaceutical/biotech)
🔹 CSV Export – Saves structured data for further analysis
🔹 Command-Line Interface (CLI) – Allows easy execution with custom search terms
🔹 Modular Code Structure – Clean and reusable Python functions

🛠️ Technology Stack
Python 3.8+ (Main programming language)
Poetry (Dependency and project management)
Requests (For making API calls to PubMed)
Pandas (For processing and exporting data)
Argparse (For command-line interface functionality)