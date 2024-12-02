<template>
  <div class="login-container">
    <h2>用户登录</h2>
    <van-field v-model="username" placeholder="请输入用户名" />
    <van-field v-model="password" type="password" placeholder="请输入密码" />
    <van-button class="login-button" type="primary" @click="handleLogin">登录</van-button>
    <van-button class="register-button" @click="handleRegister" plain>注册</van-button>
  </div>
</template>

<script lang="ts" setup>
import { ref } from 'vue';

const username = ref('');
const password = ref('');

const handleLogin = () => {
  // 登录逻辑
  console.log('登录:', username.value, password.value);
};

const handleRegister = () => {
  // 跳转到注册页面逻辑
  console.log('跳转到注册页面');
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

.login-button,
.register-button {
  width: 100%; /* Full width for mobile */
  margin-top: 10px; /* Space between buttons */
  border-radius: 8px; /* Rounded corners */
  border: none; /* Remove border */
}

.login-button {
  background-color: #007bff; /* Background color for login button */
  color: white; /* Text color for login button */
}

.register-button {
  background-color: transparent; /* No background for register button */
  color: #007bff; /* Text color for register button */
}
</style> 