<template>
  <div>
    <div style="display: flex">
      <h2 style="margin-right: 5px" class="mb-3">{{ category }}</h2>
    </div>
    <v-card :title="product[0]?.kor_co_nm + ' ' + product[0]?.fin_prdt_nm" variant="outlined" class="py-5 pl-3">
      <v-card-text>
        <div><strong>가입 방법: </strong>{{ product[0]?.join_way }}</div>
        <div>
          <strong>우대 조건</strong>
          <ul>
            <template v-for="condition in product[0]?.spcl_cnd.split(')')">
              <li v-if="condition.trim()" style="margin-left: 30px">
                {{ condition.trim() }}
              </li>
            </template>
          </ul>
        </div>
        <div><strong>가입 조건: </strong>{{ product[0]?.join_member }}</div>
        <div><strong>기타 유의사항: </strong>{{ product[0]?.join_member }}</div>
      </v-card-text>
      <v-card-actions>
        <v-btn v-if="communityStore.token && comment === '가입하기'" variant="outlined" width="100px" color="teal-darken-1">
          {{ comment }}
          <v-dialog activator="parent" class="w-50">
            <template v-slot:default="{ isActive }">
              <v-card>
                <v-card-title class="d-flex justify-space-between align-center">
                  <div>가입 정보를 입력하시오.</div>

                  <v-btn icon="mdi-close" variant="text" @click="isActive.value = false"></v-btn>
                </v-card-title>

                <v-divider></v-divider>

                <v-card-text>
                  <div>가입 금액</div>
                  <v-text-field variant="outlined" v-model="balance" :rules="balanceRule" class="w-75" density="compact"></v-text-field>
                  <div>가입 시점</div>
                  <v-date-input v-model="createdAt" max-width="368" :rules="createdAtRule" density="compact"></v-date-input>
                  <div>가입 기간</div>
                  <v-radio-group v-model="month">
                    <v-radio v-for="rate in rates" :label="Object.keys(rate) + '개월' + '  (' + Object.values(rate) + '%)'" :value="Object.keys(rate)"></v-radio>
                  </v-radio-group>
                </v-card-text>

                <v-divider class="mt-2"></v-divider>

                <v-card-actions>
                  <v-btn text="Cancel" @click="isActive.value = false"></v-btn>
                  <v-btn color="primary" text="Send" @click="isActive.value = false, subscribe()"></v-btn>
                </v-card-actions>
              </v-card>
            </template>
          </v-dialog>
        </v-btn>
        <v-btn v-if="communityStore.token && comment === '해지하기'" @click="subscribe" variant="outlined" width="100px" color="red">
          {{ comment }}
        </v-btn>
      </v-card-actions>
    </v-card>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import { useRoute, useRouter } from "vue-router";
import axios from "axios";
import { VDateInput } from "vuetify/lib/labs/components.mjs";

import { useFinanceStore } from "@/stores/finance";
import { useCommunityStore } from "@/stores/community";

const financeStore = useFinanceStore();
const communityStore = useCommunityStore();

const route = useRoute();
const router = useRouter();
const { product_id } = route.params;

const product = ref([]);
const category = ref(null);
const comment = ref("가입하기");

let isSubscribe = true;

const balance = ref(null);
const createdAt = ref(null);
const month = ref(null);
const rates = ref([]);

const balanceRule = ref([
  (value) => {
    if (parseInt(balance.value)) return true;
    return "정수를 입력하세요.";
  },
]);

const createdAtRule = ref([
  (value) => {
    if (new Date(createdAt.value).getFullYear() * 12 + new Date(createdAt.value).getMonth() < new Date().getFullYear() * 12 + new Date().getMonth()) return true;
    if (new Date(createdAt.value).getFullYear() === new Date().getFullYear() && new Date(createdAt.value).getMonth() === new Date().getMonth() && new Date(createdAt.value).getDate() < new Date().getDate()) return true;
    return "날짜를 다시 입력하세요."
  }
])

onMounted(() => {
  product.value = financeStore.deposits.filter(
    (element) => element.id == product_id
  );
  category.value = "정기예금 상세";
  if (product.value.length === 0) {
    product.value = financeStore.savings.filter(
      (element) => element.id == product_id
    );
    category.value = "정기적금 상세";
  }

  if (product.value[0].rates[4]) {
    rates.value.push({ 6: product.value[0].rates[4] });
  }
  if (product.value[0].rates[6]) {
    rates.value.push({ 12: product.value[0].rates[6] });
  }
  if (product.value[0].rates[8]) {
    rates.value.push({ 24: product.value[0].rates[8] });
  }
  if (product.value[0].rates[10]) {
    rates.value.push({ 36: product.value[0].rates[10] });
  }

  axios({
    method: "get",
    url: `${financeStore.BASE_URL}/finance/products/subscribe/`,
    params: {
      product: product_id,
    },
    headers: {
      Authorization: `Token ${communityStore.token}`,
    },
  })
    .then((res) => {
      if (0 < res.data.length) {
        isSubscribe = true;
      } else {
        isSubscribe = false;
      }
      if (isSubscribe) {
        comment.value = "해지하기";
      }
    })
    .catch((err) => {
      console.log(err);
    });
});

const subscribe = function () {
  if (comment.value === '가입하기') {
    if (!parseInt(balance.value)) {
      alert('가입 금액을 확인해주세요.')
      return
    }

    if (new Date(createdAt.value).getFullYear() === 1970) {
      alert('가입 시점을 확인해주세요.')
      return
    }

    if (new Date(createdAt.value).getFullYear() * 12 + new Date(createdAt.value).getMonth() > new Date().getFullYear() * 12 + new Date().getMonth()) {
      alert('가입 시점을 확인해주세요.')
      return
    }

    if (new Date(createdAt.value).getFullYear() === new Date().getFullYear() && new Date(createdAt.value).getMonth() === new Date().getMonth() && new Date(createdAt.value).getDate() >= new Date().getDate()) {
      alert('가입 시점을 확인해주세요.')
      return
    }

    if (!(month.value)) {
      alert('가입 기간을 확인해주세요.')
      return
    }
  }

  let interestRate = 0;
  for (const rate of rates.value) {
    if (Object.keys(rate)[0] == month.value) {
      interestRate = Object.values(rate)[0];
    }
  }

  axios({
    method: "post",
    url: `${financeStore.BASE_URL}/finance/products/subscribe/`,
    data: {
      product: product_id,
      balance: balance.value,
      profit:
        ((balance.value *
          ((new Date().getFullYear() -
            new Date(createdAt.value).getFullYear()) *
            12 +
            new Date().getMonth() -
            new Date(createdAt.value).getMonth())) /
          12) *
        (interestRate / 100),
      created_at: new Date(createdAt.value).toISOString(),
    },
    headers: {
      Authorization: `Token ${communityStore.token}`,
    },
  })
    .then((res) => {
      router.go(-1);
    })
    .catch((err) => {
      console.log(err);
    });
};
</script>

<style scoped>
.v-card-text>div {
  padding: 2px;
}
</style>
