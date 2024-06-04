<template>
  <v-container class="d-flex justify-center align-center fill-height">
    <v-card class="pa-5 text-center" min-width="600">
      <img src="../../public/mainlogo.png" alt="logo" style="height: 90px; width: 180px" class="my-5" />
      <v-spacer></v-spacer>
      <v-card-text>
        <v-form @submit.prevent="signUp">
          <v-text-field
            variant="outlined"
            v-model="username"
            label="Username"
            prepend-icon="mdi-account"
            required
            density="compact"
            class="my-3"
            :rules="usernameRule"
          ></v-text-field>
          <v-text-field
            variant="outlined"
            v-model="password1"
            label="Password"
            type="password"
            prepend-icon="mdi-lock"
            required
            density="compact"
            class="my-3"
            :rules="password1Rule"
          ></v-text-field>
          <v-text-field
            variant="outlined"
            v-model="password2"
            label="Confirm Password"
            type="password"
            prepend-icon="mdi-lock"
            required
            density="compact"
            class="my-3"
            :rules="password2Rule"
          ></v-text-field>
          <v-text-field
            variant="outlined"
            v-model="email"
            label="Email"
            type="email"
            prepend-icon="mdi-email"
            required
            density="compact"
            class="my-3"
          ></v-text-field>
          <v-text-field
            variant="outlined"
            v-model="nickname"
            label="Nickname"
            prepend-icon="mdi-account-circle"
            required
            density="compact"
            class="my-3"
          ></v-text-field>
          <v-text-field
            variant="outlined"
            v-model="first_name"
            label="First Name"
            prepend-icon="mdi-account-box"
            required
            density="compact"
            class="my-3"
          ></v-text-field>
          <v-text-field
            variant="outlined"
            v-model="last_name"
            label="Last Name"
            prepend-icon="mdi-account-box-outline"
            required
            density="compact"
            class="my-5"
          ></v-text-field>
          <v-btn color="teal-darken-1" type="submit" block>
            회원가입
          </v-btn>
        </v-form>
      </v-card-text>
    </v-card>
  </v-container>
</template>

<script setup>
import { ref } from "vue";
import { useCommunityStore } from "../stores/community";
import { useRouter } from "vue-router";

const username = ref("");
const password1 = ref("");
const password2 = ref("");
const email = ref("");
const first_name = ref("");
const last_name = ref("");
const nickname = ref("");

const store = useCommunityStore();
const router = useRouter();

const usernameRule = ref([
  (value) => {
    if (!username.value.length) return "필수 입력 사항입니다."
    return true
  }
])

const password1Rule = ref([
  (value) => {
    if (!password1.value.length) return "필수 입력 사항입니다."
    return true
  }
])

const password2Rule = ref([
  (value) => {
    if (!password2.value.length) return "필수 입력 사항입니다."
    return true
  }
])

const signUp = () => {
  const payload = {
    username: username.value,
    password1: password1.value,
    password2: password2.value,
    email: email.value,
    first_name: first_name.value,
    last_name: last_name.value,
    nickname: nickname.value,
  };

  store
    .signUp(payload)
    .then(() => {
      router.push({ name: "home" }); // 회원가입 성공 시 홈 페이지로 이동
    })
    .catch((err) => {
      console.error(err);
      alert("회원가입에 실패했습니다.");
    });
};
</script>

<style scoped>
.fill-height {
  height: 100vh;
}
</style>
