<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
import { onMounted } from 'vue'
import { GetProviderAvail } from '@/Composables/ProviderAvail'
onMounted(() => {
  GetProviderAvail()
})
</script>

<template>
  <div class=""></div>
</template>
