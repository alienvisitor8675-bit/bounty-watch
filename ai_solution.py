```python
from bs4 import BeautifulSoup
import html

# New in-scope targets for inDrive
inDrive_new = [
    'ab-api-gw-cf.global.aws.indriverapp.com',
    'ab-api-gw-scf.global.aws.indriverapp.com',
    'api-gw-scf.sa.apse1.aws.indriverapp.com',
    'arsentomsky.indrive.com',
    'ath-cf.euce1.indriverapp.com',
    'ath-gw-cf.euce1.indriverapp.com',
    'ath-gw-scf.euce1.indriverapp.com',
    'av.indrive.com',
    'baf-gw-cf.africa.afso1.aws.indriverapp.com',
    'baf-gw-scf.sa.apse1.aws.indriverapp.com',
    'balance-api-front.eu-east-1.indriverapp.com',
    'balance-api.eu-east-1.indriverapp.com',
    'bc-cf.latam-co.saea1.aws.indriverapp.com',
    'bc-gw-cf.latam-pe.saea1.aws.indriverapp.com',
    'bdu-cf.euce1.indriverapp.com',
    'bdu-gw-cf.euce1.indriverapp.com',
    'bdu-gw-scf.euce1.indriverapp.com',
    'bf-cf.latam-co.saea1.aws.indriverapp.com',
    'bf-gw-cf.latam-pe.saea1.aws.indriverapp.com',
    'bid-cf.africa.afso1.aws.indriverapp.com',
    'bid-gw-cf.africa.afso1.aws.indriverapp.com',
    'bid-gw-scf.sa.apse1.aws.indriverapp.com',
    'ca-gw-cf.latam-mx.usea1.aws.indriverapp.com',
    'cas-cf.euce1.indriverapp.com',
    'cas-gw-cf.euce1.indriverapp.com',
    'cas-gw-scf.euce1.indriverapp.com',
    'cas.eu-east-1.indriverapp.com',
    'cca-cf.latam-mx.usea1.aws.indriverapp.com',
    'chat.eu-east-1.indriverapp.com',
    'cht-cf.euce1.indriverapp.com',
    'cht-gw-cf.euce1.indriverapp.com',
    'cht-gw-scf.euce1.indriverapp.com',
    'cm-cf.euce1.indriverapp.com',
    'cmf-cf.euce1.indriverapp.com',
    'co-gw-scf.sa.apse1.aws.indriverapp.com',
    'co-in-cf.mena.meso1.aws.indriverapp.com',
    'co-in-gw-scf.sa.apse1.aws.indriverapp.com',
    'company.indrive.com',
    'coms.ryadom.kz',
    'courier-gw-cf.cis.euce1.aws.indriverapp.com'
]

# New in-scope target for StonikByte
stonikbyte_new = ['https://marketplace.atlassian.com/apps/1752044660/cumulative-flow-diagram-cfd-charts-for-agile-scrum-kanban?hosting=c']

# HTML content with the details
html_content = """
<h1>indrive</h1>
https://hackerone.com/indrive
- new in-scope: `ab-api-gw-cf.global.aws.indriverapp.com`, `ab-api-gw-scf.global.aws.indriverapp.com`, `api-gw-scf.sa.apse1.aws.indriverapp.com`, `arsentomsky.indrive.com`, `ath-cf.euce1.indriverapp.com`, `ath-gw-cf.euce1.indriverapp.com`, `ath-gw-scf.euce1.indriverapp.com`, `av.indrive.com`, `baf-gw-cf.africa.afso1.aws.indriverapp.com`, `baf-gw-scf.sa.apse1.aws.indriverapp.com`, `balance-api-front.eu-east-1.indriverapp.com`, `balance-api.eu-east-1.indriverapp.com`, `bc-cf.latam-co.saea1.aws.indriverapp.com`, `bc-gw-cf.latam-pe.saea1.aws.indriverapp.com`, `bdu-cf.euce1.indriverapp.com`, `bdu-gw-cf.euce1.indriverapp.com`, `bdu-gw-scf.euce1.indriverapp.com`, `bf-cf.latam-co.saea1.aws.indriverapp.com`, `bf-gw-cf.latam-pe.saea1.aws.indriverapp.com`, `bid-cf.africa.afso1.aws.indriverapp.com`, `bid-gw-cf.africa.afso1.aws.indriverapp.com`, `bid-gw-scf.sa.apse1.aws.indriverapp.com`, `ca-gw-cf.latam-mx.usea1.aws.indriverapp.com`, `cas-cf.euce1.indriverapp.com`, `cas-gw-cf.euce1.indriverapp.com`, `cas-gw-scf.euce1.indriverapp.com`, `cas.eu-east-1.indriverapp.com`, `cca-cf.latam-mx.usea1.aws.indriverapp.com`, `chat.eu-east-1.indriverapp.com`, `cht-cf.euce1.indriverapp.com`, `cht-gw-cf.euce1.indriverapp.com`, `cht-gw-scf.euce1.indriverapp.com`, `cm-cf.euce1.indriverapp.com`, `cmf-cf.euce1.indriverapp.com`, `co-gw-scf.sa.apse1.aws.indriverapp.com`, `co-in-cf.mena.meso1.aws.indriverapp.com`, `co-in-gw-scf.sa.apse1.aws.indriverapp.com`, `company.indrive.com`, `coms.ryadom.kz`, `courier-gw-cf.cis.euce1.aws.indriverapp.com`
"""

# Parse the HTML content
soup = BeautifulSoup(html_content, 'html.parser')

# Extract the main heading
h1 = soup.find('h1')
if h1:
    heading = h1.text
else:
    heading = "No heading found"

# Extract and process the in-scope targets for inDrive
in_drive_targets = []
list_items = soup.find_all('li')
for li in list_items:
    if 'new in-scope:' in str(li):
        targets = li.text.split('`')
        in_drive_targets = [t.strip().strip('`') for t in targets[1::2]]

# Print the result
print(f"Displaying the main heading: {heading}")
print("\nIn-Drive new in-scope targets:")
print("\n".join(in_drive_targets))
print("\nStonikByte new in-scope targets:")
print("\n".join(stonikbyte_new))
```