# 导入聚宽函数库
import jqdata


# 初始化函数，设定要操作的股票、基准等等
def initialize(context):
    # 要操作的股票
    g.security = '516160.XSHG'  # 新能源etf
    # 基准价格
    g.basis_price = 1.123
    # 买入网格宽度
    g.buy_grid_size = 0.03
    # 卖出网格宽度
    g.sell_grid_size = 0.15
    # 计算当前买入价格
    g.buy_price = g.basis_price * (1 - g.buy_grid_size)
    # 计算当前卖出价格
    g.sell_price = g.basis_price * (1 + g.sell_grid_size)
    # 买入委托量
    g.buy_count = 1000
    # 卖出委托量
    g.sell_count = -1000
    # 设定基准
    set_benchmark(g.security)
    # 开启动态复权模式(真实价格)
    set_option('use_real_price', True)
    # 股票类每笔交易时的手续费(open_tax买入时印花税，close_tax卖出时印花税，open_commission买入佣金，open_commission卖出佣金，close_today_commission今平仓佣金，min_commission最低佣金)
    set_order_cost(OrderCost(open_tax=0,  # 买入时印花税
                             close_tax=0.001,  # 卖出时印花税
                             open_commission=0.0003,  # 买入佣金
                             close_commission=0.0003,  # 卖出佣金
                             close_today_commission=0,  # 今平仓佣金
                             min_commission=5),  # 最低佣金
                   type='stock')  # 类型
    # 为股票设定滑点为百分比滑点
    set_slippage(PriceRelatedSlippage(0.00246), type='stock')
    # 运行函数
    run_daily(market_open, time='every_bar')


def market_open(context):
    security = g.security  # 获取个股信息
    current_price = get_current_data()[security].last_price  # 获取当前价格
    # log.info('当前价格：', str(current_price), '买入触发价格：', str(g.buy_price), '卖出触发价格：', str(g.sell_price))
    # 判断是否触发买入卖出条件
    if current_price < g.buy_price:
        log.info('当前价格：', str(current_price), '买入触发价格：', str(g.buy_price), '卖出触发价格：', str(g.sell_price))
        log.info(str(g.buy_price), "买入")
        buy = order(security, g.buy_count)  # 下一个市价单
        if buy is not None:
            log.info('买入成功')
            # 下单成功，更新当前基准价格
            g.basis_price = g.buy_price
            g.buy_price = g.basis_price * (1 - g.buy_grid_size)
            g.sell_price = g.basis_price * (1 + g.sell_grid_size)
    elif current_price > g.sell_price:
        log.info('当前价格：', str(current_price), '买入触发价格：', str(g.buy_price), '卖出触发价格：', str(g.sell_price))
        log.info(str(g.sell_price), "卖出")
        sell = order(security, g.sell_count)
        if sell is not None:
            log.info('卖出成功')
            # 下单成功，更新当前基准价格
            g.basis_price = g.sell_price
            g.buy_price = g.basis_price * (1 - g.buy_grid_size)
            g.sell_price = g.basis_price * (1 + g.sell_grid_size)