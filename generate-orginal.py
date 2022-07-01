import json
from types import SimpleNamespace
p = "kavsir_bboxes.json"
f = open(p)
#data = json.loads(f, object_hook=lambda d: SimpleNamespace(**d))
data = json.load(f)

for i, k in enumerate(data):
    #print(k)
    # print(i, k, data[k])
    # print(i, k, data[k].items())
    # l= data[k].items()

    ll = data[k]
    l=ll['bbox']
    s = len(l)
    print(l[0]['xmin'], s)
    # for str in ll:
    #     print(str)
    # print(ll[20])
    line =0
    h=ll['height']
    w=ll['width']
    xmax = (l[line]['xmax'])
    # if xmax==w:
    #     xmax-=1
    ymax = (l[line]['ymax'])
    # if ymax==h:
    #     ymax-=1
    print(h)
    with open(f"generate-labels/{k}.txt", 'w') as f:
        list = []
        for line in range(s):
            xmax = (l[line]['xmax'])
            ymax = (l[line]['ymax'])
            listItem = f"1 {l[line]['xmin']} {l[line]['ymin']} {xmax} {ymax}\n"
            list.append(listItem) 
        f.writelines(list)
    # print(l.bbox)

