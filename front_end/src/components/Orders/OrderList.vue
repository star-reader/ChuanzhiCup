<template>
  <div class="order-list-container">
    <van-nav-bar
      class="order-list-nav"
      title="订单列表"
      left-text="返回"
      left-arrow
      @click-left="onClickLeft"
    />
    
    <div class="order-list">
      <div class="order-item" v-for="order in orders" :key="order.id">
        <div class="img-area">
          <img :src="order.pic" alt="order_photo" />
        </div>
        <div class="info-area">
          <div class="name">{{ order.productName }}</div>
          <div class="price">{{ order.price }}元</div>
          <div class="time">{{ order.time }}</div>
          <div class="status" :class="{ shipped: order.status === 'shipped' }">
            {{ order.status === 'shipped' ? '已发货' : '待发货' }}
          </div>
        </div>
        <van-button class="notify-button" type="primary" size="small" @click="notifyCustomer(order.id)">通知
        {{ props.pageFrom === 'distributor' ? '客户' : '商家' }}
        </van-button>
      </div>
    </div>
  </div>
</template>

<script lang="ts" setup>
import { onMounted, ref } from 'vue';
import { showNotify  } from 'vant'
import axios from 'axios';
import pubsub from 'pubsub-js'
import o_orders from '@/config/data/orders';
import api from '@/config/api/api';

const props = defineProps<{
  pageFrom: string
}>();

const orders = ref(o_orders);

const onClickLeft = () => history.back();

const notifyCustomer = (orderId: number) => {
  pubsub.publish('notifyCustomer', orderId);
  showNotify({ type: 'success', message: `已通知${props.pageFrom === 'distributor' ? '客户' : '商家'}` }); // Show notification
}

onMounted(() => {
  axios.get(api.GetOrders)
  .then(res => {
    orders.value = res.data;
  })
})

</script>

<style scoped>
.order-list-nav {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
}
.order-list-container {
  position: relative;
  top: 50px;
  min-height: calc(100vh - 50px);
  padding: 0 20px;
  background-color: #f9f9f9; 
}

h2 {
  margin-bottom: 20px;
  color: #333;
  font-size: 24px;
  display: flex;
  align-items: center;
}

.header-icon {
  font-size: 28px;
  color: #007bff;
  margin-right: 10px;
}
.order-item {
  display: flex;
  padding: 10px;
  border-bottom: 1px solid #e0e0e0;
  align-items: center;
  justify-content: space-between;
}

.img-area {
  flex: 0 0 80px;
  margin-right: 10px;
}

.img-area img {
  width: 100%;
  height: auto;
  border-radius: 5px;
}

.info-area {
  flex: 1;
}

.name {
  font-size: 16px;
  font-weight: bold;
  margin-bottom: 5px;
}

.price {
  color: #ff6034;
  font-size: 14px;
  margin-bottom: 5px;
}

.time {
  font-size: 12px;
  color: #999;
}

.status {
  font-size: 14px;
  margin-top: 5px;
}

.shipped {
  color: green;
}

.notify-button {
  margin-top: 10px;
  align-self: flex-end;
}
</style>