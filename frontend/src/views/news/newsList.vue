<template>
  <div class="fillcontain">
    <div>
      <el-card class="box-card">
        <template #header>
          <div class="card-header">
            <span>新聞資訊</span>
          </div>
        </template>
        <div>
        </div>
        <el-table
            :data="tableData"
            style="width: 100%"
            max-height="450"
            border
            v-if="tableData.length > 0"
        >
          <el-table-column label="標的名稱" align="center" width="220" prop="issue_name"/>
          <el-table-column label="ISIN" align="center" width="auto" prop="isin"/>
          <el-table-column label="Moody's" align="center" width="auto" prop="credit_rating_moody"/>
          <el-table-column label="Fitch" align="center" width="auto" prop="credit_rating_fitch"/>
          <el-table-column label="SP" align="center" width="auto" prop="credit_rating_sp"/>
          <el-table-column label="發行人" align="center" width="220" prop="issuer"/>
          <el-table-column label="幣別" align="center" width="auto" prop="currency"/>
          <el-table-column label="操作" align="center" width="auto" prop="operation">
            <template #default="scope">
              <el-row justify="center">
                <el-col span="8">
                  <el-button
                      size="small"
                      type="info"
                      @click="handleDetail(scope.row)"
                      link
                  >詳情
                  </el-button>
                </el-col>
              </el-row>
            </template>
          </el-table-column>
        </el-table>
        <el-table
            v-else
            border
        >
          <el-table-column label="標的名稱" align="center" width="auto" prop="issue_name"/>
          <el-table-column label="ISIN" align="center" width="auto" prop="isin"/>
          <el-table-column label="Moody's" align="center" width="auto" prop="credit_rating_moody"/>
          <el-table-column label="Fitch" align="center" width="auto" prop="credit_rating_fitch"/>
          <el-table-column label="SP" align="center" width="auto" prop="credit_rating_sp"/>
          <el-table-column label="發行人" align="center" width="auto" prop="issuer"/>
          <el-table-column label="幣別" align="center" width="auto" prop="currency"/>
          <el-table-column label="操作" align="center" width="auto" prop="operation"/>
        </el-table>
        <el-row>
          <el-col :span="24">
            <div class="pagination">
              <el-pagination
                  v-model:currentPage="page_index"
                  v-model:page-size="page_size"
                  small="small"
                  :layout="layout"
                  :total="total"
                  @current-change="handleCurrentChange"
              />
            </div>
          </el-col>
        </el-row>
      </el-card>
    </div>
  </div>
  <DialogDetail :detailShow="detailShow"
                @closeDetailBond="detailShow = false"
                :detailData="detailData"
  />
</template>

<script lang="ts" setup>
import {onMounted, ref, watchEffect} from 'vue'
import api from '../../utils/http';
import DialogDetail from "./components/DialogDetail.vue"

const tableData = ref([])
const detailShow = ref(false)
const detailData = ref()


const page_index = ref(1), // 當前位於哪一頁
    page_size = ref(5),  // 一頁最多有幾筆
    total = ref(0),  // 總筆數
    layout = "total, prev, pager, next, jumper"  // 翻頁屬性

const handleDetail = (row: any) => {
  detailShow.value = true
  detailData.value = row
}


const getBonds = async () => {
  const resp = await api.get("/bonds")
  const result = resp.data
  if (result.code === 200) {
    tableData.value = result.data
  } else {
    tableData.value = []
  }
  setPaginations(result.meta)
}

onMounted(() => {
  getBonds()
})

const handleCurrentChange = async (page: number) => {
  const resp = await api.get(`/bonds?page=${page}`)
  const result = resp.data
  if (result.code === 200) {
    tableData.value = result.data
  } else {
    tableData.value = []
  }
  setPaginations(result.meta)
}

const setPaginations = (pageMeta: any) => {
  total.value = pageMeta.total
  page_index.value = pageMeta.page;
  page_size.value = pageMeta.per_page;
}

</script>

<style scoped>

</style>