+++
Tags = ["tech"]
Description = " massifはvalgrindに同梱の、プログラムがメモリヒープをどれくらい使っているかをプロファイリングしてくれるもの（情報が無）。  インストールをして：  sudo apt install valgrind massif-visua"
date = "2021-03-13T21:07:00+09:00"
title = "massifヒーププロファイラ"
url = "/posts/2021/massif-heap-profiler/"
author = "ompugao"
archive = ["2021"]
draft = false
+++

<body>
<p>massifはvalgrindに同梱の、プログラムがメモリヒープをどれくらい使っているかをプロファイリングしてくれるもの（情報が無）。</p>

<p>インストールをして：</p>

<pre class="code lang-sh" data-lang="sh" data-unlink> sudo apt install valgrind massif-visualizer
 </pre>


<p>実行：</p>

<pre class="code lang-sh" data-lang="sh" data-unlink> valgrind --tool=massif --time-unit=B --stacks=yes your_program program_args
 </pre>


<p>するとmassif.out.XXXX(Xは数字)というファイルができるので、これをmassif-visualizerに食わせる：</p>

<pre class="code lang-sh" data-lang="sh" data-unlink> massif-visualizer massif.out.4543
 </pre>


<p>すると以下のリンクのようにどの関数がどれくらいヒープを使っているかが可視化される。超べんり。
<iframe src="https://hatenablog-parts.com/embed?url=https%3A%2F%2Fapps.kde.org%2Fen%2Fmassif-visualizer" title="Massif-Visualizer" class="embed-card embed-webcard" scrolling="no" frameborder="0" style="display: block; width: 100%; height: 155px; max-width: 500px; margin: 10px 0px;"></iframe><cite class="hatena-citation"><a href="https://apps.kde.org/en/massif-visualizer">apps.kde.org</a></cite></p>

<p>こんな便利なプログラムがフリーで使えるのは本当にありがたい。</p>

<p><iframe src="https://hatenablog-parts.com/embed?url=https%3A%2F%2Fwww.valgrind.org%2Fdocs%2Fmanual%2Fms-manual.html" title="Valgrind" class="embed-card embed-webcard" scrolling="no" frameborder="0" style="display: block; width: 100%; height: 155px; max-width: 500px; margin: 10px 0px;"></iframe><cite class="hatena-citation"><a href="https://www.valgrind.org/docs/manual/ms-manual.html">www.valgrind.org</a></cite></p>
</body>
