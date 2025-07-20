+++
Tags = ["research"]
Description = " 色々と試行錯誤した記憶が薄れてきているので、忘れないうちに書き留めておく。ここでのpytorch/libtorchのversionは1.8.1。推論にはlibtorchを使うものとする。  1. TorchScriptを使わない  pyt"
date = "2021-10-23T18:35:00+09:00"
title = "pytorch/libtorchの推論の高速化テク"
url = "/posts/2021/speed-up-pytorch-libtorch-inference/"
author = "ompugao"
archive = ["2021"]
draft = false
+++

<body>
<p>色々と試行錯誤した記憶が薄れてきているので、忘れないうちに書き留めておく。ここでのpytorch/libtorchのversionは1.8.1。
推論にはlibtorchを使うものとする。</p>

<h4>1. TorchScriptを使わない</h4>

<p>pytorchで書いたモデルをc++に持っていくには一旦TorchScriptに吐いてc++で読み込むのが一般的だと思われる。(
参考: <a href="https://pytorch.org/tutorials/advanced/cpp_export.html">Loading a TorchScript Model in C++ — PyTorch Tutorials 1.10.0+cu102 documentation</a> )
しかし、これを行うと時々推論が遅くなるという問題に遭遇する。
具体的には普通20ms程度で推論できるはずが、なぜかたまに1secかかったりして困る。
そこでpytorchで書いたモデルをc++で書き直すと安定して速い。
もう少し頑張ってくれTorchScript。</p>

<h4>2. tensorを作るときはまとめてから</h4>

<p>以下のように小さいtensorをたくさん作って後でがっちゃんこする処理はめちゃくちゃ遅い。</p>

<pre class="code lang-cpp" data-lang="cpp" data-unlink> std::vector&lt;std::vector&lt;float&gt;&gt; data;
std::vector&lt;torch::Tensor&gt; vtensor;
for(auto&amp;&amp; d : data) {
    vtensor.emplace_back(torch::from_blob(d.data(), {1, N}, torch::kFloat32));
}
auto batch = torch::vstack(vtensor);
 </pre>


<p>そこで、以下のように<code>std::vector&lt;std::vector&lt;float&gt;&gt;</code>を一旦<code>std::vector&lt;float&gt;</code>に一列にして、一度にtorch::from_blobするとちゃんと速くなる。</p>

<pre class="code lang-cpp" data-lang="cpp" data-unlink> std::vector&lt;float&gt; data;
torch::Tensor batch = torch::from_blob(d.data(), {B, N}, torch::kFloat32);
 </pre>


<h4>3. boolean indexingを使わない</h4>

<p>boolean indexingというのは<code>[True, False, False, True, True, ...]</code>のような配列でindexを保持するやつ。
これを使って</p>

<pre class="code lang-python" data-lang="python" data-unlink> x = torch.randn(3, 4)
mask = x.ge(0.5)
x[mask]  # とか
torch.masked_select(x, mask)  # とか
 </pre>


<p>のように要素を抜き出すことはよく行われる処理である<a href="#f-5f08977e" name="fn-5f08977e" title="以下より拝借:  [https://pytorch.org/docs/stable/generated/torch.masked_select.html:title]">*1</a>。
同じようにc++で</p>

<pre class="code c++" data-lang="c++" data-unlink> x.index({"...", mask}) </pre>


<p>などとすると、この処理を何度も繰り返すような場合には遅くなる。なぜかというと以下の箇所で</p>

<p><iframe src="https://hatenablog-parts.com/embed?url=https%3A%2F%2Fgithub.com%2Fpytorch%2Fpytorch%2Fblob%2F0a07488ed2c47765e337e290bd138c0e6e459cbd%2Faten%2Fsrc%2FATen%2FTensorIndexing.h%23L523" title="pytorch/TensorIndexing.h at 0a07488ed2c47765e337e290bd138c0e6e459cbd · pytorch/pytorch" class="embed-card embed-webcard" scrolling="no" frameborder="0" style="display: block; width: 100%; height: 155px; max-width: 500px; margin: 10px 0px;"></iframe><cite class="hatena-citation"><a href="https://github.com/pytorch/pytorch/blob/0a07488ed2c47765e337e290bd138c0e6e459cbd/aten/src/ATen/TensorIndexing.h#L523">github.com</a></cite></p>

<p>boolean indexingから普通のindexingに変換されていて、その処理の中で、</p>

<p><iframe src="https://hatenablog-parts.com/embed?url=https%3A%2F%2Fgithub.com%2Fpytorch%2Fpytorch%2Fblob%2F0a07488ed2c47765e337e290bd138c0e6e459cbd%2Faten%2Fsrc%2FATen%2FTensorIndexing.h%23L258" title="pytorch/TensorIndexing.h at 0a07488ed2c47765e337e290bd138c0e6e459cbd · pytorch/pytorch" class="embed-card embed-webcard" scrolling="no" frameborder="0" style="display: block; width: 100%; height: 155px; max-width: 500px; margin: 10px 0px;"></iframe><cite class="hatena-citation"><a href="https://github.com/pytorch/pytorch/blob/0a07488ed2c47765e337e290bd138c0e6e459cbd/aten/src/ATen/TensorIndexing.h#L258">github.com</a></cite></p>

<p>毎回aten::emptyでtensorを作り直しているからである。
memory poolからあてがってくれているとは思うが、手元の処理ではこれがbottleneckとなったため、boolean indexingは一度普通のindexingに変換してから使い回すようにした。</p>

<p>以上。参考になれば幸いです。</p>
<div class="footnote">
<p class="footnote"><a href="#fn-5f08977e" name="f-5f08977e" class="footnote-number">*1</a><span class="footnote-delimiter">:</span><span class="footnote-text">以下より拝借:  <a href="https://pytorch.org/docs/stable/generated/torch.masked_select.html">torch.masked_select — PyTorch 1.10.0 documentation</a></span></p>
</div>
</body>
