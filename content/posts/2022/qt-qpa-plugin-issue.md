+++
Tags = ["tech"]
Description = " たまに発生するエラーの直し方のメモ。  どういう条件で発生するのかよく調べていないけれど、opencvとpyqt5(たぶん)を混ぜたときにplt.imshow()しようとしたりするとタイトルのエラーが出る。  こういう時はタイトルの\".."
date = "2022-01-20T17:35:00+09:00"
title = "qt.qpa.plugin"
url = "/posts/2022/qt-qpa-plugin-issue/"
author = "ompugao"
archive = ["2022"]
draft = false
+++

<body>
<p>たまに発生するエラーの直し方のメモ。</p>

<p>どういう条件で発生するのかよく調べていないけれど、
opencvとpyqt5(たぶん)を混ぜたときにplt.imshow()しようとしたりするとタイトルのエラーが出る。</p>

<p><s>こういう時はタイトルの"..."のパス(例えば"/usr/lib/python3.7/site-packages/cv2/qt/plugins")を消すと治る。</s>
訂正：以下で治った。
<a href="https://askubuntu.com/questions/308128/failed-to-load-platform-plugin-xcb-while-launching-qt5-app-on-linux-without/1069502#1069502">“Failed to load platform plugin ”xcb“ ” while launching qt5 app on linux without qt installed - Ask Ubuntu</a></p>

<pre class="code lang-sh" data-lang="sh" data-unlink> sudo apt-get install --reinstall libxcb-xinerama0
 </pre>


<p>ビルドされたqtのバージョンのmismatchか何かなのかな？</p>

<p>ref: <a href="https://github.com/wkentaro/labelme/issues/842">[BUG] qt.qpa.plugin: Could not load the Qt platform plugin "xcb" -- fixed · Issue #842 · wkentaro/labelme · GitHub</a></p>
</body>
