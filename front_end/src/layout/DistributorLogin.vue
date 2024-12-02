<template>
  <div class="login-container">
    <h2>经销商登录</h2>
    <van-field v-model="authCode" placeholder="请输入授权码" />
    <van-button class="login-button" type="primary" @click="handleLogin">登录</van-button>
  </div>
</template>

<script lang="ts" setup>
import { ref } from 'vue';

const authCode = ref('');

const handleLogin = () => {
  // 登录逻辑
  console.log('登录:', authCode.value);
};
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