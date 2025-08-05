<i18n>
en:
  harbor_label: Harbor Params
  harbor_description: Harbor parameters.

zh:
  harbor_label: Harbor 配置
  harbor_description: Harbor 参数设置。
  harbor_vip_place_holder: Harbor virtual IP v4
  harbor_vip_ipv6_place_holder: Harbor virtual IP v6
</i18n>

<template>
  <ConfigSection v-model:enabled="enabled" :label="t('harbor_label')" :description="t('harbor_description')"
    disabled anti-freeze>
    <EditString v-model="modelValue.all.children.target.children.harbor.vars.harbor_vip" :prop="prop + '.harbor_vip'"
      label="harbor_vip" :placeholder="t('harbor_vip_place_holder')">
    </EditString>
    <EditString v-model="modelValue.all.children.target.children.harbor.vars.harbor_vip_ipv6" :prop="prop + '.harbor_vip_ipv6'"
      label="harbor_vip_ipv6" :placeholder="t('harbor_vip_ipv6_place_holder')">
    </EditString>
    <EditNumber v-model="modelValue.all.children.target.children.harbor.vars.harbor_vip_port"
      :prop="prop + '.harbor_vip_port'" label="harbor_vip_port">
    </EditNumber>
    <EditNumber v-model="modelValue.all.children.target.children.harbor.vars.harbor_metrics_port"
      :prop="prop + '.harbor_metrics_port'" label="harbor_metrics_port">
    </EditNumber>
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


const prop = 'all.children.target.children.harbor.vars'

</script>