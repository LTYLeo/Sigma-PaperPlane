# Sigma PaperPlane - 智能纸飞机优化系统

一个基于人工智能的纸飞机折叠优化系统，通过生成不同的折叠形状并在流体仿真中测试飞行性能，找到最优的折叠方案。

## 功能特性

- 🛩️ 自动生成多种纸飞机折叠形状
- 🌬️ 流体动力学仿真测试
- 📊 多条件测试（不同风速、角度）
- 🎯 遗传算法优化
- 📈 性能可视化
- 🎨 3D折叠动画展示

## 项目结构

```
Sigma PaperPlane/
├── src/
│   ├── __init__.py
│   ├── paper_plane_generator.py    # 纸飞机形状生成器
│   ├── fluid_simulation.py         # 流体仿真模块
│   ├── optimization.py             # 优化算法
│   └── visualization.py            # 可视化模块
├── tests/
│   └── test_sigma_paperplane.py
├── examples/
│   └── demo.py
├── requirements.txt
├── main.py
└── README.md
```

## 安装和使用

```bash
pip install -r requirements.txt
python main.py
```

## 技术栈

- Python 3.8+
- NumPy - 数值计算
- Matplotlib - 2D可视化
- Plotly - 3D可视化
- SciPy - 科学计算
- Pygame (可选) - 实时仿真
