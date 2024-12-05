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
      
      <h2>
        <van-icon name="cart" class="header-icon" /> 订单管理
      </h2>
      
      <van-card
        class="product-item"
        @click="manageOrders"
        :title="'管理订单'"
        :desc="'点击管理现有订单'"
        :thumb="OrderManage"
      />
    </div>
</template>
  
<script lang="ts" setup>
import FoodAdd from '@/assets/imgs/food-add.png';
import FoodManage from '@/assets/imgs/food-manage.png';
import OrderManage from '@/assets/imgs/order-manage.png';
import router from '@/router';
  
const addProduct = () => router.push('/product-form')
  
const manageProducts = () => router.push('/manage-product')
  
const manageOrders = () => router.push('/order-list')
  
</script>
  
<style lang="less" scoped>
.product-list-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  min-height: 100vh;
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

.product-item {
  width: 100%;
  max-width: 400px;
  margin: 10px 0;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.product-item:hover {
  background-color: #e0f7fa;
}
</style> 