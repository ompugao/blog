+++
Categories = ["tech"]
Description = " 以前妻にc++のクラスの使い方を教えたときに、ブログ記事にしたらいいのに、と言われたので公開しておく。  対象者：intとかdoubleの変数やその配列を扱え、関数を作ったり使ったりできる。ポインタも一応わかる。でもclassの使い方がわ"
Tags = []
date = "2021-03-01T23:07:00+09:00"
title = "ポケモンで学ぶC++オブジェクト指向入門"
url = "/posts/2021/learning-cpp-oop-through-pokemon/"
author = "ompugao"
archive = ["2021"]
draft = false
+++

<body>
<p>以前妻にc++のクラスの使い方を教えたときに、ブログ記事にしたらいいのに、と言われたので公開しておく。</p>

<p>対象者：intとかdoubleの変数やその配列を扱え、関数を作ったり使ったりできる。ポインタも一応わかる。でもclassの使い方がわからない。そんな人。</p>

<p>記事を読むと？：
c++でif else分岐の多かったコードを少し見通しよくできるようになる。
(c++で継承を利用したポリモーフィズムなプログラムを書けるようになる)</p>

<p>本題：</p>

<p>あなたはポケモンを実装しているプログラマです。
ポケモンバトルにおける"こうげき処理"をc++で実装しようとしています。
「プレイヤーがてもちのポケモンから一匹えらんで、あいてのポケモンをこうげきする」という処理について考えています。
ここでは、ポケモンは一つのわざしか覚えていないと仮定します。
一旦c++の正しい文法は無視して、実直に書くとこうなります。</p>

<pre class="code lang-cpp" data-lang="cpp" data-unlink> ポケモン = ポケモンを選ぶ();
if (ポケモン == ピカチュウ) {
    十万ボルト(ポケモン);
} else if (ポケモン == ゼニガメ) {
    ハイドロポンプ(ポケモン);
} else {
    ...
}
 </pre>


<p>ポケモンの数だけif elseが続きますね。
ポケモンが増えるごとにこの処理を変更しないといけません。
大変です。</p>

<p>そこで、オブジェクト指向プログラミング(Object Oriented Programming)です。
以下のように考えます。こちらも一旦正しいc++の文法を無視します。</p>

<pre class="code lang-cpp" data-lang="cpp" data-unlink> // 基底クラス
class ポケモン {
    void こうげき();
};

// ポケモンクラスを"継承"したピカチュウクラス
class ピカチュウ : ポケモン {
    void こうげき() override {
        十万ボルト();
    }
    void 十万ボルト() {
        // 十万ボルトの実装
    }
};

class ゼニガメ : ポケモン {
    void こうげき() override {
        ハイドロポンプ();
    }
    void ハイドロポンプ() {
        // ハイドロポンプの実装
    }
};
 </pre>


<p>まず、「ポケモン」というクラスを作ります。
これはポケモンがどういうことができるか、という特性を示してくれます。
ここではポケモンは「void こうげき()」関数を持っていることがわかります。</p>

