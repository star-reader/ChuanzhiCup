<template>
  <div class="login-container">
    <h2>经销商登录</h2>
    <van-field v-model="authCode" placeholder="请输入授权码" />
    <van-field v-model="code" center clearable label="验证码" placeholder="">
        <template #button>
            <Verification :identifyCode="realCode" @click="refreshCode"></Verification>
        </template>
    </van-field>
    <van-button class="login-button" type="primary" @click="handleLogin">登录</van-button>
  </div>
</template>

<script lang="ts" setup>
import api from '@/config/api/api';
import router from '@/router';
import axios from 'axios';
import { showNotify } from 'vant';
import { onMounted, ref } from 'vue';

const authCode = ref('');
const identifyCodes = "1234567890abcdefjhijklinopqrsduvwxyz"
const code = ref('');
let realCode = ref('')

const handleLogin = () => {
  if (code.value !== realCode.value) {
    refreshCode()
    return showNotify({
      message: '验证码错误',
      type: 'danger'
    })
  }
  // for test
  router.push('/manage-index')
  axios.post(api.DistributorLogin,{authCode}).then(res => {
    localStorage.setItem('token', res.data.token)
    router.push('/manage-index')
  }).catch(err => {
    // showNotify({
    //   message: err.response.data.message,
    //   type: 'danger'
    // })
  })
};

const refreshCode = () => {
    realCode.value = "";
    makeCode(identifyCodes, 4);
}
    //获取验证码的值
const makeCode = (o: string, l: number) => {
    for (let i = 0; i < l; i++) {
        //通过循环获取字符串内随机几位
        realCode.value += identifyCodes[randomNum(0, identifyCodes.length)]
    }
}
    //随机数字：用于当角标拿字符串的值
const randomNum = (min: number, max: number) => {
    return Math.floor(Math.random() * (max - min) + min)
}


onMounted(() => {
  refreshCode()
})

</script>


<style scoped>
.login-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  min-height: 100vh;
  padding: 0 20px;
}

h2 {
  margin-bottom: 20px;
}

.van-field {
  width: 100%; /* Full width for mobile */
  margin-bottom: 15px; /* Space between fields */
}

.login-button {
  width: 100%; /* Full width for mobile */
  margin-top: 10px; /* Space between buttons */
  border-radius: 8px; /* Rounded corners */
  background-color: #007bff; /* Background color for login button */
  color: white; /* Text color for login button */
}
</style> 