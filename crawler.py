import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import sys

def get_all_forms(url):
    """Fetch all form tags from the given URL."""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Error fetching URL: {e}")
        return []

    soup = BeautifulSoup(response.text, "html.parser")
    return soup.find_all("form")

def form_has_csrf(form):
    """Check if the form contains a CSRF token."""
    csrf_keywords = ['csrf', '__RequestVerificationToken', 'token']

    inputs = form.find_all("input")
    for input_tag in inputs:
        name = input_tag.get("name", "").lower()
        id_ = input_tag.get("id", "").lower()

        if any(keyword in name or keyword in id_ for keyword in csrf_keywords):
            return True
    return False

def scan_for_csrf(url):
    """Scan the given URL for forms missing CSRF tokens."""
    forms = get_all_forms(url)

    if not forms:
        print("❌ No forms found on the page.")
        return

    print(f"✅ Found {len(forms)} form(s) on {url}\n")

    for i, form in enumerate(forms, 1):
        print(f"--- Form #{i} ---")
        action = form.get("action")
        method = form.get("method", "get").upper()
        print(f"Action: {action}")
        print(f"Method: {method}")

        if form_has_csrf(form):
            print("✅ CSRF token found.\n")
        else:
            print("⚠️  CSRF token NOT found!\n")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python crawler.py <URL>")
        sys.exit(1)

    target_url = sys.argv[1]
    scan_for_csrf(target_url)
