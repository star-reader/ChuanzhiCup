<template>
  <div class="product-detail-container">
    <van-card
      class="product-card"
      :title="product.name"
      :desc="product.description"
      :thumb="product.image"
    >
      <template #footer>
        <van-button type="primary" @click="addToCart">加入购物车</van-button>
      </template>
    </van-card>
  </div>
</template>

<script lang="ts" setup>
import { ref } from 'vue';

const product = ref({
  name: '示例商品',
  description: '这是一个示例商品的描述信息。',
  image: 'https://fastly.jsdelivr.net/npm/@vant/assets/ipad.jpeg', // Replace with your product image path
});

const addToCart = () => {
  // Logic to add the product to the cart
  console.log('加入购物车:', product.value.name);
};
</script>

<style scoped>
.product-detail-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  min-height: 100vh;
  padding: 0 20px;
  background-color: #f9f9f9; /* Light background for the container */
}

.product-card {
  width: 100%; /* Full width for mobile */
  max-width: 400px; /* Maximum width for larger screens */
}
</style> 