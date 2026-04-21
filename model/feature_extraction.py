from urllib.parse import urlparse
import re

PHISHING_KEYWORDS = [
    "login","verify","secure","account","update",
    "bank","confirm","password","paypal","signin"
]

def has_ip(url):
    return 1 if re.search(r'(?:\d{1,3}\.){3}\d{1,3}', url) else 0


def extract_features(url):

    parsed = urlparse(url)

    suspicious_tlds = ['.tk', '.ml', '.ga', '.cf', '.gq']
    tld_flag = 1 if any(url.endswith(tld) for tld in suspicious_tlds) else 0
    shorteners = ['bit.ly', 'tinyurl.com', 'goo.gl', 'ow.ly', 't.co']
    shortener_flag = 1 if any(shortener in url for shortener in shorteners) else 0
    long_url = 1 if len(url) > 75 else 0

    features = [
        len(url),                        # 1 URL length
        len(parsed.netloc),              # 2 Domain length
        len(parsed.path),                # 3 Path length
        url.count("."),                 # 4 Dot count
        url.count("-"),                 # 5 Hyphen count
        url.count("@"),                 # 6 @ count
        url.count("?"),                 # 7 Query count
        url.count("="),                 # 8 Equal count
        sum(c.isdigit() for c in url),  # 9 Digit count
        sum(c.isalpha() for c in url),  # 10 Alphabet count
        sum(not c.isalnum() for c in url), # 11 Special char count
        1 if parsed.scheme == "https" else 0, # 12 HTTPS
        has_ip(url),                    # 13 IP usage
        parsed.netloc.count("."),       # 14 Subdomain count
        sum(1 for word in PHISHING_KEYWORDS if word in url.lower()), # 15 Keywords
        tld_flag,                       # 16 Suspicious TLD
        shortener_flag,                 # 17 URL Shortener
        long_url                        # 18 Long URL
    ]
    

    return features
