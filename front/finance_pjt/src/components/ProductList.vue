<template>
  <div>
    <div style="display: flex">
      <v-select
        label="은행"
        v-model="bankName"
        :items="props.bankNameProps"
        variant="outlined"
        class="mr-3"
        density="compact"
      ></v-select>
      <v-btn variant="outlined" @click="initialize" color="teal-darken-1">초기화</v-btn>
    </div>

    <v-data-table>
      <thead>
        <tr>
          <th class="text-left">공시 제출일</th>
          <th class="text-left">금융회사명</th>
          <th class="text-left">상품명</th>
          <th><button @click="sort6Months">6개월</button></th>
          <th><button @click="sort12Months">12개월</button></th>
          <th><button @click="sort24Months">24개월</button></th>
          <th><button @click="sort36Months">36개월</button></th>
        </tr>
      </thead>
      <tbody>
        <tr
          v-for="product of products"
          @click="
            router.push({
              name: 'detail',
              params: { product_id: product.id },
            })
          "
        >
          <td>{{ product.dcls_month }}</td>
          <td>
            {{ product.kor_co_nm }}
          </td>
          <td>
            {{ product.fin_prdt_nm }}
          </td>
          <td v-if="product.rates[4]">{{ product.rates[4] }}</td>
          <td v-else>-</td>
          <td v-if="product.rates[6]">{{ product.rates[6] }}</td>
          <td v-else>-</td>
          <td v-if="product.rates[8]">{{ product.rates[8] }}</td>
          <td v-else>-</td>
          <td v-if="product.rates[10]">{{ product.rates[10] }}</td>
          <td v-else>-</td>
        </tr>
      </tbody>
    </v-data-table>
  </div>
</template>

<script setup>
import { ref, watch, onMounted } from "vue";
import { useRouter } from "vue-router";

const props = defineProps({
  productsProps: Array,
  bankNameProps: Array,
});
const router = useRouter();

const products = ref(null);
const bankName = ref(null);

const sort6MonthsOption = ref("des");
const sort12MonthsOption = ref("des");
const sort24MonthsOption = ref("des");
const sort36MonthsOption = ref("des");

onMounted(() => {
  products.value = props.productsProps.sort(function (a, b) {
    return a.id - b.id;
  });
  bankName.value = "전체은행";
});

watch(bankName, (newValue) => {
  if (bankName.value == "전체은행") {
    products.value = props.productsProps;
  } else {
    products.value = props.productsProps.filter(
      (element) => element.kor_co_nm === newValue
    );
  }
});

const sort6Months = function () {
  if (sort6MonthsOption.value == "des") {
    products.value = products.value.sort(function (a, b) {
      return a.rates[4] - b.rates[4];
    });
    sort6MonthsOption.value = "asc";
  } else {
    products.value = products.value.sort(function (a, b) {
      return b.rates[4] - a.rates[4];
    });
    sort6MonthsOption.value = "des";
  }
};

const sort12Months = function () {
  if (sort12MonthsOption.value == "des") {
    products.value = products.value.sort(function (a, b) {
      return a.rates[6] - b.rates[6];
    });
    sort12MonthsOption.value = "asc";
  } else {
    products.value = products.value.sort(function (a, b) {
      return b.rates[6] - a.rates[6];
    });
    sort12MonthsOption.value = "des";
  }
};

const sort24Months = function () {
  if (sort24MonthsOption.value == "des") {
    products.value = products.value.sort(function (a, b) {
      return a.rates[8] - b.rates[8];
    });
    sort24MonthsOption.value = "asc";
  } else {
    products.value = products.value.sort(function (a, b) {
      return b.rates[8] - a.rates[8];
    });
    sort24MonthsOption.value = "des";
  }
};

const sort36Months = function () {
  if (sort36MonthsOption.value == "des") {
    products.value = products.value.sort(function (a, b) {
      return a.rates[10] - b.rates[10];
    });
    sort36MonthsOption.value = "asc";
  } else {
    products.value = products.value.sort(function (a, b) {
      return b.rates[10] - a.rates[10];
    });
    sort36MonthsOption.value = "des";
  }
};

const initialize = function () {
  products.value = props.productsProps.sort(function (a, b) {
    return a.id - b.id;
  });
  bankName.value = "전체은행";
};
</script>

<style scoped>
tbody > tr {
  cursor: pointer;
}
</style>
