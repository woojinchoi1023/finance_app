<script setup>
import { ref, onMounted } from "vue";
import { useCommunityStore } from "@/stores/community.js";
import { useRoute, useRouter } from "vue-router";

import axios from "axios";

const store = useCommunityStore();
const route = useRoute();
const router = useRouter();

const article = ref(null);

onMounted(() => {
  axios({
    method: "get",
    url: `http://127.0.0.1:8000/articles/${route.params.article_id}/`,
    headers: {
      Authorization: `Token ${store.token}`,
    },
  }).then((res) => {
    article.value = res.data;
  });
});

const updateArticle = function () {
  axios({
    method: "put",
    url: `http://127.0.0.1:8000/articles/${article.value.id}/`,
    data: {
      title: article.value.title,
      content: article.value.content,
    },
    headers: {
      Authorization: `Token ${store.token}`,
    },
  })
    .then((res) => {
      router.go(-1);
    })
    .catch((err) => console.log(err));
};
</script>

<template>
  <v-container>
    <div class="text-h4 mb-5">게시글 수정</div>
    <div v-if="article">
      <v-form @submit.prevent="updateArticle">
        <v-text-field v-model="article.title" label="제목"></v-text-field>
        <v-textarea v-model="article.content" label="내용"></v-textarea>
        <v-btn color="primary" type="submit">게시글 수정</v-btn>
      </v-form>
    </div>
  </v-container>
</template>

<style scoped></style>
