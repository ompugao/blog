+++
Categories = ["tech"]
Description = " 購入した新しいPC(Asus ROG Zephyrus G14 GA401)が届いたのでセットアップした。ompugao.hatenablog.com  購入後に新モデルのリリース時期が発表されて(4月末発売開始)少しぐんにょりしたものの"
Tags = []
date = "2021-03-11T16:21:00+09:00"
title = "Asus ROG Zephyrus G14 GA401のセットアップ"
url = "/posts/2021/setting-up-the-asus-rog-zephyrus-g14-ga401/"
author = "ompugao"
archive = ["2021"]
draft = false
+++

<body>
<p>購入した新しいPC(Asus ROG Zephyrus G14 GA401)が届いたのでセットアップした。
<iframe src="https://hatenablog-parts.com/embed?url=https%3A%2F%2Fompugao.hatenablog.com%2Fentry%2F2021%2F02%2F28%2F011049" title="新しいパソコンをポチった - おんぷの日記" class="embed-card embed-blogcard" scrolling="no" frameborder="0" style="display: block; width: 100%; height: 190px; max-width: 500px; margin: 10px 0px;"></iframe><cite class="hatena-citation"><a href="https://ompugao.hatenablog.com/entry/2021/02/28/011049">ompugao.hatenablog.com</a></cite></p>

<p>購入後に新モデルのリリース時期が発表されて(4月末発売開始)少しぐんにょりしたものの、ラップトップは新しすぎるとlinuxを入れるのに苦労するので、まぁよかろうと思い直した。
あーでもRTX20XXよりRTX30XXのがいいよなー（ﾌﾞﾂﾌﾞﾂ
<a href="https://jp.store.asus.com/store/asusjp/ja_JP/list/categoryID.5057114400">ASUS Store（エイスース ストア） - 【14インチ】ゲーミングノートパソコン一覧</a></p>

<p>リリースから1年もすると、ubuntuがout of boxで動くんだからありがたい。
今回初めてbtrfsを利用してファイルシステムのスナップショットが取れるようにした。</p>

<p>以下手順:</p>

<ul>
<li>ubuntu20.04のインストーラをダウンロードして、startup disk creatorでusbに入れる。</li>
<li>/をbtrfs、/bootをext4にしてインストールする。usb-ethernet変換器をつないでインストーラを起動しないとwifiのインターフェースを認識してくれなかった。</li>
<li>とりあえずetckeeperをいれる。</li>
</ul>


<pre class="code lang-sh" data-lang="sh" data-unlink> sudo apt install git etckeeper
 </pre>


<ul>
<li>以下を参考にsnapper用に設定する。ubuntuのinstallerは@ subvolumeを/、@home subvolumeを/homeにあてがってくれるので、適宜追加して@snapshotsや@var、@var/lib/dockerなどなどを設定してfstabで然るべき位置にマウントする。

<ul>
<li><a href="https://thinca.hatenablog.com/entry/2020/10/btrfs-memo">https://thinca.hatenablog.com/entry/2020/10/btrfs-memo</a></li>
<li><a href="https://wiki.archlinux.jp/index.php/Snapper">https://wiki.archlinux.jp/index.php/Snapper</a></li>
<li><a href="https://www.ncaq.net/2019/01/28/13/37/05/">https://www.ncaq.net/2019/01/28/13/37/05/</a></li>
<li>@から始まるsubvolumeってどう作るんだ？と思ったら以下がヒットした。 <a href="https://askubuntu.com/questions/331233/creating-btrfs-subvolume-like-or-home">https://askubuntu.com/questions/331233/creating-btrfs-subvolume-like-or-home</a>
</li>
</ul>
</li>
</ul>


<pre class="code lang-sh" data-lang="sh" data-unlink> sudo mkdir -p /mnt/btrfs_root
sudo mount UUID={{btrfsのfile system rootのuuid}} /mnt/btrfs_root/
cd /mnt/btrfs_root
sudo btrfs subvolume create @var
sudo btrfs subvolume create @var/lib/docker
sudo btrfs subvolume create @snapshots
echo "UUID={{btrfsのfile system rootのuuid}} /var/lib/docker           btrfs   defaults,subvol=@var/lib/docker 0       2" |sudo tee &gt;&gt; /etc/fstab
echo "UUID={{btrfsのfile system rootのuuid}} /var/lib/docker           btrfs   defaults,subvol=@var/lib/docker 0       2"|sudo tee &gt;&gt; /etc/fstab
echo "UUID={{btrfsのfile system rootのuuid}} /var/tmp           btrfs   defaults,subvol=@var/tmp 0       2"|sudo tee &gt;&gt; /etc/fstab
echo "UUID={{btrfsのfile system rootのuuid}} /var/log           btrfs   defaults,subvol=@var/log 0       2"|sudo tee &gt;&gt; /etc/fstab
echo "UUID={{btrfsのfile system rootのuuid}} /.snapshots           btrfs   defaults,subvol=@snapshots 0       2"|sudo tee &gt;&gt; /etc/fstab
sudo snapper create-config
 </pre>


<ul>
<li>ファンクションキーが効かないので以下の入れる

<ul>
<li><a href="https://gitlab.com/asus-linux/hid-asus-rog">https://gitlab.com/asus-linux/hid-asus-rog</a></li>
<li><a href="https://gitlab.com/asus-linux/asus-rog-nb-wmi">https://gitlab.com/asus-linux/asus-rog-nb-wmi</a></li>
<li>
<a href="https://gitlab.com/asus-linux/asus-nb-ctrl">https://gitlab.com/asus-linux/asus-nb-ctrl</a>

<ul>
<li>
asus-nb-ctrlはrustで実装されているのと、dkms.confがないことから、rustup.rsからrustを入れて自分でビルドしてインストールした。</li>
</ul>
</li>
</ul>
</li>
<li>あとはお好きなように。</li>
</ul>


<p>kernel 5.11を入れると上記asus-linuxの諸々が要らなくなるけれど、
<a href="https://wiki.ubuntu.com/Kernel/MainlineBuilds">Kernel/MainlineBuilds - Ubuntu Wiki</a>からインストールしたupstream kernelに
<a href="https://launchpad.net/~graphics-drivers/+archive/ubuntu/ppa">Proprietary GPU Drivers : “Graphics Drivers” team</a>の nvidia-driverを入れようとすると、5.9.?(わすれた), 5.10.22, 5.11.1, 5.11.5のどれを使ってもubuntuの起動が途中でハングするのでやめた。やはり公式こそが正義。</p>

<p>18万円くらいでこんなスペック(Ryzen9 4000, RTX2060 Max-Q, 16GB Memory, SSD 1TB, 1.7kg)のPCが買えるのはすごい。ありがたし。</p>
</body>
