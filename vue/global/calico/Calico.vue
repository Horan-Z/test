<i18n>
en:
  calico_label: Calico Params
  calico_description: Calico parameters.

zh:
  calico_label: Calico 配置
  calico_description: Calico 配置，用于设置 Calico 网络插件的变量。
  calico_ippool_cidr_place_holder: Calico ip pool CIDR
  calico_ippool_cidr_ipv6_place_holder: Calico ip pool CIDR ipv6
</i18n>

<template>
  <ConfigSection v-model:enabled="enabled" :label="t('calico_label')" :description="t('calico_description')" disabled
    anti-freeze>
    <EditRadio v-model="modelValue.all.children.target.children.k8s_cluster.vars.calico_ippool_vxlan"
      label="calico_ippool_vxlan" :prop="prop + '.calico_ippool_vxlan'" :options="options"></EditRadio>
    <EditString v-model="modelValue.all.children.target.children.k8s_cluster.vars.calico_ippool_cidr"
      prop="modelValue.all.children.target.children.k8s_cluster.vars.calico_ippool_cidr" label="calico_ippool_cidr"
      :placeholder="t('calico_ippool_cidr_place_holder')">
    </EditString>
    <EditString v-if="modelValue.all.children.target.vars.kube_network_dualstack_enabled"
      v-model="modelValue.all.children.target.children.k8s_cluster.vars.calico_ippool_cidr_ipv6"
      prop="modelValue.all.children.target.children.k8s_cluster.vars.calico_ippool_cidr_ipv6"
      label="calico_ippool_cidr_ipv6" :placeholder="t('calico_ippool_cidr_ipv6_place_holder')">
    </EditString>
  </ConfigSection>
</template>

<script lang="ts" setup>
import { inject, ref } from "vue"

const t = inject("t");

const modelValue = defineModel<any>();

const enabled = ref(true)

defineProps<{
  resourcePackage: any;
}>()


const prop = 'all.children.target.children.k8s_cluster.vars'

const options = [
  {
    label: "Always",
    value: "Always"
  },
  {
    label: "CrossSubnet",
    value: "CrossSubnet"
  },
  {
    label: "Never",
    value: "Never"
  }
]

</script>