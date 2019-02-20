# 環境構築

pythonインストール
```
$ brew install python
```

確認
```
$ python3 --version
```

virtualenvインストール
```
$ pip3 install virtualenv
```

仮想環境を作る
```
$ cd 作成する場所
$ mkdir nirs-analysis
$ virtualenv nirs-analysis
```

仮想環境を有効化する
```
$ cd nirs-analysis
$ source bin/activate
(nirs-analysis) $
```

無効化
```
(nirs-analysis) $ deactivate
```