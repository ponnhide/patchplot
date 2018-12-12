# [matplotlib]Subplotで疲れるのはもうやめたい。

Matplotlibで、Figureを並べて表示するのは割と疲れる。いや、GridSpecみたいな便利な機能があるのはしっている。

https://qiita.com/simonritchie/items/da54ff0879ad8155f441

でも、こういったライブラリを使って複雑なレイアウトを作成する場合、最初に完成のレイアウトを決める必要があって、出力を確認しながらレイアウトを少しづつ修正していくみたいな作業には不向きである。とくに、ラベルの文字やプロット同士の衝突が起こると図の調整で数時間以上消耗することも珍しくない。

一方で、ipython notebook、 jupiter notebook、jupyter labでは、コードがセルごとに分割されているので、データもセルごとに可視化することができ、図の修正だってその都度行える。

で、こうした潮流にのって、複数のプロットを組み合わせたようなFigure作成においても、出力を確認→その都度修正みたいなことができればいいのになぁと思うわけである。



実際、ggplotにはpatchwork (https://qiita.com/nozma/items/4512623bea296ccb74ba) という素晴らしいライブラリが存在し、いとも簡単に複数の図を組み合わせることができる。が、matplotlibにはない。



ということで、即席ではあるがちょっとしたモジュール(https://github.com/ponnhide/patchplot)を作ってみた。

## patchplot

プロット同士を結合させるメソッドはstackというメソッドのみ。ある’1つのプロットを基準にして、その上下左右に新しいオブジェクトを配置することができる。

aspectの引数を使えば、図の縦横比も調節できる。ただしプロットの端が自動的に揃うように調整している関係上、プロットの縦横比は厳密にはaspect通りにはならない。



 実演。まずは１つ目のaxes objectを作成。

```python
import patchplot as pp
fig = pp.set_fig() #figure objectの作成
ax1 = pp.set_ax(fig,label=1) #一つ目のaxesオブジェクトの作成。
```

この時点で、できているものは



こんな感じ。このax1オブジェクトの下に新しいプロットを置きたい場合は下記のようにすれば良い。`

```python
ax2 = pp.set_ax(fig,label=2)
pp.stack(fig,ax1,ax2,d="b") 
#1つ目の引数はfigureオブジェクト、2つ目は配置の基準となるaxesオブジェクト、3つ目は結合させるaxesオブジェクト、4つ目は結合させる際の向き。"b"なら下、"t"なら上、”l”なら左、"r"なら右側に基準オブジェクトと揃うように結合される
```

こんな感じ。



ax1の右に、さらに別のプロットをおくこともできる。このときaspectの引数をつければ、横長の図になる。

```python
ax3 = pp.set_ax(fig,label=3,aspect=(2,1))
pp.stack(fig,ax1,ax3,d="r")
```

するとこんな感じ。



ax3の下が空いてるから、ax2の左側にプロットでも置くかなぁいう場合は

```
ax4 = pp.set_ax(fig,label=4,aspect=(0.5,1))
pp.stack(fig,ax2,ax4,d="l")
```

するとこんな感じ。



ax4の左がまだ空いてるなぁということで、ax3と揃うように別のプロットでも置くかぁと思ったら、

```Python
ax5 = pp.set_ax(fig,label=5,aspect=(1.5,1))
pp.stack(fig,ax4,ax5,d="l")
```

するとこんな感じ。ax4のアスペクトを(0.5,1)で作ったので、ax3と右端を揃えるためにax5のアスペクトは(1.5,1)にしてある。



最後に、ax5を基準にして、その左に縦長の図でも置く場合は、

````
ax7 = set_ax(fig,label=7,aspect=(1,3))
stack(fig,ax6,ax7,d="l")
````

でこんな感じ。





なんとなく作りたいものは作れた気がする。

















