+++
Categories = ["tech"]
Description = " vimでscrapboxっぽいフォーマットでメモをとりたくて、以前pythonでlsp serverを実装していた:   ただ、やはりpythonで実装するとパースが遅すぎてだんだん使い辛くな"
Tags = []
date = "2025-01-16T20:10:00+09:00"
title = "Vimでscrapboxのようにメモを取りたいので、RustでLSPサーバを書いている"
url = "/posts/2025/writing-an-lsp-server-in-rust-to-take-notes-like-scrapbox-in-vim/"
author = "ompugao"
archive = ["2025"]
draft = false
+++

<body>
<p>vimでscrapboxっぽいフォーマットでメモをとりたくて、以前pythonでlsp serverを実装していた:</p>

[Language Serverの仕組みに乗っかればscrapboxっぽいwikiをvimで実現できる - おんぷの日記]({{% ref path="/posts/2022/build-scrapbox-like-wiki-in-vim-using-lsp" %}})

<p>ただ、やはりpythonで実装するとパースが遅すぎてだんだん使い辛くなっていた。
また、pythonのランタイムが必要というのも(特にwindowsでインストールする際に)イマイチだった。</p>

<p>そこで今はrustで少しずつ実装し直している:</p>

<p><iframe src="https://hatenablog-parts.com/embed?url=https%3A%2F%2Fgithub.com%2Fompugao%2Fpatto" title="GitHub - ompugao/patto: 🐙 A simple, language server-powered plain-text format for quick note-taking, outlining, and task management." class="embed-card embed-webcard" scrolling="no" frameborder="0" style="display: block; width: 100%; height: 155px; max-width: 500px; margin: 10px 0px;" loading="lazy"></iframe><cite class="hatena-citation"><a href="https://github.com/ompugao/patto">github.com</a></cite></p>

{{< figure src="/images/2025/01/20250116200432.gif" title="デモ" >}}

<p>rustのstrがutf-8なのでほとんどなにも考えなくていいのが非常に楽。
crateもたくさんあるし速度も速いし言うことなし。rust最高!</p>

<p>今回の再実装にあたり、Todo管理するための記法を取り入れた。
すでに普段使いlしていて、シンプルながら結構いい感じになっている。</p>

{{< figure src="/images/2025/01/20250116201454.gif" title="タスク管理">}}

<p>Live previewがまだなかったり、markdownへのエクスポートの作りが甘かったりとまだまだ作りこめていないけれど、少しずつ進めていくつもり。</p>

<p>ただ、チャットツールやAIへの入力のデファクトスタンダードがmarkdownとなっている現状、どこまで自分を貫けるかのチキンレースとなっており、悩んでないと言えば嘘になる…</p>
</body>
