<template>
  <div class="production-form">
    <van-nav-bar
      title="新增商品"
      left-text="返回"
      left-arrow
      @click-left="onClickLeft"
    />
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

      <div class="submit-button">
        <van-button round block type="primary" native-type="submit">
          提交
        </van-button>
      </div>
    </van-form>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import axios from 'axios';
import { showToast } from 'vant';
import router from '@/router';

const name = ref('');
const tags = ref('');
const price = ref();
const description = ref('');
const image = ref([]);
const period = ref('');
const ranking = ref('');

// Date picker
const showPicker = ref(false);

const onConfirm = ({ selectedValues }) => {
  period.value = selectedValues.join('/');
  showPicker.value = false;
};

const uploadFile = (file) => {
  // Logic to upload the file to the server
  console.log(file);
};

const onSubmit = () => {
  showToast({'type': 'success', 'message': '提交成功'})
  router.push('/manage-index')
};

const sendItemToServer = async (item) => {
  const response = await axios.post('/item/add', item, {
    headers: {
      Authorization: '',
    },
  });
};

const onClickLeft = () => history.back();
</script>

<style lang="less" scoped>
.production-form {
  margin: 0;
  padding: 0;
  height: 100vh; /* Set height to 100vh for full screen */
}

.submit-button {
  margin: 16px; /* Margin for the submit button */
}
</style>