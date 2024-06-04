import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
import ProductView from "../views/ProductView.vue";
import DepositView from "../views/DepositView.vue";
import SavingView from "@/views/SavingView.vue";
import ProductDetailView from "../views/ProductDetailView.vue";
import ExchangeRateView from "../views/ExchangeRateView.vue";
import MapView from "../views/MapView.vue";
import CommunityView from "../views/CommunityView.vue";
import CommunityCreateView from "../views/CommunityCreateView.vue";
import CommunityDetailView from "../views/CommunityDetailView.vue";
import CommunityUpdateView from "../views/CommunityUpdateView.vue";
import LoginView from "../views/LoginView.vue";
import SignUpView from "../views/SignUpView.vue";
import ProfileView from "../views/ProfileView.vue";

import { useCommunityStore } from "@/stores/community";
import axios from "axios";
import { ref } from "vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "home",
      component: HomeView,
    },
    {
      path: "/products",
      component: ProductView,
      children: [
        { path: "", name: "products", component: DepositView },
        { path: "deposit", name: "deposit", component: DepositView },
        { path: "saving", name: "saving", component: SavingView },
        { path: ":product_id", name: "detail", component: ProductDetailView },
      ],
    },
    {
      path: "/exchange-rate",
      name: "exchangeRate",
      component: ExchangeRateView,
    },
    {
      path: "/map",
      name: "map",
      component: MapView,
    },
    {
      path: "/community",
      name: "community",
      component: CommunityView,
    },
    {
      path: "/community/create",
      name: "communityCreate",
      component: CommunityCreateView,
    },
    {
      path: "/community/:article_id",
      name: "communityDetail",
      component: CommunityDetailView,
    },
    {
      path: "/community/:article_id/update",
      name: "communityUpdate",
      component: CommunityUpdateView,
      beforeEnter: async (to, from, next) => {
        const store = useCommunityStore();
        const articleAuthor = await getArticleAuthorById(to.params.article_id);
        if (store.userInfo?.id === articleAuthor) {
          next();
        } else {
          next({
            name: "communityDetail",
            params: { article_id: to.params.article_id },
          });
        }
      },
    },
    {
      path: "/accounts/login",
      name: "logIn",
      component: LoginView,
    },
    {
      path: "/accounts/signup",
      name: "signUp",
      component: SignUpView,
    },
    {
      path: "/accounts/profile",
      name: "profile",
      component: ProfileView,
    },
  ],
});

async function getArticleAuthorById(article_id) {
  const response = await axios.get(
    `http://127.0.0.1:8000/articles/${article_id}/`
  );
  return response.data.user.id;
}

router.beforeEach((to, from) => {
  const store = useCommunityStore();
  // 인증되지 않은 사용자는 메인 페이지에 접근 할 수 없음
  if (
    !(
      to.name === "logIn" ||
      to.name === "signUp" ||
      to.name === "home" ||
      to.name === "products" ||
      to.name === "map" ||
      to.name === "exchangeRate" ||
      to.name === "deposit" ||
      to.name === "saving" ||
      to.name === "detail"
    ) &&
    store.isLogin === false
  ) {
    return { name: "logIn" };
  }

  // 인증된 사용자는 회원가입과 로그인 페이지에 접근 할 수 없음
  if ((to.name === "logIn" || to.name === "signUp") && store.isLogin === true) {
    return { name: "home" };
  }
});

export default router;
