<template>
  <v-container class="d-flex justify-center align-center fill-height pt-16 pb-0">
    <v-card class="pa-5 text-center" min-width="500">
      <img src="../../public/mainlogo.png" alt="logo" style="height: 90px; width: 180px" class="my-5" />
      <!-- <v-card-title class="text-center">
        <span class="text-h3">로그인</span>
      </v-card-title> -->
      <v-card-text>
        <v-form @submit.prevent="logIn">
          <v-text-field variant="outlined" v-model="username" label="Username" prepend-icon="mdi-account" required
            density="compact" class="my-3"></v-text-field>
          <v-text-field variant="outlined" v-model="password" label="Password" type="password" prepend-icon="mdi-lock"
            required density="compact" class="my-5"></v-text-field>
          <div class="d-flex justify-end">
            <v-btn color="teal-darken-1" type="submit" class="px-6">
              로그인
            </v-btn>
          </div>
        </v-form>
      </v-card-text>
    </v-card>
  </v-container>
  <div class="d-flex justify-center">
    <RouterLink :to="{ name: 'signUp' }" style="color: gray;" class="text-decoration-none">회원가입</RouterLink>
  </div>
</template>

<script setup>
import { ref } from "vue";
import { useRouter, RouterLink } from "vue-router";
import { useCommunityStore } from "../stores/community";

const username = ref(null);
const password = ref(null);
const router = useRouter();
const store = useCommunityStore();

const logIn = () => {
  const payload = {
    username: username.value,
    password: password.value,
  };
  store.logIn(payload);
};
</script>

<style scoped>
.fill-height {
  height: 100vh;
}
</style>
