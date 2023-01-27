import re
x=re.search('^bon','bonjour')
print(x)
x=re.search('soir$','bonsoir')
print(x)
x=re.search('soir$','bonjour')
print(x)

if re.match('soir$','soir')!=None:
    print("oui, conforme aux criteres de recherche")
else:
    print("Non, conforme aux criteres de recherche")

telephone='0645124511'
if re.match('^0[5-6]([.-]?[0-9]{2}){4}$',telephone):
    print("oui, numéro de telephone valide")
else:
    print("Non ! numéro de telephone invalide")


mails= ["olivier@mailbidon.com", "olivier@mailbidon.ma",
"8@mailbidon.com", "@mailbidon.com","olivier@mailbidon"]

expression="^[a-zA-Z][A-Za-z0-9._-]+@[A-Za-z._-]+.[(com|fr|ma)]$"
for mail in mails:
    if re.match(expression,mail)!=None:
        print ("Ce mail : %s est valide" % mail) 
    else:
        print ("Erreur ce mail : %s est non valide" % mail)

print(re.match(r'From\s*', 'Fromage amk')!=None)
print(re.match(r'From\s+', 'Fromage amk')!=None)

import re
print(re.match('chat*','chapeau')!=None)
print(re.match('chat*','chatterton')!=None)
print(re.match('chat*','chameau')!=None)

