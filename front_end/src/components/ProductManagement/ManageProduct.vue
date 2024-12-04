<template>
    <van-nav-bar
    class="product-list-nav"
      title="管理商品"
      left-text="返回"
      left-arrow
      @click-left="onClickLeft"
    />
    <div class="product-list">
        <ManageItem 
            v-for="item in list" 
            :key="item.id" 
            :item="item" 
        />
    </div>
</template>

<script lang='ts' setup>
import { ref } from 'vue';
import ManageItem from './ManageItem.vue';

const list = ref<Items[]>([{
    id: 1,
    name: 'test',
    tags: 'test,test2，test3',
    price: 1,
    description: 'test',
    image: 'https://fastly.jsdelivr.net/npm/@vant/assets/ipad.jpeg',
    createdAt: 'test',
    fresh_level: 'test',
    period: 'test',
    ranking: 1,
}]);

const onClickLeft = () => history.back()

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