<template>
  <v-container>
    <v-select
      label="상품 종류"
      variant="outlined"
      v-model="bankType"
      :items="['정기 예금', '정기 적금']"
      density="compact"
    ></v-select>
    <RouterView />
  </v-container>
</template>

<script setup>
import { onMounted, ref, watch } from "vue";
import { RouterView, useRouter } from "vue-router";
import { useFinanceStore } from "@/stores/finance";

const store = useFinanceStore();
const router = useRouter();
const bankType = ref("정기 예금");

onMounted(() => {
  if (store.deposits.length === 0 && store.savings.length == 0) {
    store.getProducts();
  }
});

watch(bankType, (newValue) => {
  if (bankType.value == "정기 예금") {
    router.push({ name: "deposit" });
  } else {
    router.push({ name: "saving" });
  }
});
</script>

<style scoped></style>
