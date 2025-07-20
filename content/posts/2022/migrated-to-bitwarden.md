+++
Tags = ["tech"]
Description = " 以下の理由でbitwardenを使い始めた   androidのchromeで広告が鬱陶しすぎるので、brave browserを使いたい  googleのパスワードマネージャーとkeepassで二重管理するのをやめたい   chromi"
date = "2022-10-10T15:07:00+09:00"
title = "bitwardenに移行した"
url = "/posts/2022/migrated-to-bitwarden/"
author = "ompugao"
archive = ["2022"]
draft = false
+++

<body>
<p>以下の理由でbitwardenを使い始めた</p>

<ol>
<li>
androidのchromeで広告が鬱陶しすぎるので、brave browserを使いたい</li>
<li>
googleのパスワードマネージャーとkeepassで二重管理するのをやめたい</li>
</ol>


<p>chromiumのパスワードマネージャーがsecure note等の付加情報を保存させてくれるのが一番楽で安心なんだけど…。
bitwardenのimporterだとめちゃくちゃ重複が発生するので自前で重複するパスワードを一つのentryにまとめてからimportする。</p>

<ol>
<li>
googleからパスワードをcsvとしてexportする</li>
<li>以下のスクリプトでbitwarden形式のcsvに変換する</li>
<li>bitwardenに生成されたcsvファイルをインポートする</li>
<li>keepassの方はkeepassxcでcsvないしxmlに掃き出してからbitwardenにimport…せずに、重複やsecure notesがあるので自分でちまちまと入れていく(大変だった...)</li>
</ol>


<p><script src="https://gist.github.com/e62d14098b2ba567c0b39e339faded4c.js"> </script></p>

<p><a href="https://gist.github.com/e62d14098b2ba567c0b39e339faded4c">password duplicates merger for conversion of passwords fr…</a></p>

<p>時間はかかったがやっとすっきりした。</p>
</body>
