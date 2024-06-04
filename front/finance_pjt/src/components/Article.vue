<template>
  <v-card @click="detail">
    <v-card-title>
      <v-layout class="align-center">
        <span class="article-title">
          {{ article.title }}
          <span class="text-red"> [{{ article.comment_set.length }}] </span>
        </span>
        <v-spacer></v-spacer>
        <span class="font-weight-light text-right">
          <v-icon style="height: auto">mdi-thumb-up-outline</v-icon>
          {{ article.article_likes_set.length }}
        </span>
      </v-layout>
    </v-card-title>
    <v-card-subtitle>{{ article.created_at.slice(5, 10) }}</v-card-subtitle>
    <v-card-text>
      <p>{{ article.user.username }}</p>
    </v-card-text>
  </v-card>
</template>

<script setup>
import { useCommunityStore } from "@/stores/community.js";
import { useRouter } from "vue-router";

const store = useCommunityStore();
const router = useRouter();
const props = defineProps({
  article: Object,
});

const detail = () => {
  router.push({
    name: "communityDetail",
    params: { article_id: props.article.id },
  });
};
</script>

<style scoped>
.article-title,
.article-content {
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}
</style>
