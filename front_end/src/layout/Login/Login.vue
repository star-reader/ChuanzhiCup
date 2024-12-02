<template>
  <div class="login-container">
    <van-field v-model="username" placeholder="用户名" />
    <van-field v-model="password" type="password" placeholder="密码" />
    <van-button type="primary" @click="handleLogin">登录</van-button>
    <van-button @click="$router.push('/register')">注册</van-button>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';

export default defineComponent({
  data() {
    return {
      username: '',
      password: ''
    };
  },
  methods: {
    handleLogin() {
      // 登录逻辑
      console.log('登录:', this.username, this.password);
    }
  }
});
</script>

<style scoped>
.login-container {
  padding: 20px;
}
</style> 