+++
Tags = ["tech"]
Description = " 論文を書くためのLaTeX環境は、vscode+latex workshop+dockerで整備している。いつものようにwindowsでwsl2をbackendにするdockerを起動しようとしたら、なぜか起動しない。なんでやと思ってws"
date = "2022-02-19T00:47:00+09:00"
title = "wslが起動しなくなった"
url = "/posts/2022/wsl-wont-start/"
author = "ompugao"
archive = ["2022"]
draft = false
+++

<body>
<p>論文を書くためのLaTeX環境は、vscode+latex workshop+dockerで整備している。
いつものようにwindowsでwsl2をbackendにするdockerを起動しようとしたら、なぜか起動しない。
なんでやと思ってwsl2のdebianを起動しようとすると、
"The service has not been started."
とだけ表示され、起動しない。
serviceってなんぞ！とぷんすこしながらインターネットを彷徨った結果復旧したので記録しておく.</p>

<p>結論としては以下だった。
<iframe src="https://hatenablog-parts.com/embed?url=https%3A%2F%2Fgithub.com%2Fmicrosoft%2FWSL%2Fissues%2F6191%23issuecomment-727038515" title="Error installing Ubuntu and Debian - WslRegisterDistribution failed with error: 0x80070426 Error: 0x80070426 The service has not been started. · Issue #6191 · microsoft/WSL" class="embed-card embed-webcard" scrolling="no" frameborder="0" style="display: block; width: 100%; height: 155px; max-width: 500px; margin: 10px 0px;"></iframe><cite class="hatena-citation"><a href="https://github.com/microsoft/WSL/issues/6191#issuecomment-727038515">github.com</a></cite></p>

<p>DNS Client Serviceが無効にされているとだめらしい。
<a href="https://www.thewindowsclub.com/enable-the-dns-client-service-if-greyed-out#:~:text=System%20Configuration%20applet-,Open%20the%20Run%20dialog%20box%20using%20the%20Windows%20key%20%2B%20R,the%20left%20of%20the%20service.">How to enable the DNS Client Service if greyed out in Windows 10</a>に従って、
win+Rでregeditを起動、<code>HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\services\Dnscache</code>に移動して<code>Start</code>の値を3(マニュアル起動)にしてwindowsを再起動すると復活した。</p>
</body>
