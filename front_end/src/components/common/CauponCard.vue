<template>
    <!-- Coupon Cell -->
    <van-coupon-cell
        :coupons="coupons"
        :chosen-coupon="chosenCoupon"
        @click="showList = true"
        />
        <!-- Coupon List -->
        <van-popup
        v-model:show="showList"
        round
        position="bottom"
        style="height: 90%; padding-top: 4px;"
        >
        <van-coupon-list
            :coupons="coupons"
            :chosen-coupon="chosenCoupon"
            :disabled-coupons="disabledCoupons"
            @change="onChange"
            @exchange="onExchange"
        />
    </van-popup>
</template>

<script lang='ts' setup>
import { ref } from 'vue';

const coupon = {
    available: 1,
    originCondition: 0,
    reason: '',
    value: 150,
    name: '水果品鉴官优惠卷',
    startAt: 1489104000,
    endAt: 1614592000,
    valueDesc: '5.5',
    unitDesc: '元',
};

const coupons = ref([coupon]);
const showList = ref(false);
const chosenCoupon = ref(-1);

const onChange = (index) => {
    showList.value = false;
    chosenCoupon.value = index;
};
const onExchange = (code) => {
    coupons.value.push(coupon);
};
</script>

<style lang='less' scoped>

</style>