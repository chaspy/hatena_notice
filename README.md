# hatena_notice
This is a script to make a notice on update of Hatena blog.

# requirements
python3.

modules:
* beautifulsoup4
* requests
* requests_oauthlib

# usage

```
python3 hatena_notice.py
```

# configure
please replace your own value in hatena_auth.py and twitter_tokens.py

# reference

* [はてなblog AtomPub](http://developer.hatena.ne.jp/ja/documents/blog/apis/atom)
* [Twitter Developer Documentation](https://dev.twitter.com/docs)

# tests

```
python3 -m unittest tests/test_hatena_notice.py
```
