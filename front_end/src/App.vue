<template>
    <RouterView />
</template>

<script lang='ts' setup>
import { RouterView } from 'vue-router'
</script>

<style lang='less' scoped>
body {
  margin: 0;
  padding: 0;
  overflow-x: hidden; /* Prevent horizontal overflow */
}
</style>