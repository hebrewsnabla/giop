from bs4 import BeautifulSoup
import sys,io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')

overlay = sys.argv[1]
ioplab = sys.argv[2]
if len(sys.argv)==4:
    style = sys.argv[3]
else:
    style = 'txt'
gioppath = sys.path[0]
file = open(gioppath + '/G16html/Overlay%s.html'%overlay,'r',encoding='utf-8')
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
                try:
                    keystr += item.string
                except:
                    try:
                        keystr += ('(' + parse_sup(item) + ')')
                    except:
                        print('err:', item)
            elif 'span' in item.name or 'a' in item.name:
                try:
                    keystr += ('`' + item.string + '`')
                except:
                    print('err:', item)
            elif 'i' in item.name:
                keystr += item.string
            elif 'br' in item.name or 'em' in item.name:
                #print('\n')
                pass
            else:
                print("err:", item)
                keystr += item.string
    return keystr

def detect_table(key):
    has_table = False
    for k in key.contents:
        try:
            istable = 'table' in k.name
        except:
            #print(k)
            pass
        else:
            if istable:
                has_table = True
                print_table(k, '\t\t')
    return has_table

def print_table(table, sep='* '):
    #table = iop.next_sibling.next_sibling.next_sibling.next_sibling
    #print(table.name)
    #if 'table' not in table.name: continue
    tbody = table.tbody
    #print(s,table)
    #tabdict = {}
    try:
        rows = tbody.children
    except:
        #print("err:", tbody)
        rows = table.children
    for n,row in enumerate(rows):
        #print(n,tag)
        try:
            td = row.td.string
            #print(td)
        except:
            continue
        else:
            #print(row.children)
            rowstr = ""
            if style=='md':
                rowstr += sep
            for m,key in enumerate(row.children):
                try:
                    cont = key.contents
                except:
                    pass
                else:
                    #print(key.contents)
                    has_table = detect_table(key)
                    if not has_table:
                        rowstr += parse_sup(key)
                        rowstr += '&nbsp;'*8                   
                #try:
                #    rowstr += key.string.strip('\n')
                #    rowstr += '  '
                #except:
                #    continue
            print(rowstr)



#print(soup.table)
data = {}
iopname = soup.find_all('p', {'class':'iop_name'})
for iop in iopname:
    id = iop.attrs['id']
    #print(id)
    id = id.split('_')[-1]
    
    if ioplab=='all':
        pass
    elif id != ioplab: 
        continue
    iopstr = iop.string
    if style=='md':
        iopstr = '### ' + iopstr
    print(iopstr)
    
    #siblings = iop.next_siblings
    #intro = iop.next_sibling.next_sibling
    #intro = intro.string
    #print(intro.string)
    nextsib = iop.next_sibling.next_sibling

    while(True):
        try:
            nextsibname = nextsib.name
        except:
            #if '/div' in nextsib:
            #    pass
            #else:
            #print("Err:", nextsib)
            break
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
