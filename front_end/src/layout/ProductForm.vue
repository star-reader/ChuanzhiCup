<template>
<div class="production-form">
<van-form @submit="onSubmit">
  <van-cell-group inset>
    <van-field
      v-model="name"
      name="商品名"
      label="商品名"
      placeholder="商品名"
      :rules="[{ required: true, message: '请填写商品名' }]"
    />

    <van-field
      v-model="price"
      name="价格"
      label="价格"
      placeholder="价格"
      type="number"
      :rules="[{ required: true, message: '请填写价格' }]"
    />
    <van-field
      v-model="tags"
      name="标签"
      label="标签"
      placeholder="用,或，分割标签"
    />
    <van-field
      v-model="description"
      name="描述"
      label="描述"
      placeholder="商品描述"
    />
    <van-field
        v-model="period"
        is-link
        readonly
        name="datePicker"
        label="保质期"
        placeholder="点击选择时间"
        @click="showPicker = true"
    />
    <van-popup v-model:show="showPicker" position="bottom">
        <van-date-picker @confirm="onConfirm" @cancel="showPicker = false" />
    </van-popup>

    <van-field name="uploader" label="文件上传" :after-read="uploadFile">
      <template #input>
        <van-uploader v-model="image" />
      </template>
    </van-field>

  </van-cell-group>
  
  <div  class="submit-button">
    <van-button round block type="primary" native-type="submit">
      提交
    </van-button>
  </div>
</van-form>
</div>

</template>

<script setup >

import { ref } from 'vue';
import axios from 'axios';

const name = ref('')
const tags = ref('')
const price = ref()
const description = ref('')
const image = ref([])
const period = ref('')
const ranking = ref()

//date
const showPicker = ref(false);


const onConfirm = ({ selectedValues }) => {
      period.value = selectedValues.join('/');
      showPicker.value = false;
    };


const uploadFile = (file) => {
      // 此时可以自行将文件上传至服务器
  console.log(file);
};




const onSubmit = () => {
  console.log({
    "name":name.value
  })
}


const sendItem2server = async (item) => {
    Response = await axios.post("/item/add",item,{
        headers: {
            "Authoriztion":''
        }
    })
}
</script>

<style lang="less" scoped>
.production-form {
  margin: 0;
  padding: 0;
  margin-top: 50px;
  height: 100vh; /* 设置高度为100vh以实现全屏 */
  //padding: 0 16px; /* 调整内边距以适应移动端 */
  //background-color: #f9f9f9; /* 轻背景色 */
}

.submit-button {
  margin: 16px; /* 提交按钮的上下边距 */
}
</style>