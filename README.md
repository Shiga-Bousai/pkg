# pkg
pkgは[滋賀県コロナ・防災・交通Bot @covid19_shiga](https://twitter.com/covid19_shiga)の独自ライブラリです。

## twitter_python.py
Twitterの独自ライブラリです。  
画像だけでなく動画、gifなどのlarge media に対応しています。  
また以下の形式の.envをルートに置くことで使用できます。

```env
TWITTER_API_KEY=""
TWITTER_API_SECRET=""
TWITTER_BEARER_TOKEN=""
TWITTER_ACCESS_TOKEN=""
TWITTER_ACCESS_TOKEN_SECRET=""
```

### 関連ファイル
twitterModule
˪mediaUpload.py
  メディアアップロードに特化したプログラムです。
˪twitterOAuth1.py
  認証のために使用します。
  
### インストール物 作者環境
requirements.txt参照

```
Python 3.9.10

requests 2.27.1
requests-oauthlib 1.3.0
python-dotenv 0.15.0
```
