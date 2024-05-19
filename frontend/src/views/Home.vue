<template>
  <div class="home">
    <Navbar/>
    <SideBar/>
    <div class="container-right">
      <router-view/>
    </div>
  </div>
</template>

<script setup lang="ts">
import Navbar from '../components/Navbar.vue'
import SideBar from "../components/SideBar.vue";

</script>

<style scoped>
.home {
  width: 100%;
  height: 100%;
  background-size: 100% 100%;
}
.container-right {
  position: relative;
  top: 0;
  left: 180px;
  width: calc(100% - 180px);
  height: calc(100% - 71px);
  overflow: auto;
}
</style>