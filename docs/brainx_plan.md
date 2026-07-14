## 1.各包文档首页统一风格：添加安装卡片和指引卡片。

1. installation 卡片
2. Learn more 卡片，点击可到链接
3. Brainx ecosystem链接。统一小标题术语 See also the ecosystem

## 2.统一文档结构

目录：

* Overview
* Getting Started✔ 【installation、Quickstart】
* Tutorials✔
* Concept
* Guides
* Examples
* ...
* API Reference✔

### 1.`braintrace`、`braintools`  没有Getting Started: installation 和Quickstart。是否需要？

### 2.`brainmass`、`brainevent`、`brainunit`、`btaintools`没有example。是否需要？

## 3.文档内容完善修改

1.`brainunit`

2.`brainevent`

3.`brainstate`

4.`brainpy.state`

5.`braintrace`:

* installation覆盖 Python/JAX/CPU/CUDA/TPU、验证和常见 compile 错误。
* Quickstart：小型 RNN、合成序列、一次 online update、打印 loss/gradient shape；不在首跑中加入完整 copying task。
* Concepts 单独目录，增加“什么时候使用 BrainTrace，什么时候使用 BPTT/Optax”的边界。
* RNN Online Learning和SNN Online Learning可放到 tutorials
* 增加 D-RTRL、e-prop、OTPE、OTTT、OSTL 选择表,用户能按复杂度和网络类型选算法
* example里的示例文件加上链接点击可直接进入

6.`braintools`:

* 新建installation：列出 visualization、SciPy、Nevergrad、Plotly 等可选依赖教程运行前能正确装包
* 新建Quickstart：串联 input、connectivity、metric、visualization 的小型工作流展示工具包整体用途

7.`braincell`

8.`brainmass`

## 4. 排期


| 顺序 | 内容                                                                 |
| ---- | -------------------------------------------------------------------- |
| 1    | 各包首页统一，清晰明了                                               |
| 2    | `braintrace`、`braintools` 的installation和Quickstart，文档内容      |
| 3    | `brainunit`、`brainevent`、`brainstate` 、`brainpy.state` 文档内容 |
| 4    | `braincell`、`brainmass` 文档内容                                    |
| 5    | 确保文档内容正确、代码示例可成功运行。                               |
