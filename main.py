import os
import zipfile

import wget
import yaml

if __name__ == '__main__':
    wget.download(url="https://github.com/ssrsub/ssr/archive/refs/heads/master.zip", out='ssr-master.zip')
    zip_files = zipfile.ZipFile(file='ssr-master.zip')
    for zip_file in zip_files.namelist():
        zip_files.extract(zip_file)
    zip_files.close()
    with open('./ssr-master/Clash.yml', 'r', encoding='utf-8') as clash_file:
        clash_content = yaml.load(clash_file, Loader=yaml.FullLoader)
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
