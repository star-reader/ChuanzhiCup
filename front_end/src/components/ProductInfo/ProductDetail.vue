<template>
  <div class="product-detail-container">
    <van-card
      class="product-card"
      :title="props.item.name"
      :desc="useCreateDescription(props.item)"

      :price="props.item.price"
      :thumb="props.item.image"
    >
    <template #tags>
      <van-tag plain type="primary" v-for="i in useCreateTag(props.item.tags)">{{i}}</van-tag>
    </template>
      <template #footer>
        <van-button color="linear-gradient(to right, #ff6034, #ee0a24)" size="small">
          加入购物车
        </van-button>
      </template>
    </van-card>
  </div>
</template>

<script lang="ts" setup>
import useCreateDescription from '@/hooks/useCreateDescription'
import useCreateTag from '@/hooks/useCreateTag'
import { ref } from 'vue';

const props = defineProps<{
    item: Items
}>();


const addToCart = () => {
  
};
</script>

<style scoped>
.product-detail-container {
  min-height: 100vh;
  width: 100%;
  padding: 0;
  background-color: #f9f9f9; /* Light background for the container */
}

.product-card {
  width: 100%; /* Full width for mobile */
  max-width: 400px; /* Maximum width for larger screens */
}
</style> 