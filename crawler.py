import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def find_csrf_vulnerabilities(url):
    """
    Crawls a given URL to find forms and checks if they lack CSRF tokens.

    Args:
        url: The starting URL to crawl.
    """
    print(f"--- Scanning {url} for CSRF Vulnerabilities ---")
    
    try:
        response = requests.get(url)
        response.raise_for_status() 
    except requests.exceptions.RequestException as e:
        print(f"Error: Could not connect to {url}. {e}")
        return

    soup = BeautifulSoup(response.text, 'html.parser')
    forms = soup.find_all('form')

    if not forms:
        print("Result: No HTML forms found on this page.")
        return

    print(f"Found {len(forms)} form(s). Analyzing for anti-CSRF tokens...")
    vulnerable_form_count = 0

    for i, form in enumerate(forms, 1):
        has_csrf_token = False
        
        csrf_token_names = ['csrf_token', 'csrfmiddlewaretoken', 'authenticity_token', '_token', '_csrf']
        
       
        for token_name in csrf_token_names:
            if form.find('input', {'type': 'hidden', 'name': token_name}):
                has_csrf_token = True
                break
        
      
        action = form.get('action', 'N/A')
        method = form.get('method', 'GET').upper()

        print(f"\n- Analyzing Form #{i} (Action: {action}, Method: {method})")
        if not has_csrf_token:
            print("  [!] VULNERABILITY DETECTED: Form appears to be missing a CSRF token.")
            vulnerable_form_count += 1
        else:
            print("  [+] OK: Form appears to have an anti-CSRF token.")
            
    print("\n--- Scan Complete ---")
    if vulnerable_form_count > 0:
        print(f"Summary: Found {vulnerable_form_count} form(s) that are potentially vulnerable to CSRF.")
    else:
        print("Summary: No forms without CSRF tokens were found.")
