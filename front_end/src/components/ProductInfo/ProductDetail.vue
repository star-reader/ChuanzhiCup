<template>
  <div class="product-detail-container">
    <van-card
      class="product-card"
      :title="props.item.name"
      :desc="useCreateDescription(props.item)"
      :thumb="props.item.image"
      :price="props.item.price"
    >
      <template #tags>
        <van-tag
          plain
          type="primary"
          v-for="tag in useCreateTag(props.item.tags)"
          :key="tag"
        >
          {{ tag }}
        </van-tag>
      </template>
      <template #footer>
        <van-button
          color="linear-gradient(to right, #ff6034, #ee0a24)"
          size="small"
          @click="addToCart"
        >
          加入购物车
        </van-button>
      </template>
    </van-card>

    <van-submit-bar
      v-show="totalPrice > 0"
      :price="totalPrice"
      button-text="去结算"
      @submit="onCheckout"
    />
  </div>
</template>

<script lang="ts" setup>
import { ref } from 'vue';
import useCreateDescription from '@/hooks/useCreateDescription';
import useCreateTag from '@/hooks/useCreateTag';

const props = defineProps<{
  item: Items;
}>();

const totalPrice = ref(0);

const addToCart = () => {
  totalPrice.value += props.item.price*100;
  console.log('加入购物车:', props.item.name);
};

const onCheckout = () => {
  
};
</script>

<style scoped>
.product-detail-container {
  /* min-height: calc(100vh - 50px); */
  height: 140px;
  width: 100%;
  padding: 0;
  background-color: #f9f9f9;
}

.product-card {
  width: 100%;
  max-width: 400px;
}
</style> 