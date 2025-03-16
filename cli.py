import argparse
from pubmed_fetcher import fetch_papers

def main():
    parser = argparse.ArgumentParser(description="Fetch research papers from PubMed based on a query.")

    parser.add_argument("query", type=str, help="Search query for PubMed")
    parser.add_argument("-f", "--file", type=str, help="Save results to a specified CSV file")
    parser.add_argument("-d", "--debug", action="store_true", help="Enable debug mode")

    args = parser.parse_args()

    if args.debug:
        print(f"Debug Mode: Fetching papers for query '{args.query}'")

    results = fetch_papers(args.query)

    if args.file:
        import pandas as pd
        df = pd.DataFrame(results)
        df.to_csv(args.file, index=False)
        print(f"Results saved to {args.file}")
    else:
        for paper in results:
            print(paper)

if __name__ == "__main__":
    main()
