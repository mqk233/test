import os
import zipfile

import wget
import yaml

if __name__ == '__main__':
    wget.download(url="https://github.com/ssrsub/ssr/raw/master/Clash.yml", out='Clash.yml')
    with open(file='Clash.yml', mode='r', encoding='utf-8') as clash_file:
        lines_to_keep = []
        for line in clash_file:
            if '!<str>' not in line:
                lines_to_keep.append(line)
        clash_content = yaml.safe_load(''.join(lines_to_keep))
        proxies = clash_content['proxies']
        remove_index = -1
        for i in range(len(proxies)):
            if proxies[i]['name'].find('公益机场') != -1:
                remove_index = i
                break
        if remove_index != -1:
            proxies.pop(remove_index)
    os.mkdir(path='myfiles')
    with open(file='myfiles/MyClash.yml', mode='w', encoding='utf-8') as result_clash_file:
        yaml.dump(data={'mixed-port': 7890, 'mode': 'global', 'proxies': proxies},
                  stream=result_clash_file,
                  allow_unicode=True,
                  sort_keys=False)
