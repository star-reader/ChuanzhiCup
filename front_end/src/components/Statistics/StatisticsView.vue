<template>
  <div class="statistics-container">
    <van-nav-bar
      title="数据统计"
      left-text="返回"
      left-arrow
      @click-left="onClickLeft"
    />
    
    <div class="chart-container">
      <!-- 销售趋势图 -->
      <div class="chart-card">
        <h3>销售趋势</h3>
        <div ref="salesTrendChart" class="chart"></div>
      </div>

      <!-- 商品销量排行 -->
      <div class="chart-card">
        <h3>商品销量排行</h3>
        <div ref="productRankChart" class="chart"></div>
      </div>

      <!-- 销售额统计 -->
      <div class="chart-card">
        <h3>销售额统计</h3>
        <div class="data-grid">
          <van-grid :column-num="2">
            <van-grid-item>
              <template #text>
                <div class="grid-data">
                  <span class="label">今日销售额</span>
                  <span class="value">¥{{ todaySales }}</span>
                </div>
              </template>
            </van-grid-item>
            <van-grid-item>
              <template #text>
                <div class="grid-data">
                  <span class="label">本月销售额</span>
                  <span class="value">¥{{ monthSales }}</span>
                </div>
              </template>
            </van-grid-item>
          </van-grid>
        </div>
      </div>

      <!-- 订单分析 -->
      <div class="chart-card">
        <h3>订单分析</h3>
        <div ref="orderAnalysisChart" class="chart"></div>
      </div>
    </div>
  </div>
</template>

<script lang="ts" setup>
import { ref, onMounted, onUnmounted } from 'vue';
import * as echarts from 'echarts';

const salesTrendChart = ref();
const productRankChart = ref();
const orderAnalysisChart = ref();
let charts: echarts.ECharts[] = [];

const todaySales = ref('2,356.00');
const monthSales = ref('68,234.00');

onMounted(() => {
  // 初始化销售趋势图
  const salesChart = echarts.init(salesTrendChart.value);
  salesChart.setOption({
    title: {
      text: '近7天销售趋势',
      left: 'center'
    },
    tooltip: {
      trigger: 'axis'
    },
    xAxis: {
      type: 'category',
      data: ['周一', '周二', '周三', '周四', '周五', '周六', '周日']
    },
    yAxis: {
      type: 'value'
    },
    series: [{
      data: [820, 932, 901, 934, 1290, 1330, 1320],
      type: 'line',
      smooth: true,
      areaStyle: {
        opacity: 0.3
      },
      itemStyle: {
        color: '#007bff'
      }
    }]
  });

  // 初始化商品销量排行图
  const rankChart = echarts.init(productRankChart.value);
  rankChart.setOption({
    title: {
      text: '商品销量TOP5',
      left: 'center'
    },
    tooltip: {
      trigger: 'axis',
      axisPointer: {
        type: 'shadow'
      }
    },
    xAxis: {
      type: 'value'
    },
    yAxis: {
      type: 'category',
      data: ['新鲜番茄', '特色蔬菜', '阳江胡萝卜', '甜橙', '芒果']
    },
    series: [{
      type: 'bar',
      data: [58, 52, 48, 44, 40],
      itemStyle: {
        color: '#4CAF50'
      }
    }]
  });

  // 初始化订单分析图
  const orderChart = echarts.init(orderAnalysisChart.value);
  orderChart.setOption({
    title: {
      text: '订单状态分布',
      left: 'center'
    },
    tooltip: {
      trigger: 'item'
    },
    legend: {
      orient: 'horizontal',
      bottom: 'bottom'
    },
    series: [{
      type: 'pie',
      radius: '50%',
      data: [
        { value: 235, name: '已完成' },
        { value: 110, name: '待发货' },
        { value: 134, name: '配送中' },
        { value: 35, name: '已取消' }
      ],
      emphasis: {
        itemStyle: {
          shadowBlur: 10,
          shadowOffsetX: 0,
          shadowColor: 'rgba(0, 0, 0, 0.5)'
        }
      }
    }]
  });

  charts = [salesChart, rankChart, orderChart];

  window.addEventListener('resize', handleResize);
});

const handleResize = () => {
  charts.forEach(chart => chart.resize());
};

const onClickLeft = () => history.back();

onUnmounted(() => {
  charts.forEach(chart => chart.dispose());
  window.removeEventListener('resize', handleResize);
});
</script>

<style scoped>
.statistics-container {
  position: relative;
  padding-top: 0px;
  height: 100vh;
  background-color: #f7f8fa;
  overflow: hidden;
}

.chart-container {
  position: relative;
  height: calc(100vh - 50px);
  overflow: hidden auto;
}

.chart-card {
  background: #fff;
  border-radius: 12px;
  padding: 16px;
  margin-bottom: 16px;
  box-shadow: 0 2px 12px rgba(100, 101, 102, 0.12);
}

.chart-card h3 {
  margin: 0 0 16px;
  font-size: 16px;
  color: #323233;
}

.chart {
  height: 300px;
  width: 100%;
}

.data-grid {
  padding: 8px 0;
}

.grid-data {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 12px;
}

.grid-data .label {
  font-size: 14px;
  color: #646566;
  margin-bottom: 8px;
}

.grid-data .value {
  font-size: 20px;
  font-weight: bold;
  color: #323233;
}

:deep(.van-grid-item__content) {
  padding: 0;
}
</style> 