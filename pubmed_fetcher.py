import csv
import re

def is_non_academic(email, affiliation):
    """
    Determine if an author is non-academic based on email domain and affiliation.
    """
    academic_keywords = ["university", "institute", "college", "school", "laboratory", "research center"]
    non_academic_keywords = ["pharma", "biotech", "corporation", "inc", "ltd"]

    # Check email domain
    academic_email_domains = [r"\.edu$", r"\.ac\.", r"\.gov$"]
    if email and any(re.search(pattern, email) for pattern in academic_email_domains):
        return False  # Academic author

    # Check affiliation name
    if affiliation:
        affiliation_lower = affiliation.lower()
        if any(word in affiliation_lower for word in academic_keywords):
            return False  # Academic author
        if any(word in affiliation_lower for word in non_academic_keywords):
            return True  # Non-academic author

    return False  # Default to academic if uncertain

def fetch_pubmed_papers(query, debug=False):
    """
    Fetch research papers from PubMed and identify non-academic authors.
    """
    if debug:
        print(f"Fetching papers for query: {query}")

    # TODO: Implement actual API call to PubMed
    results = [
        {
            "PubmedID": "123456",
            "Title": "Sample Research Paper",
            "Publication Date": "2025-03-16",
            "Authors": [
                {"Name": "John Doe", "Email": "john.doe@abcpharma.com", "Affiliation": "ABC Pharma"},
                {"Name": "Alice Smith", "Email": "alice.smith@university.edu", "Affiliation": "XYZ University"},
            ]
        },
        {
            "PubmedID": "789012",
            "Title": "Cancer Treatment Advances",
            "Publication Date": "2024-11-20",
            "Authors": [
                {"Name": "Mark Lee", "Email": "mark.lee@biotechlabs.com", "Affiliation": "Biotech Labs"},
                {"Name": "Sophia Brown", "Email": "sophia.brown@research.edu", "Affiliation": "National Research Institute"},
            ]
        }
    ]

    processed_results = []
    for paper in results:
        non_academic_authors = []
        company_affiliations = []
        corresponding_author_email = None

        for author in paper["Authors"]:
            name, email, affiliation = author["Name"], author["Email"], author["Affiliation"]

            if is_non_academic(email, affiliation):
                non_academic_authors.append(name)
                if affiliation and affiliation not in company_affiliations:
                    company_affiliations.append(affiliation)

            # Assume the first author with an email is the corresponding author
            if not corresponding_author_email and email:
                corresponding_author_email = email

        processed_results.append({
            "PubmedID": paper["PubmedID"],
            "Title": paper["Title"],
            "Publication Date": paper["Publication Date"],
            "Non-academic Author(s)": ", ".join(non_academic_authors),
            "Company Affiliation(s)": ", ".join(company_affiliations),
            "Corresponding Author Email": corresponding_author_email or "N/A"
        })

    return processed_results

def save_to_csv(data, filename="pubmed_results.csv"):
    """
    Save processed results to a CSV file.
    """
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["PubmedID", "Title", "Publication Date",
                                                  "Non-academic Author(s)", "Company Affiliation(s)",
                                                  "Corresponding Author Email"])
        writer.writeheader()
        writer.writerows(data)

def main():
    """
    Main function to fetch and save PubMed papers.
    """
    query = "cancer research"
    print(f"Fetching PubMed papers for query: {query}")

    papers = fetch_pubmed_papers(query, debug=True)
    save_to_csv(papers)

    print(f"Results saved to pubmed_results.csv")

if __name__ == "__main__":
    main()
