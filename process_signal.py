import sys

def process_signal(title, body):
    # Your processing logic goes here
    # For now, it just prints the title and body
    print(f"Issue Title: {title}")
    print(f"Issue Body: {body}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python process_signal.py [title] [body]")
        sys.exit(1)

    issue_title = sys.argv[1]
    issue_body = sys.argv[2]
    
    process_signal(issue_title, issue_body)
