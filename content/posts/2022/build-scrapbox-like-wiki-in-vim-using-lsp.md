+++
Tags = ["tech"]
Description = " scrapboxみたいなwikiを好きなエディタ(vim)で編集したい。そこでLanguage Serverとして作った。  github.com  こんな感じ(ちょっと長めの動画。2倍速でどうぞ):    syntax  scrapbo"
date = "2022-11-26T00:00:00+09:00"
title = "Language Serverの仕組みに乗っかればscrapboxっぽいwikiをvimで実現できる"
url = "/posts/2022/build-scrapbox-like-wiki-in-vim-using-lsp/"
author = "ompugao"
archive = ["2022"]
draft = false
+++

<body>
<p>scrapboxみたいなwikiを好きなエディタ(vim)で編集したい。
そこでLanguage Serverとして作った。</p>

<p><iframe src="https://hatenablog-parts.com/embed?url=https%3A%2F%2Fgithub.com%2Fompugao%2Fmarkshift" title="GitHub - ompugao/markshift: Yet antoher indentation-based markup languange with language server/vim plugin" class="embed-card embed-webcard" scrolling="no" frameborder="0" style="display: block; width: 100%; height: 155px; max-width: 500px; margin: 10px 0px;" loading="lazy"></iframe><cite class="hatena-citation"><a href="https://github.com/ompugao/markshift">github.com</a></cite></p>

<p>こんな感じ(ちょっと長めの動画。2倍速でどうぞ):</p>

{{< youtube dk67x74Z7cs >}}

<h2 id="syntax">syntax</h2>

<p>scrapboxとpythonに大いに影響を受けている。
全ての文章が箇条書きで、タブ文字で右にシフトして入れ子的にリストをつくっていく。</p>

<pre class="code" data-lang="" data-unlink> 地の文。
改行は改行として扱う。
    タブ文字でインデントするとリストができる
        ネストしてもよい
    2こ目の要素
    [@quote]
        引用するときはこんな風に。
        一段インデントする。


装飾:
    [* 太字]はこう。
    [/ イタリック]はこう。
    [*/ 太字イタリック]はこう。

