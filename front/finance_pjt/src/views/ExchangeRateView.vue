<template>
  <v-container>
    <div class="text-h4">환율 계산기</div>
    <v-col>
      <p>
        비영업일의 데이터, 혹은 영업당일 11시 이전에는 환율 계산기가 제대로
        작동하지 않을 수 있습니다.
      </p>
    </v-col>
    <v-col>
      <v-select
        variant="outlined"
        label="통화 선택"
        name="country"
        v-model="selectCountry"
        :items="countryNames"
        class="w-75"
      >
      </v-select>
      <br />
      <v-text-field
        variant="outlined"
        :label="selectCountry"
        type="text"
        v-model="koreaCurrency"
        @input="input2"
        :disabled="selectCountry === null"
        class="w-75"
      />
      <v-text-field
        variant="outlined"
        label="대한민국 원"
        type="text"
        v-model="foreignCurrency"
        @input="input1"
        :disabled="selectCountry === null"
        class="w-75"
      />
    </v-col>
  </v-container>
</template>

<script setup>
import axios from "axios";
import { onMounted, ref } from "vue";
import { useCommunityStore } from "@/stores/community";
import { watch } from "vue";

const countries = ref([]);
const selectCountry = ref(null);
const foreignCurrency = ref(null);
const koreaCurrency = ref(null);
let changeRate = 1;
let userTarget = "input1";
const countryNames = ref([]);

onMounted(() => {
  const store = useCommunityStore();
  axios({
    method: "get",
    url: "http://127.0.0.1:8000/finance/exchange_rate/",
    headers: {
      Authorization: store.token,
    },
  })
    .then((res) => {
      console.log(res);
      for (const data of res.data.data) {
        countries.value.push(data);
        countryNames.value.push(data.cur_nm);
      }
    })
    .catch((err) => {
      console.log(err);
    });
});

watch(selectCountry, (newVal) => {
  change();
});

const change = function () {
  console.log("hi");
  const target = countries.value.find((ele) => {
    return ele.cur_nm === selectCountry.value;
  });
  changeRate = target.kftc_deal_bas_r;
  console.log(changeRate);
  if (userTarget == "input1") {
    input1();
  } else {
    input2();
  }
};

const input1 = function () {
  koreaCurrency.value = (foreignCurrency.value / changeRate).toFixed(2);
  userTarget = "input1";
};

const input2 = function () {
  foreignCurrency.value = (koreaCurrency.value * changeRate).toFixed(2);
  console.log(changeRate);
  userTarget = "input2";
};
</script>

<style scoped></style>
