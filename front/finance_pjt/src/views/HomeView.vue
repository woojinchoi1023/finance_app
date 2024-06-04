<template>
  <v-container>
    <!-- Carousel Section -->
    <v-carousel show-arrows="hover" :cycle="true" interval="3000">
      <v-carousel-item
        src="https://pentagonal-fir-043.notion.site/image/https%3A%2F%2Fprod-files-secure.s3.us-west-2.amazonaws.com%2F7279217f-4624-488b-944f-2d58ebc80e14%2F045dc35f-772b-470f-8528-2aef614f0a43%2F001.png?table=block&id=15ffe138-2d13-47c9-8e93-c41f116c0e27&spaceId=7279217f-4624-488b-944f-2d58ebc80e14&width=1420&userId=&cache=v2"
        cover
      >
      </v-carousel-item>
      <v-carousel-item
        src="https://pentagonal-fir-043.notion.site/image/https%3A%2F%2Fprod-files-secure.s3.us-west-2.amazonaws.com%2F7279217f-4624-488b-944f-2d58ebc80e14%2F1ac0c1f7-23da-47bb-9681-04a5e9df6d53%2F002.png?table=block&id=6460eb50-82d9-4555-9be5-15702a3bc444&spaceId=7279217f-4624-488b-944f-2d58ebc80e14&width=1420&userId=&cache=v2"
        cover
        @click="router.push({ name: 'community' })"
      >
      </v-carousel-item>
      <v-carousel-item
        src="https://pentagonal-fir-043.notion.site/image/https%3A%2F%2Fprod-files-secure.s3.us-west-2.amazonaws.com%2F7279217f-4624-488b-944f-2d58ebc80e14%2F80cc71de-39e4-42ee-8589-6b77faee799d%2F003.png?table=block&id=7f6c008a-82e9-4608-b2f8-bfc0fd016d88&spaceId=7279217f-4624-488b-944f-2d58ebc80e14&width=1420&userId=&cache=v2"
        cover
        @click="router.push({ name: 'map' })"
      ></v-carousel-item>
      <v-carousel-item
        src="https://pentagonal-fir-043.notion.site/image/https%3A%2F%2Fprod-files-secure.s3.us-west-2.amazonaws.com%2F7279217f-4624-488b-944f-2d58ebc80e14%2F33d30705-4313-496e-a153-cf454d115bb5%2F004.png?table=block&id=2f948da1-9be8-4c57-b22f-39be787dcdde&spaceId=7279217f-4624-488b-944f-2d58ebc80e14&width=1420&userId=&cache=v2"
        cover
        @click="router.push({ name: 'exchangeRate' })"
      ></v-carousel-item>
    </v-carousel>

    <img
      src="https://pentagonal-fir-043.notion.site/image/https%3A%2F%2Fprod-files-secure.s3.us-west-2.amazonaws.com%2F7279217f-4624-488b-944f-2d58ebc80e14%2F4e84bb8a-5932-468d-8049-833cec7078d2%2Fmain_(1).png?table=block&id=79fdf54d-4c73-4e48-8312-25f3bebe15ca&spaceId=7279217f-4624-488b-944f-2d58ebc80e14&width=2000&userId=&cache=v2"
      alt="main"
      style="width: 100%"
    />

    <!-- Recommendation Section -->
    <div class="text-h3 text-center text-decoration-overline">
      <br />
      AI에게 물어보세요!
    </div>
    <v-card class="pa-5 my-5 text-center">
      <v-card-title class="headline text-h4"
        >필요한 상품을 알려주세요.</v-card-title
      >
      <v-card-text>
        <v-btn-toggle
          v-model="preference.type"
          color="deep-purple-accent-2"
          rounded="0"
          group
        >
          <v-btn value="예금상품"> 예금 </v-btn>
          <v-btn value="적금상품"> 적금 </v-btn>
          <v-btn value=""> 상관없음 </v-btn>
        </v-btn-toggle>
        <br />
        <v-btn-toggle
          v-model="preference.bank"
          color="deep-purple-accent-2"
          rounded="0"
          group
        >
          <v-btn value="국민은행"> 국민은행 </v-btn>
          <v-btn value="신한은행"> 신한은행 </v-btn>
          <v-btn value="NH농협은행"> NH농협은행 </v-btn>
          <v-btn value="우리은행"> 우리은행 </v-btn>
          <v-btn value=""> 상관없음 </v-btn>
        </v-btn-toggle>
        <br />
        <v-btn-toggle
          v-model="preference.month"
          color="deep-purple-accent-2"
          rounded="0"
          group
        >
          <v-btn value="1개월"> 1개월 </v-btn>
          <v-btn value="3개월"> 3개월 </v-btn>
          <v-btn value="6개월"> 6개월 </v-btn>
          <v-btn value="12개월"> 12개월 </v-btn>
          <v-btn value="24개월"> 24개월 </v-btn>
          <v-btn value="36개월"> 36개월 </v-btn>
        </v-btn-toggle>
        <br />
        <v-btn-toggle
          v-model="preference.join"
          color="deep-purple-accent-2"
          rounded="0"
          group
        >
          <v-btn value="가입 방식은 인터넷"> 인터넷 </v-btn>
          <v-btn value="가입 방식은 스마트폰"> 스마트폰 </v-btn>
          <v-btn value="가입 방식은 영업점"> 영업점 </v-btn>
          <v-btn value=""> 상관없음 </v-btn>
        </v-btn-toggle>
      </v-card-text>
      <v-card-actions>
        <v-btn
          @click="surveyDone"
          :loading="gptLoading"
          color="deep-purple-accent-2"
          class="mx-auto border pa-3"
          size="x-large"
        >
          추천받기
        </v-btn>
      </v-card-actions>
    </v-card>

    <!-- Answer Section -->
    <v-card class="pa-5 text-center">
      <v-card-title class="headline text-h4 mb-4">당신을 위한 추천</v-card-title>
      <v-card-text class="text-subtitle-1">
        <p>{{ answer }}</p>
      </v-card-text>
    </v-card>
  </v-container>
</template>

<script setup>
import { ref } from "vue";
import axios from "axios";
import { useFinanceStore } from "@/stores/finance";
import { useCommunityStore } from "@/stores/community";
import Dialog from "@/components/Dialog.vue";
import router from "@/router";
const financeStore = useFinanceStore();
const communityStore = useCommunityStore();

const preference = ref({
  bank: "",
  join: "",
  month: "3개월",
  type: "",
});
const gptLoading = ref(false);

const query = ref("");
const answer = ref("추천받기를 눌러 확인하세요.");

const conversation = ref([]);

const surveyDone = () => {
  gptLoading.value = true;
  const { bank, join, month, type } = preference.value;
  query.value =
    bank +
    " " +
    type +
    join +
    ", 기간은 " +
    month +
    "인 상품 중에 가장 높은 금리 상품을 찾아줘";
  queryGPT();
};

const queryGPT = function () {
  conversation.value.push(query.value);
  axios({
    method: "get",
    url: `${financeStore.BASE_URL}/finance/products/gpt/`,
    params: {
      query: query.value,
    },
  })
    .then((res) => {
      answer.value = res.data.response;
      // console.log(answer.value);
      conversation.value.push(answer.value);
      gptLoading.value = false;
    })
    .catch((err) => console.log(err));
};
</script>

<style scoped>
.container {
  margin-top: 20px;
}

.on-hover {
  opacity: 0.6;
}
</style>
