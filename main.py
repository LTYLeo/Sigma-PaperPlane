#!/usr/bin/env python3
"""
Sigma PaperPlane 主程序
智能纸飞机折叠优化系统
"""

import sys
import os
import argparse
from src.paper_plane_generator import PaperPlaneGenerator
from src.fluid_simulation import FluidSimulation
from src.optimization import GeneticOptimizer
from src.visualization import Visualization

def main():
    """主程序入口"""
    parser = argparse.ArgumentParser(description='Sigma PaperPlane - 智能纸飞机优化系统')
    parser.add_argument('--mode', choices=['optimize', 'test', 'visualize'], 
                       default='optimize', help='运行模式')
    parser.add_argument('--generations', type=int, default=50, 
                       help='遗传算法进化代数')
    parser.add_argument('--population', type=int, default=30, 
                       help='种群大小')
    parser.add_argument('--objective', choices=['distance', 'stability', 'balanced'], 
                       default='balanced', help='优化目标')
    parser.add_argument('--output', type=str, default='results', 
                       help='输出目录')
    
    args = parser.parse_args()
    
    # 创建输出目录
    os.makedirs(args.output, exist_ok=True)
    
    print("=" * 60)
    print("Sigma PaperPlane - 智能纸飞机优化系统")
    print("=" * 60)
    
    if args.mode == 'optimize':
        run_optimization(args)
    elif args.mode == 'test':
        run_testing(args)
    elif args.mode == 'visualize':
        run_visualization(args)

def run_optimization(args):
    """运行优化模式"""
    print(f"\n开始优化模式...")
    print(f"目标: {args.objective}")
    print(f"种群大小: {args.population}")
    print(f"进化代数: {args.generations}")
    
    # 初始化优化器
    optimizer = GeneticOptimizer(
        population_size=args.population,
        mutation_rate=0.1,
        crossover_rate=0.8,
        elite_count=5
    )
    
    # 运行优化
    print("\n正在运行遗传算法优化...")
    result = optimizer.optimize(
        generations=args.generations,
        objective=args.objective
    )
    
    # 生成优化摘要
    summary = optimizer.get_optimization_summary(result)
    
    # 可视化结果
    visualizer = Visualization()
    
    print("\n生成可视化结果...")
    # 优化进度图
    visualizer.plot_optimization_progress(
        result, 
        save_path=os.path.join(args.output, 'optimization_progress.png')
    )
    
    # 折叠图案
    visualizer.plot_fold_pattern(
        result['best_individual'],
        save_path=os.path.join(args.output, 'best_plane_fold_pattern.png')
    )
    
    # 交互式仪表板
    visualizer.create_interactive_dashboard(result)
    
    # 生成报告
    report = visualizer.generate_optimization_report(
        result,
        save_path=os.path.join(args.output, 'optimization_report.md')
    )
    
    # 输出结果摘要
    print("\n" + "=" * 40)
    print("优化结果摘要")
    print("=" * 40)
    print(f"最佳纸飞机类型: {summary['best_plane_type']}")
    print(f"最终适应度: {summary['best_fitness']:.3f}")
    print(f"关键参数:")
    print(f"  - 翼展: {summary['key_parameters']['wing_span']:.1f} cm")
    print(f"  - 机身长度: {summary['key_parameters']['body_length']:.1f} cm")
    print(f"  - 鼻角: {summary['key_parameters']['nose_angle']:.1f} 度")
    print(f"  - 重量分布: {summary['key_parameters']['weight_distribution']:.1f}%")
    
    print(f"\n各条件性能:")
    for condition, perf in summary['performance_by_condition'].items():
        print(f"  - {condition}:")
        print(f"     飞行距离: {perf['flight_distance']:.2f} m")
        print(f"     飞行时间: {perf['flight_time']:.2f} s")
        print(f"     稳定性: {perf['stability']:.3f}")
        print(f"     成功: {'是' if perf['success'] else '否'}")

