def subdomainVisits(cpdomains):
    res = []
    domain_to_number = {}
    for cpdomain in cpdomains:
        count, domain = cpdomain.split(' ')
        domains = domain.split('.')
        for i in range(len(domains)):
            domain_name = '.'.join(domains[i:]) 
            if domain_name not in domain_to_number:
                domain_to_number[domain_name] = int(count)
            else:
                domain_to_number[domain_name] += int(count)
    for item in domain_to_number.items():
        res.append(' '.join([str(item[1]), item[0]]))
    return res

if __name__ == '__main__':
    cpdomains = ["900 google.mail.com", "50 yahoo.com", \
    "1 intel.mail.com", "5 wiki.org"]
    print(subdomainVisits(cpdomains))
