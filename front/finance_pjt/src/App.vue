<template>
  <v-app>
    <v-toolbar app class="bg-light-grey">
      <v-toolbar-title>
        <v-btn
          icon
          @click="router.push({ name: 'home' })"
          style="height: 50px; width: 100px"
        >
          <img
            src="../public/mainlogo.png"
            alt="logo"
            style="height: 50px; width: 100px"
          />
        </v-btn>
        <v-btn :to="{ name: 'profile' }" v-if="user" class="toolbar-text">
          <span v-if="user?.nickname" @click="router.push({ name: 'profile' })">
            {{ user.nickname }}님, 안녕하세요
          </span>
          <span v-else-if="user" @click="router.push({ name: 'profile' })">
            {{ user.username }}님, 안녕하세요
          </span>
        </v-btn>
      </v-toolbar-title>
      <v-toolbar-items class="hidden-xs">
        <v-btn :to="{ name: 'community' }" class="toolbar-text toolbar-community">커뮤니티</v-btn>
        <v-btn :to="{ name: 'products' }" class="toolbar-text toolbar-products">금융상품</v-btn>
        <v-btn :to="{ name: 'exchangeRate' }" class="toolbar-text toolbar-exchange">환율계산기</v-btn>
        <v-btn :to="{ name: 'map' }" class="toolbar-text toolbar-map">지도</v-btn>
        <template v-if="user">
          <v-btn class="bg-light-grey toolbar-text" @click="logOut">로그아웃</v-btn>
          <v-btn class="bg-light-grey toolbar-text" :to="{ name: 'profile' }">
            My Page
          </v-btn>
        </template>
        <template v-else>
          <v-btn :to="{ name: 'logIn' }" class="toolbar-text">로그인</v-btn>
          <v-btn :to="{ name: 'signUp' }" class="toolbar-text">회원가입</v-btn>
        </template>
      </v-toolbar-items>
    </v-toolbar>
    <v-container>
      <RouterView />
    </v-container>
  </v-app>
</template>

<script setup>
import { RouterView } from "vue-router";
import { useCommunityStore } from "./stores/community.js";
import { ref, onMounted, computed } from "vue";
import router from "./router";

const store = useCommunityStore();
const user = computed(() => store.userInfo);
const logOut = () => {
  store.logOut();
};
</script>

<style scoped>
.v-toolbar-title > span {
  margin: auto;
  font-size: 24px;
}

.v-container {
  padding: 3rem;
  max-width: 1200px;
}

.toolbar-text {
  font-size: 16px;
  color: #757575;
  border-radius: 40%; /* 사각형의 모서리를 더 둥글게 만듦 */
  transition: background-color 0.3s;
}

.bg-light-grey {
  background-color: #f5f5f5;
}

/* 마우스 호버 효과 추가 및 툴바 별로 색상 지정 */
.toolbar-community:hover {
  color: #000;
  background-color: #bbdefb;
}

.toolbar-products:hover {
  color: #000;
  background-color: #ffcdd2;
}

.toolbar-exchange:hover {
  color: #000;
  background-color: #c8e6c9;
}

.toolbar-map:hover {
  color: #000;
  background-color: #fff9c4;
}
</style>
