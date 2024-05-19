<template>
  <el-dialog
      :draggable="true"
      :before-close="handleClose"
      v-model="detailShow"
      title="標的詳情"
      width="60%"
  >
    <el-form
        :model="formData"
        ref="form"
        label-width="140px"
        style="margin: 10px; width: auto"
    >
      <el-form-item
          label="ISIN"
          prop="isin"
      >
        <el-input
            v-model="formData.isin"
            :readonly="true"
            :disabled="true"
        />
      </el-form-item>
      <el-form-item
          prop="issue_name"
          label="發行名稱"
      >
        <el-input
            v-model="formData.issue_name"
            :readonly="true"
            :disabled="true">
        </el-input>
      </el-form-item>
      <el-form-item
          prop="issuer"
          label="發行人"
      >
        <el-input
            v-model="formData.issuer"
            :readonly="true"
            :disabled="true"/>
      </el-form-item>

      <el-form-item
          prop="parent_company"
          label="母公司"
      >
        <el-input
            v-model="formData.parent_company"
            :readonly="true"
            :disabled="true"
        />
      </el-form-item>

      <el-form-item
          prop="origin_company_industry"
          label="母公司產業"
      >
        <el-input
            v-model="formData.parent_company_industry"
            :readonly="true"
            :disabled="true"/>
      </el-form-item>

      <el-form-item
          prop="sp_credit_rating"
          label="信評 S&P">
        <el-input
            v-model="formData.credit_rating_sp"
            :readonly="true"
            :disabled="true"/>
      </el-form-item>
      <el-form-item
          prop="fitch_credit_rating"
          label="信評 Fitch"
      >
        <el-input
            v-model="formData.credit_rating_fitch"
            :readonly="true"
            :disabled="true"/>
      </el-form-item>
      <el-form-item
          prop="moody_credit_rating"
          label="信評 Moody's">
        <el-input
            v-model="formData.credit_rating_moody"
            :readonly="true"
            :disabled="true"/>
      </el-form-item>
      <el-form-item
          prop="country_credict.credit_rating_moody"
          label="國家信評 S&P">
        <el-input
            v-model="formData.country_credict.credit_rating_sp"
            :readonly="true"
            :disabled="true"/>
      </el-form-item>
      <el-form-item
          prop="country_credict.credit_rating_fitch"
          label="國家信評 Fitch">
        <el-input
            v-model="formData.country_credict.credit_rating_fitch"
            :readonly="true"
            :disabled="true"/>
      </el-form-item>
      <el-form-item
          prop="country_credict.credit_rating_moody"
          label="國家信評 Moody's">
        <el-input
            v-model="formData.country_credict.credit_rating_moody"
            :readonly="true"
            :disabled="true"/>
      </el-form-item>
      <el-form-item
          prop="maturity_date"
          label="到期日">
        <el-input
            v-model="formData.maturity_datetime"
            :readonly="true"
            :disabled="true"
        />
      </el-form-item>
      <el-form-item
          prop="currency"
          label="幣別"
      >
        <el-input
            v-model="formData.currency"
            :readonly="true"
            :disabled="true"
        />
      </el-form-item>
      <el-form-item
          prop="issue_size"
          label="發行總量">
        <el-input
            v-model="formData.issue_size"
            :readonly="true"
            :disabled="true"/>
      </el-form-item>
      <el-form-item
          prop="annual_coupon_frequency"
          label="配息頻率">
        <el-input
            v-model="formData.annual_coupon_frequency"
            :readonly="true"
            :disabled="true"/>
      </el-form-item>
      <el-form-item
          prop="coupon_dates"
          label="配息日">
        <el-input
            v-model="formData.coupon_dates"
            :readonly="true"
            :disabled="true"/>
      </el-form-item>
      <el-form-item
          prop="annual_coupon_rate"
          label="票面利率(%)">
        <el-input
            v-model="formData.annual_coupon_rate"
            :readonly="true"
            :disabled="true"/>
      </el-form-item>
      <el-form-item
          prop="minimum_investment_quantity"
          label="最低交易面額">
        <el-input
            v-model="formData.minimum_investment_quantity"
            :readonly="true"
            :disabled="true"/>
      </el-form-item>
      <el-form-item
          prop="債券種類"
          label="債券種類">
        <el-input
            v-model="formData.bond_type"
            :readonly="true"
            :disabled="true"/>
      </el-form-item>
      <el-form-item
          prop="seniority"
          label="清償順位">
        <el-input
            v-model="formData.seniority"
            :readonly="true"
            :disabled="true"/>
      </el-form-item>
      <el-form-item
          prop="coupon_type"
          label="利息分類">
        <el-input
            v-model="formData.coupon_type"
            :readonly="true"
            :disabled="true"/>
      </el-form-item>
      <el-form-item
          prop="issue_datetime"
          label="發行日">
        <el-input
            v-model="formData.issue_datetime"
            :readonly="true"
            :disabled="true"/>
      </el-form-item>
      <el-form-item
          prop="擔保人"
          label="擔保人"
      >
        <el-input
            v-model="formData.guarantor"
            :readonly="true"
            :disabled="true"/>
      </el-form-item>
      <el-form-item
          prop="is_callable"
          label="是否可提前買回">
        <el-input
            v-model="formData.is_callable"
            :readonly="true"
            :disabled="true"/>
      </el-form-item>
      <el-form-item
          prop="callable_dates"
          label="提前贖回日">
        <el-input
            v-model="formData.callable_dates"
            :readonly="true"
            :disabled="true"/>
      </el-form-item>
      <el-form-item
          prop="bond_contract_type"
          label="債券條款">
        <el-input
            v-model="formData.bond_contract_type"
            :readonly="true"
            :disabled="true"/>
      </el-form-item>
      <el-form-item
          prop="callable_price"
          label="提前贖回價">
        <el-input
            v-model="formData.callable_price"
            :readonly="true"
            :disabled="true"/>
      </el-form-item>
      <el-form-item
          prop="investor"
          label="投資人身份限制">
        <el-input
            v-model="formData.investor"
            :readonly="true"
            :disabled="true"/>
      </el-form-item>
      <el-form-item
          prop="introduction"
          label="發行人或母公司介紹">
        <el-input
            v-model="formData.introduction"
            :readonly="true"
            :disabled="true"/>
      </el-form-item>
      <el-form-item
          prop="note"
          label="備註">
        <el-input
            v-model="formData.note"
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
  emits("closeDetailBond")
}

const emits = defineEmits(["closeDetailBond"])


watch(() => props.detailData
    , () => {
      formData.value = props.detailData
    })
</script>

<style scoped>
</style>