<script setup>
import { ref } from "vue";
import { useCommunityStore } from "@/stores/community.js";
import { useRouter } from "vue-router";
import axios from "axios";

const store = useCommunityStore();
const router = useRouter();

const title = ref("");
const content = ref("");

const createArticle = function () {
  axios({
    method: "post",
    url: "http://127.0.0.1:8000/articles/",
    data: {
      title: title.value,
      content: content.value,
    },
    headers: {
      Authorization: `Token ${store.token}`,
    },
  })
    .then((res) => {
      router.push({ name: "community" });
    })
    .catch((err) => console.log(err));
};
</script>

<template>
  <v-container>
    <div class="text-h4 mb-5">게시글 작성</div>
    <v-form @submit.prevent="createArticle">
      <v-text-field v-model="title" label="제목" outlined></v-text-field>
      <v-textarea v-model="content" label="내용" outlined></v-textarea>
      <v-btn color="teal-darken-1" variant="outlined" type="submit">게시글 작성</v-btn>
    </v-form>
  </v-container>
</template>

<style scoped></style>
