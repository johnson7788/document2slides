## SciDuet
```console
pip install -r requirements.txt
```

### Scrape conference archives
```console
python scrape_urls.py  # 生成external_urls.csv
python collect_files.py  # 下载论文和ppt，保存到data/papers 和data/slides 目录下
```

### Paper Extraction: Grobid + PDFFigures 2.0

Follow installation steps from https://grobid.readthedocs.io/en/latest/Install-Grobid/ and https://github.com/kermitt2/grobid_client_python.
提取pdf的文本
```console
cd grobid-0.6.2
./gradlew run
cd path/to/grobid-client-python/grobid_client
# 在sciduet-build目录下，创建teidir
# 注意config.json中改成你自己的grobid_server和端口， grobid_client.py改成相对路径导入client，即去掉.
grobid_client --config ../config.json --input /Users/admin/git/document2slides/sciduet-build/data/papers --output /Users/admin/git/document2slides/sciduet-build/teidir --teiCoordinates processFulltextDocument
```

OPTIONAL: Use pdffigures2 提取图片和表格 (this repo omits automatic figure selection). https://github.com/allenai/pdffigures2
```console
git clone https://github.com/allenai/pdffigures2.git
cd pdffigures2
export JAVA_HOME="/Library/Java/JavaVirtualMachines/adoptopenjdk-8.jdk/Contents/Home"
# -s 是中间的状态文件，-m 图片文件 -d 表格文件
sbt "runMain org.allenai.pdffigures2.FigureExtractorBatchCli /home/wac/johnson/johnson/document2slides/sciduet-build/data/papers/ -s sciduet/stat_file.json -m sciduet/image/ -d sciduet/data/" 
```

grobid提取的 tei.xml 文件转换成 json格式, 保存到paper_jsons目录下，保存papers.pkl

```console
python extract_papers.py
```

### Slide Extraction: Poppler pdftotext
提取ppt到text文本, 保存到slide_txts目录下和suppl_slides_filter.json，suppl_slides_prefilter.json
Original code uses IBM Watson Discovery Package and Tesseract-OCR to extract text from slides.  
We provide code for running the open-source command-line utility _pdftotext_ to achieve comparable results.

```console
python extract_slides.py
```


### Merge ACL with supplemental data
# 如果有ACL数据
Finished ACL data is provided in inputs/. The code in this dir provides functionality for preprocessing ICML and NeurIPS data.
You can supplement ACL however you like. In the paper, all supplemental data are in the train split.

Run the following to merge into inputs/ and resplit the data.

```console
python merge_acl_suppl.py
```