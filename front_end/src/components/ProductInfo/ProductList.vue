<template>
    <van-nav-bar
    class="product-list-nav"
      title="商品列表"
      left-text="返回"
      left-arrow
      @click-left="onClickLeft"
    />
    <div class="product-list">
        <ProductDetail 
            v-for="item in list" 
            :key="item.id" 
            :item="item" 
        />
    </div>
    <van-submit-bar
      v-show="totalPrice > 0"
      :price="totalPrice"
      button-text="去结算">
        <CauponCard />
    </van-submit-bar>
</template>

<script lang='ts' setup>
import { onMounted, ref } from 'vue';
import pubsub from 'pubsub-js';
import ProductDetail from './ProductDetail.vue';
import products from '@/config/data/products'
import axios from 'axios';
import api from '@/config/api/api';
import CauponCard from '@/components/common/CauponCard.vue';

const list = ref<Items[]>(products);
const totalPrice = ref(0);

const onClickLeft = () => history.back()

onMounted(() => {
    axios.get(api.GetProducts)
    .then(res => {
        list.value = res.data;
    })
    pubsub.subscribe('addToCart', (_, price) => {
        totalPrice.value += price;
    })
})

</script>

<style lang='less' scoped>
.product-list-nav {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
}
.product-list {
    position: relative;
    top: 50px;
    left: 0;
    width: 100%;
    height: calc(100% - 50px);
    overflow: hidden auto;
    touch-action: none;
}
</style>