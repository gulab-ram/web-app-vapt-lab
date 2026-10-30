# Web App VAPT Lab (in progress)

A hands-on lab for learning web application security testing.

- Environment: Kali Linux VM, Docker, Burp Suite Community
- Target: OWASP Juice Shop (a deliberately vulnerable web app), run locally in a container
- Done so far:
  - Lab setup; Nmap service scans of the Juice Shop container (see `nmap_juiceshop.txt`, `nmap_http_scripts.txt`)
  - Reviewed HTTP response headers
  - Set up Burp Suite with its built-in browser; captured Juice Shop traffic in HTTP history and replayed a request in Repeater (see `04_burp_history.png`, `05_burp_repeater.png`)
  - Captured normal browsing traffic with Zeek (see `zeek_http_baseline.log`, `06_zeek_http_log.png`)
  - Built a Python detection script (`detect.py`) that parses Zeek HTTP logs for SQL injection, XSS, path traversal and scanner user-agents; verified zero false positives on clean baseline traffic and correct detection on synthetic attack-pattern log entries (`test_attack_patterns.log`)
- Observation to investigate: the app sends `Access-Control-Allow-Origin: *` (permissive CORS); not yet tested for exploitability
- Next: guided practice (PortSwigger Web Security Academy, OWASP Juice Shop Score Board), then testing real OWASP Top 10 issues in Juice Shop, detecting those live attacks with Zeek + detect.py, and a CVSS-rated report

Note: all testing is done only on my own local lab environment.# Web App VAPT Lab (in progress)

A hands-on lab for learning web application security testing.

- Environment: Kali Linux VM, Docker, Burp Suite Community
- Target: OWASP Juice Shop (a deliberately vulnerable web app), run locally in a container
- Done so far:
  - Lab setup; Nmap service scans of the Juice Shop container (see `nmap_juiceshop.txt`, `nmap_http_scripts.txt`)
  - Reviewed HTTP response headers
  - Set up Burp Suite with its built-in browser; captured Juice Shop traffic in HTTP history and replayed a request in Repeater (see `04_burp_history.png`, `05_burp_repeater.png`)
- Observation to investigate: the app sends `Access-Control-Allow-Origin: *` (permissive CORS); not yet tested for exploitability
- Next: guided practice (PortSwigger Web Security Academy, TryHackMe), then Burp Suite testing of OWASP Top 10 issues in Juice Shop, Zeek attack detection, CVSS-rated report

Note: all testing is done only on my own local lab environment.