<p>そしてポケモンクラスの子供にあたる「ピカチュウ」クラスを作ります。
ピカチュウはポケモンなので自然です<a href="#f-99411860" name="fn-99411860" title="これらはis-aの関係にあります。
[https://ja.wikipedia.org/wiki/Is-a#:~:text=%E7%9F%A5%E8%AD%98%E8%A1%A8%E7%8F%BE%E3%80%81%E3%82%AA%E3%83%96%E3%82%B8%E3%82%A7%E3%82%AF%E3%83%88%E6%8C%87%E5%90%91%E3%83%97%E3%83%AD%E3%82%B0%E3%83%A9%E3%83%9F%E3%83%B3%E3%82%B0,%E3%81%82%E3%82%8B%E3%81%93%E3%81%A8%E3%82%92%E6%84%8F%E5%91%B3%E3%81%99%E3%82%8B%E3%80%82:embed:cite]">*1</a>。
これを基底クラスを継承して派生クラス（子クラス）を作る、といいます。
そしてピカチュウクラスの中で、ピカチュウは実際にどのようなこうげきをするのかを具体的に記述します。
ピカチュウは十万ボルトが使えるので十万ボルトについて書きましょう。
ゼニガメについても同様です。</p>

<p>ピカチュウクラスは、あくまでピカチュウという種族についての書いているだけです。
「サトシのピカチュウ」、というある個体を表現するにはこうです。</p>

<pre class="code lang-cpp" data-lang="cpp" data-unlink> ピカチュウ  サトシのピカチュウ();
 </pre>


<p>この「サトシのピカチュウ」のことをピカチュウクラスの「インスタンス」と呼びます。</p>

<pre class="code lang-cpp" data-lang="cpp" data-unlink> int i(0);
 </pre>


<p>のようにintの変数を宣言するのと同じことです。
intがピカチュウになっただけです。</p>

<p>ポケモンがこうげきするときはこのように書きます。</p>

<pre class="code lang-cpp" data-lang="cpp" data-unlink> サトシのピカチュウ.こうげき();
 </pre>


<p>サトシのピカチュウへのポインタを知っているときには"-&gt;"を使って書きます。</p>

<pre class="code lang-cpp" data-lang="cpp" data-unlink> サトシのピカチュウ-&gt;こうげき();
// 以下と同じ
(*サトシのピカチュウ).こうげき();
 </pre>


<p>さて、「てもちのポケモンから一匹えらんで、あいてのポケモンをこうげきする」という処理はどのように書けるでしょうか。</p>

<pre class="code lang-cpp" data-lang="cpp" data-unlink> ポケモン* 手持ちのポケモン[2];
ピカチュウ  サトシのピカチュウ();
ゼニガメ サトシのゼニガメ();
手持ちのポケモン[0] = &amp;サトシのピカチュウ;
手持ちのポケモン[1] = &amp;サトシのゼニガメ;

int i = ポケモンを選ぶ();
手持ちのポケモン[i]-&gt;こうげき();
 </pre>


<p>if elseを使わなくて済み、
ポケモンの種類が増えた場合、例えばミュウツーが生み出された場合には、
ポケモンクラスを継承したミュウツークラスを作るだけです。べんりですね！</p>

<p>さて、c++を使って正しい文法で実装してみましょう。</p>

<pre class="code lang-cpp" data-lang="cpp" data-unlink> #include &lt;iostream&gt;
 
class Pokemon {
public:
    // コンストラクタ
    Pokemon(const std::string&amp; nickname) {
        this-&gt;nickname_ = nickname;
        // nickname_ = nickname; と省略できる
    }
    // デストラクタ
    virtual ~Pokemon() {
    }
    virtual void attack() = 0;
protected:
    std::string nickname_;
};

class Pikachu : public Pokemon {
public:
    Pikachu(const std::string&amp; nickname) : Pokemon(nickname) {
    }
    virtual ~Pikachu() {
    }
    void attack() override {
        std::cout &lt;&lt; nickname_  &lt;&lt; "の十万ボルト!" &lt;&lt; std::endl;
    }
};

class Zenigame : public Pokemon {
public:
    Zenigame(const std::string&amp; nickname) : Pokemon(nickname) {
    }
    virtual ~Zenigame() {
    }
    void attack() override {
        std::cout &lt;&lt; nickname_ &lt;&lt; "のハイドロポンプ!" &lt;&lt; std::endl;
    }
};


int main() {
    int i;
    Pokemon* monsters[2];
    monsters[0] = new Pikachu("サトシのピカチュウ");
    monsters[1] = new Zenigame("サトシのゼニガメ");
    std::cin &gt;&gt; i;
    if (i &gt;=0 &amp;&amp; i &lt; 2) {
        monsters[i]-&gt;attack();
    }
    delete monsters[0];
    delete monsters[1];
}
 </pre>


<p>なんだか色々増えましたね。</p>

<p>まず「コンストラクタ」と「デストラクタ」はそれぞれそのインスタンスを作ったときと消えるときに呼ばれる関数です。
ポケモンの個体にはニックネームがあるので、そのポケモン個体を宣言し生み出す時に同時にニックネームも設定したいですね？
まず、ポケモンクラスの中にニックネームを格納する部分を作ります。
それが<code>std::string nickname_;</code>の部分で、これをクラスメンバ変数と言います。
<code>Pickachu("サトシのピカチュウ");</code>でピカチュウクラスに渡されたニックネームが巡り巡って、
<code>this-&gt;nickname_ = nickname;</code>の部分で<code>nickname_</code>に設定されます。
<code>this</code>というのは今作ったり消したりしようとしているポケモン個体（インスタンス）へのポインタです。
各個体ごとに別のニックネームが設定されることになります。</p>

<pre class="code lang-cpp" data-lang="cpp" data-unlink>     virtual void attack() = 0;
 </pre>


<p><code>virtual なんとか = 0;</code>は純粋仮想関数といいます。継承先（ピカチュウ等各ポケモンクラス）でちゃんと実装してくださいね〜でないと空っぽのままですからね〜と指示しています。</p>

<pre class="code lang-cpp" data-lang="cpp" data-unlink>     new Pikachu("サトシのピカチュウ");
    delete pikachu;
 </pre>


<p>new/deleteはご存知でしょうか？まぁ<code>Pikachu satoshi_pikachu();</code>と同じようなもの<a href="#f-232ccad6" name="fn-232ccad6" title="いいえ、全然違います。普通のsatoshi_pikachuはスタック領域に存在しますが、newで作られたピカチュウはヒープ領域にいます。
[https://keens.github.io/blog/2017/04/30/memoritosutakkutohi_puto/:title]
">*2</a>ですが、newはポケモン個体を作った後ポインタが帰ってきます。ポインタの先の実体はスコープを抜けても終了処理が行われずメモリリークするので、使わなくなったらdeleteをしなければなりません。普通はnew/deleteを使わずshared_ptrやunique_ptrを使います。気になったら調べてみてください。</p>

<p>また、publicやprotectedという言葉が出てきました。他にもprivateがあります。
これはアクセス指定子といってその変数やクラスが内外のスコープからアクセスできるかどうかを示しています。</p>

<ul>
<li>publicは、どこからでもアクセスできます。</li>
<li>protectedだと継承先のクラスでは見えますが(main関数など)外からは見えません。</li>
<li>privateだと宣言したクラスでしかアクセスできません。</li>
</ul>


<p>という意味になります。</p>

<pre class="code lang-cpp" data-lang="cpp" data-unlink> class Zenigame : public Pokemon {
 </pre>


<p>この部分のpublicについての解説は省略します。大抵の場合でpublicを用います。</p>

<p>実行してみましょう。</p>

<pre class="code lang-sh" data-lang="sh" data-unlink> $ g++ pokemon.cpp -o pokemon
$ ./pokemon
0
サトシのピカチュウの十万ボルト!
$ ./pokemon
1
サトシのゼニガメのハイドロポンプ!
 </pre>


<p>いいですね！</p>
<div class="footnote">
<p class="footnote"><a href="#fn-99411860" name="f-99411860" class="footnote-number">*1</a><span class="footnote-delimiter">:</span><span class="footnote-text">これらはis-aの関係にあります。
<iframe src="https://hatenablog-parts.com/embed?url=https%3A%2F%2Fja.wikipedia.org%2Fwiki%2FIs-a%23%3A~%3Atext%3D%25E7%259F%25A5%25E8%25AD%2598%25E8%25A1%25A8%25E7%258F%25BE%25E3%2580%2581%25E3%2582%25AA%25E3%2583%2596%25E3%2582%25B8%25E3%2582%25A7%25E3%2582%25AF%25E3%2583%2588%25E6%258C%2587%25E5%2590%2591%25E3%2583%2597%25E3%2583%25AD%25E3%2582%25B0%25E3%2583%25A9%25E3%2583%259F%25E3%2583%25B3%25E3%2582%25B0%2C%25E3%2581%2582%25E3%2582%258B%25E3%2581%2593%25E3%2581%25A8%25E3%2582%2592%25E6%2584%258F%25E5%2591%25B3%25E3%2581%2599%25E3%2582%258B%25E3%2580%2582" title="is-a - Wikipedia" class="embed-card embed-webcard" scrolling="no" frameborder="0" style="display: block; width: 100%; height: 155px; max-width: 500px; margin: 10px 0px;"></iframe><cite class="hatena-citation"><a href="https://ja.wikipedia.org/wiki/Is-a#:~:text=%E7%9F%A5%E8%AD%98%E8%A1%A8%E7%8F%BE%E3%80%81%E3%82%AA%E3%83%96%E3%82%B8%E3%82%A7%E3%82%AF%E3%83%88%E6%8C%87%E5%90%91%E3%83%97%E3%83%AD%E3%82%B0%E3%83%A9%E3%83%9F%E3%83%B3%E3%82%B0,%E3%81%82%E3%82%8B%E3%81%93%E3%81%A8%E3%82%92%E6%84%8F%E5%91%B3%E3%81%99%E3%82%8B%E3%80%82">ja.wikipedia.org</a></cite></span></p>
<p class="footnote"><a href="#fn-232ccad6" name="f-232ccad6" class="footnote-number">*2</a><span class="footnote-delimiter">:</span><span class="footnote-text">いいえ、全然違います。普通のsatoshi_pikachuはスタック領域に存在しますが、newで作られたピカチュウはヒープ領域にいます。
<a href="https://keens.github.io/blog/2017/04/30/memoritosutakkutohi_puto/">メモリとスタックとヒープとプログラミング言語 | κeenのHappy Hacκing Blog</a>
</span></p>
</div>
</body>
