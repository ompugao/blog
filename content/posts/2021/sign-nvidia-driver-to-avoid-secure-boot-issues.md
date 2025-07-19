+++
Categories = ["tech"]
Description = " 目下windows10とubuntu20.04のデュアルブートのマシンを主に使用している。windows 11にupgradeするのにsecure boot関係でコケたら嫌だなぁと思って、キチンとsecure bootを有効にした。以下は"
Tags = []
date = "2021-11-14T15:58:00+09:00"
title = "kernel module(nvidia driver)に署名してsecure bootで困らないようにする"
url = "/posts/2021/sign-nvidia-driver-to-avoid-secure-boot-issues/"
author = "ompugao"
archive = ["2021"]
draft = false
+++

<body>
<p>目下windows10とubuntu20.04のデュアルブートのマシンを主に使用している。
windows 11にupgradeするのにsecure boot関係でコケたら嫌だなぁと思って、キチンとsecure bootを有効にした。
以下はメモ書き。</p>

<h5>仕組み</h5>

<p>ubuntuのsecure bootの対応・仕組みはこちらに詳しい。</p>

<ul>
<li><a href="https://kledgeb.blogspot.com/2020/06/ubuntu-2004-74-ubuntuuefi.html">Ubuntu 20.04 その74 - UbuntuとUEFIセキュアブート - kledgeb</a></li>
<li><a href="https://wiki.ubuntu.com/UEFI/SecureBoot">UEFI/SecureBoot - Ubuntu Wiki</a></li>
<li><a href="https://wiki.ubuntu.com/UEFI/SecureBoot/Signing">UEFI/SecureBoot/Signing - Ubuntu Wiki</a></li>
</ul>


<p>ubuntuがbootするときには</p>

<ul>
<li>shim(Microsoftにより署名済み)</li>
<li>grub</li>
<li>if 鍵の管理するように言われている

<ul>
<li>MokManager</li>
</ul>
</li>
<li>else

<ul>
<li>OS起動</li>
</ul>
</li>
</ul>


<p>という感じで起動するらしい。MOK: Machine-Owner Keyとのこと。
普通はMicrosoftに署名されたものしかブート時に読みこめないが、MokManagerを起動してそこに自分で作ったMOKを登録してあげると、
kernel moduleを事前にそのMOKで署名しておくことで読み込めるようになる、という風に理解した。</p>

<h5>手順</h5>

<p>secure bootを有効にして起動したubuntu20.04でnvidia driverを入れると、
ncursesなUIでMOKをshimに登録するためのパスワードを要求してきて、そこで勝手にMOKを生成してくれる。
dkmsによりビルドされたnvidia driverもその生成されたMOKにより署名つきになる。
もしそのMOK生成を手動で行うには</p>

<blockquote><p>Use the following command to enroll an existing key into shim:<br>
   $ sudo update-secureboot-policy --enroll-key<br>
If no MOK exists, the script will exit with a message to that effect. If the key is already enrolled, the script will exit, doing nothing. If the key exists but it not shown to be enrolled, the user will be prompted for a password to use after reboot, so that the key can be enrolled.<br>
One can generate a new MOK using the following command:<br>
  $ sudo update-secureboot-policy --new-key<br></p></blockquote>

<p>のようなコマンドで鍵が生成される。
出力先は /var/lib/shim-signed/mok/MOK.priv (秘密鍵) と /var/lib/shim-signed/mok/MOK.der (証明書、公開鍵)。</p>

<p>この公開鍵をshimに登録するようOSからお願いする。
先程のパスワードを入力する。</p>

<pre class="code bash" data-lang="bash" data-unlink> $ sudo mokutil --import /var/lib/shim-signed/mok/MOK.der
input password: xxxxx
input password again: xxxxx </pre>


<p>これで再起動すると</p>

<pre class="code" data-lang="" data-unlink> Perform MOK management

 Continue boot
  &lt;Enroll MOK&gt;
Enroll key from disk
Enroll hash from disk </pre>


<p>という画面が現れるので、 <enroll mok>を選択し</enroll></p>

<pre class="code" data-lang="" data-unlink> [Enroll MOK]
View Key 0
&lt;Continue&gt; </pre>


<p>でView Key 0で証明書の内容を確認したら<continue>。
あとは先程のpasswordをいれて再起動する。
nvidia-smiがちゃんとdriverを認識して色々出力してくれればOK.</continue></p>

<p>他のdkmsなモジュールを自動でsignしてくれるスクリプトも見つけたものの、なぜかすでに勝手に登録されている。<s>要確認。</s>
先のURL(<a href="https://kledgeb.blogspot.com/2020/06/ubuntu-2004-74-ubuntuuefi.html">Ubuntu 20.04 その74 - UbuntuとUEFIセキュアブート - kledgeb</a>)によるとdkmsが勝手に署名してくれるらしい。便利だなぁ。</p>

<ul>
<li><a href="https://gist.github.com/sbueringer/bd8cec239c44d66967cf307d808f10c4">Make DKMS sign kernel modules on installation, with full script support and somewhat distro independent · GitHub</a></li>
<li><a href="https://gist.github.com/lijikun/22be09ec9b178e745758a29c7a147cc9">Automatic Signing of DKMS-Generated Kernel Modules for Secure Boot · GitHub</a></li>
</ul>


<p>ちなみにsecurebootではhibernationやsuspendはサポートされてないらしい。この点は不便だな。
<iframe src="https://hatenablog-parts.com/embed?url=https%3A%2F%2Funix.stackexchange.com%2Fquestions%2F598786%2Flockdown-systemd-logind-hibernation-is-restricted-see-man-kernel-lockdown-7%2F624739%23624739" title="Lockdown: systemd-logind: hibernation is restricted; see man kernel_lockdown.7" class="embed-card embed-webcard" scrolling="no" frameborder="0" style="display: block; width: 100%; height: 155px; max-width: 500px; margin: 10px 0px;"></iframe><cite class="hatena-citation"><a href="https://unix.stackexchange.com/questions/598786/lockdown-systemd-logind-hibernation-is-restricted-see-man-kernel-lockdown-7/624739#624739">unix.stackexchange.com</a></cite></p>
</body>
