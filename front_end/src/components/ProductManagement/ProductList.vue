<template>
  <div class="product-list-container">
    <h2>商品管理</h2>
    
    <van-card
      class="product-item"
      @click="addProduct"
      :title="'新增商品'"
      :desc="'点击添加新商品'"
    >
      <van-button size="small" type="primary" @click.stop="addProduct">添加</van-button>
    </van-card>

    <van-card
      class="product-item"
      @click="manageProducts"
      :title="'管理商品'"
      :desc="'点击管理现有商品'"
    >
      <van-button size="small" type="info" @click.stop="manageProducts">管理</van-button>
    </van-card>
  </div>
</template>

<script lang="ts" setup>
const addProduct = () => {
  // Logic to add a product
  console.log('新增商品');
};

const manageProducts = () => {
  // Logic to manage products
  console.log('管理商品');
};
</script>

<style scoped>
.product-list-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  min-height: 100vh;
  padding: 0 20px;
  background-color: #f9f9f9; /* Light background for the container */
}

h2 {
  margin-bottom: 20px;
  color: #333; /* Dark text color for the heading */
  font-size: 24px; /* Increased font size for better readability */
}

.product-item {
  width: 100%; /* Full width for mobile */
  max-width: 400px; /* Maximum width for larger screens */
  margin: 10px 0; /* Space between items */
  border-radius: 8px; /* Rounded corners */
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1); /* Subtle shadow for depth */
}

.product-item:hover {
  background-color: #e0f7fa; /* Light blue background on hover */
}
</style> 