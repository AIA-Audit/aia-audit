import { createApp } from "vue";
import { createPinia } from "pinia";

import axios from 'axios';
import App from "./App.vue";
import PrimeVue from 'primevue/config';
import router from "./router";
import ToastService from 'primevue/toastservice';
import { io } from "socket.io-client";
import moment from 'moment';

import "./assets/main.css";
import "primevue/resources/primevue.min.css";
import "primevue/resources/themes/tailwind-light/theme.css"
import "primeicons/primeicons.css";

const app = createApp(App);

app.config.globalProperties.axios=axios;
app.config.globalProperties.socketio=io;
app.config.globalProperties.moment=moment;

app.use(createPinia());
app.use(PrimeVue);
app.use(router);
app.use(ToastService);

app.mount("#app");