リンク:
    [wiki内リンク]
    [https://google.com google]
    [google https://google.com] タイトルとURLはどっちが先でも可。
    [@img https://via.placeholder.com/50 width=100 height=100] 画像はこう。
    [@img https://via.placeholder.com/50 "altテキストもいれていいよ"] altテキストとurlの順番も入れ替え可。


コードハイライトはhighlight.jsがやってくれる
    [@code python]
        import numpy as np
        print(np.sum(10))
    [` インラインコードはこう `]

数式はkatexにお任せ
    [@math]
        O(n^2)\\
        sum_{i=0}^{10}{i} = 55
    インライン数式はこう: [$ O(n log(n)) $]

テーブルもタブで区切ってね
    [@table]
        hoge    fuga
        piyo    asdf </pre>


{{< figure src="/images/2022/11/20221125162941.png" title="preview画像。なぜか画像が荒い">}}

<h2 id="実装">実装</h2>

<p>pythonに慣れてるのでpythonで。
pyinstallerにかければ実行ファイルも簡単にできる。
パースはgrammarを定義すれば<a href="https://github.com/lark-parser/lark">lark</a>がよしなにやってくれる。
lspについては、最近はべんりなものでgeneric language serverなるものがあり、
ベースの実装にちょっと書き足すだけでLanguage Serverになる。
<iframe src="https://hatenablog-parts.com/embed?url=https%3A%2F%2Fgithub.com%2Fopenlawlibrary%2Fpygls" title="GitHub - openlawlibrary/pygls: A pythonic generic language server" class="embed-card embed-webcard" scrolling="no" frameborder="0" style="display: block; width: 100%; height: 155px; max-width: 500px; margin: 10px 0px;" loading="lazy"></iframe><cite class="hatena-citation"><a href="https://github.com/openlawlibrary/pygls">github.com</a></cite></p>

<p>僕はそこにrendererもくっつけた。
なぜならrendererのwikiリンクをクリックしたらエディタ側もそのテキストを表示してほしいし、
それをするには双方向の通信が必要で、lspの仕組みにのっかるのが楽だったから。
lspにのっかっておけば他のエディタでも使える。
completionもdiagnosticsも簡単に出せる。</p>

<p>無論Zettelkastenに対応した。Language Serverは起動するとフォルダ内のファイルをスキャンしてグラフを作る。
<code>[</code>を入力するとグラフ内のページが補完される。
プレビューアの下部にはバックリンクが表示される。
これが欲しかった。</p>

<p>動画には入れてないけれど、zoteroのデータベースを指定するとzoteroのアイテム補完もできるようにした。べんり。</p>

<h2 id="なんでmarkdownじゃないの">なんでmarkdownじゃないの</h2>

<p>markdownが好きじゃないから。flavorやextensionによって挙動が異なるせいで、</p>

<ul>
<li>改行は改行と認識されるのか？</li>
<li>インデントしたときcode blockもインデントも揃えないといけないのか？</li>
<li>quote内の改行は改行として扱われるのか？</li>
<li>mathの記号はどれか？</li>
<li>リストの前に改行は必要か？</li>
</ul>


<p>などと書いてる最中に気になることが多すぎて、何を書こうとしていたのかわからなくなって、書く気力が削がれてしまう。
二つ目のcode blockが特に嫌いで、例えば</p>

<pre class="code lang-markdown" data-lang="markdown" data-unlink> - 箇条書きの中でコードスニペットを書こうとする
    - こんなふうに:
    - ```python
      def fn(arg):
          print(arg)
      print(fn('asdf'))
      ```
    - 箇条書きの続き
 </pre>


<p>のように書こうとすると、3行目のコード片のところでインデントを揃えるためには"- "の二文字のせいでたくさんスペースを手で打ちまくる必要がある。
そもそも箇条書き中のcodeはmarkedjs等では書けるのにobsidianでは書けない。
ポータブルなマークアップ言語とはなんだったのか。
{{< figure src="/images/2022/11/20221116121107.png" title="obsidianでのコードスニペットの認識のされ方の画像。箇条書きの中ではcodeとして認識されなくなる。" >}}

<p>逆に自作しちゃえば実装==仕様になる。ﾌﾌﾝ<a href="#f-ee40a67d" name="fn-ee40a67d" title="ﾌﾌﾝではない。現状specはｶﾞﾊﾞｶﾞﾊﾞである">*1</a>。</p>

<h2 id="そんなわけわからん言語にロックインされる方がよくないのでは">そんなわけわからん言語にロックインされる方がよくないのでは</h2>

<p>現状markdownへのexportが可能。
文法の機能的にはmarkdownやその他言語の下位互換なので、ちょっとrendererを書けば簡単に移行できるのでヨシ。</p>

<h2 id="これから">これから</h2>

<p>とりあえず常用するには困らない分だけ実装したところで、lspの実装できてないところはたくさんある。
めんどくさくなってvim plugin側で書いてしまったところもある(<s>DocumentLinkとか</s>←対応した)。
<s>vscode extensionの実装も途中で止まってしまっている。</s>←とりあえず<a href="https://github.com/ompugao/markshift/tree/master/src/markshift/langserver">動いた</a>。
ちょっとずつ進める予定→<a href="https://github.com/ompugao/markshift/issues">issues</a>。</p>
<div class="footnote">
<p class="footnote"><a href="#fn-ee40a67d" name="f-ee40a67d" class="footnote-number">*1</a><span class="footnote-delimiter">:</span><span class="footnote-text">ﾌﾌﾝではない。現状specはｶﾞﾊﾞｶﾞﾊﾞである</span></p>
</div>
</body>
