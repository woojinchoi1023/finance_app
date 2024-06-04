<template>
  <div>
    <ProductList
      :products-props="store.savings"
      :bank-name-props="store.savingBanks"
    />
  </div>
</template>

<script setup>
import { useFinanceStore } from "@/stores/finance";

import ProductList from "@/components/ProductList.vue";

const store = useFinanceStore();
</script>

<style scoped></style>