def run_testing(args):
    """运行测试模式"""
    print(f"\n开始测试模式...")
    
    # 初始化组件
    generator = PaperPlaneGenerator()
    simulator = FluidSimulation()
    visualizer = Visualization()
    
    # 生成几个不同类型的纸飞机进行测试
    plane_types = ['classic', 'delta', 'glider', 'stunt', 'long_distance']
    test_planes = []
    
    print("生成测试纸飞机...")
    for plane_type in plane_types:
        if plane_type == 'classic':
            plane = generator._generate_classic_plane()
        elif plane_type == 'delta':
            plane = generator._generate_delta_plane()
        elif plane_type == 'glider':
            plane = generator._generate_glider_plane()
        elif plane_type == 'stunt':
            plane = generator._generate_stunt_plane()
        else:  # long_distance
            plane = generator._generate_long_distance_plane()
        test_planes.append(plane)
    
    # 测试条件
    test_conditions = [
        {'name': '无风', 'wind_velocity': [0, 0, 0]},
        {'name': '顺风', 'wind_velocity': [3, 0, 0]},
        {'name': '逆风', 'wind_velocity': [-2, 0, 0]},
    ]
    
    # 运行测试
    print("运行流体仿真测试...")
    all_results = []
    for i, plane in enumerate(test_planes):
        print(f"测试 {plane['type']} 纸飞机...")
        results = simulator.test_multiple_conditions(plane, test_conditions)
        all_results.append(results)
    
    # 可视化比较结果
    print("生成比较图表...")
    visualizer.plot_plane_comparison(
        test_planes, all_results,
        save_path=os.path.join(args.output, 'plane_comparison.png')
    )
    
    # 绘制每个纸飞机的折叠图案
    for i, plane in enumerate(test_planes):
        visualizer.plot_fold_pattern(
            plane,
            save_path=os.path.join(args.output, f'{plane["type"]}_fold_pattern.png')
        )
    
    print(f"\n测试完成！结果保存在 {args.output} 目录")

def run_visualization(args):
    """运行可视化模式"""
    print(f"\n开始可视化模式...")
    
    # 这里可以加载之前保存的结果进行可视化
    # 目前先演示基本功能
    
    generator = PaperPlaneGenerator()
    visualizer = Visualization()
    
    # 生成一个示例纸飞机
    plane = generator.generate_random_plane()
    
    print(f"生成 {plane['type']} 纸飞机的折叠图案...")
    visualizer.plot_fold_pattern(
        plane,
        save_path=os.path.join(args.output, 'example_fold_pattern.png')
    )
    
    print("可视化演示完成！")

def demo():
    """演示函数"""
    print("Sigma PaperPlane 演示模式")
    print("=" * 40)
    
    # 快速演示基本功能
    generator = PaperPlaneGenerator()
    simulator = FluidSimulation()
    visualizer = Visualization()
    
    # 生成一个随机纸飞机
    print("1. 生成随机纸飞机...")
    plane = generator.generate_random_plane()
    print(f"  类型: {plane['type']}")
    print(f"  翼展: {plane['wing_span']:.1f} cm")
    print(f"  机身长度: {plane['body_length']:.1f} cm")
    
    # 显示折叠图案
    print("2. 显示折叠图案...")
    visualizer.plot_fold_pattern(plane)
    
    # 简单仿真测试
    print("3. 运行简单仿真测试...")
    geometry = generator.get_plane_geometry(plane)
    initial_conditions = {
        'position': [0, 0, 2.0],
        'velocity': [6.0, 0, 0],
        'orientation': [10, 0, 0]
    }
    wind_conditions = {
        'velocity': [0, 0, 0],
        'gradient': 0.0,
        'turbulence': 0.0
    }
    
    result = simulator.simulate_flight(geometry, initial_conditions, wind_conditions)
    print(f"  飞行距离: {result['flight_distance']:.2f} m")
    print(f"  飞行时间: {result['flight_time']:.2f} s")
    print(f"  稳定性: {result['stability_metrics']['overall_stability']:.3f}")
    
    print("\n演示完成！")

if __name__ == "__main__":
    if len(sys.argv) == 1:
        # 如果没有参数，运行演示模式
        demo()
    else:
        main()
