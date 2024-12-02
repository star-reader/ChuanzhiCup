<template>
  <div class="product-list-container">
    <h2>
      <van-icon name="manager" class="header-icon" /> 商品管理
    </h2>
    
    <van-card
      class="product-item"
      @click="addProduct"
      :title="'新增商品'"
      :desc="'点击添加新商品'"
      :thumb="FoodAdd"
    />
    
    <van-card
      class="product-item"
      @click="manageProducts"
      :title="'管理商品'"
      :desc="'点击管理现有商品'"
      :thumb="FoodManage"
    />
  </div>
</template>

<script lang="ts" setup>
import FoodAdd from '@/assets/imgs/food-add.png';
import FoodManage from '@/assets/imgs/food-manage.png';

const addProduct = () => {
  // Logic to add a product
  console.log('新增商品');
};

const manageProducts = () => {
  // Logic to manage products
  console.log('管理商品');
};
</script>

<style lang="less" scoped>
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
  display: flex;
  align-items: center; /* Center the icon and text vertically */
}

.header-icon {
  font-size: 28px; /* Adjust icon size */
  color: #007bff; /* Color for the icon */
  margin-right: 10px; /* Space between icon and text */
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