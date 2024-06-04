<template>
  <v-container class="border-double">
    <v-col class="articleDetail" v-if="article">
      <!-- <v-btn class="bg-red" @click="router.go(-1)">뒤로가기</v-btn> -->
      <v-card
        style="
          display: flex;
          justify-content: space-between;
          margin-bottom: 1rem;
        "
        class="px-5 py-1"
      >
        <div class="text-overline">
          <v-icon icon="mdi-account"></v-icon>
          {{ article.user.username }}
        </div>
        <p class="text-overline">
          {{ article.created_at.slice(0, 10) }}
          {{ article.created_at.slice(11, 19) }}
        </p>
        <p v-if="likes" class="text-overline">추천: {{ likes.length }}</p>
      </v-card>
      <div style="display: flex; justify-content: end">
        <p @click="router.push({ name: 'community' })" class="pointer-cursor">
          목록
        </p>
        <span style="margin-left: 7px; margin-right: 7px"> | </span>
        <p>댓글({{ article.comment_set.length }})</p>
      </div>
      <div class="text-h4">{{ article.title }}</div>
      <div class="content">
        <p>{{ article.content }}</p>
      </div>
      <p class="text-disabled" v-if="article.updated_at !== article.created_at">
        수정일자: {{ article.updated_at.slice(0, 10) }}
        {{ article.updated_at.slice(11, 19) }}
      </p>
      <br />
      <p>
        <v-btn v-if="!hasLiked" class="mr-3" @click="likeArticle" color="blue" variant="outlined"
          ><v-icon style="width: 30px">mdi-thumb-up-outline</v-icon>
          {{ likes?.length }}
        </v-btn>
        <v-btn v-else color="blue" class="mr-3" @click="likeArticle"
          ><v-icon style="width: 30px">mdi-thumb-up-outline</v-icon>
          {{ likes?.length }}
        </v-btn>
        <span v-if="article.user.id === store.userInfo.id">
          <v-btn @click="deleteArticle" color="red" variant="outlined">삭제</v-btn>
          <v-btn @click="updateArticle" color="teal-darken-1" variant="outlined">수정</v-btn>
        </span>
      </p>
      <v-row class="align-center justify-center" style="height: 100px">
        <v-col cols="10">
          <form @submit.prevent="createComment">
            <br />
            <v-text-field
              label="명예훼손, 개인정보 유출, 분쟁 유발, 허위사실 유포 등의 글은 이용약관에 의해 제재는 물론 볍률에 의해 처벌 받을 수 있습니다."
              type="text"
              id="content"
              v-model="content"
              density="compact"
            />
          </form>
        </v-col>
        <v-col cols="2">
          <v-row>
            <v-spacer></v-spacer>
            <v-btn @click="createComment" color="teal-darken-1" variant="outlined">등록</v-btn>
          </v-row>
        </v-col>
      </v-row>
      <div
        class="comment"
        v-for="(comment, idx) in article.comment_set"
        :key="comment.id"
        style="padding: 9px"
      >
        <Comment :comment="comment" :idx="idx" />
      </div>
    </v-col>
  </v-container>
</template>

<script setup>
import { useRoute, useRouter } from "vue-router";
import { onMounted, ref, computed } from "vue";
import { useCommunityStore } from "@/stores/community.js";
import axios from "axios";
import Comment from "@/components/Comment.vue";

const route = useRoute();
const router = useRouter();
const store = useCommunityStore();
const article = ref(null);
const content = ref(""); // 댓글 작성시 사용
const likes = ref(null); // 좋아요 정보
const hasLiked = ref(null); // 좋아요 정보

onMounted(() => {
  axios({
    method: "get",
    url: `http://127.0.0.1:8000/articles/${route.params.article_id}/`,
    headers: {
      Authorization: `Token ${store.token}`,
    },
  })
    .then((res) => {
      article.value = res.data;
    })
    .catch((err) => console.log(err))
    .then((res) => {
      axios({
        // 좋아요 했는지 검사
        method: "GET",
        url: `http://127.0.0.1:8000/articles/${article.value.id}/like/`,
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
});

const deleteArticle = () => {
  axios({
    method: "delete",
    url: `http://127.0.0.1:8000/articles/${article.value.id}/`,
    headers: {
      Authorization: `Token ${store.token}`,
    },
  })
    .then((res) => {
      router.push({ name: "community" });
    })
    .catch((err) => console.log(err));
};

const createComment = () => {
  axios({
    method: "post",
    url: `http://127.0.0.1:8000/articles/${article.value.id}/comments/`,
    data: {
      content: content.value,
    },
    headers: {
      Authorization: `Token ${store.token}`,
    },
  })
    .then((res) => {
      router.go(0);
    })
    .catch((err) => console.log(err));
};

const updateArticle = () => {
  router.push({
    name: "communityUpdate",
    params: { article_id: article.value.id },
  });
};

const likeArticle = () => {
  axios({
    method: "POST",
    url: `http://127.0.0.1:8000/articles/${article.value.id}/like/`,
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
.articleDetail {
  padding: 1rem;
}

.text-h2 {
  margin: 1rem 0;
  font-size: 24px;
  font-weight: bold;
}

.text-h4 {
  margin: 1rem 0;
  font-size: 18px;
}

.content {
  margin: 1rem 0;
}

.comment {
  border: 1px solid #ccc;
  padding: 1rem;
  margin: 1rem 0;
}

.v-btn {
  margin-right: 1rem;
}
/* .v-container {
  border: 1px solid black;
  border-radius: 3%;
} */

.pointer-cursor {
  cursor: pointer;
}
</style>
