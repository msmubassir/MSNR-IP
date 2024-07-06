from flask import Flask, request, render_template
import requests

app = Flask(__name__)

request_uri = 'https://ipgeolocation.abstractapi.com/v1'
auth = 'b426095506ac4d2aa3d5ac2e899326eb'

def fetch_ip_details(ip_address):
    url = f"{request_uri}?api_key={auth}&ip_address={ip_address}"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}

@app.route('/')
def index():
    ip_address = request.args.get('ip', request.remote_addr)
    heading = f"IP Details for {ip_address}"
    details = fetch_ip_details(ip_address)
    return render_template('index.html', heading=heading, details=details)

if __name__ == '__main__':
    app.run(debug=True)
