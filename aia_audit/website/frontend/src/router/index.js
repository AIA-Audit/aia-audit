import { createRouter, createWebHistory } from "vue-router";
import AboutView from "../views/AboutView.vue";
import HelpView from "../views/HelpView.vue";
import HomeView from "../views/HomeView.vue";
import MyScansView from "../views/MyScansView.vue";
import NewScanView from "../views/NewScanView.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    /* User Routes */
    {
      path: "/",
      name: "home",
      component: HomeView,
      meta: { title: 'Dashboard' },
    },
    {
      path: "/new/scan",
      name: "new-scan",
      component: NewScanView,
      meta: { title: 'New Scan' },
    },
    {
      path: "/scans",
      name: "scans",
      component: MyScansView,
      meta: { title: 'My Scans' },
    },
    {
      path: "/about",
      name: "about",
      component: AboutView,
      meta: { title: 'About' },
    },
    {
      path: "/help",
      name: "help",
      component: HelpView,
      meta: { title: 'Help' },
    },
  ],
});

router.beforeEach((to, from, next) => {
  document.title = to.meta.title;
  next();
});

export default router;
