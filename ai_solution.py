```python
def extract_in_scope_targets(text):
    programs = []
    current_program = {}
    current_items = []
    
    lines = text.split('\n')
    for line in lines:
        line = line.strip()
        if line.startswith('###'):
            if current_program:
                programs.append(current_program)
            current_program = {'name': line[3:].strip()}
        elif line.startswith('https:'):
            current_program['link'] = line
        elif line.startswith('- new in-scope:'):
            items = line[len('- new in-scope:'):].strip().split('\n')
            current_items = [item.strip() for item in items if item.strip()]
            current_program['items'] = current_items
    if current_program:
        programs.append(current_program)
        
    return programs

# Example usage:
text = """
### Water-Link (`it:waterlink/water-link`)  💰 $5000
https://www.intigriti.com/programs/waterlink/water-link/detail
- new in-scope: `*.aww.be`, `*.water-link.be`, adelta.be`, `aquawardsoperate.water-link.be`, `aquawardsspatial.water-link.be`, `aww.eu`, `desktop.water-link.be`, `induss.eu`, `indussiibis.water-link.be`, `pit.water-link.be`, `rio-link.be`, `water-kracht-levering.be`, `water-kracht-levering.eu`, `water-link-jaarverslag.be`, `waterkracht-levering.be`, `waterkracht-levering.eu`, `waterlink.be`, `waterstoringen.be`

### DevAcrobats (`bc:devacrobats-market`)  💰 $1500
https://bugcrowd.com/engagements/devacrobats-market
- new in-scope: `https://marketplace.atlassian.com/apps/1218655/performance-charts-and-reports-for-jira-dashboards?hosting=cloud&tab=overview`, `https://marketplace.atlassian.com/apps/1218655/performance-charts-and-reports-for-jira-dashboards?hosting=datacenter&tab=overview`

### Databricks (`h1:databricks`)
https://hackerone.com/databricks
- new in-scope: `https://github.com/databricks/*`
"""

result = extract_in_scope_targets(text)
for program in result:
    print(program)
```