+++
Tags = ["research", "singapore"]
Description = " 昨日期末試験がやっとこさ終わった。いい機会なので取った講義をまとめておく。どこにも需要はないだろうけど…  2020-21 Sem. 1  コロナの関係で渡航できなかったため、完全オンラインの講義のみ受講*1。  DM6190 Speci"
date = "2021-05-06T11:15:00+09:00"
title = "NTUの博士課程前半で受講した講義のまとめ"
url = "/posts/2021/summary-of-courses-taken-in-the-first-half-of-ntu-phd/"
author = "ompugao"
archive = ["2021"]
draft = false
+++

<body>
<p>昨日期末試験がやっとこさ終わった。
いい機会なので取った講義をまとめておく。
どこにも需要はないだろうけど…</p>

<h3 id="2020-21-Sem-1">2020-21 Sem. 1</h3>

<p>コロナの関係で渡航できなかったため、完全オンラインの講義のみ受講<a href="#f-a2dc3586" name="fn-a2dc3586" title="完全オンラインである、とシラバスに書いてあるわけではないので、受講可能な講義を探すのが大変だった…">*1</a>。</p>

<h4 id="DM6190-Special-Topic-Image-Segmentation">DM6190 Special Topic: Image Segmentation</h4>

<p>画像処理の基礎からState-of-the-artのImage Segmentationまで一気に駆け抜ける授業。
自分でDNNベースのモデルをkaggleのデータセットに適用してスコアを上げてみる、というプログラミング課題と、画像処理の論文について発表する課題があった。
DNNを独学しようとすると、著者がどういう意図を持ってモデルを組み立てているのか全然わからないけれど、その辺りのニュアンスを先生から聞けるのは非常によかった。
講義で触れられるDeepLabv3等の超有名モデルはある程度おきもちが感じられるのだが、学生が課題で紹介してくれたNIPS等に発表された論文はまるでおきもちが理解できないので、この界隈は関わりたくないなという強い決意を新たにした。</p>

<p>自分の発表課題では、ちょうど半年前に発表されてシンプルで面白いなと思ったNeRFを紹介したのだが、その後NeRFベースの研究が爆発的に増え、自分結構見る目あるんちゃうかと勝手に思っている。</p>

<h4 id="CE7491-Special-Advanced-Topic-Digital-Image-Processing">CE7491 Special Advanced Topic: Digital Image Processing</h4>

<p>こちらも画像処理の講義。前半は古典的な画像処理について、後半は画像・動画復元、セグメンテーション、Image to Image Translationについて講義。
前半は既知の内容が多く、後半はDM6190同様ニュアンスや意図を聞けてよかった。</p>

<h3 id="2020-21-Sem-2">2020-21 Sem. 2</h3>

<h4 id="CE7426-Advanced-Topics-of-Convex-Optimization">CE7426 Advanced Topics of Convex Optimization</h4>

<p>凸最適化についてStephen P. Boyd先生の教科書の内容をベースに教えてくれる授業。
わからないことがわからない、みたいな質問にも根気強く説明していただけたので非常によかった。
<iframe src="https://hatenablog-parts.com/embed?url=https%3A%2F%2Fweb.stanford.edu%2F~boyd%2Fcvxbook%2F" title="Convex Optimization – Boyd and Vandenberghe" class="embed-card embed-webcard" scrolling="no" frameborder="0" style="display: block; width: 100%; height: 155px; max-width: 500px; margin: 10px 0px;" loading="lazy"></iframe><cite class="hatena-citation"><a href="https://web.stanford.edu/~boyd/cvxbook/">web.stanford.edu</a></cite>
Boyd先生も授業動画を公開してくれているので、それを見てさくっと理解できればいいのだけれど、さくっと理解できない話は動画を見るだけではわかったかどうかもわからない、みたいになりがち。
全然わからない話は、毎週強制的に講義を受け、頑張って理解しようと悶々とすることが大事で、そういう努力は独学ではやっぱり難しい。
凸最適化は幾何的な解釈ができるので想像しやすくて、講義と試験が終わった今となっては、概念としては簡単じゃん、と思うのだけれど、わかるまではしんどかった…
今までは双対って結局なんやねん、と思っていたけれど、ようやく血肉になった気がする。</p>

<h5 id="CE7453-Numerical-Algorithms">CE7453: Numerical Algorithms</h5>

<p>Tim Sauer先生の数値解析本をベースにした講義で、方程式の求解、微積分、補間、固有値・特異値分解、などなどに触れる。
パッと見簡単そうだな、と思って受講したのだけれど、自身の理解が浅いことを痛感した。
B-Splineのknot vectorをいじると曲線がどうなるか、という直感が得られなくて厳しかった。
内容自体はそんなに難しいわけではないけど、体調が悪かったために期末試験で講義内容を覚えていなくてだいぶやらかした。</p>

<p><iframe src="https://hatenablog-parts.com/embed?url=https%3A%2F%2Fwww.pearson.com%2Fus%2Fhigher-education%2Fprogram%2FSauer-Numerical-Analysis-3rd-Edition%2FPGM1735484.html" title="Numerical Analysis" class="embed-card embed-webcard" scrolling="no" frameborder="0" style="display: block; width: 100%; height: 155px; max-width: 500px; margin: 10px 0px;" loading="lazy"></iframe><cite class="hatena-citation"><a href="https://www.pearson.com/us/higher-education/program/Sauer-Numerical-Analysis-3rd-Edition/PGM1735484.html">www.pearson.com</a></cite></p>

<h5 id="EE6221-Robotics-and-Intelligent-Sensors">EE6221: Robotics and Intelligent Sensors</h5>

<p>これはロボティクスの基礎の授業。単位を取りにいっただけなのでこれといって目新しさはなかった。
復習としては非常によかったし、期末試験でもないとちゃんと覚えるという行為をしないので良い機会だった。</p>

<p>以上、講義を受けて単位をとるのは大変だけど楽しいね。</p>
<div class="footnote">
<p class="footnote"><a href="#fn-a2dc3586" name="f-a2dc3586" class="footnote-number">*1</a><span class="footnote-delimiter">:</span><span class="footnote-text">完全オンラインである、とシラバスに書いてあるわけではないので、受講可能な講義を探すのが大変だった…</span></p>
</div>
</body>
