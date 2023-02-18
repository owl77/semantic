import random
import os
import re
import copy

def GetKey(a,dic):
 for x in dic.keys():
   if a == dic[x]:
      return x
 return 0           
   
v = open('verbs.txt','r') 
preroget = v.read()
v.close()
roget = preroget.split('\n')
verbs = []
for x in roget:
  verbs.append(x.split(' '))
  
    
#e = open('encyc.txt','r') 
#preenc = e.read()
#e.close()
#enc = preenc.split('.')

#encyclo = []
#for x in enc:
    
 #encyclo.append(x.strip())
 
gram = ["the","a","for","to","if"",all","some","very","I","you","he","she","on","at","from"]
#complete... 

def getenc(word):
 aux = []    
 for x in encyclo:
  aux2 = x.split(' ')
  if word in aux2 and not word in gram:
      
    aux.append(x)
           
 return aux   
  
   

f = open('roget6.txt','r') 
preroget = f.read()
f.close()
roget = preroget.split('#')
length = len(roget)
web = {}
key = {}
net = {}
for x in range(0,length):
 net[x] = re.findall(r'\d+', roget[x])    
 net[x] = net[x] + re.findall(r'\d+a', roget[x]) 
 net[x] = net[x] + re.findall(r'\d+b', roget[x]) 
 aux = roget[x].split('.')
 aux2 = [y.strip() for y in aux]
 web[x] = [y for y in aux2 if not y.isdigit() and  y!="adj" and  y!="adv" and y!='' and y!='—n' and y!='v' and y!='n' and y!='s' and y[0]!='(' and y!='phr' and y[0]!='_' and not y[0] in ['[',']']]
 
 #print(x)
 #print(aux[0])     
 #print(aux)
 key[x] = aux[0]
key.pop(0) 
#print(key)
#print(net)
net2 = {}
#print("")
#print("")
web.pop(0)

for x in net.keys():   
 net2[x] = [GetKey(y, key) for y in net[x][1:] ]
#print(net2) 

#print("")


def move(p,mem):
 if p == 0:
    return mem
 if len(web[p]) == 0:
     return mem       
 n = random.randint(1,len(web[p])-1)
 mem.append((web[p][n]))
 l = len(net2[p])
 if l != 0:
    m = random.randint(0,l-1)
    move(copy.deepcopy(m),mem)
 return mem    
    

def talk():
 l = len(web.keys())
 s = random.randint(1,l-1)
 return move(s,[])
   
   
def assoc(p,k):
  mem = []
  for i in range(0,k):    
   n = random.randint(1,len(web[p])-1)   
   mem.append(web[p][n])
  return mem              
     
#A RANDOM WALK THROUGH THE SEMANTIC NETWORK WILL MINIMUM BOUND ON PATH LENGTH - WARNING, POSSIBLE CYCLES     
     
def conv(n):
 aux = talk()
 while len(aux) < n:
     aux = talk()
 print('\n'.join(aux))
 

def find(word):
 aux = []
 l = len(web.keys())
 for n in range(1,l):
  for m in range(0, len(web[n])) :    
   if word == web[n][m]:
     
     aux.append([n, web[n]])
 l2 = len(aux)
 if l2 > 0:
  r = random.randint(0,l2-1)     
  return [aux[r]]     
 return aux
 
def randext(list,k):
 l = len(list)  
 if l == 0:
  return []    
 aux = []
 for i in range(0,k):
   r = random.randint(0,l-1)
   aux.append(list[r])
 return aux  
               

#THIS IS THE MAIN FUNCTION
#========================

def semantic(sen,depth):
# strip double spaces
# process plurals, verbal forms
 sent = sen.split(' ')
 sent2 = []
 for w in sent:
  if w[0] =="s":
    sent2.append(w[0:len(w)-1])
  if len(w) > 1:
    if w[len(w)-2:]=="ed":
      sent2.append(w[0:len(w)-2])
      sent2.append(w[0:len(w)-1])
  if len(w) > 2:
     if w[len(w)-3:]=="ing":
       sent2.append(w[0:len(w)-3])
  for ir in verbs:
    if w in ir:
     for e in ir:
      sent2.append(e)             
#strong verb table
 sent = sent + sent2               
 #print(sent)
 #em = [randext(getenc(w),1) for w in sent]
 #en = []
 #for x in em:
 # if len(x)!=0:
  #  en.append(x[0])
 
 sem1 = [find(w) for w in sent]
 sem = []
 for x in sem1:
  sem = sem + x
 
       
 clus = [w[0] for w in sem]
 #print(clus)
 cont = [randext(net2[s],depth) for s in clus]
 print(clus)
 print(cont)
 clus2 = copy.deepcopy(clus)
 for x in cont:
  clus2 = clus2 + x
 print(clus2) 
 out1 = [assoc(p,depth) for p in clus2]
 out2 = []
 for x in out1:
    out2 = out2 + x
 #out2 = list(set(out2))
 
 speech = ' . '.join(out2)
 print(speech)
 
 talk = "say " + '"' + speech + '"'
#This for MacOs ! Change according to your OS ! 
 os.system(talk)
 
 
# speech2 = ' '.join(en)
# print(speech2)
# talk2 =  "say " + '"' + speech2 + '"'
# os.system(talk2)
 
# print(len(out2))
 return 
        
                          
#EXAMPLE

# $ python3.9 -i semantic.py
# >>> semantic("worried about money",1)
#marginated roll in riches environ cut up cornucopia in a state of pain


# com = "curl -s https://en.wiktionary.org/wiki/" + word +  " > dic/" + word + ".html"
# os.system(com)


