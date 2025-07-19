+++
Categories = ["tech"]
Description = " git-credential-libsecretがkeyringに登録してくれなくなった。Authenticaiton Required: An application wants access to the keyring \"Defau"
Tags = []
date = "2024-08-26T10:47:00+09:00"
title = "git-credential-libsecretがkeyringに登録してくれなくなった"
url = "/posts/2024/git-credential-libsecret-stopped-saving-to-keyring/"
author = "ompugao"
archive = ["2024"]
draft = false
+++

<body>
<p>git-credential-libsecretがkeyringに登録してくれなくなった。
<code>Authenticaiton Required: An application wants access to the keyring "Default Keyring", but it is locked.</code>
というポップアップが毎回出てくる。</p>

<p><iframe src="https://hatenablog-parts.com/embed?url=https%3A%2F%2Fompugao.hatenablog.com%2Fentry%2F2021%2F04%2F14%2F112236" title="git-credential-gnome-keyringを捨てよ、git-credential-libsecretと旅に出よう - おんぷの日記" class="embed-card embed-blogcard" scrolling="no" frameborder="0" style="display: block; width: 100%; height: 190px; max-width: 500px; margin: 10px 0px;" loading="lazy"></iframe><cite class="hatena-citation"><a href="https://ompugao.hatenablog.com/entry/2021/04/14/112236">ompugao.hatenablog.com</a></cite></p>

<p><code>~/.local/share/keyrings</code>ディレクトリが消えていたせいっぽい。</p>

<pre class="code lang-sh" data-lang="sh" data-unlink> mkdir -p ~/.local/share/keyrings
 </pre>


<p>で解決。</p>
</body>
