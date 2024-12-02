<template>
  <div class="register-container">
    <van-field v-model="username" placeholder="用户名" />
    <van-field v-model="password" type="password" placeholder="密码" />
    <van-field v-model="confirmPassword" type="password" placeholder="确认密码" />
    <van-button type="primary" @click="handleRegister">注册</van-button>
    <van-button @click="$router.push('/login')">登录</van-button>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';

export default defineComponent({
  data() {
    return {
      username: '',
      password: '',
      confirmPassword: ''
    };
  },
  methods: {
    handleRegister() {
      // 注册逻辑
      console.log('注册:', this.username, this.password);
    }
  }
});
</script>

<style scoped>
.register-container {
  padding: 20px;
}
</style> 