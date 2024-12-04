<template>
  <div class="login-container">
    <h2>用户登录</h2>
    <van-field v-model="username" placeholder="请输入用户名" />
    <van-field v-model="password" type="password" placeholder="请输入密码" />
    <van-field v-model="code" center clearable label="验证码" placeholder="">
        <template #button>
            <Verification :identifyCode="realCode" @click="refreshCode"></Verification>
        </template>
    </van-field>
    <van-button class="login-button" type="primary" @click="handleLogin">登录</van-button>
    <van-button class="register-button" @click="handleRegister" plain>注册</van-button>
   
  </div>
</template>

<script lang="ts" setup>
import { onMounted, ref } from 'vue';

const username = ref('');
const password = ref('');
const identifyCodes = "1234567890abcdefjhijklinopqrsduvwxyz"
const code = ref('');
let realCode = ref('')

const handleLogin = () => {
  // 登录逻辑
  console.log('登录:', username.value, password.value);
};

const handleRegister = () => {
  console.log('跳转到注册页面');
};

const refreshCode = () => {
    realCode.value = "";
    makeCode(identifyCodes, 4);
}

const makeCode = (o: string, l: number) => {
    for (let i = 0; i < l; i++) {
        //通过循环获取字符串内随机几位
        realCode.value += identifyCodes[randomNum(0, identifyCodes.length)]
    }
}

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