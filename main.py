import requests
from tqdm import tqdm

with open('2021.md', encoding="utf-8") as f:
    metadata = f.read()
    
    links = []
    for line in metadata.splitlines():
        link = line.split(']')[1][1:].split(')')[0]
        print(link)
        if not link.startswith('http'):
            assert False
        links.append(link)
    
    count = 0
    
with open('output_2021.txt', 'w', encoding="utf-8") as output:
    for link in tqdm(links):
        r = None
        for i in range(3):
            try:
                r = requests.get(link, timeout=15)
                break
            except Exception as e:
                print(link, "   ---FAILED")
                output.write(link + '   ---FAILED\n')
                output.flush()
        if r is None:
            print(link, "---FAILED")
            output.write(link + '   ---FAILED\n')
            output.flush()
            continue
        if r.status_code in [200, 403]:
            count += 1
            print(link, "   ---OK")
            output.write(link + '   ---OK\n')
            output.flush()
print(count)
output.write(count)