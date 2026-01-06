def classify():
    vulns = ['XSS', 'CSRF', 'IDOR', 'SQLi', 'SSRF']
    for v in vulns:
        print('Category:', v)