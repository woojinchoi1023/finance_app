<template>
  <v-container fluid>
    <v-row class="align-center" style="margin-bottom: 20px">
      <v-col>
        <span class="text-h4">자유 게시판</span>
      </v-col>
      <v-spacer></v-spacer>
      <v-col class="text-right">
        <v-btn @click="communityCreate" color="teal-darken-1" variant="outlined">게시글 작성</v-btn>
      </v-col>
    </v-row>
    <v-row>
      <v-col
        v-for="article in articles"
        :key="article.id"
        cols="12"
        sm="6"
        md="4"
        class="article"
      >
        <Article :article="article" />
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup>
import { onMounted, ref } from "vue";
import { useCommunityStore } from "@/stores/community.js";
import Article from "../components/Article.vue";
import { useRouter } from "vue-router";
import axios from "axios";

const router = useRouter();
const store = useCommunityStore();
const articles = ref([]);
onMounted(() => {
  axios({
    method: "get",
    url: "http://127.0.0.1:8000/articles/",
  }).then((res) => {
    articles.value = res.data;
  });
});
const communityCreate = () => {
  router.push({ name: "communityCreate" });
};
</script>

<style scoped>
.article {
  /* margin: 1rem; */
  padding: 1rem;
}

.v-card {
  height: 100%;
  max-height: 400px; /* 최대 높이 설정 */
}
</style>
