# Collect files from external_urls.csv
import requests
from pathlib import Path
import pandas as pd
from tqdm import tqdm

df = pd.read_csv('external_urls.csv')
Path("data/papers").mkdir(parents=True, exist_ok=True)
Path("data/slides").mkdir(parents=True, exist_ok=True)
for i, row in tqdm(df.iterrows(),desc="下载中"):
    if i < 910:
        continue
    print(f"正在下载第{i}个论文和ppt: 论文: {row['papers']}, PPT: {row['slides']}")
    r1 = requests.get(row['papers'])
    r2 = requests.get(row['slides'])
    f1 = Path('data/papers/{}.pdf'.format(i))
    f1.write_bytes(r1.content)
    f2 = Path('data/slides/{}.pdf'.format(i))
    f2.write_bytes(r2.content)
