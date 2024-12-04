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
          <img src="https://fastly.jsdelivr.net/npm/@vant/assets/ipad.jpeg" alt="order_photo" />
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
import { ref } from 'vue';
import { showNotify  } from 'vant'
import pubsub from 'pubsub-js'

const props = defineProps<{
  pageFrom: string
}>();

const orders = ref([
  {
    id: 1,
    orderId: '123456',
    productName: '商品 A',
    price: 100,
    time: '2024-01-01 12:00:00',
    status: 'shipped', // Example status
  },
  {
    id: 2,
    orderId: '789012',
    productName: '商品 B',
    price: 150,
    time: '2024-01-02 14:00:00',
    status: 'pending', // Example status
  },
]);

const onClickLeft = () => history.back();



const notifyCustomer = (orderId: number) => {
  pubsub.publish('notifyCustomer', orderId);
  showNotify({ type: 'success', message: `已通知${props.pageFrom === 'distributor' ? '客户' : '商家'}` }); // Show notification
};
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
  background-color: #f9f9f9; /* Light background for the container */
}

h2 {
  margin-bottom: 20px;
  color: #333; /* Dark text color for the heading */
  font-size: 24px; /* Increased font size for better readability */
  display: flex;
  align-items: center; /* Center the icon and text vertically */
}

.header-icon {
  font-size: 28px; /* Adjust icon size */
  color: #007bff; /* Color for the icon */
  margin-right: 10px; /* Space between icon and text */
}

.order-item {
  display: flex;
  padding: 10px;
  border-bottom: 1px solid #e0e0e0;
  align-items: center;
  justify-content: space-between; /* Align items to space between */
}

.img-area {
  flex: 0 0 80px; /* Fixed width for image area */
  margin-right: 10px;
}

.img-area img {
  width: 100%;
  height: auto;
  border-radius: 5px; /* Rounded corners for the image */
}

.info-area {
  flex: 1; /* Take the remaining space */
}

.name {
  font-size: 16px;
  font-weight: bold;
  margin-bottom: 5px;
}

.price {
  color: #ff6034; /* Price color */
  font-size: 14px;
  margin-bottom: 5px;
}

.time {
  font-size: 12px;
  color: #999; /* Lighter color for time */
}

.status {
  font-size: 14px;
  margin-top: 5px;
}

.shipped {
  color: green; /* Green color for shipped status */
}

.notify-button {
  margin-top: 10px; /* Space above the button */
  align-self: flex-end; /* Align button to the bottom */
}
</style>