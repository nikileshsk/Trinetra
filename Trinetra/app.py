from flask import Flask, render_template, request
import requests


app = Flask(__name__)

# Function to check if a URL is valid
def is_valid_url(url):
    # Placeholder implementation for testing purposes
    # Replace this with your actual implementation
    return True if url.startswith("http://") or url.startswith("https://") else False

# Function to check if a URL exists on the internet


def url_exists(url):
    try:
        response = requests.get(url)
        return response.status_code == 200  # Check if response status is in the 2xx range
    except Exception as e:
        return False
# Function to check URL safety using Google Safe Browsing API
def check_safe_browsing(url):
    # Perform safe browsing check using Google Safe Browsing API
    # You need to replace 'YOUR_API_KEY' with your actual API key
    api_key = 'AIzaSyD64jTRQPB2PwODH--W981VjXLsZmTVQVc'
    url_safe_browsing_api = f'https://safebrowsing.googleapis.com/v4/threatMatches:find?key={api_key}'

    # Function to recursively follow redirects and check each intermediate URL
    def check_redirects(url):
        try:
            response = requests.head(url, allow_redirects=True)
            if response.status_code == 200:
                # Check if the final URL is safe
                payload = {
                    "client": {
                        "clientId": "yourcompanyname",
                        "clientVersion": "1.0"
                    },
                    "threatInfo": {
                        "threatTypes": ["MALWARE", "SOCIAL_ENGINEERING", "THREAT_TYPE_UNSPECIFIED", "UNWANTED_SOFTWARE"],
                        "platformTypes": ["ANY_PLATFORM"],
                        "threatEntryTypes": ["URL"],
                        "threatEntries": [{"url": response.url}]
                    }
                }
                response = requests.post(url_safe_browsing_api, json=payload)
                if response.status_code == 200:
                    data = response.json()
                    if data.get("matches"):
                        return "Unsafe", f"Redirecting to phishing or malware content: {response.url}"
                return "Safe", "No phishing or malware content detected"
            else:
                return "Unsafe", f"Failed to retrieve final URL: {response.status_code}"
        except Exception as e:
            return "Unsafe", f"Error while checking redirects: {str(e)}"

    return check_redirects(url)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check', methods=['POST'])
def check():
    url = request.form.get('url')
    if not url:
        return "Please enter a URL"  # Display message if no URL is provided
    else:
        # Perform URL validation
        if not is_valid_url(url):
            return "Invalid URL"

        # Check if the URL exists
        if not url_exists(url):
            return "URL does not exist"

        # Check URL safety using Google Safe Browsing API
        safe_browsing_result, safe_browsing_message = check_safe_browsing(url)

        return render_template('result.html', url=url, safe=safe_browsing_result, message=safe_browsing_message)

if __name__ == '__main__':
    app.run(debug=True)
