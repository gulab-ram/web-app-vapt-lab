# Web App VAPT Lab (in progress)

A hands-on lab for learning web application security testing.

- Environment: Kali Linux VM, Docker
- Target: OWASP Juice Shop (a deliberately vulnerable web app), run locally in a container
- Done so far: lab setup; Nmap service scans of the Juice Shop container (see `nmap_juiceshop.txt`, `nmap_http_scripts.txt`); review of HTTP response headers
- Observation to investigate: the app sends `Access-Control-Allow-Origin: *` (permissive CORS); not yet tested for exploitability
- Next: Burp Suite testing of OWASP Top 10 issues, Zeek attack detection, CVSS-rated report

Note: all testing is done only on my own local lab environment.
