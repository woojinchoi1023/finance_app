<template>
  <v-container>
    <v-col>
      <span class="text-h4"
        >{{ info?.nickname ? info.nickname : info.username }}님의 프로필
        페이지</span
      >
    </v-col>
    <div class="infoView" v-show="!updateView">
      <v-table class="text-subtitle-1">
        <tbody>
          <tr>
            <td>이름</td>
            <td>{{ info.first_name }}{{ info.last_name }}</td>
          </tr>
          <tr>
            <td>ID</td>
            <td>{{ info.username }}</td>
          </tr>
          <tr>
            <td>닉네임</td>
            <td>{{ info.nickname }}</td>
          </tr>
          <tr>
            <td>email</td>
            <td>{{ info.email }}</td>
          </tr>
          <tr>
            <td>가입 날짜</td>
            <td>
              {{ info.date_joined.slice(0, 10) }}
              {{ info.date_joined.slice(11, 19) }}
            </td>
          </tr>
              <v-btn
                @click="
                  () => {
                    updateView = !updateView;
                  }
                "
                variant="outlined"
                class="mt-5"
                color="teal-darken-1"
                >정보 수정</v-btn
              >
        </tbody>
      </v-table>
    </div>
    <div class="changeView" v-show="updateView" style="margin-bottom: 10px">
      <form @submit.prevent="update">
        <div class="text-h6 my-3">기본 정보 수정</div>
        <v-text-field label="Email" v-model="email"></v-text-field>
        <v-text-field label="First Name" v-model="first_name"></v-text-field>
        <v-text-field label="Last Name" v-model="last_name"></v-text-field>
        <v-text-field label="닉네임" v-model="nickname"></v-text-field>
        <v-btn
          @click="
            () => {
              updateView = !updateView;
            }
          "
          variant="outlined"
          style="margin-right: 4px"
          >돌아가기</v-btn
        >
        <v-btn type="submit" variant="outlined" color="teal-darken-1">업데이트</v-btn>
      </form>
    </div>
    <div>
      <v-card title="가입 상품" variant="outlined" class="mt-16 mb-5">
        <v-card-text class="text-subtitle-1">
          <v-list>
            <v-list-item
              v-for="subscribe in subscribes"
              :key="subscribe.id"
              @click="
                router.push({
                  name: 'detail',
                  params: { product_id: subscribe.product.id },
                })
              "
            >
              {{ subscribe.product.fin_prdt_nm }}
              <span class="text-green">[+{{ parseInt(subscribe.profit) }}원]</span>
            </v-list-item>
          </v-list>
        </v-card-text>
      </v-card>
    </div>
    <div class="chart">
      <canvas ref="barChart"></canvas>
    </div>
  </v-container>
</template>

<script setup>
import { onMounted, ref } from "vue";
import { useRoute, RouterLink } from "vue-router";
import { useCommunityStore } from "@/stores/community";
import { useFinanceStore } from "@/stores/finance";

import axios from "axios";
import { computed } from "vue";

import { Chart } from "chart.js/auto";
import router from "@/router";

const subscribes = ref([]);
const route = useRoute();
const communityStore = useCommunityStore();
const financeStore = useFinanceStore();
const info = computed(() => communityStore.userInfo);
const email = ref(null);
const nickname = ref(null);
const first_name = ref(null);
const last_name = ref(null);
const updateView = ref(false);

const barChart = ref(null);

onMounted(() => {
  axios({
    method: "get",
    url: "http://127.0.0.1:8000/finance/products/subscribe_list/",
    headers: {
      Authorization: `Token ${communityStore.token}`,
    },
  })
    .then((res) => {
      subscribes.value = res.data;
      initChart(res.data);
    })
    .catch((err) => {
      console.log(err);
    });
  email.value = communityStore.userInfo.email;
  nickname.value = communityStore.userInfo.nickname;
  first_name.value = communityStore.userInfo.first_name;
  last_name.value = communityStore.userInfo.last_name;
});

const initChart = (data) => {
  const labels = [];
  const profits = [];
  data.forEach((element) => {
    labels.push(element.product.fin_prdt_nm);
    profits.push(element.profit);
  });

  const ctx = barChart.value.getContext("2d");
  new Chart(ctx, {
    type: "bar",
    data: {
      labels: labels,
      datasets: [
        {
          label: "수익 (대한민국 원)",
          backgroundColor: [
            "#bbdefb",
            "#ffcdd2",
            "#c8e6c9",
            "#fff9c4",
          ],
          barThickness: 100,
          data: profits,
        },
      ],
    },
    options: {
      legend: { display: false },
      title: {
        display: true,
        text: "그래프",
      },
    },
  });
};

const update = () => {
  axios({
    method: "put",
    url: `http://127.0.0.1:8000/accounts/${communityStore.userInfo.id}/`,
    headers: {
      Authorization: `Token ${communityStore.token}`,
    },
    data: {
      email: email.value,
      nickname: nickname.value,
      first_name: first_name.value,
      last_name: last_name.value,
    },
  })
    .then((res) => {
      communityStore.userInfo = res.data;
      updateView.value = false;
    })
    .catch((err) => {
      console.log(err);
    });
};
</script>

<style scoped>
li {
  margin-left: 40px;
  cursor: pointer;
}
</style>
