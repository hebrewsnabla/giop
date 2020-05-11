from bs4 import BeautifulSoup
import sys

overlay = sys.argv[1]
ioplab = sys.argv[2]
html_str = open('Overlay%s.html'%overlay,'r',encoding='utf-8').read()
soup = BeautifulSoup(html_str, 'lxml')

#print(soup.table)
data = {}
iopname = soup.find_all('p', {'class':'iop_name'})
for iop in iopname:
    id = iop.attrs['id']
    #print(id)
    id = id.split('_')[-1]
    
    if id != ioplab: continue
    print(iop.string)
    
    #siblings = iop.next_siblings
    intro = iop.next_sibling.next_sibling
    #intro = intro.string
    print(intro.string)
    
    table = iop.next_sibling.next_sibling.next_sibling.next_sibling
    #print(table.name)
    if 'table' not in table.name: continue
    tbody = table.tbody
    #print(s,table)
    #tabdict = {}
    rows = tbody.children
    for n,row in enumerate(rows):
        #print(n,tag)
        if n%2==1:
            key = row.td
            value = key.next_sibling.next_sibling
            print(key.string, '  ', value.string)

