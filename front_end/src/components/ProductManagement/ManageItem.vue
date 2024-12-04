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
      <van-button size="small" type="primary" @click="editProduct">编辑</van-button>
      <van-button size="small" type="danger" @click="deleteProduct">删除</van-button>
  </template>
    </van-card>
  </div>
</template>

<script lang="ts" setup>
import useCreateDescription from '@/hooks/useCreateDescription'
import useCreateTag from '@/hooks/useCreateTag'
import { showConfirmDialog, showToast } from 'vant';
import router from '@/router'
import pubsub from 'pubsub-js'
const props = defineProps<{
    item: Items
}>();

const editProduct = () => {
  router.push('/product-form')
}

const deleteProduct = () => {
  showConfirmDialog({
    title: '确认删除',
    message:
      '是否确认删除商品？',
  })
    .then(() => {
      pubsub.publish('deleteProduct', props.item.id)
      showToast({type: 'success', message: '已通知系统删除商品'})
    })
    .catch(() => {});
}

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