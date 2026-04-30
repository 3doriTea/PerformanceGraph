# PerformanceGraph

学校が提供しているゲームベースと、自作のゲームベースのパフォーマンス差分を  
グラフ化するためのPython プロジェクト。

## 環境

- Python 3.14.4
- 仕様ライブラリ
  - [matplotlib-fontja](https://github.com/ciffelia/matplotlib-fontja)
  - [matplotlib](https://matplotlib.org/)

## パフォーマンス計測対象

- C++ DirectX 11 で作成した はねねこボール のゲームベース
  - 以下「自作ゲームベース」
- C++ DirectX 11 での開発を手助けする学校のゲームベース
  - 以下「学校ゲームベース」

## 計測

### 前提

- パフォーマンスとは、描画オブジェクトの数が増えても、FPS (1秒間にクライアント領域が描き変わる回数) が60を維持できるかを
  本プロジェクトでは評価対象する。
  - CPUの限界、最大限FPSを出すことは可能だが、人間が視認できると言われているFPS、  
  60を保つようにすることで、CPUの負荷を減らす。
  - パフォーマンスが下がる、FPSが下がるとプレイヤーの操作がゲーム内に反映されるまでラグが発生する。

### 計測前の予想

計測前に、予想を立てた。

- ECS設計を組み込んだため、自作ゲームベースは学校ゲームベースに比べて、緩やかな傾斜になる。
- 自作ゲームベースはコンポーネントプールに限りがあるため、オブジェクト総数が定数を超えるとエラーが発生する。

### 計測結果

![結果の画像](image/ResultGraph.png)



### 計測中の様子

#### 学校ゲームベース

![59fps](image/GBDX11-59fps.png)
![14fps](image/GBDX11-14fps.png)
![3fps](image/GBDX11-3fps.png)

#### 自作ゲームベース

![59fps](image/SGB-59fps.png)
![46fps](image/SGB-46fps.png)
![34fps](image/SGB-34fps.png)
