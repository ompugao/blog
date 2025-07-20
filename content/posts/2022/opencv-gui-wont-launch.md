+++
Tags = ["tech"]
Description = " pythonでopencvを使っていると以下のエラーでGUIが使えなかった。適当にググるとcondaを使え、などと書いてある。condaは使いたくない。   error: (-2:Unspecified error) The functi"
date = "2022-05-14T18:04:00+09:00"
title = "opencvのGUIが起動できない"
url = "/posts/2022/opencv-gui-wont-launch/"
author = "ompugao"
archive = ["2022"]
draft = false
+++

<body>
<p>pythonでopencvを使っていると以下のエラーでGUIが使えなかった。
適当にググるとcondaを使え、などと書いてある。condaは使いたくない。</p>

<blockquote><p>error: (-2:Unspecified error) The function is not implemented. Rebuild the library with Windows, GTK+ 2.x or Carbon support. If you are on Ubuntu or Debian, install libgtk2.0-dev and pkg-config, then re-run cmake or configure script in function 'cvNamedWindow'</p></blockquote>

<p>以下で解決。</p>

<pre class="code lang-python" data-lang="python" data-unlink> # opencv-pythonやopencv-python-headlessとversionを揃える
pip3 install opencv-contrib-python==$(pip3 list 2&gt;&amp;1|grep opencv-python|head -n1|awk '{print $2}')
 </pre>

</body>
