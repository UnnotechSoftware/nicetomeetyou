<template>
  <nav class="nav">
    <el-row>
      <el-col :span="12" class="logo-container">
        <img src="../assets/logo.png" class="logo" alt="logo" />
        <span class="title">焦點新聞管理</span>
      </el-col>
    </el-row>
  </nav>
</template>

<script  setup lang="ts">
import {useAuthStore} from '../store'
import router from "../router";

</script>

<style scoped>
.nav {
  width: 100%;
  height:60px;
  min-width: 600px;
  padding: 5px;
  background: #074c62;
  color: #fff;
  border-bottom: 1px solid #1f2d3d;

}
.logo-container {
  line-height: 60px;
  min-width: 400px;
}
.logo {
  height: 50px;
  width: 50px;
  margin-right: 5px;
  vertical-align: middle;
  display: inline-block;
}
.title {
  vertical-align: middle;
  font-size: 22px;
  letter-spacing: 3px;
}
.dropdown i {
  margin-top: 40px;
}
</style>