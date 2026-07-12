import re, socket, ssl
import tldextract, whois
from urllib.parse import urlparse
import numpy as np

def having_IP_Address(url):
    try:
        ip = urlparse(url).netloc
        socket.inet_aton(ip)
        return -1
    except:
        return 1

def URL_Length(url):
    length = len(url)
    if length < 54: return 1
    elif 54 <= length <= 75: return 0
    else: return -1

def Shortening_Service(url):
    return -1 if re.search(r"bit\.ly|goo\.gl|tinyurl|ow\.ly", url) else 1

def having_At_Symbol(url):
    return -1 if "@" in url else 1

def double_slash_redirecting(url):
    return -1 if url.rfind("//") > 6 else 1

def Prefix_Suffix(url):
    return -1 if '-' in urlparse(url).netloc else 1

def having_Sub_Domain(url):
    ext = tldextract.extract(url)
    subdomain = ext.subdomain.split('.')
    if len(subdomain) == 0 or subdomain == ['']: return 1
    elif len(subdomain) == 1: return 0
    else: return -1

def domain_registration_length(url):
    try:
        domain = whois.whois(urlparse(url).netloc)
        if domain.expiration_date and domain.creation_date:
            exp = domain.expiration_date[0] if isinstance(domain.expiration_date, list) else domain.expiration_date
            creation = domain.creation_date[0] if isinstance(domain.creation_date, list) else domain.creation_date
            age = (exp - creation).days
            return 1 if age >= 365 else -1
    except:
        return -1

def ssl_final_state(url):
    try:
        hostname = urlparse(url).netloc
        ctx = ssl.create_default_context()
        with ctx.wrap_socket(socket.socket(), server_hostname=hostname) as s:
            s.settimeout(3.0)
            s.connect((hostname, 443))
            return 1
    except:
        return -1

def dns_record(url):
    try:
        socket.gethostbyname(urlparse(url).netloc)
        return 1
    except:
        return -1

# Collect all features
def extract_full_features(url, df_columns):
    features = {}

    features["having_IP_Address"] = having_IP_Address(url)
    features["URL_Length"] = URL_Length(url)
    features["Shortining_Service"] = Shortening_Service(url)
    features["having_At_Symbol"] = having_At_Symbol(url)
    features["double_slash_redirecting"] = double_slash_redirecting(url)
    features["Prefix_Suffix"] = Prefix_Suffix(url)
    features["having_Sub_Domain"] = having_Sub_Domain(url)
    features["SSLfinal_State"] = ssl_final_state(url)
    features["Domain_registeration_length"] = domain_registration_length(url)
    features["DNSRecord"] = dns_record(url)

    # Default 0 for missing ones
    for col in df_columns:
        if col not in features:
            features[col] = 0

    # Replace NaN/None
    for k, v in features.items():
        if v is None or (isinstance(v, float) and np.isnan(v)):
            features[k] = 0

    return [features[col] for col in df_columns]
