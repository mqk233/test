import os
import zipfile

import wget
import yaml

if __name__ == '__main__':
    wget.download(url="https://github.com/ssrsub/ssr/raw/master/Clash.yml", out='Clash.yml')
    with open(file='Clash.yml', mode='r', encoding='utf-8') as clash_file:
        lines_to_keep = []
        for line in clash_file:
            if '!<str>' not in line or '公益机场' not in line:
                lines_to_keep.append(line)
        clash_content = yaml.safe_load(''.join(lines_to_keep))
    os.mkdir(path='myfiles')
    with open(file='myfiles/MyClash.yml', mode='w', encoding='utf-8') as result_clash_file:
        yaml.dump(data={'mixed-port': 7890, 'mode': 'global', 'proxies': clash_content['proxies']},
                  stream=result_clash_file,
                  allow_unicode=True,
                  sort_keys=False)
