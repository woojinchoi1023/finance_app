<template>
  <div class="commentDetail">
    <div style="display: flex; justify-content: space-between">
      <p>
        <v-icon icon="mdi-account"></v-icon>
        <span class="font-weight-bold">
          {{ comment.user.username }}
        </span>
        <span class="text-disabled">
          ({{ comment.created_at.slice(0, 10) }}
          {{ comment.created_at.slice(11, 19) }})
        </span>
      </p>
      <div style="display: flex">
        <v-btn v-if="!hasLiked" class="mr-3" @click="likeComment" color="blue" variant="outlined"
          ><v-icon style="width: 30px">mdi-thumb-up-outline</v-icon>
          {{ likes?.length }}
        </v-btn>
        <v-btn v-else color="blue" class="mr-3" @click="likeComment"
          ><v-icon style="width: 30px">mdi-thumb-up-outline</v-icon>
          {{ likes?.length }}
        </v-btn>
        <!-- <p v-if="likes">추천 : {{ likes.length }}</p> -->
        <v-btn
          v-if="comment.user.id === store.userInfo.id"
          @click="deleteComment"
          style="margin-left: 9px"
          color="red" variant="outlined"
        >
          삭제
        </v-btn>
      </div>
    </div>
    <p>{{ comment.content }}</p>
    <p></p>
  </div>
</template>

<script setup>
import { useCommunityStore } from "@/stores/community.js";
import { useRouter } from "vue-router";
import { onMounted, ref, defineProps } from "vue";
import axios from "axios";

const store = useCommunityStore();
const router = useRouter();
const likes = ref(null); // 좋아요 정보
const hasLiked = ref(null); // 좋아요 했는지

onMounted(() => {
  axios({
    // 좋아요 했는지 검사
    method: "GET",
    url: `http://127.0.0.1:8000/articles/${props.comment.article}/comments/${props.comment.id}/like/`,
    headers: {
      Authorization: `Token ${store.token}`,
    },
  })
    .then((res) => {
      likes.value = res.data.likes;
      hasLiked.value = res.data.hasLiked;
    })
    .catch((err) => console.log(err));
});

const props = defineProps({
  comment: Object,
  idx: Number,
});
const deleteComment = () => {
  axios({
    method: "delete",
    url: `http://127.0.0.1:8000/articles/${props.comment.article}/comments/${props.comment.id}/`,
    headers: {
      Authorization: `Token ${store.token}`,
    },
  })
    .then((res) => {
      router.go(0);
    })
    .catch((err) => console.log(err));
};

const likeComment = () => {
  axios({
    method: "POST",
    url: `http://127.0.0.1:8000/articles/${props.comment.article}/comments/${props.comment.id}/like/`,
    headers: {
      Authorization: `Token ${store.token}`,
    },
  })
    .then((res) => {
      likes.value = res.data.likes;
      hasLiked.value = res.data.hasLiked;
    })
    .catch((err) => console.log(err));
};
</script>

<style scoped>
.commentDetail {
  /* padding: 0.5rem; */
  /* border: 1px solid #ccc; */
  border-radius: 8px;
  margin-bottom: 1rem;
}

.commentDetail p {
  margin: 0.5rem 0;
}
</style>
