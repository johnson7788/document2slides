# document2slides

**This code is for NAACL 2021 paper [D2S: Document-to-Slide Generation Via Query-Based Text Summarization](https://arxiv.org/pdf/2105.03664v1.pdf)**

input目录是已经处理好的数据
```angular2html
tree -d 1 input/
1 [error opening dir]
input/
├── sciduet_papers    # 论文的内容的json格式
└── split    #论文的序号，
acl_slides_prefilter.json # ppt的内容
```



这个资源库包含。
1) sciduet-build: 从PDF格式的NLP/ML论文中重构训练数据集的代码，以及其相应的幻灯片
2) SciDuet-ACL：完成的ACL训练数据的预处理
3) 衍生性标注以及训练好的分类器
4) d2s-model：用于训练和评估自动幻灯片生成系统的代码。 

Edward Sun, Yufang Hou, Dakuo Wang, Yunfeng Zhang, Nancy X.R. Wang. D2S: Document-to-Slide Generation Via Query-Based Text Summarization. In Proceedings of the 18th Annual Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (NAACL-HLT 2021), Online, 6 - 11 June 2021
