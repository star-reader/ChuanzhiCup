<template>
  <div class="container">
    <div class="column consumer">
      <van-icon name="user" class="icon" />
      <h2>消费者</h2>
      <p>这里是消费者的相关信息。</p>
      <button class="action-button">进入</button>
    </div>
    <div class="column distributor">
      <van-icon name="shop" class="icon" />
      <h2>经销商</h2>
      <p>这里是经销商的相关信息。</p>
      <button class="action-button">进入</button>
    </div>
  </div>
</template>

<script lang="ts" setup>
</script>

<style scoped>
.container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  min-height: 100vh;
  overflow: hidden;
  padding: 0 20px;
}

.column {
  width: 60%;
  max-width: 400px;
  text-align: center;
  margin: 10px 0;
  padding: 20px;
  border: none;
  border-radius: 16px;
  transition: background 0.3s ease;
  cursor: pointer;
}

.consumer {
  background: linear-gradient(135deg, #e0f7fa, #80deea);
}

.consumer:hover {
  background: linear-gradient(135deg, #80deea, #e0f7fa);
}

.distributor {
  background: linear-gradient(135deg, #ffe0b2, #ffcc80);
}

.distributor:hover {
  background: linear-gradient(135deg, #ffcc80, #ffe0b2);
}

.icon {
  font-size: 60px;
  margin-bottom: 10px;
}

.action-button {
  width: 80px;
  height: 40px;
  border: none;
  border-radius: 8px;
  background-color: #007bff;
  color: white;
  cursor: pointer;
  transition: background-color 0.3s, transform 0.3s;
}

.action-button:hover {
  background-color: #0056b3;
  transform: scale(1.05);
}
</style> 