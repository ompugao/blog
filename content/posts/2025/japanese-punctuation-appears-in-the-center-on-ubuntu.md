+++
Categories = ["tech"]
Description = " Ubuntu 24.04 にアップグレードしたから、句読点の位置が変だなぁとずっと思っていた：  https://github.com/canonical/Ubuntu-Sans-fonts/issues/117#issuecomment"
Tags = []
date = "2025-02-17T17:08:00+09:00"
title = "Ubuntuで日本語の句読点の位置が中心あたりに表示される"
url = "/posts/2025/japanese-punctuation-appears-in-the-center-on-ubuntu/"
author = "ompugao"
archive = ["2025"]
draft = false
+++

<body>
<p>Ubuntu 24.04 にアップグレードしたから、句読点の位置が変だなぁとずっと思っていた：</p>

{{< figure src="/images/2025/02/20250219141129.png" title="なんか変" >}}
<a href="https://github.com/canonical/Ubuntu-Sans-fonts/issues/117#issuecomment-2203047924">https://github.com/canonical/Ubuntu-Sans-fonts/issues/117#issuecomment-2203047924</a></p>

<p>直し方は、下記issueの通り、<code>/etc/fonts/local.conf</code>に以下の内容のファイルを置いて再起動すれば直る：</p>

<pre class="code lang-xml" data-lang="xml" data-unlink> &lt;?xml version="1.0"?&gt;
&lt;!DOCTYPE fontconfig SYSTEM "fonts.dtd"&gt;
&lt;fontconfig&gt;

  &lt;alias&gt;
    &lt;family&gt;sans-serif&lt;/family&gt;
    &lt;prefer&gt;
      &lt;family&gt;Noto Sans&lt;/family&gt;
      &lt;family&gt;Noto Sans CJK SC&lt;/family&gt;
      &lt;family&gt;Noto Sans CJK TC&lt;/family&gt;
      &lt;family&gt;Noto Sans CJK HK&lt;/family&gt;
      &lt;family&gt;Noto Sans CJK JP&lt;/family&gt;
      &lt;family&gt;Noto Sans CJK KR&lt;/family&gt;
    &lt;/prefer&gt;
  &lt;/alias&gt;
  &lt;alias&gt;
    &lt;family&gt;serif&lt;/family&gt;
    &lt;prefer&gt;
      &lt;family&gt;Noto Serif&lt;/family&gt;
      &lt;family&gt;Noto Serif CJK SC&lt;/family&gt;
      &lt;family&gt;Noto Serif CJK TC&lt;/family&gt;
      &lt;family&gt;Noto Serif CJK HK&lt;/family&gt;
      &lt;family&gt;Noto Serif CJK JP&lt;/family&gt;
      &lt;family&gt;Noto Serif CJK KR&lt;/family&gt;
    &lt;/prefer&gt;
  &lt;/alias&gt;

&lt;/fontconfig&gt;
 </pre>


<p><iframe src="https://hatenablog-parts.com/embed?url=https%3A%2F%2Fgithub.com%2Fcanonical%2FUbuntu-Sans-fonts%2Fissues%2F117%23issuecomment-2439368846" title="Problem with handling Chinese punctuation, such as enumeration comma(、) and full stop(。). · Issue #117 · canonical/Ubuntu-Sans-fonts" class="embed-card embed-webcard" scrolling="no" frameborder="0" style="display: block; width: 100%; height: 155px; max-width: 500px; margin: 10px 0px;" loading="lazy"></iframe><cite class="hatena-citation"><a href="https://github.com/canonical/Ubuntu-Sans-fonts/issues/117#issuecomment-2439368846">github.com</a></cite></p>

<p>以上。Linuxのこういうところが初心者に優しくないね…</p>
</body>
