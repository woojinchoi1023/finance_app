import { createApp } from "vue";
import { createPinia } from "pinia";
import piniaPluginPersistedstate from "pinia-plugin-persistedstate";
// import BootstrapVue3 from 'bootstrap-vue-3'
// import 'bootstrap/dist/css/bootstrap.css'
// import 'bootstrap-vue-3/dist/bootstrap-vue-3.css'
import App from "./App.vue";
import router from "./router";
// Vuetify
import vuetify from './vuetify'  // 새로 만든 구성 파일을 임포트

const app = createApp(App);
const pinia = createPinia();

pinia.use(piniaPluginPersistedstate);

// app.use(createPinia())
app.use(router);
app.use(pinia);
// app.use(BootstrapVue3);
app.use(vuetify);

app.mount("#app");
