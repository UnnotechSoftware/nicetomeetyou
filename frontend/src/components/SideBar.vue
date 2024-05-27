<template>
  <!--側邊欄-->
  <el-row class="menu-container">
    <el-col :span="12">
      <el-menu
          active-text-color="#ffd04b"
          background-color="#074c62"
          class="el-menu-vertical-demo"
          default-active="1"
          text-color="#fff"
      >
        <router-link to="/">
          <el-menu-item index="1">
            <el-icon><HomeFilled /></el-icon>
            <span>首頁</span>
          </el-menu-item>
        </router-link>
        <el-scrollbar height="500px">
          <template v-for="menu in menus" :key="menu.path">
            <el-sub-menu v-if="menu.children" :index="menu.path">
              <template #title>
                <el-icon>
                  <component :is="menu.icon"></component>
                </el-icon>
                <span>{{ menu.name }}</span>
              </template>
              <el-menu-item-group>
                <router-link v-for="(item,index) in menu.children"
                             :key="index"
                             :to=item.path
                             @click="addTabs(item)"

                >
                  <el-menu-item index="item.path">
                    {{ item.name }}
                  </el-menu-item>
                </router-link>
              </el-menu-item-group>
            </el-sub-menu>
          </template>
        </el-scrollbar>
      </el-menu>
    </el-col>
  </el-row>
</template>

<script setup lang="ts">
import {ref} from 'vue'
import {useDynamicTabs} from "../store";
import {tabsType} from "../utils/types/tabs";

const menus = ref([
  {
    icon: "Opportunity",
    name: "新聞",
    path: "bonds",
    children: [
      {path: "/admin_news/news", name: "新聞列表", menuId: 2000},
    ]
  },
])
const tabs = useDynamicTabs()
const addTabs = (row: tabsType) => {
  tabs.setTabsArray(row)
}
</script>

<style scoped>
.menu-container {
  position: fixed;
  top: 71px;
  left: 0;
  min-height: 100%;
  background-color: #074c62;
  z-index: 99;
}
.el-menu {
  border: none;
}
.fa-margin {
  margin-right: 5px;
}
.el-menu-vertical-demo:not(.el-menu--collapse) {
  width: 180px;
  min-height: 100vh;
}
.el-menu-vertical-demo {
  width: 35px;
}
.el-sub-menu .el-menu-item {
  min-width: 180px;
  padding-left: 48px !important;
}
a {
  text-decoration: none;
}
</style>