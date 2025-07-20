+++
Tags = ["tech"]
Description = " git credentialにgit-credential-gnome-keyringを使うのは推奨されていない。なぜならlibgnome-keyringがdeprecatedのため。実際ubuntu20.04ではgit-credenti"
date = "2021-04-14T11:22:00+09:00"
title = "git-credential-gnome-keyringを捨てよ、git-credential-libsecretと旅に出よう"
url = "/posts/2021/ditch-gnome-keyring-use-libsecret/"
author = "ompugao"
archive = ["2021"]
draft = false
+++

<body>
<p>git credentialにgit-credential-gnome-keyringを使うのは推奨されていない。
なぜならlibgnome-keyringがdeprecatedのため。
実際ubuntu20.04ではgit-credential-gnome-keyringのビルドに必要なlibgnome-keyring-devなるpackageは存在しない、
代わりにlibsecretに移行せよとある。
<a href="https://wiki.gnome.org/Initiatives/GnomeGoals/LibsecretMigration">Initiatives/GnomeGoals/LibsecretMigration - GNOME Wiki!</a></p>

<p>ということで以下ubuntu20.04での設定方法。</p>

<pre class="code lang-sh" data-lang="sh" data-unlink> sudo apt install libsecret-1-dev
cd /usr/share/doc/git/contrib/credential/libsecret
sudo make 
git config --global credential.helper /usr/share/doc/git/contrib/credential/libsecret/git-credential-libsecret
 </pre>


<p>おわり。</p>
</body>
