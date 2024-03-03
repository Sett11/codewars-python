def get_issuer(n):
    s=str(n)
    l=len(s)
    if s.startswith(('34','37')) and l==15:
        return 'AMEX'
    if s.startswith('6011') and l==16:
        return 'Discover'
    if s.startswith(('51','52','53','54','55')) and l==16:
        return 'Mastercard'
    if s.startswith('4') and (l==13 or l==16):
        return 'VISA'
    return 'Unknown'

print(get_issuer(4111111111111111))