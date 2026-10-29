import json,sys
r=json.load(open('equations.json'))
for x in r:
    if x['ch']==sys.argv[1]: print(x['id'].rsplit('-',1)[1],x['page'],'['+x['tag']+']',x['latex'].replace('\n',' '))
