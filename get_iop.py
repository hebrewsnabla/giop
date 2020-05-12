from bs4 import BeautifulSoup
import sys,io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')

overlay = sys.argv[1]
ioplab = sys.argv[2]
file = open('G16html/Overlay%s.html'%overlay,'r',encoding='utf-8')
html_str = file.read()
file.close()
soup = BeautifulSoup(html_str, 'lxml')

def parse_sup(key):
    cont = key.contents
    keystr = ""
    for item in cont:
        try:
            s = item.name[0]
        except:
            keystr += item
        else:
            if 'sup' in item.name:
                keystr += '^'
                keystr += item.string
            else:
                keystr += item.string
    return keystr

def print_table(table):
    #table = iop.next_sibling.next_sibling.next_sibling.next_sibling
    #print(table.name)
    #if 'table' not in table.name: continue
    tbody = table.tbody
    #print(s,table)
    #tabdict = {}
    rows = tbody.children
    for n,row in enumerate(rows):
        #print(n,tag)
        try:
            td = row.td.string
            #print(td)
        except:
            continue
        else:
            rowstr = ""
            for m,key in enumerate(row.children):
                try:
                    sup = key.sup.string
                except:
                    pass
                else:
                    #print(key.contents)
                    rowstr += parse_sup(key)
                    rowstr += '  '
                try:
                    rowstr += key.string.strip('\n')
                    rowstr += '  '
                except:
                    continue
            print(rowstr)



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
    #intro = iop.next_sibling.next_sibling
    #intro = intro.string
    #print(intro.string)
    nextsib = iop.next_sibling.next_sibling

    while(True):
        if 'table' in nextsib.name:
            print_table( nextsib )
            nextsib = nextsib.next_sibling.next_sibling
        elif 'hr' in nextsib.name:
            break
        elif 'p' in nextsib.name:
            pstr = parse_sup(nextsib)
            print(pstr)
            nextsib = nextsib.next_sibling.next_sibling
        elif 'h4' in nextsib.name:
            print(nextsib.string)
            nextsib = nextsib.next_sibling.next_sibling
        elif 'div' in nextsib.name:
            for i,divchild in enumerate(nextsib.children):
                try:
                    name = divchild.name[0]
                    #print(divchild.name)
                except:
                    continue
                if 'table' in divchild.name:
                    print_table(divchild)
                elif 'p' in divchild.name:
                    pstr = parse_sup(divchild)
                    print(pstr)
                else:
                    print("Error: label name not recognized")
            nextsib = nextsib.next_sibling.next_sibling
        else:
            print("Error: label name not recognized")
            break
