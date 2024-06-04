<template>
  <div>
    <ProductList
      :products-props="store.deposits"
      :bank-name-props="store.depositBanks"
    />
  </div>
</template>

<script setup>
import { useFinanceStore } from "@/stores/finance";

import ProductList from "@/components/ProductList.vue";

const store = useFinanceStore();
</script>

<style scoped></style>
