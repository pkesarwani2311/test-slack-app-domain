import os
from flask import Flask, request, jsonify
import dns.resolver
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

@app.route("/")
def health_check():
    return "OK", 200

@app.route("/domainInfo", methods=["POST"])
def domain_info():
    domain = request.form.get("text", "").strip()
    if not domain:
        return jsonify({
            "response_type": "in_channel",
            "text": "Please provide a domain name. Usage: /domainInfo <domain>"
        }), 200
    
    try:
        answers = dns.resolver.resolve(domain, 'CNAME')
        cnames = [rdata.target.to_text() for rdata in answers]
        if not cnames:
            message = f"No CNAME records found for {domain}."
        else:
            message = f"CNAME records for {domain}:\n" + "\n".join(f"• {cname}" for cname in cnames)
        
        return jsonify({
            "response_type": "in_channel",
            "text": message
        }), 200
        
    except dns.resolver.NoAnswer:
        return jsonify({
            "response_type": "in_channel",
            "text": f"No CNAME records found for {domain}."
        }), 200
    except dns.resolver.NXDOMAIN:
        return jsonify({
            "response_type": "in_channel",
            "text": f"Domain {domain} does not exist."
        }), 200
    except Exception as e:
        return jsonify({
            "response_type": "in_channel",
            "text": f"Error looking up CNAME records: {str(e)}"
        }), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000))) 