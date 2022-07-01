import json
from types import SimpleNamespace
p = "kavsir_bboxes.json"
f = open(p)
#data = json.loads(f, object_hook=lambda d: SimpleNamespace(**d))
data = json.load(f)

def convert(size, box):
    dw = 1./size[0]
    dh = 1./size[1]
    x = (box[0] + box[2])/2.0
    y = (box[1] + box[3])/2.0
    w = box[2] - box[0]
    h = box[3] - box[1]
    x = x*dw
    w = w*dw
    y = y*dh
    h = h*dh
    return (x,y,w,h)

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

    size=[]
    size.append(w)
    size.append(h)
    print(h)
    with open(f"generate-labels1/{k}.txt", 'w') as f:
        list = []
        
        for line in range(s):
            box1=[]
            xmax = (l[line]['xmax'])
            ymax = (l[line]['ymax'])
            xmin = (l[line]['xmin'])
            ymin = (l[line]['ymin'])
            box1.append(xmin)
            box1.append(ymin)
            box1.append(xmax)
            box1.append(ymax)
            a,b,c,d=convert(size, box1)
            
            listItem = f"0 {a} {b} {c} {d}\n"
            list.append(listItem) 
        f.writelines(list)
    # print(l.bbox)

