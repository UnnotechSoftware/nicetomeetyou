<template>
  <el-dialog
      :draggable="true"
      :before-close="handleClose"
      v-model="detailShow"
      title="新聞詳情"
      width="60%"
  >
    <el-form
        :model="formData"
        ref="form"
        label-width="140px"
        style="margin: 10px; width: auto"
    >
      <el-form-item
          prop="content"
          label="內容">
        <el-input
            v-model="formData.content"
            :readonly="true"
            :disabled="true"/>
      </el-form-item>
      <el-form-item class="text-right">
        <el-button @click="handleClose">取消</el-button>
      </el-form-item>
    </el-form>
  </el-dialog>
</template>

<script setup lang="ts">
import {ref, watch} from "vue"
import {FormInstance} from "element-plus";
import { bondType } from '../../../utils/types/bond'
import { bondRulesType } from "../../../utils/rules/bond";

const form = ref<FormInstance>()
const props = defineProps({
  detailShow: {
    type: Boolean
  },
  detailData: {
    type: Object
  }
})
let formData = ref(props.detailData)

const handleClose = () => {
  emits("closeDetailNews")
}

const emits = defineEmits(["closeDetailNews"])


watch(() => props.detailData
    , () => {
      formData.value = props.detailData
    })
</script>

<style scoped>
</style>