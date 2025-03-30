# coding: utf-8
'''
Emoji Counter
Count all the emojis and embed them into a .json file
'''
import os
import sys
import json
import datetime
from pathlib import Path


def current_dir() -> str:
    '''
    获取当前主程序所在目录
    '''
    return str(Path(__file__).parent)


def get_path(path: str) -> Path:
    '''
    相对路径 (基于主程序目录) -> 绝对路径
    '''
    if current_dir().startswith('/var/task') and path == 'data.json':
        # 适配 Vercel 部署 (调整 data.json 路径为可写的 /tmp/)
        return '/tmp/sleepy_data.json'
    else:
        return str(Path(__file__).parent.joinpath(path))


def loaddir(dir: str = '.'):
    '''
    load all .yaml files in a folder (dont count sub!)
    '''
    ret = []
    print(f'Loading dir `{dir}`: [ ', end='')
    dirlst = os.listdir(dir)
    for n in dirlst:
        n: str
        if n.endswith('.jpg') or n.endswith('.png') or n.endswith('.webp') or n.endswith('.gif'):
            if n.startswith('./'):
                n = n[1:]
            print(n, end=' ')
            ret.append(n)
    print(']')
    return ret


print('========== Build Script Start ==========')
print(f'Script Path: {sys.argv[0]}')
if os.environ.get('CF_PAGES'):
    print('CF Pages Detected')

# with open(get_path('meta.json'), 'r', encoding='utf-8') as f:
#     meta: dict = json.load(f)
# print(f'Loaded Metadata: {meta}')

timenow = datetime.datetime.now(datetime.timezone.utc)
emoji = {
    'utc_build_timestamp': int(timenow.timestamp()),
    'utc_build_time': str(timenow),
    'is_cf_pages': bool(os.environ.get('CF_PAGES', False)),
    'commit_id': os.environ.get('CF_PAGES_COMMIT_SHA', None),
    'commit_branch': os.environ.get('CF_PAGES_BRANCH', None)
}

# emojis = []
# for path in meta['paths']:
#     path = get_path(path)
#     path_emojis = loaddir(path)

path = get_path('.')
emoji['emojis'] = loaddir(path)

print(f'Saving emoji to: {get_path("emoji.json")}')
with open(get_path('emoji.json'), 'w', encoding='utf-8') as f:
    json.dump(emoji, f, indent=4, ensure_ascii=False)
print(f'Saved Emoji: {emoji}')

print('=========== Build Script End ===========')
