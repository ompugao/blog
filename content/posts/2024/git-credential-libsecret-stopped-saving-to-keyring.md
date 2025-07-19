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

<p><a href="{{% ref path="/posts/2021/ditch-gnome-keyring-use-libsecret/\"%}}">Related post: git-credential-gnome-keyringを捨てよ、git-credential-libsecretと旅に出よう</a></p>

<p><code>~/.local/share/keyrings</code>ディレクトリが消えていたせいっぽい。</p>

<pre class="code lang-sh" data-lang="sh" data-unlink> mkdir -p ~/.local/share/keyrings
 </pre>


<p>で解決。</p>
</body>
