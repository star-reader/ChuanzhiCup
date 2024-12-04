<template>
    <OrderList :pageFrom="from" />
</template>

<script lang='ts' setup>
import OrderList from '@/components/Orders/OrderList.vue'
import { ref } from 'vue';

const from = ref(location.search.includes('customer') ? 'customer' : 'distributor')

</script>

<style lang='less' scoped>

</style>