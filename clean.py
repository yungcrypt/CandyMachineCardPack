import os, json, uuid
import shutil
targetDir = "targ/"
collectionCount=1000

def itemCount():
    items = []
    assets = []
    for directory in os.walk("asset/"):
        items.append(directory)

    assetsDir = items[0][1]
    rarityCheck = 0
    for asset in assetsDir:
        contents = asset.split('-')
        print(contents)
        path = asset
        name = contents[0]
        rarity = int(contents[1])
        rarityCheck += rarity
        editions = (collectionCount*(rarity*10**-2))
        print(editions)
        item = {"path": path,"name": name,"editions": editions}
        assets.append(item)
    if rarityCheck == 100:
            
        return assets

    else:
        return print('MAKE SURE RARITY ADDS UP TO 100')
        
        
    
def goDoIt(assets): 
    x=0
    for asset in assets:
        count = int(asset['editions'])
        editions = asset['editions']
        path = (asset['path'])
        print(path)
        name = asset['name']
        filepath = "asset/{0}/0.json".format(path)
        imageFile = "asset/{0}/0.png".format(path)

        for w in range(count):
                
            with open(filepath, 'r') as f:
                data = json.load(f)
                data['name'] = "{0}".format(name)
                data['image'] = "{0}.png".format(x)
                data['properties']['files'][0]['uri'] = "{0}.png".format(x)

            tempfile = os.path.join(os.path.dirname(filepath),str(uuid.uuid4))

            with open(tempfile, 'w') as f:
                json.dump(data, f, indent=4)

            shutil.copy(tempfile, (targetDir+str(x)+".json"))
            shutil.copy(imageFile, (targetDir+str(x)+".png"))
            os.remove(tempfile)
            w+=1
            x+=1
    return print('complete')


def generate():
    x=0
    assets = itemCount()
    print(assets)
    print('------------------------------')
    goDoIt(assets)
    



generate()

