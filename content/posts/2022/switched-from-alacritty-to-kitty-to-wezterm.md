+++
Categories = ["tech"]
Description = " サーバにsshしてdockerで開発する時間が増え、tmuxで二つpaneをつくって一つはdocker exec -it docker_image /bin/bashしてmakeしたりipythonを起動したりし、もう一つはvimで編集と"
Tags = []
date = "2022-10-18T15:56:00+09:00"
title = "alacrittyからkittyを経由してweztermに移行した"
url = "/posts/2022/switched-from-alacritty-to-kitty-to-wezterm/"
author = "ompugao"
archive = ["2022"]
draft = false
+++

<body>
<p>サーバにsshしてdockerで開発する時間が増え、tmuxで二つpaneをつくって一つは<code>docker exec -it docker_image /bin/bash</code>してmakeしたりipythonを起動したりし、もう一つはvimで編集というスタイルで開発をしていた。
そこで不便に思っていたのが、サーバのvimからクライアントからclipboardにコピーできないという点だった。
vimからコードの一部をコピーして、ipythonに貼り付けて実行、というのがスムーズにできず不満だった。</p>

<p>長い間<a href="https://github.com/lemonade-command/lemonade">lemonade</a>や<a href="https://github.com/wincent/clipper">clipper</a>を使っていたけれど、port forwardingせずにsshしている時に繋ぎ直すのが面倒だった。
またtailscale sshが現状port forwardingできない
<a href="#f-1653248f" name="fn-1653248f" title="Does port forwarding work with tailscale ssh? - Tailscale About articles (troubleshooting, info) - Tailscale ">*1</a>。
vscode remote developmentに浮気したりもしたけど、やっぱり慣れたvimがよい。
vimで:terminalするのもよいが、普段bashでctrl-wを使って単語消去しているので、ctrl-wの挙動がvim内外で変わるのが好みではない。vimがたまにクラッシュして内部で起動したbashを持っていくこともあってあまり常用していない。</p>

<p>ターミナルエミュレータって文字列を通信しあってるんだから、同じようにターミナルエミュレータの方で情報を通信してクリップボードを読み書きしてくれればいいじゃん、と思ってググってみると、kittyにそういう機能があるらしい(<a href="https://sw.kovidgoyal.net/kitty/kittens/clipboard/">clipboard - kitty</a>)ということでkittyを一通りセットアップし、
vimrcに以下を追記した。
kittyコマンドは<code>kitty +kitten ssh server</code>とすると自動的にインストールされる(要python)。</p>

<pre class="code lang-vim" data-lang="vim" data-unlink> if executable('kitty')
  nnoremap &lt;leader&gt;Y :call system('kitty +kitten clipboard', @0)&lt;CR&gt;
  vnoremap &lt;leader&gt;Y :call system('kitty +kitten clipboard', @0)&lt;CR&gt;
else
  " clipper https://github.com/wincent/clipper
  nnoremap &lt;leader&gt;Y :call system('nc -N localhost 8377', @0)&lt;CR&gt;
  vnoremap &lt;leader&gt;Y :call system('nc -N localhost 8377', @0)&lt;CR&gt;
endif
 </pre>


<p>ﾌｰこれでコピペができる快適~と思って使っていると、一つkittyのバグに遭遇してしまった。
kittyでvimを起動して日本語を使っていると、確定せずに次の単語を入力した際にpreeditがうまく描画されてくれない。</p>

<p><a href="https://github.com/kovidgoyal/kitty/issues/3330#issuecomment-1273590741">Japanese input bug? · Issue #3330 · kovidgoyal/kitty</a></p>

<p>実装もちょっと見た感じだとrace conditionが絡むめんどくさいバグっぽくて修正は諦めた。</p>

<p>そもそもclipboard情報の送信ってどうやって実現してるんだろう、と思って調べてみると、
ANSI OSC sequenceというプロトコル(?)があって、若干の方言はあるもののOSC52に対応しているものであればうまくクリップボードを制御できるらしい。
で、vim plugin (<a href="https://github.com/ojroques/vim-oscyank">ojroques/vim-oscyank: A Vim plugin to copy text through SSH with OSC52</a>) もある.</p>

<p>じゃあと思ってvim-jpで最近話題のweztermを使い始めた。
ちゃんとIMEも動作し、GPUも使ってくれ、拡張性が異常に高く、ドキュメンテーションも個人開発なのに凄まじい充実度を見せる <a href="#f-9b1f9798" name="fn-9b1f9798" title="開発者の負担が心配">*2</a>。
クリップボードも制御できる<a href="#f-dc58a6d8" name="fn-dc58a6d8" title=" weztermではセキュリティの問題でclipboardへのwriteはできるがreadはできない。kittyではreadもできるように設定できる。理屈はわかるけれど、そんなやばいサーバにsshしてる時点でもうダメだと思うんだが…[https://github.com/wez/wezterm/issues/2050:title] ">*3</a>。
フォントも<code>font_with_fallback</code>で複数自由に設定できる。
alacrittyでもよかったけれど、タブがやっぱり欲しかったのでweztermの方がよい。</p>

<p>当分weztermで過ごしてみようと思う。</p>

<p>追記:
ちょっとwezterm描画が遅くない？</p>
<div class="footnote">
<p class="footnote"><a href="#fn-1653248f" name="f-1653248f" class="footnote-number">*1</a><span class="footnote-delimiter">:</span><span class="footnote-text"><a href="https://forum.tailscale.com/t/does-port-forwarding-work-with-tailscale-ssh/2664">Does port forwarding work with tailscale ssh? - Tailscale About articles (troubleshooting, info) - Tailscale</a> </span></p>
<p class="footnote"><a href="#fn-9b1f9798" name="f-9b1f9798" class="footnote-number">*2</a><span class="footnote-delimiter">:</span><span class="footnote-text">開発者の負担が心配</span></p>
<p class="footnote"><a href="#fn-dc58a6d8" name="f-dc58a6d8" class="footnote-number">*3</a><span class="footnote-delimiter">:</span><span class="footnote-text"> weztermではセキュリティの問題でclipboardへのwriteはできるがreadはできない。kittyではreadもできるように設定できる。理屈はわかるけれど、そんなやばいサーバにsshしてる時点でもうダメだと思うんだが…<a href="https://github.com/wez/wezterm/issues/2050">Support OSC 52 clipboard querying (opt-in) · Issue #2050 · wez/wezterm · GitHub</a> </span></p>
</div>
</body>
